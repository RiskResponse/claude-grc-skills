# Vanta Platform Audit Workflow

## Overview

This guide explains how to conduct ISO 27001:2022 internal audits using Vanta as your GRC (Governance, Risk, and Compliance) platform. Vanta centralizes policies, controls, risks, evidence, and tasks - making it an ideal platform for audit management.

**References**:
- [Vanta Internal Audit Guide](https://help.vanta.com/en/articles/11345810-understanding-an-iso-internal-audit)
- [Vanta GRC Collection](https://www.vanta.com/collection/grc/internal-compliance-audit)

---

## Pre-Audit: Exporting Evidence from Vanta

###Export Checklist

Before beginning the audit, export the following from Vanta:

**1. Policies** (`/policies` or export function):
- All published policies
- Policy approval records
- Version history
- Review dates and responsible parties
- Employee acknowledgments

**2. Controls** (`/controls` dashboard):
- Control inventory with implementation status
- Control owners and descriptions
- Test results and frequencies
- Evidence uploads per control
- Control mapping to frameworks

**3. Risks** (`/risks` module):
- Complete risk register
- Risk assessments with likelihood/impact
- Risk treatment plans
- Risk owners
- Residual risk levels

**4. Tasks** (`/tasks` view):
- Completed and pending compliance tasks
- Task assignments and due dates
- Task completion evidence
- Overdue task report

**5. Tests** (`/tests` section):
- Automated and manual test results
- Test schedules and frequencies
- Pass/fail status
- Test evidence

**6. Vendors** (`/vendors` or `/trust` section):
- Vendor inventory
- Vendor risk assessments
- Security questionnaires
- Vendor SOC 2/certifications
- Vendor monitoring activities

**7. Personnel** (`/personnel` or `/access`):
- User access reviews
- Training completion records
- Onboarding/offboarding records
- Role assignments

**8. Reports and Dashboards**:
- Compliance posture overview
- Control effectiveness metrics
- Risk heat map
- Task completion rates
- Overdue items report

---

## Step-by-Step Vanta Audit Process

### Step 1: Document Review in Vanta

**Review Policies**:
1. Navigate to Vanta policies section
2. For each required policy (see Annex A.5.1):
   - Check policy exists
   - Verify management approval (approval workflow/signatures)
   - Check last review date (must be within 12 months)
   - Verify version control
   - Confirm communication/publication to personnel
3. Export policies for detailed review
4. Note gaps: missing policies, overdue reviews, no approvals

**Review Statement of Applicability (SoA)**:
1. Locate SoA in Vanta (often in `/framework` or `/controls`)
2. Verify all 93 Annex A controls addressed
3. Check justifications for:
   - Controls included
   - Controls excluded
   - Controls not applicable
4. Confirm SoA approved by management
5. Verify SoA updated when risks change

**Review Risk Assessment**:
1. Access Vanta risk register
2. Verify risk assessment methodology documented
3. Check all critical assets have risks identified
4. Validate likelihood and impact ratings
5. Confirm risk acceptance criteria defined
6. Verify risk owners assigned
7. Check risk assessment performed/updated within 12 months

**Review Risk Treatment Plan**:
1. Identify all risks rated as unacceptable
2. Verify treatment plan exists for each
3. Check controls from Annex A selected for treatment
4. Confirm treatment plan approved by risk owners
5. Verify implementation status of treatments

### Step 2: Evidence Analysis

**For Each Control in Vanta**:

**Control Status Check**:
- "Implemented" - Proceed to evidence review
- "Not Implemented" - Verify if control should be N/A or is gap
- "In Progress" - Check target date, may be observation/NC

**Evidence Adequacy Assessment**:

**Question 1**: Is evidence uploaded?
- No evidence → Potential NC (control not really implemented)
- Evidence uploaded → Proceed to Question 2

**Question 2**: Is evidence recent and relevant?
- Check evidence date (should be within test frequency period)
- Verify evidence actually demonstrates control operation
- Confirm evidence relates to correct control

**Question 3**: Is evidence complete?
- For access reviews: List of users, review date, approver
- For backups: Backup logs, success indicators, restore tests
- For training: Training records, completion dates, employee names
- For vulnerability scans: Scan results, remediation tracking

**Red Flags (Potential NCs)**:
- ✗ Control marked "Implemented" with no evidence
- ✗ Evidence older than test frequency (e.g., quarterly test, evidence from 8 months ago)
- ✗ Generic screenshots without context or dates
- ✗ "Coming soon" or placeholder evidence
- ✗ Evidence doesn't actually prove control works

**Good Evidence Examples**:
- ✓ Access review report dated within last quarter showing all users reviewed
- ✓ Backup logs from last 30 days showing daily successful backups
- ✓ Vulnerability scan results from last month with remediation status
- ✓ Training completion report showing all employees completed annual training

### Step 3: Test Result Validation

**Automated Tests**:
1. Review test configuration in Vanta
2. Check test frequency (daily, weekly, monthly, quarterly)
3. Verify tests ran on schedule
4. Review pass/fail results
5. For failures: Check remediation actions

**Manual Tests**:
1. Review test procedure/description
2. Check test performer and date
3. Verify test evidence uploaded
4. Assess test adequacy (does it really test the control?)

**Common Test Gaps**:
- Tests not run per schedule
- Failed tests with no remediation
- Test procedures unclear
- Test evidence insufficient

### Step 4: Task and Workflow Review

**Completed Tasks**:
- Verify tasks completed on time
- Check completion evidence adequate
- Confirm responsible party assigned

**Overdue Tasks**:
- Identify all overdue tasks
- Assess impact on ISMS (may be NC if critical)
- Understand root cause of delays

**Recurring Tasks**:
- Verify recurring tasks configured correctly
- Check completion pattern (are they being done consistently?)

---

## Audit Finding Documentation with Vanta Evidence

### Referencing Vanta Evidence in Findings

**Format**: Be specific about Vanta source

**Policy Reference Example**:
> **Evidence**: Vanta Policy "Incident Response Procedure" (ID: POL-2024-015, Version 2.1, Published: 2023-04-15, Last Review: 2023-04-15). Review date exceeds 12-month requirement (19 months old as of audit date 2024-11-04).

**Control Evidence Example**:
> **Evidence**: Vanta Control A.8.13 (Information Backup). Control status: "Implemented." Control owner: IT Operations Manager. Last test date: 2024-09-15. Test frequency: Quarterly. Evidence uploaded: "Backup_Logs_Q3_2024.pdf" showing daily backups successful. Evidence adequate and recent.

**Risk Evidence Example**:
> **Evidence**: Vanta Risk Register, Risk ID: RISK-2024-042 "Unauthorized access to customer database." Risk level: High (Likelihood: 3, Impact: 4). Treatment plan: Empty. Risk owner: CISO. No controls assigned for treatment. Risk assessed: 2024-02-20 (9 months ago).

**Task Evidence Example**:
> **Evidence**: Vanta Task "Quarterly Access Review Q3 2024" (TASK-2024-Q3-AR). Due date: 2024-09-30. Status: Overdue (35 days). Assigned to: IT Security Manager. No completion evidence. Previous quarterly reviews (Q1, Q2) completed on time.

### Mapping Vanta Controls to ISO 27001

Vanta often uses control IDs that map to ISO 27001 Annex A. Verify mapping:

**In Your Finding**:
> **Reference**: ISO 27001:2022 Control A.5.15 (Access Control)
>
> **Vanta Control**: "Access Control Policy" (CTRL-AC-001)
>
> [Continue with finding details...]

---

## Nonconformity Examples from Vanta Audits

### Example 1: Missing Evidence (Minor NC)

**Reference**: ISO 27001:2022 Control A.8.8 (Management of Technical Vulnerabilities)

**Requirement**: Technical vulnerabilities shall be identified and remediated

**Finding**: While quarterly vulnerability scans are configured in Vanta, no scan results were uploaded for Q2 2024.

**Evidence**:
- Vanta Control A.8.8 status: "Implemented"
- Test schedule: Quarterly
- Evidence uploads:
  - Q1 2024: "Vuln_Scan_Q1_2024.pdf" (uploaded 2024-04-05)
  - Q2 2024: No evidence
  - Q3 2024: "Vuln_Scan_Q3_2024.pdf" (uploaded 2024-10-02)
- Interview with Security Engineer (2024-11-01): confirmed scan performed in Q2 but forgot to upload to Vanta

**Classification**: Minor NC (isolated incident, scan was performed, just not documented)

### Example 2: Policy Not Reviewed (Minor NC)

**Reference**: ISO 27001:2022 Control A.5.1 (Policies for Information Security)

**Requirement**: Policies shall be reviewed at planned intervals

**Finding**: The Backup and Recovery Policy has not been reviewed within the required 12-month interval.

**Evidence**:
- Vanta Policy "Backup and Recovery Policy v1.3"
- Last review date: 2023-05-20
- Audit date: 2024-11-04 (18 months since review)
- Policy states "Annual review by IT Manager"
- Interview with IT Manager (2024-11-01): acknowledged review overdue

**Classification**: Minor NC

### Example 3: Risk Treatment Not Implemented (Major NC)

**Reference**: ISO 27001:2022 Clause 6.1.3 (Information Security Risk Treatment)

**Requirement**: Unacceptable risks must be treated with selected controls

**Finding**: High-risk finding "Lack of MFA for admin accounts" identified 8 months ago has no treatment plan or controls implemented.

**Evidence**:
- Vanta Risk ID: RISK-2024-018
- Risk title: "Lack of MFA for privileged accounts"
- Risk level: High (L:4, I:4)
- Risk date: 2024-03-10
- Treatment plan: None
- Controls assigned: None
- Risk owner: CISO
- Follow-up: Vanta shows no task created, no controls implemented, no progress notes

**Classification**: Major NC (systematic failure to treat identified high risks)

### Example 4: Observation (Not NC)

**Finding Type**: Observation

**Description**: Backup restore testing is performed annually, meeting minimum requirements. However, industry best practice for SaaS companies is quarterly restore testing to ensure faster recovery and higher confidence in backup integrity.

**Evidence**: Vanta Control A.8.13 test records show annual restore test (last: 2024-03-15, successful). Backup Policy specifies annual testing.

**Recommendation**: Consider increasing restore test frequency to quarterly.

---

## Vanta Evidence Types and Adequacy

### Policy Evidence

**Adequate**:
- ✓ Signed approval form or email
- ✓ Version-controlled document
- ✓ Publication/distribution records
- ✓ Employee acknowledgment reports

**Inadequate**:
- ✗ Draft policies marked "final"
- ✗ Unapproved policies
- ✗ No evidence of communication
- ✗ Policies with [TODO] or placeholders

### Access Control Evidence

**Adequate**:
- ✓ User access list with roles and permissions
- ✓ Access review report with reviewer signature and date
- ✓ Approval for new access (ticket, email, form)
- ✓ Termination checklist showing access revoked

**Inadequate**:
- ✗ Screenshot of login page (proves nothing)
- ✗ Generic statement "access is controlled"
- ✗ Unsigned access review
- ✗ Outdated user list

### Backup Evidence

**Adequate**:
- ✓ Backup logs showing successful daily backups
- ✓ Restore test results with date and success confirmation
- ✓ Backup monitoring dashboard
- ✓ Backup schedule configuration

**Inadequate**:
- ✗ Statement "backups are performed"
- ✗ Screenshot of backup tool without logs
- ✗ Backup policy only (no proof backups actually run)
- ✗ No restore testing

### Training Evidence

**Adequate**:
- ✓ Training completion report with names and dates
- ✓ Training materials/curriculum
- ✓ Attendance sheets or LMS records
- ✓ Training acknowledgment forms

**Inadequate**:
- ✗ Training policy only
- ✗ Generic "all employees trained"
- ✗ No completion dates
- ✗ Missing records for some employees

---

## Post-Audit: Managing Findings in Vanta

### Creating Nonconformity Tasks

For each nonconformity found:

1. **Create Task in Vanta**:
   - Title: "NC-[number]: [Brief description]"
   - Description: Full NC details (requirement, finding, evidence)
   - Assign to: Control owner or responsible manager
   - Due date: Based on severity (30 days minor, 60 days major)
   - Tags: "Internal Audit," "Nonconformity," "ISO 27001"

2. **Link to Control**:
   - Associate task with related Annex A control
   - Update control status if needed

3. **Define Acceptance Criteria**:
   - What evidence is needed to close?
   - Root cause analysis required
   - Corrective action implementation proof

### Tracking Corrective Actions

**In Vanta**:
- Monitor task status (Not Started → In Progress → Complete)
- Review uploaded evidence for adequacy
- Communicate with task owners
- Set reminders for follow-up audits

**Follow-Up Audit**:
- Review completed tasks
- Verify new evidence uploaded
- Conduct mini-audit to validate fix
- Close or re-open based on findings

---

## Vanta Reporting Features

### Audit Trail in Vanta

Vanta automatically tracks:
- Policy changes and versions
- Control status changes
- Evidence uploads
- Task completions
- Test results over time

**Use for Audit**:
- Review activity logs
- Identify when changes occurred
- Track compliance trends
- Prepare audit report metrics

### Compliance Dashboard

**Key Metrics from Vanta**:
- Control implementation %
- Overdue tasks count
- Risk treatment coverage
- Policy review status
- Test pass rates

**Include in Audit Report**:
- Current compliance posture
- Trends (improving/declining)
- Areas of concern

---

## Common Vanta-Specific Findings

### Missing Evidence in Vanta

**NC**: Control marked "Implemented" but no evidence uploaded

**Example**:
> Control A.6.3 (Information Security Awareness) status: "Implemented."  
> Evidence uploads: None.  
> This is a nonconformity - implementation cannot be verified.

### Overdue Policy Reviews

**NC/Observation**: Policies in Vanta showing review dates > 12 months

**Check**: Vanta policy list, sort by "Last Review Date"

### Incomplete Risk Treatment

**NC**: Vanta risks at "High" or "Critical" with no treatment plan

**Check**: Risk register filtered by severity, verify treatment plans exist

### Failed Tests Not Addressed

**NC/Observation**: Vanta test results showing failures without remediation

**Check**: Test history, filter for "Failed," verify follow-up actions

---

## Integration with ISO 27001 Requirements

### Clause 9.2: Internal Audit

Vanta helps satisfy ISO 27001 Clause 9.2 by:
- Documenting audit program (in Vanta or externally)
- Tracking audit schedule
- Storing audit results
- Managing corrective actions
- Providing audit evidence trail

**What to Verify**:
- Audit program documented (can be in Vanta tasks/calendar)
- Audit results stored (upload audit reports to Vanta)
- Corrective actions tracked (Vanta tasks)
- Independence maintained (auditor doesn't audit own work)

---

## Best Practices for Vanta Audits

1. **Export Early**: Get all exports 1-2 weeks before audit
2. **Organize Exports**: Create folder structure for easy reference
3. **Cross-Reference**: Link Vanta IDs in your audit checklist
4. **Screenshot Dashboard**: Capture compliance posture at audit date
5. **Validate in Person**: Don't rely solely on Vanta - interview and observe
6. **Document Vanta Gaps**: If evidence missing in Vanta, note it
7. **Use Vanta for CARs**: Create tasks for all nonconformities
8. **Track in One Place**: Centralize audit management in Vanta
9. **Export Audit Report**: Upload final report to Vanta for records
10. **Set Reminders**: Use Vanta to schedule next internal audit

---

## Troubleshooting

**Issue**: Control shows "Implemented" but seems inadequate

**Solution**: Interview control owner, observe actual implementation, don't assume Vanta status is accurate. Vanta is a tool; verify reality.

**Issue**: Evidence in Vanta is generic/unclear

**Solution**: Request additional evidence during audit. Adequate evidence is auditor's requirement, not Vanta's.

**Issue**: Can't find specific evidence in Vanta

**Solution**: Ask auditee directly. Vanta may not contain everything - documentation could be in SharePoint, Google Drive, etc.

**Issue**: Vanta shows conflicts (e.g., control marked complete but test failed)

**Solution**: Investigate discrepancy. This is often an audit finding.

---

Vanta is a powerful tool for managing ISO 27001 compliance, but the audit must verify reality, not just Vanta status. Use Vanta exports as starting point, then validate through interviews, document review, and observation.

