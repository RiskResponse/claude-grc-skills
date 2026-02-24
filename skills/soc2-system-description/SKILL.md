---
name: soc2-system-description
description: Expert guidance for writing and updating SOC 2 system descriptions with focus on Security (TSC SEC) and Availability (TSC A) trust service criteria. Optimized for experienced compliance teams in SaaS and Healthcare industries. Use when drafting system descriptions, updating existing descriptions for annual audits, or ensuring completeness of SOC 2 documentation.
license: Apache-2.0
---

# SOC 2 System Description Expert

## Overview

This skill provides comprehensive guidance for creating and updating SOC 2 system descriptions that comply with AICPA Trust Services Criteria, specifically focusing on:

- **Security (Common Criteria - SEC)**
- **Availability (Common Criteria - A)**

Optimized for experienced compliance teams in **SaaS** and **Healthcare** industries who need to update existing system descriptions or ensure completeness for auditor review.

**Keywords**: SOC 2, system description, Trust Services Criteria, Security, Availability, SaaS, Healthcare, HIPAA, compliance, audit, AICPA

## When to Use This Skill

Use this skill when you need to:
- Write a new SOC 2 system description
- Update an existing system description for annual audit
- Ensure completeness of system description sections
- Document controls for Security and Availability criteria
- Address SaaS multi-tenancy considerations
- Incorporate HIPAA requirements for Healthcare organizations
- Validate control coverage against TSC requirements
- Compare versions to track changes

## Quick Decision Tree

### Step 1: Determine Your Scenario

**New System Description?**
- Start with: `templates/system_description_complete.md`
- Review: `references/system_description_requirements.md`
- Industry template: `templates/saas_system_description.md` OR `templates/healthcare_system_description.md`

**Updating Existing Description?**
- Use: `scripts/version_comparison.py` to analyze changes needed
- Focus on: Updated controls, infrastructure changes, organizational changes
- Review: Change management requirements in `references/system_description_requirements.md`

### Step 2: Select Industry Focus

**SaaS Company?**
- Primary template: `templates/saas_system_description.md`
- Review: `references/saas_considerations.md`
- Focus on: Multi-tenancy, cloud infrastructure, API security

**Healthcare Company?**
- Primary template: `templates/healthcare_system_description.md`
- Review: `references/healthcare_hipaa_considerations.md`
- Focus on: PHI protection, HIPAA alignment, BAA requirements

### Step 3: Use Common Controls
- Use `references/common_saas_controls.md` to copy-paste standard controls (AWS, GitHub, etc.)
- Customize them to your specific environment
- This speeds up drafting significantly

### Step 4: Generate Diagrams
- Use `templates/diagram_templates.md` for Mermaid.js code blocks
- Create System Architecture, Network, and Data Flow diagrams instantly
- Copy-paste into Appendices B, C, and D

### Step 5: Validate Completeness

After drafting:
1. Run `scripts/completeness_checker.py` - Ensures all required sections present
2. Run `scripts/control_coverage_validator.py` - Validates TSC coverage
3. Review against auditor-specific requirements

## Workflow for AI Agents

When acting as an AI assistant helping a user write a SOC 2 system description:

1. **Initialize**: Ask the user for their company type (SaaS/Healthcare), cloud provider (AWS/GCP/Azure), and key tools (GitHub, Jira, etc.).
   - **Tip**: If the user uses **Drata**, refer to `references/common_saas_controls.md` for mappings to Drata controls.
2. **Select Template**: Load `templates/system_description_complete.md`.
3. **Drafting Strategy**:
   - **Draft Sections 1-3 First**: These are foundational context.
   - **Draft Section 5 (Controls) Next**: Use `references/common_saas_controls.md` to populate standard controls based on the user's stack.
   - **Create Diagrams**: Use `templates/diagram_templates.md` to generate Mermaid diagrams for the appendices.
   - **Draft Section 4 (Commitments) Last**: Ensure commitments align with the controls you just documented.
4. **Review**: Run `scripts/completeness_checker.py` iteratively to catch missing sections or placeholders.
5. **Final Polish**: Ensure tone is professional, objective, and specific (avoid "periodically", "regularly").

## System Description Structure (AICPA Required)

A complete SOC 2 system description must include these five sections:

### Section 1: Overview of the System

**Purpose**: Provide context about your organization and services

**Must Include**:
- Company background and history
- Nature of services provided
- Service delivery model
- Key stakeholders and their responsibilities
- Organizational structure relevant to controls
- Physical locations

**Template**: `templates/system_description_complete.md` (Section 1)

**Key Considerations**:
- Be specific about what services are in scope
- Clearly identify management responsible for controls
- For SaaS: Describe delivery model and architecture overview
- For Healthcare: Identify PHI handling and BAA relationships

### Section 2: System Components

**Purpose**: Describe the principal components of the system

**Five Required Components**:

1. **Infrastructure**: Hardware, physical facilities, network
2. **Software**: Applications, databases, operating systems, utilities
3. **People**: Personnel involved in governance, operations, security
4. **Procedures**: Automated and manual procedures for operating the system
5. **Data**: Information used and supported by the system

**Template**: `templates/system_description_complete.md` (Section 2)

**Key Considerations**:
- Document both internal and third-party components
- For SaaS: Detail cloud infrastructure (AWS, Azure, GCP)
- For Healthcare: Clearly identify PHI data flows
- Include logical and physical architecture diagrams
- List all significant third-party service providers

### Section 3: Boundaries

**Purpose**: Define what is and isn't included in the system

**Must Include**:
- Clear definition of system boundaries
- In-scope systems, applications, infrastructure
- Out-of-scope items with justification
- Integration points with other systems
- Third-party services (in-scope vs out-of-scope)
- Shared responsibility model (especially for cloud/SaaS)

**Template**: `templates/system_description_complete.md` (Section 3)

**Key Considerations**:
- Be explicit about exclusions to avoid scope creep
- Document customer responsibilities vs your responsibilities
- For SaaS: Define multi-tenant vs single-tenant boundaries
- For Healthcare: Clarify PHI vs non-PHI system boundaries
- Align boundaries with service commitments

### Section 4: Principal Service Commitments and System Requirements

**Purpose**: Articulate commitments to customers and system requirements

**Must Include**:
- Service Level Agreements (SLAs)
- Availability commitments and uptime targets
- Security commitments
- Performance requirements
- Recovery time objectives (RTO) and recovery point objectives (RPO)
- How commitments are measured and monitored
- Customer communication procedures

**Template**: `templates/system_description_complete.md` (Section 4)

**Key Considerations**:
- Commitments must be measurable
- Link commitments to specific controls
- For SaaS: Document API availability, multi-tenant SLAs
- For Healthcare: Include HIPAA-required commitments (breach notification, etc.)
- Ensure commitments align with contracts and marketing materials

### Section 5: Control Environment and Control Objectives

**Purpose**: Describe control environment and specific controls

**Must Include**:

**A. Control Environment Overview**:
- Organizational structure and governance
- Risk assessment process
- Information and communication systems
- Monitoring activities
- Management philosophy and operating style

**B. Control Objectives by Trust Service Criteria**:
- Security (Common Criteria) - all applicable control objectives
- Availability (Common Criteria) - all applicable control objectives

**C. Control Activities**:
- Detailed description of each control
- How controls operate
- Frequency of operation
- Who performs the control
- Evidence generated

**Templates**: 
- `templates/system_description_complete.md` (Section 5)
- `templates/control_matrix_security.md`
- `templates/control_matrix_availability.md`

**Key Considerations**:
- One control objective per TSC point requirement
- Controls should be testable and produce evidence
- Document compensating controls where applicable
- For SaaS: Address multi-tenant control considerations
- For Healthcare: Map controls to HIPAA safeguards

## Security (TSC SEC) - Common Criteria

The Security category addresses risks that could affect system security, including:

### TSC SEC Control Areas

**CC1: Control Environment**
- Demonstrates commitment to integrity and ethical values
- Board independence and oversight
- Management structure and responsibility
- Competence and accountability
- Performance measures and incentives

**CC2: Communication and Information**
- Obtains and uses relevant information
- Internal communication of information
- External communication with parties

**CC3: Risk Assessment**
- Specifies suitable objectives
- Identifies and analyzes risk
- Assesses fraud risk
- Identifies significant changes

**CC4: Monitoring Activities**
- Selects and develops ongoing evaluations
- Evaluates and communicates deficiencies

**CC5: Control Activities**
- Selects and develops control activities
- Technology controls
- Policies and procedures deployment

**CC6: Logical and Physical Access Controls**
- System access restriction and authorization
- User identification and authentication
- Prior access authorization removal
- Physical access controls
- System access logging and monitoring

**CC7: System Operations**
- System operation management
- Job scheduling and processing
- System capacity monitoring
- System monitoring and incident response
- Data backup and restoration

**CC8: Change Management**
- Change management procedures
- Change authorization and testing
- Emergency changes

**CC9: Risk Mitigation**
- Vendor and business partner risk management
- Asset inventory management
- Security incident response
- Business continuity and disaster recovery

For detailed Security criteria, see: `references/tsc_security_criteria.md`

### Security Control Documentation Best Practices

1. **Be Specific**: "Access is reviewed quarterly" not "Access is reviewed periodically"
2. **Identify Responsible Parties**: Name roles, not just "management"
3. **Link to Evidence**: Reference specific logs, reports, or artifacts
4. **Address Exceptions**: Document any gaps or compensating controls
5. **Update Regularly**: Controls change; keep descriptions current

## Availability (TSC A) - Common Criteria

The Availability category addresses system availability for operation and use as committed or agreed.

### TSC A Control Areas

**A1.1: Availability Objectives**
- Define and document availability objectives
- Communicate to stakeholders
- Monitor and measure against objectives

**A1.2: System Capacity**
- Monitor current system capacity
- Plan for future capacity needs
- Test capacity during peak loads
- Address capacity constraints

**A1.3: System Monitoring**
- Monitor system performance and availability
- Automated alerting for availability issues
- Dashboard and reporting
- Threshold definition and review

**Additional Availability Controls** (often integrated with Security):
- **Recovery Procedures**: Backup, restore, failover testing
- **Redundancy**: System redundancy, failover capabilities
- **Incident Response**: Availability incident procedures
- **Maintenance**: Planned maintenance with minimal disruption
- **SLA Monitoring**: Track and report on uptime commitments

For detailed Availability criteria, see: `references/tsc_availability_criteria.md`

### Availability Control Documentation Best Practices

1. **Quantify Commitments**: "99.9% uptime" not "high availability"
2. **Document Testing**: Include DR testing frequency and results
3. **Define RTO/RPO**: Specific recovery objectives
4. **Monitor and Report**: Describe how availability is measured
5. **Address Failures**: Document incident response for outages

## SaaS-Specific Considerations

When writing system descriptions for SaaS organizations:

### Multi-Tenancy

**Address**:
- Logical data segregation between customers
- Tenant isolation controls
- Resource allocation and limits
- Customer-specific configurations

**Documentation Approach**:
- Describe architecture ensuring tenant separation
- Detail controls preventing cross-tenant access
- Explain monitoring for isolation breaches

### Cloud Infrastructure

**Address**:
- Cloud provider details (AWS, Azure, GCP, etc.)
- Shared responsibility model
- Cloud-native security controls
- Infrastructure as Code (IaC)

**Documentation Approach**:
- Be explicit about what provider controls vs your controls
- Reference provider's SOC 2 reports
- Describe how you monitor provider security

### API Security and Availability

**Address**:
- API authentication and authorization
- API rate limiting
- API availability and performance
- API security testing

**Documentation Approach**:
- Document API security architecture
- Define API availability SLAs
- Describe API monitoring and alerting

For comprehensive SaaS guidance, see: `references/saas_considerations.md`

## Healthcare-Specific Considerations

When writing system descriptions for Healthcare organizations:

### HIPAA Alignment

**Address**:
- How SOC 2 controls support HIPAA compliance
- Business Associate Agreement (BAA) requirements
- PHI identification and protection
- HIPAA Security Rule alignment

**Documentation Approach**:
- Map SOC 2 controls to HIPAA safeguards
- Document PHI encryption (at rest and in transit)
- Describe access controls for PHI
- Detail audit logging for PHI access

### PHI Protection

**Address**:
- PHI identification in data flows
- Encryption requirements
- Access controls specific to PHI
- PHI disposal procedures

**Documentation Approach**:
- Clearly distinguish PHI from other data
- Detail technical safeguards
- Describe minimum necessary access
- Document de-identification processes (if applicable)

### Breach Notification

**Address**:
- Breach detection procedures
- HIPAA breach notification timeline (60 days)
- Breach assessment process
- Customer/patient notification procedures

**Documentation Approach**:
- Align with both SOC 2 and HIPAA requirements
- Document breach notification procedures
- Describe breach risk assessment process

For comprehensive Healthcare guidance, see: `references/healthcare_hipaa_considerations.md`

## Updating Existing System Descriptions

### Annual Update Workflow

**Step 1: Assess Changes Since Last Audit**
- Infrastructure changes (new cloud services, data centers)
- Organizational changes (new roles, restructuring)
- Process changes (new procedures, updated policies)
- Control changes (new controls, modified controls, removed controls)
- Third-party changes (new vendors, terminated vendors)

**Step 2: Use Version Comparison Tool**
```bash
python3 scripts/version_comparison.py old_description.md new_description.md
```
Generates change summary highlighting modifications.

**Step 3: Update Affected Sections**
- Focus updates on changed areas
- Maintain consistency across all five sections
- Update dates and version numbers
- Ensure control descriptions match actual operations

**Step 4: Validate Completeness**
```bash
python3 scripts/completeness_checker.py updated_description.md
python3 scripts/control_coverage_validator.py updated_description.md
```

**Step 5: Review with Stakeholders**
- Technical teams verify accuracy
- Security team confirms control descriptions
- Compliance team reviews for completeness
- Legal reviews commitments and contracts alignment

### Common Update Scenarios

**New Third-Party Service Added**:
- Update Section 2 (System Components) - add vendor
- Update Section 3 (Boundaries) - if impacts scope
- Update Section 5 (Controls) - add vendor management controls
- Update risk assessment documentation

**Infrastructure Migration** (e.g., moving to cloud):
- Update Section 2 (System Components) - new infrastructure
- Update Section 3 (Boundaries) - shared responsibility model
- Update Section 5 (Controls) - new cloud controls
- May require new control objectives

**Organizational Restructuring**:
- Update Section 1 (Overview) - new organizational chart
- Update Section 5 (Controls) - responsible parties
- Ensure reporting lines clear for control owners

**New Service/Feature Launched**:
- Assess if in scope for SOC 2
- Update Section 1 (Overview) - service description
- Update Section 2-5 as needed for new functionality
- May expand system boundaries

## Control Documentation Guidelines

### Writing Effective Control Descriptions

**Good Control Description Structure**:
1. **What**: Clearly state what the control does
2. **How**: Describe how the control operates
3. **Who**: Identify who performs the control
4. **When**: Specify frequency (daily, weekly, monthly, annually, event-driven)
5. **Evidence**: Note what evidence is generated

**Example - Good Control Description**:
> **Access Review Control (CC6.1)**
>
> **What**: The IT Security Manager reviews user access rights to production systems quarterly to ensure only authorized personnel have access.
>
> **How**: An automated report is generated from the identity management system listing all users with production access. The IT Security Manager reviews each user against their current role and employment status. Any inappropriate access is documented and removed within 48 hours.
>
> **Who**: IT Security Manager performs review; System Administrators execute removals
>
> **When**: Quarterly (by the 15th of January, April, July, October)
>
> **Evidence**: Signed access review reports with dates, list of removed access, ticket documentation of access removals

**Example - Poor Control Description**:
> Management reviews access periodically to ensure security.

**Problems**: Vague "management," no frequency, no evidence, no procedure

### Control Matrices

Use control matrices to map controls to TSC requirements:

**Security Control Matrix**: `templates/control_matrix_security.md`
- Lists all Security (SEC) common criteria points
- Maps your controls to each point
- Identifies control testing approach
- Notes evidence artifacts

**Availability Control Matrix**: `templates/control_matrix_availability.md`
- Lists all Availability (A) common criteria points
- Maps your controls to each point
- Identifies monitoring and measurement
- Notes availability evidence

### Addressing Control Gaps

If you identify a gap (requirement with no control):

1. **Determine if gap is real**: Some requirements may not apply
2. **Document rationale if N/A**: Explain why requirement doesn't apply
3. **If gap is real**: 
   - Design and implement control
   - Document new control in system description
   - Or document compensating control with justification
4. **Update control matrices**: Ensure all requirements covered

## Validation and Quality Assurance

### Built-in Validation Tools

**Completeness Checker**:
```bash
python3 scripts/completeness_checker.py system_description.md
```
- Verifies all 5 required sections present
- Checks for placeholder text
- Identifies missing components
- Generates completeness report

**Control Coverage Validator**:
```bash
python3 scripts/control_coverage_validator.py system_description.md
```
- Maps controls to Security (SEC) criteria
- Maps controls to Availability (A) criteria
- Identifies unmapped requirements
- Reports gaps

**Version Comparison**:
```bash
python3 scripts/version_comparison.py old.md new.md --output changes_report.txt
```
- Compares two versions
- Highlights changes
- Tracks control modifications
- Useful for annual updates

### Pre-Audit Checklist

Before submitting to auditor:

- [ ] All 5 sections complete and accurate
- [ ] Dates current (especially examination period dates)
- [ ] Organizational chart reflects current structure
- [ ] All third-party services listed
- [ ] All controls mapped to TSC requirements
- [ ] No placeholder text remaining
- [ ] Control descriptions include who/what/when/how/evidence
- [ ] SLAs and commitments match contracts
- [ ] Diagrams current and accurate
- [ ] Version control: dated and versioned
- [ ] Internal review completed (IT, Security, Legal, Compliance)
- [ ] `completeness_checker.py` passes
- [ ] `control_coverage_validator.py` shows 100% coverage
- [ ] Management has reviewed and approved

## Working with Examples

This skill includes sanitized example system descriptions:

**SaaS Example**: `examples/saas_example_redacted.md`
- Generic cloud-based SaaS company
- Multi-tenant architecture
- AWS infrastructure
- Both Security and Availability controls

**Healthcare Example**: `examples/healthcare_example_redacted.md`
- Healthcare technology company
- PHI handling
- HIPAA-aligned controls
- Both Security and Availability controls

**Control Examples**: `examples/control_description_samples.md`
- Well-written control descriptions
- Common pitfalls to avoid
- Security and Availability control samples

**How to Use Examples**:
1. Review structure and organization
2. Note level of detail
3. Adapt language and format to your organization
4. DO NOT copy verbatim - customize to your actual controls
5. Use as quality benchmark

## Common Pitfalls to Avoid

1. **Vague Language**: "regularly," "periodically," "management" without specifics
2. **Untestable Controls**: Controls that can't be validated
3. **Aspirational Controls**: Describing what you plan to do, not what you do
4. **Copy-Paste Errors**: Inconsistencies from using templates without customization
5. **Outdated Information**: Not updating after infrastructure/organizational changes
6. **Missing Evidence**: Controls without clear evidence artifacts
7. **Scope Creep**: Including out-of-scope systems
8. **Generic Descriptions**: Not specific to your actual environment
9. **Ignoring Exceptions**: Not documenting control exceptions or failures
10. **Misaligned Commitments**: SLAs in description don't match contracts

## Best Practices for Success

1. **Start Early**: Don't wait until audit kickoff
2. **Collaborate**: Work with IT, Security, Operations, Legal
3. **Be Accurate**: Describe actual controls, not desired state
4. **Be Specific**: Concrete details, not generalizations
5. **Version Control**: Track changes, maintain history
6. **Review Regularly**: Quarterly reviews, not just annual
7. **Align Documentation**: Policies, procedures, system description should align
8. **Test Controls**: Ensure controls work as described before documenting
9. **Update Continuously**: Make updates as changes occur, not annually
10. **Engage Auditor Early**: Preliminary review can prevent issues

## Additional Resources

### Reference Documents
- `references/tsc_security_criteria.md` - Complete Security (SEC) criteria breakdown
- `references/tsc_availability_criteria.md` - Complete Availability (A) criteria breakdown
- `references/system_description_requirements.md` - AICPA requirements detailed
- `references/saas_considerations.md` - SaaS-specific guidance
- `references/healthcare_hipaa_considerations.md` - Healthcare and HIPAA alignment

### Templates
- `templates/system_description_complete.md` - Full system description template (contains all sections)
- `templates/control_matrix_security.md` - Security control matrix
- `templates/control_matrix_availability.md` - Availability control matrix
- `templates/diagram_templates.md` - Mermaid.js templates for architecture/network diagrams
- `templates/saas_system_description.md` - SaaS-optimized template
- `templates/healthcare_system_description.md` - Healthcare-optimized template

### Examples
- `examples/saas_example_redacted.md` - SaaS company example
- `examples/healthcare_example_redacted.md` - Healthcare company example
- `examples/control_description_samples.md` - Well-written control examples

### Scripts
- `scripts/completeness_checker.py` - Validates completeness
- `scripts/control_coverage_validator.py` - Validates TSC coverage
- `scripts/version_comparison.py` - Compares versions

## Getting Started

1. **Determine scenario**: New or update? SaaS or Healthcare?
2. **Select template**: Start with appropriate template from `templates/`
3. **Review references**: Read relevant reference documents for your criteria
4. **Draft description**: Work through all 5 sections systematically
5. **Document controls**: Use control matrices to ensure complete coverage
6. **Validate**: Run validation scripts
7. **Review**: Internal stakeholder review
8. **Finalize**: Prepare for auditor submission

Your system description is a living document that should accurately reflect your current environment and controls. Keep it updated, specific, and aligned with actual operations.
