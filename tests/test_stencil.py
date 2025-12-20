#!/usr/bin/env python3
"""Unit tests for stencil CLI template processing."""

import importlib.util
import json
import sys
from datetime import date
from pathlib import Path
from unittest.mock import patch

import pytest

# Load the stencil script as a module (it has no .py extension)
stencil_path = Path(__file__).parent.parent / "bin" / "stencil"
spec = importlib.util.spec_from_loader("stencil", loader=None, origin=str(stencil_path))
stencil_module = importlib.util.module_from_spec(spec)

# Provide __file__ so the script can find STENCIL_ROOT
stencil_module.__dict__["__file__"] = str(stencil_path)

# Execute the script to populate the module
with open(stencil_path) as f:
    exec(f.read(), stencil_module.__dict__)

# Import the functions we need to test
substitute_variables = stencil_module.substitute_variables
load_manifest = stencil_module.load_manifest
collect_variables = stencil_module.collect_variables
is_project_scaffold = stencil_module.is_project_scaffold
process_templates = stencil_module.process_templates


class TestSubstituteVariables:
    """Tests for variable substitution in template content."""

    def test_simple_substitution(self) -> None:
        """Replace a single variable."""
        content = "Hello {{NAME}}!"
        variables = {"NAME": "World"}
        result = substitute_variables(content, variables)
        assert result == "Hello World!"

    def test_multiple_substitutions(self) -> None:
        """Replace multiple different variables."""
        content = "{{PROJECT_NAME}} - {{DESCRIPTION}}"
        variables = {"PROJECT_NAME": "my_tool", "DESCRIPTION": "A CLI tool"}
        result = substitute_variables(content, variables)
        assert result == "my_tool - A CLI tool"

    def test_repeated_variable(self) -> None:
        """Replace same variable appearing multiple times."""
        content = "{{NAME}} and {{NAME}} again"
        variables = {"NAME": "test"}
        result = substitute_variables(content, variables)
        assert result == "test and test again"

    def test_no_variables(self) -> None:
        """Content without variables passes through unchanged."""
        content = "No variables here"
        variables = {"NAME": "unused"}
        result = substitute_variables(content, variables)
        assert result == "No variables here"

    def test_missing_variable_raises_error(self) -> None:
        """Missing variable should raise KeyError."""
        content = "Hello {{MISSING}}!"
        variables = {"NAME": "World"}
        with pytest.raises(KeyError):
            substitute_variables(content, variables)

    def test_empty_content(self) -> None:
        """Empty content returns empty string."""
        result = substitute_variables("", {"NAME": "test"})
        assert result == ""

    def test_multiline_content(self) -> None:
        """Variables in multiline content are replaced."""
        content = """Line 1: {{NAME}}
Line 2: {{VALUE}}
Line 3: no variables"""
        variables = {"NAME": "test", "VALUE": "123"}
        result = substitute_variables(content, variables)
        expected = """Line 1: test
Line 2: 123
Line 3: no variables"""
        assert result == expected


class TestLoadManifest:
    """Tests for manifest.json loading."""

    def test_load_valid_manifest(self, tmp_path: Path) -> None:
        """Load a valid manifest.json file."""
        manifest_content = {
            "name": "python-cli",
            "description": "Python CLI project",
            "variables": {
                "project_name": {"prompt": "Project name", "required": True}
            },
        }
        manifest_file = tmp_path / "manifest.json"
        manifest_file.write_text(json.dumps(manifest_content))

        result = load_manifest(tmp_path)

        assert result is not None
        assert result["name"] == "python-cli"
        assert "project_name" in result["variables"]

    def test_no_manifest_returns_none(self, tmp_path: Path) -> None:
        """Return None when no manifest.json exists."""
        result = load_manifest(tmp_path)
        assert result is None

    def test_computed_variables_added(self, tmp_path: Path) -> None:
        """Computed variables like YEAR and DATE are added."""
        manifest_content = {
            "name": "test",
            "computed_variables": {"YEAR": "current_year", "DATE": "current_date"},
        }
        manifest_file = tmp_path / "manifest.json"
        manifest_file.write_text(json.dumps(manifest_content))

        result = load_manifest(tmp_path)

        assert result is not None
        # The manifest should indicate computed variables to add
        assert "computed_variables" in result


class TestCollectVariables:
    """Tests for variable collection from CLI args and prompts."""

    def test_variables_from_cli_args(self) -> None:
        """Collect variables provided via CLI arguments."""

        class MockArgs:
            project_name = "my_tool"
            cli_name = "my-tool"
            description = "A test tool"
            non_interactive = True

        manifest = {
            "variables": {
                "project_name": {"required": True},
                "cli_name": {"required": True},
                "description": {"required": True},
            }
        }

        result = collect_variables(manifest, MockArgs())

        assert result["PROJECT_NAME"] == "my_tool"
        assert result["CLI_NAME"] == "my-tool"
        assert result["DESCRIPTION"] == "A test tool"

    def test_computed_year_added(self) -> None:
        """YEAR computed variable contains current year."""

        class MockArgs:
            project_name = "test"
            cli_name = "test"
            description = "test"
            non_interactive = True

        manifest = {
            "variables": {
                "project_name": {"required": True},
                "cli_name": {"required": True},
                "description": {"required": True},
            },
            "computed_variables": {"YEAR": "current_year"},
        }

        result = collect_variables(manifest, MockArgs())

        assert result["YEAR"] == str(date.today().year)

    def test_computed_date_added(self) -> None:
        """DATE computed variable contains current date."""

        class MockArgs:
            project_name = "test"
            cli_name = "test"
            description = "test"
            non_interactive = True

        manifest = {
            "variables": {
                "project_name": {"required": True},
                "cli_name": {"required": True},
                "description": {"required": True},
            },
            "computed_variables": {"DATE": "current_date"},
        }

        result = collect_variables(manifest, MockArgs())

        assert result["DATE"] == date.today().isoformat()

    def test_missing_required_non_interactive_raises(self) -> None:
        """Missing required variable in non-interactive mode raises error."""

        class MockArgs:
            project_name = None
            cli_name = "test"
            description = "test"
            non_interactive = True

        manifest = {
            "variables": {
                "project_name": {"required": True},
                "cli_name": {"required": True},
                "description": {"required": True},
            }
        }

        with pytest.raises(ValueError):
            collect_variables(manifest, MockArgs())


class TestIsProjectScaffold:
    """Tests for detecting project scaffold vs simple file copy."""

    def test_with_templates_dir(self, tmp_path: Path) -> None:
        """Directory with templates/ subdirectory is a project scaffold."""
        templates_dir = tmp_path / "templates"
        templates_dir.mkdir()

        result = is_project_scaffold(tmp_path)

        assert result is True

    def test_with_manifest(self, tmp_path: Path) -> None:
        """Directory with manifest.json is a project scaffold."""
        manifest_file = tmp_path / "manifest.json"
        manifest_file.write_text("{}")

        result = is_project_scaffold(tmp_path)

        assert result is True

    def test_without_templates_or_manifest(self, tmp_path: Path) -> None:
        """Directory without templates/ or manifest.json is not a scaffold."""
        result = is_project_scaffold(tmp_path)

        assert result is False

    def test_file_path_returns_false(self, tmp_path: Path) -> None:
        """File path (not directory) returns False."""
        file_path = tmp_path / "somefile.txt"
        file_path.write_text("content")

        result = is_project_scaffold(file_path)

        assert result is False


class TestProcessTemplates:
    """Tests for template processing and file generation."""

    def test_template_file_substitution(self, tmp_path: Path) -> None:
        """Template files have variables substituted and .template removed."""
        source = tmp_path / "source"
        source.mkdir()
        templates = source / "templates"
        templates.mkdir()

        # Create a template file
        template_file = templates / "README.md.template"
        template_file.write_text("# {{PROJECT_NAME}}\n\n{{DESCRIPTION}}")

        dest = tmp_path / "dest"
        variables = {"PROJECT_NAME": "my_tool", "DESCRIPTION": "A CLI tool"}

        process_templates(source, dest, variables)

        output_file = dest / "README.md"
        assert output_file.exists()
        content = output_file.read_text()
        assert "# my_tool" in content
        assert "A CLI tool" in content

    def test_static_file_copied(self, tmp_path: Path) -> None:
        """Static files (no .template extension) are copied as-is."""
        source = tmp_path / "source"
        source.mkdir()
        templates = source / "templates"
        templates.mkdir()

        # Create a static file
        static_file = templates / ".gitignore"
        static_file.write_text("*.pyc\n__pycache__/")

        dest = tmp_path / "dest"
        variables = {"PROJECT_NAME": "my_tool"}

        process_templates(source, dest, variables)

        output_file = dest / ".gitignore"
        assert output_file.exists()
        assert output_file.read_text() == "*.pyc\n__pycache__/"

    def test_nested_directories_created(self, tmp_path: Path) -> None:
        """Nested directory structure is preserved."""
        source = tmp_path / "source"
        source.mkdir()
        templates = source / "templates"
        templates.mkdir()

        # Create nested structure
        src_dir = templates / "src"
        src_dir.mkdir()
        init_file = src_dir / "__init__.py.template"
        init_file.write_text('"""{{PROJECT_NAME}} package."""')

        dest = tmp_path / "dest"
        variables = {"PROJECT_NAME": "my_tool"}

        process_templates(source, dest, variables)

        output_file = dest / "src" / "__init__.py"
        assert output_file.exists()
        assert "my_tool" in output_file.read_text()

    def test_path_variable_substitution(self, tmp_path: Path) -> None:
        """Variables in directory paths are substituted."""
        source = tmp_path / "source"
        source.mkdir()
        templates = source / "templates"
        templates.mkdir()

        # Create src/{{PROJECT_NAME}}/__init__.py structure
        src_dir = templates / "src" / "{{PROJECT_NAME}}"
        src_dir.mkdir(parents=True)
        init_file = src_dir / "__init__.py.template"
        init_file.write_text('"""{{PROJECT_NAME}} package."""')

        dest = tmp_path / "dest"
        variables = {"PROJECT_NAME": "my_tool"}

        process_templates(source, dest, variables)

        # Path should have variable substituted
        output_file = dest / "src" / "my_tool" / "__init__.py"
        assert output_file.exists()

    def test_creates_dest_directory(self, tmp_path: Path) -> None:
        """Destination directory is created if it doesn't exist."""
        source = tmp_path / "source"
        source.mkdir()
        templates = source / "templates"
        templates.mkdir()

        template_file = templates / "README.md.template"
        template_file.write_text("# Test")

        dest = tmp_path / "nonexistent" / "nested" / "dest"
        variables = {}

        process_templates(source, dest, variables)

        assert dest.exists()
        assert (dest / "README.md").exists()
