---
name: iso27001-internal-auditor
description: Expert guidance for conducting ISO 27001:2022 internal audits using Vanta platform. Covers the complete 7-step audit process, evidence analysis, nonconformity identification, and audit reporting for SaaS companies. Use when performing annual ISMS internal audits, reviewing Vanta-exported evidence, or documenting audit findings.
license: Apache-2.0
---

# ISO 27001:2022 Internal Auditor

## Overview

This skill provides comprehensive guidance for conducting ISO 27001:2022 internal audits of Information Security Management Systems (ISMS), with specific focus on:

- **7-step audit methodology** from planning to corrective action follow-up
- **Vanta platform integration** for evidence review and audit management
- **All ISO 27001:2022 requirements** (Clauses 4-10 + 93 Annex A controls)
- **Finding classification** (nonconformities, observations, recommendations)
- **SaaS company considerations** (cloud controls, multi-tenancy, DevSecOps)

Designed for experienced compliance teams performing annual internal audits.

**Keywords**: ISO 27001, internal audit, ISMS, Vanta, nonconformity, audit findings, Annex A controls, information security, audit report

## When to Use This Skill

Use this skill when you need to:
- Conduct annual ISO 27001 internal audit
- Review and analyze evidence exported from Vanta
- Create audit checklists for ISO 27001:2022
- Identify nonconformities, observations, and recommendations
- Write professional internal audit reports
- Document corrective action requests
- Perform corrective action follow-up
- Ensure complete coverage of all ISO 27001 requirements

## The 7-Step Internal Audit Process

ISO 27001 internal audits follow a structured 7-step methodology:

### Step 1: Document Review

**Purpose**: Review ISMS documentation for compliance and prepare for main audit

**Activities**:
- Review Information Security Policy
- Review all applicable procedures and documented information
- Review Statement of Applicability (SoA)
- Review Risk Assessment and Risk Treatment Plan
- Review records (management review, incidents, corrective actions)
- Check documentation against ISO 27001:2022 requirements
- Identify areas to investigate during main audit

**In Vanta**:
- Export and review all policies
- Review control implementation status
- Examine risk register and treatment plans
- Review completed tasks and tests
- Check document versioning and approval status

**Output**: Notes on potential nonconformities, areas requiring investigation

**Template**: Use document review checklist from `templates/vanta_evidence_analysis_checklist.md`

### Step 2: Create Internal Audit Checklist

**Purpose**: Prepare structured notes to guide the main audit

**Activities**:
- List all requirements to be audited (clauses + Annex A controls)
- Note what evidence to look for
- Identify who to interview
- Plan which records to sample
- Prepare questions based on document review findings

**Four-Column Format**:
1. **Reference** - Clause or control number
2. **What to look for** - Requirements, questions, evidence to examine
3. **Compliance** - Y/N/Partial/N/A (fill during audit)
4. **Findings** - Evidence found (fill during audit)

**Template**: `templates/audit_checklist_iso27001_2022.md` (93 Annex A controls + clauses 4-10)

**Script**: `scripts/checklist_generator.py` can create customized checklists based on scope

### Step 3: Write Audit Plan

**Purpose**: Define detailed logistics for the audit

**Activities**:
- Set audit dates and times
- Identify departments/processes to audit
- List contact persons for each area
- Define audit team roles (if multiple auditors)
- Communicate plan to auditees
- Schedule opening meeting (if applicable)

**Template**: `templates/audit_plan_individual.md`

### Step 4: Conduct Main Audit

**Purpose**: Gather evidence through on-site examination

**Three Evidence Collection Techniques**:

1. **Reviewing Documents and Records**:
   - Most reliable evidence
   - Examine policies, procedures, records
   - Check Vanta evidence uploads (screenshots, logs, reports)
   - Verify document versions, approval dates, completeness

2. **Interviewing Employees**:
   - Speak to multiple people for same process
   - Ask open-ended questions
   - Verify understanding of procedures
   - Check awareness of responsibilities

3. **Observing Activities and Facilities**:
   - Visit server rooms, secure areas
   - Observe processes in action
   - Check physical security controls
   - Verify configurations match documentation

**During Main Audit**:
- Follow your checklist but remain flexible
- Document all evidence immediately
- Record exact names, dates, versions
- Note direct quotes from interviews
- Take photos/screenshots if appropriate
- Don't make assumptions - verify everything

**Recording Evidence**:
- Fill columns 3 and 4 of your checklist
- Note specific evidence (document names, record IDs, person names)
- Reference Vanta evidence (task IDs, test results, policy versions)
- Document timestamps and locations

### Step 5: Write Internal Audit Report

**Purpose**: Document all findings formally

**Required Sections**:
1. **General Information**:
   - Audit date, auditor name(s)
   - Audit scope and criteria
   - Audit objectives
   - Auditees

2. **Audit Findings**:
   - **Nonconformities** (with full structure - see below)
   - **Observations** (potential issues, best practices not followed)
   - **Recommendations** (improvement opportunities)

3. **Audit Conclusions**:
   - Overall compliance assessment
   - System effectiveness evaluation
   - Readiness for certification audit
   - Key themes or patterns

**Nonconformity Structure** (4 elements):
1. **Reference**: Exact clause/control number (e.g., "ISO 27001:2022 Clause 6.1.2")
2. **Requirement**: Brief description of requirement not met
3. **Finding**: What was found (the gap)
4. **Evidence**: Specific proof (document name, interview quote, observation details)

**Template**: `templates/internal_audit_report.md`

**Script**: `scripts/audit_report_generator.py` compiles findings into formatted report

### Step 6: Initiate Corrective Actions

**Purpose**: Formally request resolution of nonconformities

**Activities**:
- Create Corrective Action Request (CAR) for each nonconformity
- Assign responsible person
- Set deadline for resolution
- Define root cause analysis requirement
- Track in Vanta or corrective action system

**Template**: `templates/nonconformity_report.md` and `templates/corrective_action_plan.md`

**In Vanta**:
- Create tasks for each nonconformity
- Assign to control owners
- Set due dates
- Link to audit findings
- Track remediation progress

### Step 7: Corrective Action Follow-Up

**Purpose**: Verify nonconformities are actually resolved

**Activities**:
- Review completed corrective actions
- Verify evidence of implementation
- Conduct mini-audit of corrected areas
- Confirm root cause addressed
- Close CARs or re-open if inadequate
- Update audit records

**Timeline**: Typically 30-90 days after audit depending on NC severity

**In Vanta**:
- Review corrective action task completion
- Verify new evidence uploaded
- Validate control status updated
- Close audit findings

## Working with Vanta Platform

### Three Methods for Evidence Retrieval

**Method 1: Vanta API Scripts (Automated - Recommended)**
- Use `scripts/vanta_api/retrieve_all.py` for bulk export
- Automated download of all policies and evidence
- Auto-generates audit notes with potential findings
- See: `references/vanta_api_integration.md`

**Method 2: Vanta MCP Server (Interactive)**
- Real-time queries during audit conversations
- Natural language evidence retrieval
- Integrated with Claude Desktop
- See: `mcp/mcp_setup_guide.md` and `mcp/mcp_audit_workflow.md`

**Method 3: Manual Export (Fallback)**
- Traditional manual download from Vanta web interface
- Use when API/MCP not available

### Vanta Exports for Audit

**Using API Scripts** (Recommended):
```bash
# Retrieve all policies and evidence automatically
cd scripts/vanta_api
python3 retrieve_all.py

# Creates organized exports in vanta_exports/
```

**Using MCP Server** (Interactive):
In Claude Desktop with Vanta MCP configured:
> "Using Vanta MCP Server, export all policies and check for overdue reviews"

**Manual Export** (if needed):
Before the audit, export from Vanta:

**Policies**:
- All current policies (markdown or PDF)
- Version history
- Approval records
- Review dates

**Controls**:
- Control implementation status
- Control owners
- Test results
- Evidence uploads

**Risks**:
- Risk register export
- Risk assessments
- Treatment plans
- Risk owners

**Tasks**:
- Completed and pending tasks
- Task assignments
- Completion dates
- Evidence attached to tasks

**Tests**:
- Automated test results
- Manual test records
- Test frequencies
- Pass/fail status

**Vendors**:
- Vendor inventory
- Security assessments
- Questionnaire responses
- Vendor risk ratings

### Analyzing Vanta Evidence

**Policy Review**:
- ✓ Check: All required policies exist (see Annex A.5.1)
- ✓ Check: Policies approved by management
- ✓ Check: Policies reviewed within 12 months
- ✓ Check: Policies communicated to personnel
- ✓ Check: Version control maintained
- ✗ Common Gap: Policies not formally approved
- ✗ Common Gap: Review dates overdue

**Control Implementation**:
- ✓ Check: All applicable controls from SoA implemented
- ✓ Check: Control owners assigned
- ✓ Check: Testing completed per schedule
- ✓ Check: Evidence uploaded and adequate
- ✗ Common Gap: Controls marked "implemented" but no evidence
- ✗ Common Gap: Test frequency not followed

**Risk Assessment**:
- ✓ Check: Risk assessment methodology documented
- ✓ Check: All assets have risks identified
- ✓ Check: Likelihood and impact assessed
- ✓ Check: Treatment plans for unacceptable risks
- ✓ Check: Risk owners assigned
- ✗ Common Gap: Risk assessment not updated in 12 months
- ✗ Common Gap: Treatment plans incomplete

**Use**: `templates/vanta_evidence_analysis_checklist.md` for systematic review

### Vanta Evidence Reference Format

When documenting findings, reference Vanta evidence clearly:

**Good Example**:
> "Evidence: Vanta Policy 'Access Control Policy v2.1' shows last review date of 2023-01-15, exceeding the 12-month review requirement (ISO 27001:2022 Clause A.5.1). Current date: 2024-11-04 (22 months since review)."

**Good Example**:
> "Evidence: Vanta Control 'A.8.15 - Logging' status shows 'Implemented' but no test results uploaded. Control owner: IT Manager. Last test date field: empty."

## Finding Classification

### Nonconformity (NC)

**Definition**: A requirement is not met

**When to Raise NC**:
- ISO 27001:2022 requirement violated
- Company's own policy/procedure not followed
- Legal/regulatory requirement not met
- Contractual requirement (SLA, customer) not met

**NC Must Have**:
1. **Clear evidence** of the gap
2. **Specific requirement** violated
3. **Impact** on ISMS effectiveness

**Major NC**:
- Complete absence of required element (e.g., no management review performed)
- Systematic failure (e.g., backup performed randomly, not daily as required)
- Multiple minor NCs in same area (indicates systemic problem)
- Previous NC not resolved by deadline

**Minor NC**:
- Isolated incident (e.g., backup missed one day)
- Documentation gap (e.g., one training record missing)
- Requirement partially met

**Examples**:

**Major NC Example**:
> **Reference**: ISO 27001:2022 Clause 9.3 (Management Review)
>
> **Requirement**: Management review must be conducted at planned intervals
>
> **Finding**: No management review was conducted in 2024. The ISMS procedure requires annual management review by Q1 each year.
>
> **Evidence**: Management review procedure v1.2 states "annual review by March 31." No meeting minutes, agenda, or attendance records found for 2024. Interview with CISO (2024-11-01) confirmed no review conducted. Vanta tasks for management review show status "Not Started."

**Minor NC Example**:
> **Reference**: ISO 27001:2022 Clause A.7.2 (Competence)
>
> **Requirement**: Training records must be maintained for all personnel
>
> **Finding**: Training record for security awareness training is missing for one new employee hired in October 2024.
>
> **Evidence**: Vanta training tracker shows 47/48 employees completed security awareness training. Employee "J. Smith" (hired 2024-10-15) shows no training completion. HR Manager confirmed employee not yet trained due to onboarding delay.

### Observation

**Definition**: Potential issue that could become a nonconformity

**When to Raise Observation**:
- Isolated deviation that doesn't impact ISMS effectiveness
- Process that could be improved but meets minimum requirements
- Best practice not followed (but not required)
- Early warning of potential future NC

**Example**:
> **Observation**: The Incident Response Procedure was last reviewed 11 months ago, approaching the 12-month review requirement. While currently compliant, establish a reminder process to ensure timely reviews.

### Recommendation

**Definition**: Improvement opportunity beyond compliance

**When to Raise Recommendation**:
- Efficiency improvements possible
- Industry best practices not adopted
- Additional security measures would be beneficial
- Process optimization opportunities

**Example**:
> **Recommendation**: Consider implementing automated policy review reminders in Vanta. While manual tracking is compliant, automation would reduce administrative burden and ensure no policies exceed review dates.

## ISO 27001:2022 Audit Scope

### Clauses 4-10 (ISMS Requirements)

**Clause 4 - Context of the Organization**:
- 4.1: Understanding organization and context
- 4.2: Understanding needs of interested parties
- 4.3: Determining scope of ISMS
- 4.4: Information security management system

**Clause 5 - Leadership**:
- 5.1: Leadership and commitment
- 5.2: Policy
- 5.3: Organizational roles, responsibilities, authorities

**Clause 6 - Planning**:
- 6.1: Actions to address risks and opportunities
- 6.1.1: General
- 6.1.2: Information security risk assessment
- 6.1.3: Information security risk treatment
- 6.2: Information security objectives and planning
- 6.3: Planning of changes

**Clause 7 - Support**:
- 7.1: Resources
- 7.2: Competence
- 7.3: Awareness
- 7.4: Communication
- 7.5: Documented information

**Clause 8 - Operation**:
- 8.1: Operational planning and control
- 8.2: Information security risk assessment
- 8.3: Information security risk treatment

**Clause 9 - Performance Evaluation**:
- 9.1: Monitoring, measurement, analysis and evaluation
- 9.2: Internal audit
- 9.3: Management review

**Clause 10 - Improvement**:
- 10.1: Nonconformity and corrective action
- 10.2: Continual improvement

For detailed requirements, see: `references/iso27001_2022_requirements.md`

### Annex A Controls (93 Controls in ISO 27001:2022)

**Organizational Controls (A.5.1 - A.5.37)**: 37 controls
**People Controls (A.6.1 - A.6.8)**: 8 controls
**Physical Controls (A.7.1 - A.7.14)**: 14 controls
**Technological Controls (A.8.1 - A.8.34)**: 34 controls

**Total**: 93 controls

Complete checklist: `templates/audit_checklist_iso27001_2022.md`

## SaaS-Specific Audit Considerations

### Cloud Infrastructure Controls

**Key Annex A Controls for SaaS**:
- **A.5.23**: Information security for cloud services
- **A.8.9**: Configuration management
- **A.8.14**: Redundancy of information processing facilities
- **A.8.20**: Networks security
- **A.8.31**: Separation of development, testing, production

**What to Audit**:
- Cloud provider selection and monitoring (A.5.22)
- Shared responsibility model documentation
- Cloud configuration management
- Multi-region deployment for redundancy
- Infrastructure as Code (IaC) security

**Vanta Evidence**:
- Cloud provider SOC 2 reports
- Configuration management policies
- Infrastructure diagrams
- Backup and DR procedures
- Cloud security posture test results

### Multi-Tenant Security

**Key Controls**:
- **A.5.10**: Acceptable use of information
- **A.5.14**: Information transfer
- **A.8.11**: Data masking
- **A.8.12**: Data leakage prevention
- **A.8.22**: Segregation in networks

**What to Audit**:
- Tenant data isolation mechanisms
- Cross-tenant access prevention
- Tenant-specific access controls
- Data segregation architecture
- Isolation testing results

**Vanta Evidence**:
- Multi-tenancy architecture documentation
- Tenant isolation test results
- Access control configurations
- Penetration test reports focusing on isolation

### DevSecOps and CI/CD

**Key Controls**:
- **A.8.25**: Secure development lifecycle
- **A.8.26**: Application security requirements
- **A.8.27**: Secure system architecture
- **A.8.28**: Secure coding
- **A.8.29**: Security testing
- **A.8.30**: Outsourced development
- **A.8.32**: Change management

**What to Audit**:
- CI/CD pipeline security controls
- Code review processes
- Security testing (SAST, DAST, SCA)
- Secrets management
- Deployment approval processes
- Rollback procedures

**Vanta Evidence**:
- Secure SDLC policy
- Code review records
- Security scan results
- Deployment logs
- Change management tickets

For comprehensive SaaS guidance, see: `references/saas_isms_considerations.md`

## Evidence Analysis and Sampling

### Sampling Principles

When you cannot examine all records:

**Focus On**:
- **High-risk areas** from risk assessment
- **Critical controls** (access control, encryption, backup)
- **New employees** (higher likelihood of training gaps)
- **Recent changes** (higher likelihood of issues)
- **Previous audit findings** (verify resolution)

**Sample Size Guidelines**:
- Small population (< 20): Review all
- Medium population (20-100): Review 10-30%
- Large population (> 100): Review statistical sample or risk-based selection

**Auditor Choice**: You select records to sample, not the auditee

### Vanta Evidence Adequacy

**Adequate Evidence**:
- ✓ Screenshots showing actual configurations
- ✓ Logs with timestamps and relevant data
- ✓ Approved policy documents with dates
- ✓ Test results with pass/fail criteria
- ✓ Training completion with names and dates

**Inadequate Evidence**:
- ✗ Generic screenshots without context
- ✗ Undated documents
- ✗ Incomplete logs
- ✗ "Evidence pending" status for implemented controls
- ✗ Self-attestations without supporting proof

**When Evidence is Inadequate**: Raise observation or NC depending on severity

## Writing Effective Audit Findings

### Nonconformity Template

```
**NC-[number]**: [Brief title]

**Classification**: ☐ Major  ☐ Minor

**Reference**: ISO 27001:2022 [Clause/Control number]

**Requirement**: [Quote or paraphrase the requirement]

**Finding**: [Describe what was found that doesn't meet the requirement]

**Evidence**:
- [Specific evidence item 1 with source, date, location]
- [Specific evidence item 2]
- [Interview with [Person, Title] on [Date]]

**Impact**: [Brief description of impact on ISMS]

**Recommendation**: [Suggested corrective action - optional]
```

### Good vs. Poor Finding Examples

**Poor NC** (vague, no evidence):
> "Access control is not working properly."

**Good NC** (specific, clear evidence):
> **Reference**: ISO 27001:2022 Control A.5.18
>
> **Requirement**: Access rights shall be reviewed at regular intervals
>
> **Finding**: Access review was not performed in 2024. The Access Control Policy (v1.5, dated 2023-03-15) requires quarterly access reviews.
>
> **Evidence**:
> - Access Control Policy v1.5, Section 4.3 states "Quarterly review by IT Security Manager"
> - No access review reports found in shared drive for Q1, Q2, Q3 2024
> - Interview with IT Security Manager (2024-11-01): confirmed reviews not conducted due to resource constraints
> - Vanta Control A.5.18 status: "Implemented" but last test date: 2023-12-10
>
> **Impact**: Inappropriate access rights may persist, increasing risk of unauthorized access or privilege escalation.

## Audit Program and Planning

### Annual Audit Program

**Must Define**:
- Audit schedule for the year
- Which areas/departments to audit when
- Audit scope for each audit
- Audit criteria (ISO 27001:2022, policies, legal requirements)
- Audit methods (document review, interview, observation)
- Auditor assignments

**Template**: `templates/audit_program_annual.md`

**Focus Areas** (prioritize based on risk):
- Areas with high-risk assets
- Critical controls (access, encryption, backup)
- Areas with previous nonconformities
- New systems or significant changes
- Outsourced processes
- Third-party management

### Auditor Independence

**Conflict of Interest Rules**:
- Auditor cannot audit their own work
- Need minimum 2 auditors to cross-audit
- Auditor cannot report to person being audited
- External auditor acceptable if internal expertise lacking

**Auditor Competencies**:
- Knowledge of ISO 27001:2022
- Understanding of ISMS principles
- Familiarity with company operations
- Industry knowledge (SaaS for this skill)
- Auditing techniques
- Communication skills
- Evidence evaluation skills

## Common Pitfalls to Avoid

### Auditor Mistakes

1. **Making Assumptions**: Don't assume something is required - verify the actual requirement
2. **Being Too Prescriptive**: Focus on "what" (requirements) not "how" (implementation)
3. **Inadequate Evidence**: Every NC must have clear, documented evidence
4. **Missing Root Causes**: Don't just identify symptoms, find underlying causes
5. **Poor Communication**: Deliver findings diplomatically, not accusatorially
6. **Checklist Slavery**: Use checklist as guide, not rigid script
7. **Ignoring Positive Findings**: Note good practices, not just problems

### Documentation Mistakes

1. **Vague Language**: "Some," "regularly," "management" without specifics
2. **Missing Evidence References**: Every finding must cite specific evidence
3. **Unclear Requirements**: Must quote or precisely reference the standard
4. **Inconsistent Findings**: Same issue treated differently in different departments
5. **Typographical Errors**: Proofread before submitting

## Typical Audit Timeline

**Pre-Audit (2-4 weeks before)**:
- Week 1-2: Document review, Vanta export analysis
- Week 2-3: Checklist creation, audit plan finalization
- Week 3-4: Communicate audit plan to auditees

**Main Audit (1-3 days)**:
- Day 1 AM: Opening meeting, begin interviews
- Day 1 PM - Day 2: Evidence collection, interviews, observations
- Day 2-3: Complete evidence gathering, preliminary findings

**Post-Audit (1-2 weeks)**:
- Week 1: Compile findings, draft report
- Week 2: Finalize report, present to management, initiate CARs

**Follow-Up (30-90 days later)**:
- Verify corrective actions implemented
- Close nonconformities
- Update audit records

## Best Practices for Success

1. **Prepare Thoroughly**: Document review and checklist creation are critical
2. **Stay Objective**: Evidence-based findings only
3. **Be Specific**: Names, dates, versions, locations in all evidence
4. **Communicate Clearly**: Explain findings in plain language
5. **Focus on Improvement**: Audit is tool for system improvement, not blame
6. **Reference Vanta**: Link findings to specific Vanta evidence IDs
7. **Document Immediately**: Write evidence while fresh
8. **Verify Understanding**: Confirm your interpretation with auditees
9. **Think Risk-Based**: Prioritize high-risk areas
10. **Follow Through**: Audit isn't complete until CARs verified

## Resources

### Reference Documents
- `references/iso27001_2022_requirements.md` - All clauses and controls detailed
- `references/audit_methodology.md` - Complete 7-step process
- `references/vanta_audit_workflow.md` - Vanta platform integration
- `references/nonconformity_classification.md` - Finding types and examples
- `references/saas_isms_considerations.md` - SaaS-specific auditing
- `references/iso_internal_audit_guide_full.md` - Complete plain English guide
- `references/audit_checklist_complete.md` - Full ISO 27001 checklist
- `references/nonconformity_procedure.md` - NC handling procedure

### Templates
- `templates/audit_checklist_iso27001_2022.md` - 93 Annex A + Clauses 4-10
- `templates/audit_program_annual.md` - Annual program
- `templates/audit_plan_individual.md` - Individual audit plan
- `templates/internal_audit_report.md` - Complete report template
- `templates/nonconformity_report.md` - NC documentation
- `templates/corrective_action_plan.md` - CAR template
- `templates/vanta_evidence_analysis_checklist.md` - Vanta review checklist

### Examples
- `examples/sample_audit_findings_saas.md` - Real-world finding examples
- `examples/completed_audit_report_redacted.md` - Full audit report
- `examples/common_iso27001_gaps.md` - Common nonconformities

### Scripts
- `scripts/vanta_evidence_analyzer.py` - Analyze Vanta exports
- `scripts/checklist_generator.py` - Create custom checklists
- `scripts/finding_formatter.py` - Format findings consistently
- `scripts/audit_report_generator.py` - Generate reports

## Quick Start

1. **Export from Vanta**: Policies, controls, risks, tests, tasks
2. **Review Exports**: Use `templates/vanta_evidence_analysis_checklist.md`
3. **Create Checklist**: Use `templates/audit_checklist_iso27001_2022.md` or generate with script
4. **Plan Audit**: Complete `templates/audit_plan_individual.md`
5. **Conduct Audit**: Follow 7-step methodology
6. **Document Findings**: Use finding templates
7. **Write Report**: Use `templates/internal_audit_report.md`
8. **Initiate CARs**: Create corrective actions in Vanta

Your internal audit should be thorough, evidence-based, and focused on improving the ISMS effectiveness, not just checking boxes for certification.
