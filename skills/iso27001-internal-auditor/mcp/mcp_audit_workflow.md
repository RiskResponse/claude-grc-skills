# Conducting ISO 27001 Audits with Vanta MCP Server

## Overview

This guide explains how to conduct ISO 27001:2022 internal audits using the Vanta MCP Server for real-time evidence retrieval.

**Advantage**: Interactive, conversational auditing with direct Vanta access.

---

## MCP Audit Workflow

### Pre-Audit Phase

**Step 1: Configure MCP Server**  
Follow `mcp_setup_guide.md` to set up Vanta MCP Server in Claude Desktop.

**Step 2: Test Connection**

In Claude:
> "Using Vanta MCP Server, verify connection and list available tools"

Expected response: List of Vanta MCP tools and confirmation of connection.

**Step 3: Get Audit Overview**

> "Using Vanta MCP Server, provide an overview of our compliance posture - how many policies, controls implemented, and any overdue items"

This gives you initial context before detailed audit.

---

### Document Review Phase

**Policy Review**:

```
Auditor: "Using Vanta MCP Server, list all policies and check their review dates. Flag any policies not reviewed in the last 12 months."

Claude will:
- Query Vanta for all policies
- Check last review dates
- Identify overdue policies
- Flag potential nonconformities
```

**Example Response**:
```
Retrieved 15 policies from Vanta:

✓ Information Security Policy - Last reviewed: 2024-01-15 (Compliant)
✓ Access Control Policy - Last reviewed: 2024-08-20 (Compliant)
✗ Incident Response Procedure - Last reviewed: 2023-04-10 (OVERDUE by 7 months)
✗ Backup Policy - Last reviewed: 2023-06-15 (OVERDUE by 5 months)

FINDING: Two policies have not been reviewed within required 12-month interval (ISO 27001:2022 Control A.5.1)
```

**Control Implementation Review**:

```
Auditor: "Using Vanta MCP Server, list all Annex A controls and identify any marked as 'Implemented' but missing test evidence"

Claude will:
- Retrieve control inventory
- Check implementation status
- Verify test results exist
- Identify evidence gaps
```

**Risk Assessment Review**:

```
Auditor: "Using Vanta MCP Server, list all High and Critical risks. For each, verify a treatment plan exists with assigned controls"

Claude will:
- Query risk register
- Filter by severity
- Check treatment plans
- Identify untreated risks
```

---

### Main Audit Phase

**Evidence Validation**:

```
Auditor: "For Control A.8.13 (Backup), retrieve all evidence from Vanta and assess adequacy"

Claude will:
- Get Control A.8.13 details
- List associated evidence
- Review evidence dates and types
- Assess if evidence proves control effectiveness
```

**Interactive Investigation**:

```
Auditor: "I found that access reviews are overdue. Using Vanta, check when the last access review was completed and who was responsible"

Claude will:
- Query access review records
- Identify last completion date
- Find assigned responsible party
- Provide context for nonconformity
```

**Cross-Referencing**:

```
Auditor: "Using Vanta, compare the Statement of Applicability against implemented controls. Are there any controls in the SoA that aren't actually implemented?"

Claude will:
- Get SoA control list
- Get implemented controls
- Identify discrepancies
- Flag gaps
```

---

### Finding Documentation Phase

**Generate Nonconformity Draft**:

```
Auditor: "Based on the overdue policy reviews we found, draft a nonconformity using the proper format (Reference, Requirement, Finding, Evidence)"

Claude will:
- Use nonconformity template
- Reference ISO 27001:2022 Control A.5.1
- Document specific evidence from Vanta
- Include Vanta data references (policy IDs, dates)
- Classify as major/minor
```

**Compile Findings**:

```
Auditor: "Compile all findings we've identified into an audit report summary"

Claude will:
- Organize all NCs, observations, recommendations
- Count findings by type and severity
- Suggest audit conclusions
- Reference all Vanta evidence
```

---

## Example MCP Audit Session

**Complete Example: Auditing Backup Controls**

```
Auditor: "Let's audit backup controls. Using Vanta MCP Server, retrieve information about Control A.8.13"

Claude: Retrieving Control A.8.13 (Information Backup) from Vanta...

Control Details:
- Status: Implemented
- Owner: IT Operations Manager  
- Test Frequency: Quarterly
- Last Test: 2024-09-15
- Test Result: Pass

Evidence Attached:
1. Backup Policy v2.0 (uploaded 2024-01-10)
2. Q3 2024 Backup Logs (uploaded 2024-09-20)
3. Restore Test Results (uploaded 2024-09-18)

---

Auditor: "Check the backup logs. Do they show daily backups as required by our policy?"

Claude: [Reviews backup log evidence]

Backup logs show:
- Daily automated backups: Yes, consistently
- Backup success rate: 98% (2 failures in 90 days)
- Failed backups: 2024-08-15, 2024-09-03
- Failure resolution: Both resolved same day

Assessment: Compliant. Daily backups performed, failures promptly addressed.

---

Auditor: "What about restore testing? Our policy requires annual testing minimum. When was the last restore test?"

Claude: [Queries Vanta test history]

Last Restore Test: 2024-09-18
- Test Type: Full database restore
- Result: Success
- RTO Achieved: 3.5 hours (target: 4 hours)
- RPO Verified: 0 data loss

Previous Restore Test: 2023-10-05 (11.4 months prior)

Assessment: Compliant with annual requirement. Actually exceeds requirement (more frequent than required).

---

Auditor: "Great. Document this as compliant with positive note about exceeding requirements"

Claude: Documented:

Control A.8.13: COMPLIANT ✓

Positive Finding: Backup and restore processes exceed policy requirements with consistent daily backups (98% success rate) and more-than-annual restore testing. Last test achieved RTO target.

Recommendation: Current practices are strong. Consider documenting quarterly restore testing as formal requirement to maintain current frequency.
```

---

## MCP vs. API vs. Manual Export

| Method | Best For | Pros | Cons |
|--------|----------|------|------|
| **MCP Server** | Interactive auditing, real-time queries | Natural language, conversational, contextual | Requires Claude Desktop, limited to available tools |
| **API Scripts** | Bulk export, automation, offline review | Complete control, scriptable, reproducible | Requires coding, manual execution |
| **Manual Export** | Simple audits, one-time reviews | No setup, familiar process | Time-consuming, error-prone, not auditable |

**Recommendation**: Use **MCP Server** for interactive audit work, **API scripts** for initial bulk export, **manual export** as fallback.

---

## Best Practices

1. **Start with MCP**: Begin audit using MCP for quick assessment
2. **Bulk Export for Deep Dive**: Use API scripts for comprehensive evidence download
3. **Verify Everything**: MCP shows Vanta data - still verify through interviews/observation
4. **Document MCP Queries**: Save conversation history as audit trail
5. **Reference Vanta IDs**: Include Vanta policy IDs, control IDs in findings
6. **Cross-Check**: Validate MCP responses against actual Vanta interface periodically

---

## Limitations

- MCP Server capabilities depend on Vanta's implementation
- Some data may require manual Vanta access
- Network connectivity required
- Claude Desktop required for MCP
- Subject to Claude's context limits

For offline audits or bulk operations, use API scripts instead.

---

## Next Steps

1. Complete MCP setup using `mcp_setup_guide.md`
2. Test connection with simple queries
3. Begin audit using conversational approach
4. Document findings using templates
5. Create CARs in Vanta for all nonconformities

