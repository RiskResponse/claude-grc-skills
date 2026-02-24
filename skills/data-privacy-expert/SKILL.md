---
name: data-privacy-expert
description: Comprehensive guidance on GDPR and CCPA compliance, including data subject rights, documentation (DPAs, Certificates of Deletion), breach notifications, and risk assessments. Use when handling privacy regulations, data protection requirements, or creating privacy-related documentation.
license: Apache-2.0
---

# Data Privacy Expert

## Overview

This skill provides expert guidance on data privacy regulations, specifically GDPR (General Data Protection Regulation) and CCPA/CPRA (California Consumer Privacy Act and California Privacy Rights Act). Use this skill when:

- Drafting or reviewing Data Processing Addendums (DPAs)
- Creating Certificates of Deletion
- Responding to data subject rights requests (access, deletion, rectification, portability)
- Handling data breach notifications
- Conducting privacy risk assessments
- Ensuring compliance with privacy regulations
- Creating privacy policies and notices

**Keywords**: GDPR, CCPA, CPRA, data privacy, data protection, DPA, certificate of deletion, data subject rights, breach notification, privacy compliance

## Quick Decision Tree

To determine which regulation applies and what action to take:

### Which Regulation Applies?

**GDPR applies when:**
- Processing personal data of individuals in the EU/EEA
- Organization is established in the EU
- Offering goods/services to EU residents
- Monitoring behavior of EU residents

**CCPA/CPRA applies when:**
- Business operates in California
- Processes personal information of California residents
- Meets thresholds: $25M+ revenue, OR 100k+ consumers/households, OR 50%+ revenue from selling personal information

**Both may apply** if processing data of both EU and California residents.

### What Action Is Needed?

**For Data Subject Requests:**
- Access request → Provide data copy (30 days GDPR, 45 days CCPA)
- Deletion request → Delete data + issue Certificate of Deletion
- Rectification → Correct inaccurate data
- Portability → Provide data in structured format
- Opt-out (CCPA) → Stop selling/sharing personal information

**For Business Operations:**
- New vendor/processor → Execute Data Processing Addendum
- Data breach → Follow breach notification procedures (72 hours GDPR)
- New processing activity → Conduct risk assessment/DPIA
- Website/app → Ensure privacy policy is compliant

## GDPR Compliance

### Core Principles

Apply these principles to all data processing:

1. **Lawfulness, Fairness, Transparency**: Process data legally, fairly, and transparently
2. **Purpose Limitation**: Collect data for specified, explicit, legitimate purposes
3. **Data Minimization**: Collect only necessary data
4. **Accuracy**: Keep data accurate and up-to-date
5. **Storage Limitation**: Retain data only as long as necessary
6. **Integrity and Confidentiality**: Ensure appropriate security
7. **Accountability**: Demonstrate compliance

### Legal Bases for Processing

Identify at least one legal basis before processing personal data:

- **Consent**: Freely given, specific, informed, unambiguous
- **Contract**: Processing necessary to perform a contract
- **Legal Obligation**: Required by law
- **Vital Interests**: Protect life of data subject
- **Public Task**: Perform task in public interest
- **Legitimate Interests**: Necessary for legitimate interests (balance test required)

For detailed guidance on legitimate interest assessments, see `references/gdpr_comprehensive.md`.

### Data Subject Rights

GDPR grants individuals these rights:

- **Right to Access** (Article 15): Obtain copy of personal data
- **Right to Rectification** (Article 16): Correct inaccurate data
- **Right to Erasure** (Article 17): Request deletion ("right to be forgotten")
- **Right to Restrict Processing** (Article 18): Limit how data is used
- **Right to Data Portability** (Article 20): Receive data in structured format
- **Right to Object** (Article 21): Object to processing
- **Rights Related to Automated Decision-Making** (Article 22): Challenge automated decisions

**Response Timeline**: 30 days (extendable by 2 months if complex)

See `references/data_subject_rights.md` for detailed procedures.

## CCPA/CPRA Compliance

### Consumer Rights

CCPA/CPRA grants California consumers these rights:

- **Right to Know**: What personal information is collected, used, shared, or sold
- **Right to Delete**: Request deletion of personal information
- **Right to Opt-Out**: Opt out of sale/sharing of personal information
- **Right to Correct**: Correct inaccurate personal information
- **Right to Limit Use of Sensitive Personal Information**: Restrict use of sensitive data
- **Right to Non-Discrimination**: Equal service regardless of privacy rights exercise

**Response Timeline**: 45 days (extendable by 45 days once if necessary)

### 2026 Updates (Effective January 1, 2026)

New CCPA regulations introduce significant requirements:

**Cybersecurity Audits:**
- Required for businesses processing significant amounts of personal information
- Annual audits to assess and document cybersecurity practices
- First audit reports due starting April 1, 2028 (timeline varies by revenue)

**Risk Assessments:**
- Required before processing activities presenting significant risks to consumer privacy
- Must be reviewed and updated every three years
- First submissions due by April 1, 2028
- See `templates/risk_assessment_template.md`

**Automated Decision-Making Technology (ADMT):**
- Businesses using ADMT for significant consumer decisions must provide clear notices
- Consumers have right to opt-out of ADMT
- Compliance begins January 1, 2027

**Expanded Sensitive Personal Information:**
- Now includes "neural data" (information from measuring nervous system activity)
- Enhanced protection requirements

For comprehensive CCPA/CPRA guidance, see `references/ccpa_cpra_guide.md`.

## Documentation Tasks

### Creating Data Processing Addendums (DPAs)

When engaging a data processor (vendor, service provider), execute a DPA that includes:

**Required Elements (GDPR Article 28):**
1. Subject matter and duration of processing
2. Nature and purpose of processing
3. Type of personal data
4. Categories of data subjects
5. Controller and processor obligations
6. Security measures
7. Sub-processor provisions
8. Data subject rights assistance
9. Breach notification procedures
10. Data deletion/return obligations
11. Audit rights
12. International data transfers (if applicable)

**How to create a DPA:**
1. Use `templates/data_processing_addendum.md` as starting point
2. Customize placeholders with specific details
3. Review against checklist in `references/dpa_guidelines.md`
4. Validate completeness using `scripts/validate_dpa.py`

**CCPA-Specific Additions:**
- Service provider obligations
- Prohibition on selling/sharing data
- Certification of understanding obligations

### Creating Privacy Policies

Use `templates/privacy_policy_template.md` for GDPR and CCPA-compliant privacy policies.

**Must Include:**
- What data is collected
- How data is used
- Legal bases (GDPR) or business purposes (CCPA)
- Data sharing and recipients
- International transfers
- Retention periods
- Data subject/consumer rights
- Contact information for privacy requests
- Cookie notices (if applicable)

## Create Certificate of Deletion

A Certificate of Deletion provides formal confirmation that personal data has been deleted in compliance with data subject rights requests.

### When to Issue

Issue a Certificate of Deletion when:
- Data subject requests deletion under GDPR Article 17 (Right to Erasure)
- Consumer requests deletion under CCPA
- Contractual obligation requires proof of deletion
- Audit or compliance documentation requires verification
- Data processor completes deletion on behalf of controller

### Required Fields

Every Certificate of Deletion must include:

1. **Certificate Identifier**: Unique reference number
2. **Date of Issuance**: When certificate was created
3. **Data Subject Information**: Name and identifier of individual (or anonymized reference)
4. **Organization Information**: Legal name, address, contact details of entity performing deletion
5. **Request Details**: Date and method of deletion request receipt
6. **Data Description**: Categories and scope of data deleted (avoid including actual personal data in certificate)
7. **Deletion Date**: Date when deletion was completed
8. **Deletion Method**: How data was deleted (e.g., secure erasure, anonymization, destruction)
9. **Systems/Locations**: Where data was deleted from (databases, backups, third parties)
10. **Verification**: How deletion was verified
11. **Authorized Signatory**: Name, title, and signature of responsible person
12. **Exceptions**: Any data retained and legal basis (if applicable)

### Step-by-Step Process

**Step 1: Verify Deletion Completion**
- Confirm all personal data has been deleted from production systems
- Verify deletion from backups (or document backup deletion schedule)
- Confirm third-party processors have deleted data
- Document any legal exceptions to deletion (e.g., legal hold, regulatory retention)

**Step 2: Generate Certificate**
- Use `templates/certificate_of_deletion.md` template
- Fill in all required fields accurately
- Assign unique certificate identifier for tracking
- Include specific details about data deleted and methods used

**Step 3: Review and Verification**
- Have DPO or privacy officer review certificate
- Verify technical deletion was completed per documented process
- Confirm no exceptions were missed
- Check compliance with applicable regulations

**Step 4: Authorize and Sign**
- Obtain signature from authorized personnel (DPO, Legal, IT Manager)
- Include printed name, title, and date of signature
- Retain copy for compliance records (minimum 3-7 years depending on jurisdiction)

**Step 5: Deliver to Data Subject**
- Send certificate via secure method (encrypted email, certified mail)
- Include cover letter explaining the certificate
- Provide contact information for questions
- Retain proof of delivery

### Legal Considerations

**GDPR Context:**
- Deletion must be completed "without undue delay"
- Exceptions apply (Article 17(3)): legal obligations, public interest, legal claims, etc.
- Must verify identity of requester before deletion
- Document justification for any retention

**CCPA Context:**
- Deletion not required if necessary for specific purposes (Section 1798.105(d))
- Must delete from records and direct service providers to delete
- May retain internal records that deletion was requested

**Retention of Certificate:**
- Keep certificate and supporting documentation for compliance purposes
- Typical retention: 3 years (CCPA), 5-7 years (GDPR best practice)
- Store securely with access controls
- Do not include actual personal data in certificate itself

### Template Usage

To create a certificate:

```bash
# Use the template
cp templates/certificate_of_deletion.md certificate_[REQUEST_ID].md

# Fill in placeholders marked with [BRACKETS]
# Review checklist at end of template
# Obtain required signatures
```

For complex deletion scenarios (multiple systems, third parties, exceptions), see detailed guidance in `references/data_subject_rights.md`.

## Data Subject Requests

### Handling Access Requests

**Process:**
1. Verify identity of requester
2. Search all systems for personal data
3. Compile data in readable format
4. Review for third-party rights or confidential information
5. Provide data within timeline (30 days GDPR, 45 days CCPA)

Use `templates/data_subject_request_response.md` for response templates.

### Handling Deletion Requests

**Process:**
1. Verify identity and validity of request
2. Determine if exceptions apply
3. Delete data from all systems (production, backups, third parties)
4. Document deletion completion
5. Issue Certificate of Deletion
6. Respond to requester within timeline

**Exceptions to Deletion:**
- Legal obligations to retain data
- Exercise or defense of legal claims
- Public interest or scientific research (with safeguards)
- Contractual necessity

### Handling Rectification Requests

**Process:**
1. Verify identity of requester
2. Confirm inaccuracy of data
3. Correct data across all systems
4. Notify third parties who received data (if required)
5. Confirm rectification to requester

### Handling Portability Requests (GDPR)

**Process:**
1. Provide data in structured, commonly used, machine-readable format (JSON, CSV, XML)
2. Include only data provided by data subject (not derived data)
3. Transmit directly to another controller if technically feasible
4. Complete within 30 days

### Tracking Data Subject Requests

Use `scripts/dsr_tracker.py` to:
- Log all incoming requests
- Track deadlines (30/45 days)
- Monitor completion status
- Generate compliance reports

## Breach Response

### GDPR Breach Notification

**Timeline: 72 hours** from becoming aware of breach

**Step 1: Assess Breach (Immediately)**
- Contain the breach
- Assess severity and risk to individuals
- Document facts: what happened, when, how many affected

**Step 2: Notify Supervisory Authority (Within 72 Hours)**

Required information:
- Nature of breach
- Categories and approximate number of data subjects affected
- Categories and approximate number of records affected
- Contact details of DPO or information point
- Likely consequences of breach
- Measures taken or proposed to address breach

**Step 3: Notify Data Subjects (Without Undue Delay)**

Required when breach likely to result in high risk to individuals.

Not required if:
- Appropriate technical/organizational protection applied (e.g., encryption)
- Subsequent measures eliminate high risk
- Disproportionate effort (then public communication)

**Step 4: Document Breach**
- Maintain internal breach register
- Document facts, effects, and remedial action
- Available for supervisory authority inspection

### CCPA Breach Notification

**No specific timeline**, but "without unreasonable delay" and consistent with law enforcement needs.

Required when unencrypted/unredacted personal information was subject to unauthorized access.

Use `scripts/breach_timeline_checker.py` to track notification deadlines and status.

For detailed procedures, see `references/breach_notification.md`.

## Risk Assessments

### When Required

**GDPR Data Protection Impact Assessment (DPIA):**
- High risk to data subject rights
- Systematic monitoring on large scale
- Large-scale processing of special category data
- Automated decision-making with legal effects

**CCPA Risk Assessment (Starting 2026):**
- Before processing activities presenting significant risks to consumer privacy
- Required for covered businesses
- Must be updated every three years
- First submissions due April 1, 2028

### How to Conduct

1. Use `templates/risk_assessment_template.md`
2. Describe processing operations and purposes
3. Assess necessity and proportionality
4. Identify risks to individuals
5. Evaluate risk severity and likelihood
6. Determine mitigation measures
7. Document consultation (DPO, data subjects if appropriate)
8. Obtain sign-off from appropriate authority

For detailed guidance, see:
- `references/gdpr_comprehensive.md` (DPIA section)
- `references/ccpa_cpra_guide.md` (Risk Assessment section)

## Additional Resources

This skill includes comprehensive reference materials:

- `references/gdpr_comprehensive.md` - Complete GDPR guidance
- `references/ccpa_cpra_guide.md` - CCPA/CPRA with 2026 updates
- `references/dpa_guidelines.md` - DPA essential clauses and best practices
- `references/data_subject_rights.md` - Detailed procedures for all data subject rights
- `references/breach_notification.md` - Step-by-step breach response procedures

Templates ready for customization:

- `templates/data_processing_addendum.md` - Complete DPA with placeholders
- `templates/certificate_of_deletion.md` - Certificate template with checklist
- `templates/privacy_policy_template.md` - GDPR and CCPA compliant
- `templates/data_subject_request_response.md` - Response letter templates
- `templates/risk_assessment_template.md` - CCPA 2026 and GDPR DPIA

Helper scripts for compliance:

- `scripts/validate_dpa.py` - Check DPA for required clauses
- `scripts/breach_timeline_checker.py` - Track breach notification deadlines
- `scripts/dsr_tracker.py` - Manage data subject request pipeline

## Best Practices

1. **Document Everything**: Maintain records of processing activities, risk assessments, and data subject requests
2. **Privacy by Design**: Build privacy into systems from the start
3. **Regular Training**: Ensure staff understand privacy obligations
4. **Vendor Management**: Execute DPAs with all processors before data sharing
5. **Incident Response Plan**: Have documented breach response procedures
6. **Regular Audits**: Periodically review compliance with privacy policies
7. **Stay Updated**: Monitor regulatory changes and enforcement actions
8. **Designate Responsibility**: Appoint DPO (if required) or privacy officer
