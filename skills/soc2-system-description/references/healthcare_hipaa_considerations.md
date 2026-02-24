# Healthcare and HIPAA Considerations for SOC 2

## Overview

Healthcare organizations and companies handling Protected Health Information (PHI) must align SOC 2 compliance with HIPAA (Health Insurance Portability and Accountability Act) requirements. This document provides guidance on addressing healthcare-specific considerations in SOC 2 system descriptions.

**Key Considerations**:
- PHI identification and protection
- HIPAA Security Rule alignment
- Business Associate Agreements (BAAs)
- Breach notification requirements
- Emergency operations
- Patient care continuity

---

## HIPAA and SOC 2 Relationship

### Complementary Frameworks

**HIPAA**: Prescriptive regulatory requirements for healthcare data
**SOC 2**: Risk-based framework for service organization controls

**How They Work Together**:
- SOC 2 controls can demonstrate HIPAA compliance
- SOC 2 reports useful for HIPAA-required business associate assessments
- Many HIPAA requirements map to SOC 2 Trust Service Criteria

### SOC 2 as Evidence of HIPAA Compliance

**Covered Entities and Business Associates** can use SOC 2 reports to:
- Demonstrate safeguards are in place
- Satisfy business associate due diligence requirements
- Provide to customers as evidence of security practices
- Support HIPAA risk analyses

**However**:
- SOC 2 doesn't replace HIPAA compliance
- SOC 2 doesn't cover all HIPAA requirements
- HIPAA-specific policies and procedures still required

---

## PHI in the System Description

### Identifying PHI

**Protected Health Information (PHI)** includes:
- Patient names, addresses, dates (except year)
- Medical record numbers
- Health plan beneficiary numbers
- Device identifiers and serial numbers
- Biometric identifiers
- Full-face photos
- Any other unique identifying characteristic
- **Plus**: Information about individual's health, healthcare, or payment for healthcare

### System Description Considerations

#### Section 1 (Overview) - Healthcare Context

**Must Address**:
- Type of healthcare organization
- Covered entity vs. business associate status
- Types of PHI processed
- Healthcare services provided

**Example Description**:
> "ABC Health Technologies is a healthcare technology company that provides electronic health record (EHR) software to medical practices. As a business associate under HIPAA, ABC processes protected health information (PHI) on behalf of covered entity customers. PHI processed includes patient demographics, medical histories, clinical notes, lab results, and billing information."

#### Section 2 (System Components) - Data

**Must Address**:
- Types of PHI in the system
- PHI data flows
- PHI vs. non-PHI data segregation
- De-identification processes (if applicable)

**Example Description**:
> "Protected Health Information (PHI) processed by the system includes:
> - Patient demographic information (name, DOB, address, SSN)
> - Clinical information (diagnoses, treatments, medications, lab results)
> - Provider information (treating physicians, healthcare providers)
> - Insurance and billing information (payer, policy numbers, claims)
> - Appointment and scheduling information
>
> PHI Data Flow:
> 1. PHI enters system via provider portal or HL7/FHIR interfaces
> 2. PHI stored in encrypted databases (AES-256)
> 3. PHI transmitted via TLS 1.3 encrypted connections
> 4. PHI accessed by authorized healthcare providers via web and mobile applications
> 5. PHI backed up daily to encrypted offsite storage
> 6. PHI deleted per retention schedule (minimum 6 years per state law) or customer request
>
> PHI is logically segregated from system metadata and application logs. Personal identifiers are not written to application logs."

#### Section 3 (Boundaries) - PHI Scope

**Must Address**:
- Which systems handle PHI
- Which systems do not handle PHI (if mixed environment)
- Business associate relationships

**Example Description**:
> "PHI System Boundaries:
>
> In-Scope for PHI:
> - EHR Application (web and mobile)
> - Patient Portal
> - Clinical database
> - Billing system
> - Document storage system
> - Backup systems
>
> Out-of-Scope (No PHI):
> - Corporate website
> - Internal HR systems
> - Marketing systems
>
> Business Associate Relationships:
> - Cloud hosting provider (AWS) - BAA executed
> - Email service provider (for transactional emails) - BAA executed
> - Monitoring service (access to logs) - BAA executed"

---

## HIPAA Security Rule Mapping to SOC 2

### Administrative Safeguards

| HIPAA Requirement | SOC 2 TSC | Key Controls |
|-------------------|-----------|--------------|
| Security Management Process (§164.308(a)(1)) | CC3 Risk Assessment | Risk analysis, risk management, sanction policy, information system activity review |
| Assigned Security Responsibility (§164.308(a)(2)) | CC1 Control Environment | Security Officer designated, responsibilities documented |
| Workforce Security (§164.308(a)(3)) | CC6 Access Controls, CC1 | Authorization/supervision, workforce clearance, termination procedures |
| Information Access Management (§164.308(a)(4)) | CC6 Access Controls | Access authorization, access establishment/modification |
| Security Awareness and Training (§164.308(a)(5)) | CC1 Control Environment | Security awareness program, protection from malicious software, login monitoring, password management |
| Security Incident Procedures (§164.308(a)(6)) | CC7 System Operations | Incident response and reporting |
| Contingency Plan (§164.308(a)(7)) | A1.3 Recovery | Data backup, disaster recovery, emergency mode, testing, applications and data criticality |
| Evaluation (§164.308(a)(8)) | CC4 Monitoring | Periodic technical and non-technical evaluation |
| Business Associate Contracts (§164.308(b)(1)) | CC9 Risk Mitigation | BAAs executed, BA monitoring |

### Physical Safeguards

| HIPAA Requirement | SOC 2 TSC | Key Controls |
|-------------------|-----------|--------------|
| Facility Access Controls (§164.310(a)(1)) | CC6.4 Physical Access | Contingency operations, facility security, access control/validation, maintenance records |
| Workstation Use (§164.310(b)) | CC6 Access Controls | Workstation security policies |
| Workstation Security (§164.310(c)) | CC6 Access Controls | Physical safeguards for workstations |
| Device and Media Controls (§164.310(d)(1)) | CC6.5 Asset Disposal | Disposal, media reuse, accountability, data backup/storage |

### Technical Safeguards

| HIPAA Requirement | SOC 2 TSC | Key Controls |
|-------------------|-----------|--------------|
| Access Control (§164.312(a)(1)) | CC6 Access Controls | Unique user identification, emergency access, automatic logoff, encryption/decryption |
| Audit Controls (§164.312(b)) | CC6, CC7 | Hardware, software, procedural mechanisms to record/examine activity |
| Integrity (§164.312(c)(1)) | CC6, CC7 | Mechanisms to authenticate and ensure ePHI not improperly altered/destroyed |
| Person or Entity Authentication (§164.312(d)) | CC6 | Verify identity of person/entity seeking access |
| Transmission Security (§164.312(e)(1)) | CC6.7 | Integrity controls, encryption |

---

## Healthcare-Specific Control Examples

### CC6.1 - PHI Access Controls

```
Control: Minimum Necessary PHI Access

Access to PHI is restricted based on minimum necessary principle, with role-based access controls limiting users to only the PHI required for their job functions.

How it Works:
- Role-based access control (RBAC) implemented for all PHI access
- Roles defined based on job functions (Physician, Nurse, Billing Staff, etc.)
- Each role has access only to minimum necessary PHI
- "Break the glass" emergency access available for patient care emergencies
- All emergency access logged and reviewed within 24 hours
- Quarterly access reviews verify users still require their assigned access levels

Who: Access provisioned by IT Security based on manager approval; Quarterly reviews by Security Officer

When: Access provisioned upon hiring/role change; Reviewed quarterly; Emergency access monitored continuously

Evidence: Role definitions, access approval tickets, quarterly access review reports, emergency access logs and reviews, RBAC configuration
```

### CC6.7 - PHI Encryption

```
Control: PHI Encryption at Rest and in Transit

All PHI is encrypted at rest using AES-256 encryption and in transit using TLS 1.3 or higher.

How it Works:
At Rest:
- Database encryption enabled for all PHI databases (AWS RDS encryption)
- Full-disk encryption for all servers (AWS EBS encryption)
- Document storage encrypted (AWS S3 server-side encryption)
- Encryption keys managed via AWS KMS with key rotation
- Key access restricted to authorized systems and personnel

In Transit:
- All web and API traffic uses TLS 1.3
- TLS 1.2 minimum (TLS 1.0/1.1 disabled)
- Certificate management with automated renewal
- HL7/FHIR interfaces use TLS or VPN
- Internal service-to-service communication encrypted

Who: Enforced by infrastructure configuration; Security team manages encryption standards

When: Continuous (all PHI encrypted); Quarterly encryption configuration audit

Evidence: Encryption configuration documentation, certificate inventory, quarterly audit reports, encryption verification tests
```

### CC7.2 - PHI Access Auditing

```
Control: Comprehensive PHI Access Logging and Review

All access to PHI is logged and logs are regularly reviewed for unauthorized or inappropriate access.

How it Works:
- Database audit logging captures all PHI access with user ID, timestamp, action, and data accessed
- Application logging records PHI views, modifications, and deletions
- Logs aggregated in SIEM system
- Automated alerts for suspicious patterns:
  - Bulk PHI access (>100 records in <1 hour)
  - PHI access outside business hours
  - Access to PHI of VIPs or employees
  - Failed access attempts (>5 in 10 minutes)
- Weekly random sample review of PHI access logs (minimum 50 access events)
- Monthly comprehensive review of all alert investigations

Who: Automated logging; Security Operations Center monitors alerts; Security Officer conducts weekly reviews

When: Continuous logging; Real-time alerting; Weekly and monthly reviews

Evidence: Audit log configurations, SIEM alert rules, weekly review reports, monthly summary reports, investigation tickets
```

---

## Business Associate Agreements (BAA)

### BAA and SOC 2 Integration

**Business Associate Agreement** is required when:
- Covered entity engages business associate to handle PHI
- Business associate engages subcontractor to handle PHI

**SOC 2's Role**:
- SOC 2 report demonstrates safeguards required by BAA
- Covered entities request SOC 2 as part of BA due diligence
- SOC 2 system description should reference BAA obligations

### System Description Considerations

#### Section 1 (Overview) - Business Associate Status

**Must Address**:
- Business associate vs. covered entity status
- BAA execution process
- Subcontractor BAAs

**Example Description**:
> "As a business associate under HIPAA, the company executes Business Associate Agreements (BAAs) with all covered entity customers prior to accessing their PHI. The BAA specifies permitted uses of PHI, security obligations, breach notification requirements, and other HIPAA-mandated provisions. The company also executes BAAs with subcontractors who handle PHI on behalf of the company, including cloud infrastructure providers, monitoring services, and support tools vendors."

#### Section 2 (System Components) - People

**Must Address**:
- Workforce member training
- Sanctions for violations
- Privacy officer and security officer roles

**Example Description**:
> "All workforce members with PHI access complete HIPAA training during onboarding and annually thereafter. Training covers:
> - HIPAA Privacy Rule requirements
> - HIPAA Security Rule safeguards
> - Minimum necessary access principles
> - Breach identification and reporting
> - Sanctions for violations
>
> The company has designated:
> - Privacy Officer: Responsible for HIPAA Privacy Rule compliance
> - Security Officer: Responsible for HIPAA Security Rule compliance
> - Both officers report to the Chief Compliance Officer"

### Control Considerations

**CC9.2 - Business Associate Management**:
```
Control: Business Associate Agreement and Monitoring

Business Associate Agreements are executed with all subcontractors who handle PHI, and business associate compliance is monitored.

How it Works:
1. Before engaging any vendor with PHI access, Legal and Compliance review
2. BAA executed before PHI access granted
3. Vendor risk assessment completed (includes SOC 2 review)
4. Annual review of all business associates:
   - Verify BAA still in effect
   - Review current SOC 2 report
   - Assess any security incidents
   - Review access levels
5. BAA register maintained with all executed agreements

Who: Legal executes BAAs; Compliance team performs annual reviews; Security team reviews SOC 2 reports

When: BAA before PHI access; Annual business associate review (by March 31 each year)

Evidence: BAA register, executed BAAs, vendor risk assessments, annual review reports, vendor SOC 2 reports
```

---

## HIPAA Breach Notification

### HIPAA vs. SOC 2 Incident Response

**HIPAA Breach Notification Rule** (§164.408):
- 60-day deadline to notify HHS and affected individuals
- Notice to media if breach affects 500+ individuals in a state
- Business associates must notify covered entities within 60 days

**SOC 2 Incident Response**:
- Incident detection, response, recovery
- Communication procedures

**Integration**:
System description should address both SOC 2 incident response and HIPAA breach notification.

### System Description Considerations

#### Section 2 (System Components) - Procedures

**Must Address**:
- Breach identification and assessment
- Breach notification timelines
- Risk of harm analysis
- Breach notification procedures

**Example Description**:
> "Security Incident and Breach Response:
>
> Detection and Assessment:
> - Security incidents detected via monitoring systems, employee reports, or customer reports
> - Privacy Officer and Security Officer assess whether incident constitutes a HIPAA breach
> - Breach determination based on 4-factor risk assessment:
>   1. Nature and extent of PHI involved
>   2. Unauthorized person who accessed PHI
>   3. Whether PHI was actually acquired or viewed
>   4. Extent to which risk has been mitigated
> - If breach determination made, breach response procedures initiated
>
> Breach Notification Timeline (HIPAA):
> - Individuals: Within 60 days of discovery
> - Covered Entity Customers: Within 60 days of discovery (as business associate)
> - HHS: Within 60 days (if 500+) or annually for smaller breaches
> - Media: Within 60 days (if 500+ in a state)
> - State Attorneys General: Per state breach notification laws
>
> Risk Mitigation:
> - Investigation and containment
> - Remediation of vulnerabilities
> - Offer credit monitoring/identity theft protection (if appropriate)
> - Enhanced monitoring for affected individuals"

### Control Considerations

**CC7.3 - HIPAA Breach Assessment**:
```
Control: HIPAA Breach Risk Assessment

All security incidents involving PHI are assessed to determine if they constitute HIPAA breaches requiring notification.

How it Works:
- Privacy Officer conducts 4-factor risk assessment for each PHI incident:
  1. Nature and extent of PHI (sensitivity, identifiability)
  2. Who accessed PHI (unauthorized person's relationship to data)
  3. Was PHI acquired/viewed or just exposed?
  4. Risk mitigation implemented
- Assessment documented using breach assessment template
- If breach determination made, breach notification procedures initiated
- If not a breach, documentation of rationale maintained
- All assessments reviewed by Legal

Who: Privacy Officer conducts assessment; Legal reviews determination

When: Within 24 hours of incident discovery

Evidence: Breach assessment forms, determination documentation, legal review records
```

**CC7.4 - HIPAA Breach Notification**:
```
Control: HIPAA Breach Notification Procedures

Breaches of unsecured PHI are reported to affected individuals, covered entities, HHS, and media (if applicable) within HIPAA's 60-day requirement.

How it Works:
- Breach notification letters drafted using approved template
- Privacy Officer approves content
- Notifications sent via first-class mail or email (if individual agreed to email)
- Covered entity customers notified via email to designated contact
- HHS notification via web portal (if 500+) or annual report (if <500)
- Media notification in major publications (if 500+ in a state)
- Substitute notification if contact information insufficient (web posting + media)
- All notifications tracked in breach log with dates and methods

Who: Privacy Officer coordinates; Communications team assists with letter drafting; IT executes mailings

When: Within 60 days of breach discovery; Specific deadlines tracked per breach

Evidence: Breach notification letters, mailing receipts, email delivery confirmations, HHS submission confirmations, media publication records, breach notification log
```

---

## HIPAA Security Rule Contingency Plan

### Required Components

HIPAA Security Rule § 164.308(a)(7) requires:

**A. Data Backup Plan** (§164.308(a)(7)(ii)(A))
- Procedures to create and maintain retrievable exact copies of ePHI

**B. Disaster Recovery Plan** (§164.308(a)(7)(ii)(B))
- Procedures to restore lost data

**C. Emergency Mode Operation Plan** (§164.308(a)(7)(ii)(C))
- Procedures to enable continuation of critical business processes while operating in emergency mode

**D. Testing and Revision Procedures** (§164.308(a)(7)(ii)(D))
- Procedures for periodic testing and revision of contingency plans

**E. Applications and Data Criticality Analysis** (§164.308(a)(7)(ii)(E))
- Assessment of relative criticality of applications and data

### System Description Considerations

#### Section 5 (Controls) - HIPAA Contingency Plan Controls

**Example Control Description**:

```
Control: HIPAA Contingency Plan

The company maintains a HIPAA-compliant contingency plan covering data backup, disaster recovery, emergency operations, testing, and criticality analysis.

Data Backup (§164.308(a)(7)(ii)(A)):
- Automated daily backups of all ePHI databases
- Backups encrypted using AES-256
- Backups stored in geographically separate AWS region
- Backup retention: 30 days rolling
- Backup integrity tested weekly via automated restore to test environment

Disaster Recovery (§164.308(a)(7)(ii)(B)):
- Disaster recovery plan documented and approved annually
- RTO: 4 hours for critical systems, 24 hours for non-critical
- RPO: 24 hours (daily backup schedule)
- Failover procedures to DR region (us-west-2)
- DR tested annually with documented results

Emergency Mode Operations (§164.308(a)(7)(ii)(C)):
- Emergency mode operations plan documents procedures for:
  - Continued patient care access to EHR during system outages
  - Manual/paper-based backup procedures
  - Emergency access to PHI
  - System restoration priorities
- Emergency contacts and escalation procedures documented
- Emergency mode operations drills conducted annually

Testing and Revision (§164.308(a)(7)(ii)(D)):
- Contingency plan tested annually (minimum)
- Test scenarios include regional outage, database corruption, ransomware
- Test results documented with lessons learned
- Plan updated based on test findings
- Ad-hoc tests when significant system changes occur

Criticality Analysis (§164.308(a)(7)(ii)(E)):
- Applications and data classified by criticality (Critical, High, Medium, Low)
- Critical: EHR application, patient database, provider portal
- Criticality determines recovery priority and RTO/RPO
- Criticality reviewed annually and when new systems added

Who: IT Operations manages backups and DR; CTO owns contingency plan; Annual test conducted by IT Operations with Security Officer observation

When: Backups daily; DR test annually; Criticality review annually; Plan review and update annually

Evidence: Contingency plan document, backup logs, backup integrity test results, DR test reports, criticality analysis documentation, emergency mode operations procedures
```

---

## Patient Care Continuity

### Availability Considerations Unique to Healthcare

Unlike typical SaaS, healthcare system downtime can directly impact patient care.

### System Description Considerations

#### Section 4 (Service Commitments) - Healthcare Availability

**Must Address**:
- Availability during patient care hours
- Emergency access procedures
- Downtime notification to providers
- Alternative procedures during outages

**Example Description**:
> "System Availability Commitments:
>
> Standard Availability: 99.5% measured monthly during business hours (6 AM - 8 PM local time, Monday-Saturday)
>
> Emergency Access: In the event of system unavailability, healthcare providers can access patient information via:
> - Emergency read-only mode (if database available but application down)
> - Downloadable patient summary reports (automatically generated daily)
> - 24/7 emergency support line for critical patient care needs
>
> Downtime Notification:
> - Customers notified of planned maintenance 7 days in advance
> - Unplanned outages trigger immediate notification via email and SMS to designated contacts
> - Status page provides real-time system status
>
> Clinical Impact Assessment:
> - All outages assessed for patient care impact
> - High-impact outages escalated to executive team
> - Post-incident reviews include clinical workflow impact analysis"

### Control Considerations

**Availability - Emergency Access to PHI**:
```
Control: Emergency PHI Access Procedures

Healthcare providers can access PHI during emergencies even during system outages or when normal access procedures are unavailable.

How it Works:
- Emergency access mode available when system in degraded state
- Emergency access credentials pre-provisioned for authorized providers
- Emergency access documented:
  - User ID accessing
  - Timestamp
  - Patient(s) accessed
  - Reason for emergency access
- All emergency access reviewed within 24 hours by Privacy Officer
- Inappropriate emergency access results in investigation and sanctions

Who: Healthcare providers use emergency access; Privacy Officer reviews within 24 hours

When: As needed for patient care emergencies; Review within 24 hours

Evidence: Emergency access logs, Privacy Officer review documentation, investigation records (if applicable)
```

**Availability - Alternative Procedures During Downtime**:
```
Control: Downtime Procedures for Clinical Staff

Documented procedures enable healthcare providers to continue patient care during system downtime.

How it Works:
- Downtime procedures documented for each critical workflow:
  - Patient registration (paper forms)
  - Clinical documentation (paper charts)
  - Medication orders (verbal and written)
  - Lab orders (phone orders)
- Downtime procedure guides available at each workstation
- Staff trained on downtime procedures annually
- Downtime drills conducted annually
- Post-downtime data entry procedures to update system

Who: Clinical staff execute downtime procedures; IT Operations declares downtime and recovery; Training team conducts annual training

When: During system downtime (planned or unplanned); Annual training; Annual drill

Evidence: Downtime procedure documentation, training records, downtime drill reports, downtime event logs
```

---

## Healthcare-Specific System Description Template

Use the template: `templates/healthcare_system_description.md`

This template is pre-structured for healthcare companies with sections for:
- Business associate status and BAA process
- PHI identification and data flows
- HIPAA Security Rule alignment
- Emergency operations and patient care continuity
- Breach assessment and notification procedures
- Contingency plan documentation

---

## Common Healthcare System Description Pitfalls

1. **Not Clearly Identifying PHI**: Be explicit about what PHI the system processes
2. **Missing BAA Documentation**: Document all business associate relationships
3. **Vague Access Controls**: Be specific about minimum necessary implementation
4. **Insufficient Audit Logging**: HIPAA requires comprehensive audit logs for PHI
5. **No Emergency Procedures**: Healthcare systems need emergency access and downtime procedures
6. **Weak Encryption Documentation**: Must clearly document encryption at rest AND in transit
7. **Missing Breach Procedures**: HIPAA breach assessment and notification must be documented
8. **No Contingency Plan Testing**: HIPAA requires documented testing
9. **Ignoring Patient Care Impact**: Availability commitments should consider clinical impact
10. **Not Mapping to HIPAA**: Show how SOC 2 controls satisfy HIPAA requirements

---

## Healthcare Compliance Checklist

### PHI Protection
- [ ] All PHI types identified in system description
- [ ] PHI data flows documented with diagrams
- [ ] Encryption at rest documented (AES-256 or stronger)
- [ ] Encryption in transit documented (TLS 1.2 minimum)
- [ ] PHI access controls documented (minimum necessary)
- [ ] PHI audit logging documented (comprehensive)
- [ ] PHI disposal procedures documented

### HIPAA Security Rule
- [ ] All administrative safeguards addressed
- [ ] All physical safeguards addressed
- [ ] All technical safeguards addressed
- [ ] Safeguards mapped to SOC 2 controls
- [ ] Risk analysis conducted and documented

### Business Associates
- [ ] BAA process documented
- [ ] All business associates identified
- [ ] All BAAs executed before PHI access
- [ ] Subcontractor BAAs documented
- [ ] Business associate monitoring procedures documented

### Contingency Planning
- [ ] Data backup plan documented
- [ ] Disaster recovery plan documented
- [ ] Emergency mode operations documented
- [ ] Testing procedures documented (annual minimum)
- [ ] Criticality analysis documented

### Breach Response
- [ ] Breach assessment procedures documented (4-factor test)
- [ ] Breach notification procedures documented (60-day timeline)
- [ ] Notification to individuals procedures
- [ ] Notification to covered entities procedures (if BA)
- [ ] HHS notification procedures
- [ ] Media notification procedures (if 500+)

### Patient Care
- [ ] Emergency PHI access procedures documented
- [ ] Downtime procedures for clinical staff documented
- [ ] Alternative care delivery procedures documented
- [ ] Clinical staff training on downtime procedures
- [ ] Patient care continuity addressed in availability commitments

---

## Key Takeaways for Healthcare Organizations

1. **Be Explicit About PHI**: Clearly identify what PHI is processed and how it's protected
2. **Document BAAs**: All business associate relationships and how they're managed
3. **Map to HIPAA**: Show how SOC 2 controls satisfy HIPAA requirements
4. **Emphasize Encryption**: Both at rest and in transit for all PHI
5. **Comprehensive Audit Logging**: All PHI access must be logged and reviewed
6. **Emergency Procedures**: Healthcare requires emergency access and downtime procedures
7. **Breach Procedures**: HIPAA breach assessment and notification clearly documented
8. **Test Contingency Plan**: Annual testing is required, not optional
9. **Consider Patient Care**: Availability commitments consider clinical impact
10. **Privacy and Security Officers**: Clearly identify designated officials

Healthcare organizations have heightened security and availability obligations due to the sensitive nature of PHI and the impact on patient care. Address these thoroughly in your SOC 2 system description to demonstrate mature understanding of healthcare-specific requirements.

