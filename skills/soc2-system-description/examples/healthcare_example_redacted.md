# SYSTEM DESCRIPTION - HEALTHTECH SOLUTIONS (EXAMPLE)

**This is a sanitized example system description for a Healthcare company. Use for reference only. Customize for your own organization.**

---

## HealthTech Solutions, Inc.
**SOC 2 Type II Examination**
**Trust Service Criteria: Security and Availability**
**Examination Period: January 1, 2024 - December 31, 2024**
**Description as of December 31, 2024**

---

## SECTION 1: OVERVIEW

### 1.1 Company Background

HealthTech Solutions, Inc. ("HealthTech") is a healthcare technology company providing electronic health record (EHR) software to medical practices. Founded in 2015 and headquartered in Austin, Texas, HealthTech serves over 500 medical practices across the United States.

**Business Associate Status:** HealthTech is a business associate under HIPAA, processing protected health information (PHI) on behalf of covered entity customers.

### 1.2 Services

HealthTech provides cloud-based EHR software enabling healthcare providers to manage patient records, schedule appointments, prescribe medications, and bill for services.

**Core Services:**
- Electronic health records management
- Patient portal
- e-Prescribing
- Practice management and scheduling
- Medical billing
- Clinical reporting and analytics

**Service Delivery:** Cloud-based SaaS hosted on Microsoft Azure

**Data Processed:** Protected Health Information (PHI) including patient demographics, clinical data, insurance information

### 1.3 Organization

**Key Roles:**
- CEO: Overall responsibility
- CTO: Technology and product
- CISO / Security Officer: HIPAA Security Officer, security program
- Privacy Officer: HIPAA Privacy Officer, PHI protection
- Compliance Officer: HIPAA and SOC 2 compliance
- VP Engineering: Software development
- Director of IT Operations: System operations and availability

**HIPAA Designations:**
- Security Officer: CISO
- Privacy Officer: Chief Compliance Officer

---

## SECTION 2: SYSTEM COMPONENTS

### 2.1 Infrastructure

**Cloud Provider:** Microsoft Azure

**Primary Region:** East US (Virginia)
**Secondary Region:** West US 2 (Washington) - Disaster Recovery

**Azure Services:**
- Virtual Machines: Application servers
- Azure SQL Database: Patient database (encrypted)
- Azure Blob Storage: Document storage, backups
- Azure Front Door: CDN and WAF
- Azure Active Directory: Identity management
- Azure Monitor: Monitoring and alerting
- Azure Key Vault: Encryption key management

**HIPAA Compliance:** Microsoft Azure BAA executed. Azure maintains HIPAA compliance and SOC 2 certification.

### 2.2 Software

**Application Stack:**
- Frontend: Angular web application
- Backend: .NET Core Web API
- Database: Azure SQL Database
- Document storage: Azure Blob Storage (encrypted)
- Integration: HL7 v2.x and FHIR R4 interfaces

**Security Software:**
- Azure Sentinel: SIEM
- Microsoft Defender: Endpoint protection
- Qualys: Vulnerability scanning
- Okta: SSO and MFA

### 2.3 People

**Total Employees:** 120
- Engineering: 50
- Clinical/Product: 15
- Operations: 10
- Security/Compliance: 8
- Customer Success: 25
- Administrative: 12

**Training:**
- **All Employees:** Annual HIPAA training (Privacy and Security Rule)
- **PHI Access Roles:** Additional training on minimum necessary, audit logging
- **Security Team:** Advanced security training
- **Developers:** Secure coding training

**Background Checks:** All workforce members undergo background checks prior to hire

### 2.4 Procedures

**Development:**
- Secure SDLC with security requirements
- Code review (all code)
- Security testing (SAST, DAST)
- Staging environment testing
- Production deployment with approval

**Operations:**
- 24/7 monitoring and on-call
- Incident response procedures
- Daily backup procedures
- Quarterly DR testing
- Monthly vulnerability scanning

**PHI-Specific:**
- PHI access request and approval
- PHI access logging and review
- PHI breach assessment procedures
- PHI disposal procedures

### 2.5 Data

**Protected Health Information (PHI):**
- **Patient Demographics:** Name, DOB, address, SSN, contact information
- **Clinical Data:** Diagnoses, procedures, medications, lab results, clinical notes, allergies, immunizations
- **Insurance:** Payer, policy number, claims information
- **Provider Data:** Treating physicians, referrals, care team

**Non-PHI Data:**
- Practice information (practice name, address, tax ID)
- User accounts (provider and staff logins)
- System configuration data
- Audit logs (PHI access logs stored separately)

**Data Flows:**
1. PHI enters via provider portal, HL7 interfaces, or FHIR API
2. PHI stored in encrypted Azure SQL Database
3. PHI documents stored in encrypted Blob Storage
4. PHI transmitted via TLS 1.3
5. PHI accessed by authorized providers via web/mobile apps
6. PHI backed up daily to encrypted storage in DR region
7. PHI deleted per retention policy (6 years minimum per state law) or customer request

---

## SECTION 3: BOUNDARIES

### 3.1 In-Scope

- EHR Application (web and mobile)
- Patient Portal
- HL7/FHIR Integration Engine
- Production infrastructure (East US and West US 2 regions)
- All systems processing, storing, or transmitting PHI

### 3.2 Out-of-Scope

- Corporate website (marketing only)
- Internal HR system (Workday)
- Internal financial system (QuickBooks)

### 3.3 Business Associate Relationships

**BAAs Executed With:**
- Microsoft Azure: Infrastructure and hosting
- Okta: Identity management
- SendGrid: Transactional email (appointment reminders)
- Twilio: SMS notifications
- AWS: Backup storage (S3 in isolated account)

All business associates have executed BAAs before PHI access granted.

### 3.4 Shared Responsibility

**HealthTech Responsibilities:**
- Application security and PHI protection
- Access controls and authentication
- Encryption at rest and in transit
- PHI audit logging
- Breach assessment and notification
- HIPAA compliance program

**Customer (Covered Entity) Responsibilities:**
- Appropriate use of system per HIPAA
- User access management in their practice
- End-user training
- Patient consent management
- Breach notification to patients (HealthTech assists)

**Azure Responsibilities:**
- Physical security
- Environmental controls
- Infrastructure security
- Hardware maintenance

---

## SECTION 4: SERVICE COMMITMENTS

### 4.1 Availability SLA

**Commitment:** 99.5% uptime during business hours (6 AM - 8 PM local time, Monday-Saturday), measured monthly

**Exclusions:** Planned maintenance (max 4 hours/month, 7-day notice)

**Clinical Impact:** Availability commitments consider patient care impact. Critical issues escalated immediately.

**Emergency Access:** During outages, providers can access patient summaries via emergency read-only mode or downloaded reports.

### 4.2 Security Commitments

**PHI Encryption:**
- At Rest: AES-256
- In Transit: TLS 1.3

**Access Controls:**
- Minimum necessary access to PHI
- Role-based access control
- Multi-factor authentication required for admin accounts
- Emergency access procedures with audit review

**Audit Logging:**
- Comprehensive logging of all PHI access
- Logs retained for 7 years
- Weekly sample reviews, monthly comprehensive reviews

**Breach Notification:**
- Risk assessment within 24 hours of incident
- Notification to covered entities within 60 days (HIPAA requirement)
- Assistance with patient notification

### 4.3 Recovery Objectives

**RTO:** 4 hours for EHR application (critical)
**RPO:** 15 minutes (database replication to DR region)

**Backup:**
- Continuous database replication to DR region
- Daily snapshots retained 30 days
- Weekly full backups retained 90 days

---

## SECTION 5: CONTROL EXAMPLES

### HIPAA-Aligned Security Control

**Control ID:** SEC-PHI-001
**TSC Point:** CC6.1, CC6.7
**HIPAA:** §164.312(a)(1) Access Control, §164.312(e)(1) Transmission Security

**Control:** PHI Encryption and Access Control

All PHI is encrypted at rest (AES-256) and in transit (TLS 1.3). Access to PHI is restricted to authorized workforce members based on minimum necessary principle.

**How it Works:**
- Azure SQL Database encryption enabled for all PHI databases
- Transparent Data Encryption (TDE) with keys in Azure Key Vault
- TLS 1.3 required for all client connections
- Application enforces minimum necessary: users see only patients they're treating
- Role-based access: physicians see full record, billing staff see only billing info
- All PHI access logged with user ID, timestamp, patient ID, action

**Who:** Enforced by database encryption and application code; Security team manages encryption keys

**When:** Continuous (all PHI encrypted and access-controlled); Key rotation annually

**Evidence:** Encryption configuration, TDE status, TLS configuration, access control code, PHI access logs

---

### HIPAA-Aligned Availability Control

**Control ID:** AV-HC-001
**TSC Point:** A1.3 (Recovery and Continuity)
**HIPAA:** §164.308(a)(7) Contingency Plan

**Control:** HIPAA Contingency Plan

HealthTech maintains a HIPAA-compliant contingency plan including data backup, disaster recovery, emergency mode operations, testing, and criticality analysis.

**Data Backup (§164.308(a)(7)(ii)(A)):**
- Automated continuous replication of PHI database to DR region
- Daily snapshots for point-in-time recovery
- Backup integrity tested weekly

**Disaster Recovery (§164.308(a)(7)(ii)(B)):**
- Documented DR plan with failover to West US 2 region
- RTO: 4 hours, RPO: 15 minutes
- Quarterly DR testing with documented results

**Emergency Mode Operations (§164.308(a)(7)(ii)(C)):**
- Emergency read-only access mode if application down
- Downloadable patient summary reports
- Manual downtime procedures for practices
- Annual emergency mode drills

**Testing (§164.308(a)(7)(ii)(D)):**
- Quarterly DR test
- Annual full contingency plan test
- Plan updated based on test results

**Criticality Analysis (§164.308(a)(7)(ii)(E)):**
- EHR application and patient database: Critical (RTO 4 hours)
- Billing system: High (RTO 24 hours)
- Reporting: Medium (RTO 48 hours)

**Who:** IT Operations manages backups and DR; CTO owns contingency plan; Quarterly tests by Operations with Compliance observation

**When:** Backups continuous; DR test quarterly; Full contingency test annually

**Evidence:** Contingency plan document, backup logs, DR test reports, criticality analysis, emergency mode procedures

---

### PHI Access Auditing Control

**Control ID:** SEC-PHI-005
**TSC Point:** CC7.2 (System Monitoring)
**HIPAA:** §164.312(b) Audit Controls

**Control:** Comprehensive PHI Access Logging and Review

All access to PHI is logged and logs reviewed for unauthorized access.

**How it Works:**
- Database audit logging captures all PHI access (user, timestamp, patient, action)
- Application logging records PHI views, modifications, deletions
- Logs centralized in Azure Sentinel
- Automated alerts for suspicious activity:
  - Bulk access (>100 patients in 1 hour)
  - Access outside business hours
  - Failed access attempts (>5 in 10 minutes)
  - Access to VIP patients or employee records
- Weekly: Random sample review (50 access events minimum)
- Monthly: All alert investigations reviewed
- Ad-hoc: Investigations upon patient or provider complaint

**Who:** Automated logging; Security Operations monitors alerts; Privacy Officer performs weekly reviews

**When:** Continuous logging; Real-time alerting; Weekly and monthly reviews

**Evidence:** Audit log configurations, SIEM alert rules, weekly review reports, monthly summary reports, investigation tickets

---

## KEY TAKEAWAYS FROM THIS EXAMPLE

1. **Business Associate Status**: Clearly stated upfront
2. **PHI Identification**: Specific types of PHI listed
3. **HIPAA Alignment**: Controls mapped to HIPAA requirements
4. **BAA Documentation**: All business associates listed
5. **Contingency Plan**: HIPAA-required components detailed
6. **PHI Controls**: Encryption, access controls, audit logging all addressed
7. **Patient Care Focus**: Availability commitments consider clinical impact
8. **Emergency Procedures**: Emergency access and downtime procedures documented

This example demonstrates appropriate healthcare-specific considerations for a SOC 2 system description.

