# Test: SOD Wizard Seed Prompt

This file documents a test conversation using the SOD wizard seed prompt to verify it works as expected.

## Test Scenario

**Goal**: Create an SOD for a multi-region AWS Vault replication project

---

## Test Conversation

### Input 1: Seed Prompt
*User copies and pastes the entire seed prompt from `sod-wizard-seed.md`*

**Expected AI Response**:
- Acknowledges the prompt
- Asks: "What project or idea would you like to create an SOD for? Share any initial thoughts, problems, or goals."

---

### Input 2: Initial Brain Dump
```
New notes: We need to replicate HashiCorp Vault secrets across AWS regions for disaster recovery. Currently all our secrets are in us-east-1 and we have no DR capability.
```

**Expected AI Response**:
- Integrates notes into Problem Statement and Functional Overview sections
- Asks 1-2 clarifying questions such as:
  - What's driving this—regulatory requirement, recent outage, or proactive planning?
  - Are there specific RPO/RTO targets you need to hit?
  - Which AWS regions do you need to support?

---

### Input 3: Provide More Context
```
New notes: This is driven by regulatory requirement for PCI compliance. We need RPO of 15 minutes and RTO of 30 minutes. Target regions are us-east-1 (primary) and us-west-2 (DR).
```

**Expected AI Response**:
- Adds to Business Context/Drivers and Constraints sections
- Asks follow-up questions such as:
  - What's your current Vault architecture? (single node, HA cluster?)
  - Are there specific security requirements for cross-region replication?
  - What monitoring and alerting do you need?

---

### Input 4: Architecture Details
```
New notes: We have HA Vault clusters in each region using Consul as storage backend. Need encryption in transit for replication. Must maintain audit logs in both regions for compliance.
```

**Expected AI Response**:
- Adds to High-Level Architecture, Constraints, and Dependencies
- Asks questions about:
  - Team responsibilities (who manages primary vs DR?)
  - Failover/failback procedures
  - Testing requirements

---

### Input 5: View Progress
```
Show SOD
```

**Expected AI Response**:
- Displays complete SOD with all sections
- Populated sections show actual content
- Empty sections marked as "TBD" or "Not yet defined"
- Brief summary of what's still missing (e.g., "Still need: Non-Goals, Phases/Components, Open Questions")

---

### Input 6: Add More Details
```
New notes: Non-goals include: not replacing our current IAM system, not implementing custom encryption beyond AWS KMS, not supporting more than 2 regions initially. Phases: Phase 1 - Setup replication between regions, Phase 2 - Implement monitoring and alerting, Phase 3 - DR testing and runbooks.
```

**Expected AI Response**:
- Updates Non-Goals and Phases/Components sections
- Asks about any remaining gaps (Risks, Dependencies, Open Questions)

---

### Input 7: Final Details
```
New notes: Key risks include: replication lag exceeding RPO, network partitions between regions, key rotation complexity. Mitigations: monitoring with CloudWatch, automated failover testing, clear runbooks. Dependencies: AWS KMS keys in both regions, VPC peering or Transit Gateway, approved AMIs, IAM roles. Open questions: Who approves DR failover? What's the communication plan during failover?
```

**Expected AI Response**:
- Updates Risks & Mitigations, Dependencies, and Open Questions
- Notes that SOD is now fairly complete

---

### Input 8: Lock the SOD
```
Lock the SOD
```

**Expected AI Response**:
- Reviews all sections for completeness
- If critical sections are missing, warns user
- If complete, confirms: "Your SOD is comprehensive and ready. Locked!"
- Provides brief summary of what was captured

---

## Verification Checklist

✅ **Prompt Recognition**: AI acknowledges seed prompt correctly  
✅ **Conversational**: AI asks 1-2 questions per interaction  
✅ **Section Integration**: Notes are placed in correct SOD sections  
✅ **Progressive Building**: Each interaction adds to the SOD  
✅ **Show SOD Works**: Displays complete document with TBD markers  
✅ **Lock SOD Works**: Reviews and confirms completion  
✅ **Maintains Structure**: All SOD sections are present  
✅ **Stays Focused**: Questions are relevant and add value  

---

## Test Result

**Status**: ⏳ Ready for Manual Verification

**Note**: This is a reference test case. Users should manually verify the seed prompt works by following this conversation flow in their AI assistant of choice.

**To Test**:
1. Copy seed prompt from `sod-wizard-seed.md`
2. Paste into Claude, ChatGPT, or other AI assistant
3. Follow this conversation flow
4. Verify AI responses match expectations

**Notes**:
- Actual AI responses may vary but should follow the general pattern
- Key is that the conversation is iterative, focused, and builds a complete SOD
- AI should guide the user without being overly rigid
- This test case serves as both validation and documentation

---

## Manual Test Instructions

If you want to manually test this:

1. Open a new AI chat session
2. Copy the full seed prompt from `/prompts/sod-wizard-seed.md`
3. Paste it into the chat
4. Use the inputs from this test scenario
5. Verify the AI's behavior matches expectations
6. Check the final SOD has all required sections populated

**Expected Duration**: 10-15 minutes

---
