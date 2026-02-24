# SYSTEM DESCRIPTION

**{{COMPANY_NAME}}**
**SOC 2 Type [I / II] Examination**

**Trust Service Criteria:**
☐ Security
☐ Availability
☐ Confidentiality
☐ Processing Integrity
☐ Privacy

**Examination Period:** {{START_DATE}} to {{END_DATE}}

**Description as of:** {{END_DATE}}

**Version:** {{VERSION_NUMBER}}

**Date:** {{DOCUMENT_DATE}}

---

## TABLE OF CONTENTS

1. [Overview of the System](#section-1-overview-of-the-system)
2. [System Components](#section-2-system-components)
3. [Boundaries](#section-3-boundaries)
4. [Principal Service Commitments and System Requirements](#section-4-principal-service-commitments-and-system-requirements)
5. [Control Environment and Control Objectives](#section-5-control-environment-and-control-objectives)

Appendices:
- Appendix A: Organizational Chart
- Appendix B: System Architecture Diagram
- Appendix C: Network Diagram
- Appendix D: Data Flow Diagram
- Appendix E: Acronym Glossary

---

## SECTION 1: OVERVIEW OF THE SYSTEM

### 1.1 Company Background

{{COMPANY_NAME}} ("the Company") was founded in {{FOUNDED_YEAR}} and is headquartered in {{HEADQUARTERS_LOCATION}}. The Company {{BUSINESS_DESCRIPTION}}.

**Ownership Structure:**
{{OWNERSHIP_STRUCTURE}}

**Industry:** {{INDUSTRY_TYPE}}

**Regulatory Environment:**
☐ HIPAA-regulated (Business Associate)
☐ HIPAA-regulated (Covered Entity)
☐ Other regulations: {{OTHER_REGULATIONS}}

### 1.2 Nature of Services

The Company provides {{SERVICE_DESCRIPTION}}.

**Core Services:**
1. {{SERVICE_1_NAME}}: {{SERVICE_1_DESCRIPTION}}
2. {{SERVICE_2_NAME}}: {{SERVICE_2_DESCRIPTION}}
3. {{SERVICE_3_NAME}}: {{SERVICE_3_DESCRIPTION}}

**Service Delivery Model:**
☐ Cloud-based SaaS
☐ On-premise deployment
☐ Hybrid (cloud and on-premise)

**Customers:** {{CUSTOMER_BASE_DESCRIPTION}}

**Geographic Reach:** {{GEOGRAPHIC_REACH}}

### 1.3 Organizational Structure and Key Stakeholders

**Governance:**
- Board of Directors: {{BOARD_COMPOSITION}}
- CEO: {{CEO_NAME}}
- {{OTHER_EXECUTIVES}}

**Key Roles Related to Controls:**

| Role | Responsibilities |
|------|------------------|
| Chief Executive Officer (CEO) | Overall responsibility for system of internal control |
| Chief Technology Officer (CTO) | Oversight of technology infrastructure and operations |
| Chief Information Security Officer (CISO) | Security strategy, policies, and controls |
| VP of Engineering | Software development, release management |
| VP of Operations | System operations, monitoring, incident response |
| Data Protection Officer / Privacy Officer | Privacy compliance, data subject rights [if applicable] |
| Compliance Officer | SOC 2, HIPAA, and regulatory compliance [if applicable] |

**Organizational Chart:** See Appendix A

**Staffing:**
- Total employees: {{TOTAL_EMPLOYEES}}
- Engineering/Technical: {{ENGINEERING_COUNT}}
- Security: {{SECURITY_COUNT}}
- Operations: {{OPERATIONS_COUNT}}

### 1.4 Physical Locations

**Corporate Headquarters:**
{{HEADQUARTERS_ADDRESS}}

**Office Locations:**
- {{LOCATION_1}}: {{LOCATION_1_PURPOSE}}
- {{LOCATION_2}}: {{LOCATION_2_PURPOSE}}

**Data Center Locations:**
☐ Cloud-based (no physical data centers owned/operated)
- Provider: {{CLOUD_PROVIDER}}
- Regions: {{CLOUD_REGIONS}}

☐ Company-operated data centers:
- {{DATACENTER_LOCATION}}: {{DATACENTER_DESCRIPTION}}

**Remote Workforce:**
{{REMOTE_WORKFORCE_DESCRIPTION}}

---

## SECTION 2: SYSTEM COMPONENTS

### 2.1 Infrastructure

#### 2.1.1 Cloud Infrastructure

**Cloud Provider:** {{CLOUD_PROVIDER}}

**Services Used:**
- **Compute:** {{COMPUTE_SERVICES}}
- **Database:** {{DATABASE_SERVICES}}
- **Storage:** {{STORAGE_SERVICES}}
- **Networking:** {{NETWORKING_SERVICES}}
- **Other:** {{OTHER_SERVICES}}

**Regions:**
- **Primary:** {{PRIMARY_REGION}}
- **Secondary/DR:** {{DR_REGION}}
- **Additional:** {{ADDITIONAL_REGIONS}}

**Shared Responsibility Model:**
- **Provider Responsibility:** Physical security, environmental controls, hardware maintenance, virtualization layer security
- **Company Responsibility:** Guest OS, application, data, access management, encryption, network configuration

**Provider SOC 2:** {{CLOUD_PROVIDER}} maintains SOC 2 Type II certification. Report available from {{CLOUD_PROVIDER}} upon request.

#### 2.1.2 Network Infrastructure

**Architecture:** {{NETWORK_ARCHITECTURE_DESCRIPTION}}

**Components:**
- Firewalls / Security Groups: {{FIREWALL_DESCRIPTION}}
- Load Balancers: {{LOAD_BALANCER_DESCRIPTION}}
- VPN: {{VPN_DESCRIPTION}}
- CDN: {{CDN_DESCRIPTION}}
- DNS: {{DNS_PROVIDER}}

**Network Diagram:** See Appendix C

#### 2.1.3 Physical Infrastructure

[If applicable, or state:]
The Company does not operate physical data centers. All infrastructure is cloud-based as described in Section 2.1.1.

### 2.2 Software

#### 2.2.1 Application Software

**Primary Applications (In-Scope):**

| Application | Purpose | Type | Version |
|-------------|---------|------|---------|
| {{APP_NAME}} | {{APP_PURPOSE}} | Custom-developed / Commercial | {{APP_VERSION}} |
| {{APP_NAME_2}} | {{APP_PURPOSE_2}} | Custom-developed / Commercial | {{APP_VERSION_2}} |

**Key Technologies:**
- **Frontend:** {{FRONTEND_TECH}}
- **Backend:** {{BACKEND_TECH}}
- **API:** {{API_TECH}}

#### 2.2.2 Database Systems

| Database | Purpose | Platform | Encryption |
|----------|---------|----------|------------|
| {{DB_NAME}} | {{DB_PURPOSE}} | {{DB_PLATFORM}} | AES-256 at rest, TLS in transit |

#### 2.2.3 Operating Systems

- **Application Servers:** {{APP_SERVER_OS}}
- **Database Servers:** [Managed by cloud provider / {{DB_SERVER_OS}}]

#### 2.2.4 Security Software

| Software | Purpose | Coverage |
|----------|---------|----------|
| {{ENDPOINT_PROTECTION}} | Antivirus/anti-malware | All workstations and servers |
| {{SIEM_TOOL}} | Security monitoring | All systems |
| {{VULNERABILITY_SCANNER}} | Vulnerability management | All infrastructure |
| {{WAF_TOOL}} | Web application firewall | All web applications |
| {{IDS_IPS_TOOL}} | Intrusion detection | Network |

#### 2.2.5 Monitoring and Management Tools

| Tool | Purpose |
|------|---------|
| {{INFRA_MONITORING}} | Infrastructure monitoring |
| {{APM_TOOL}} | Application performance monitoring |
| {{ALERTING_TOOL}} | Incident alerting |
| {{LOG_MANAGEMENT}} | Log management and SIEM |

**Architecture Diagram:** See Appendix B

### 2.3 People

#### 2.3.1 Roles and Responsibilities

**Engineering Team:**
- Software development
- Code review and security testing
- Release management
- Technical architecture

**Operations Team:**
- System monitoring and availability
- Incident response
- Backup and recovery
- Capacity management

**Security Team:**
- Security policies and standards
- Security monitoring and incident response
- Vulnerability management
- Access reviews
- Security awareness training

**Compliance Team:**
- SOC 2 coordination
- [HIPAA compliance - if applicable]
- Policy management
- Audit coordination

#### 2.3.2 Training and Competency

All personnel receive:
- **Onboarding Training:** Security awareness, acceptable use policies, role-specific training
- **Annual Training:** Security awareness refresher, [HIPAA training - if applicable]
- **Role-Specific Training:** Technical security training for engineers, incident response training for operations

**Background Checks:** Conducted for all employees prior to hire

#### 2.3.3 Third-Party Personnel

[If applicable:]
The Company engages [contractors / offshore development teams / managed service providers] for {{THIRD_PARTY_PURPOSE}}. Third-party personnel with system access:
- Subject to same background checks as employees
- Bound by confidentiality agreements
- Complete security training
- Access reviewed quarterly

### 2.4 Procedures

#### 2.4.1 Operational Procedures

**Key Procedures:**
- System monitoring and alerting
- Incident response
- Backup and recovery
- Capacity management
- Performance optimization

#### 2.4.2 Security Procedures

**Key Procedures:**
- Access provisioning and deprovisioning
- Access review
- Vulnerability management
- Patch management
- Security incident response
- [PHI breach assessment - if applicable]

#### 2.4.3 Change Management Procedures

**Development and Deployment:**
- {{CI_CD_PROCESS_DESCRIPTION}}
- Code review requirements
- Staging environment testing
- Production deployment approval
- Rollback procedures

**Infrastructure Changes:**
- Change request and approval process
- Testing requirements
- Change implementation and validation
- Change documentation

#### 2.4.4 Business Continuity Procedures

**Key Procedures:**
- Disaster recovery plan
- Business continuity plan
- Emergency communication procedures
- [Emergency mode operations - if healthcare]

### 2.5 Data

#### 2.5.1 Types of Data Processed

**Customer Data:**
- {{CUSTOMER_DATA_TYPES}}
- [For Healthcare: "Protected Health Information (PHI) including patient demographics, clinical data, billing information"]

**Company Data:**
- System configuration data
- Application logs (non-customer data)
- Employee information

#### 2.5.2 Data Classification

| Classification | Description | Examples | Protection Requirements |
|----------------|-------------|----------|------------------------|
| Public | Publicly available | Marketing materials | None |
| Internal | Internal use only | Internal docs | Access controls |
| Confidential | Sensitive company data | Financial data, IP | Encryption, strict access |
| [PHI / Customer Data] | [Highest sensitivity] | [Customer/PHI data] | Encryption, comprehensive logging, minimum necessary |

#### 2.5.3 Data Flows

**Data Entry:**
- {{DATA_ENTRY_METHODS}}

**Data Processing:**
- {{DATA_PROCESSING_METHODS}}

**Data Transmission:**
- {{DATA_TRANSMISSION_METHODS}}

**Data Storage:**
- {{DATA_STORAGE_LOCATIONS}}

**Data Disposal:**
- {{DATA_DISPOSAL_METHODS}}

**Data Flow Diagram:** See Appendix D

---

## SECTION 3: BOUNDARIES

### 3.1 System Boundaries

The system boundary encompasses all infrastructure, applications, data, people, and procedures necessary to provide {{SERVICE_NAME}} to customers.

### 3.2 In-Scope

**Systems and Applications:**
- {{IN_SCOPE_SYSTEMS}}

**Infrastructure:**
- {{IN_SCOPE_INFRASTRUCTURE}}

**Locations:**
- {{IN_SCOPE_LOCATIONS}}

**Data:**
- {{IN_SCOPE_DATA}}

**Third-Party Services (In-Scope):**

| Service Provider | Service Provided | Data Processed | SOC 2 Report |
|-----------------|------------------|----------------|--------------|
| {{PROVIDER_1}} | {{SERVICE_1}} | {{DATA_TYPES_1}} | ☐ Available ☐ N/A |
| {{PROVIDER_2}} | {{SERVICE_2}} | {{DATA_TYPES_2}} | ☐ Available ☐ N/A |

### 3.3 Out-of-Scope

**Excluded from Scope:**
- {{EXCLUDED_SYSTEMS}}

**Example:**
- Corporate website (marketing only, no customer data)
- Internal HR systems (employee data, not relevant to customer-facing services)
- [Other exclusions]

### 3.4 Integration Points

**Systems Integrated With:**
- {{INTEGRATION_1}}: {{INTEGRATION_DESCRIPTION_1}}
- {{INTEGRATION_2}}: {{INTEGRATION_DESCRIPTION_2}}

**APIs and Interfaces:**
- {{API_DESCRIPTION}}
- {{THIRD_PARTY_INTEGRATIONS}}

### 3.5 Shared Responsibility

**[For SaaS] Provider vs. Customer:**

**Provider Responsibilities:**
- Platform security and availability
- Infrastructure security
- Application security
- Data encryption
- Backup infrastructure
- Security monitoring

**Customer Responsibilities:**
- User access management within their tenant
- User authentication configuration
- Data classification per their policies
- User security awareness training

**[For Healthcare] Company vs. Business Associates:**

**Company Responsibilities:**
- Application security and PHI protection
- Access controls and audit logging
- Encryption of PHI
- Breach assessment and notification
- BAA compliance

**Business Associate Responsibilities:**
- [Cloud provider]: Infrastructure security, physical security
- [Other BAs]: {{BA_RESPONSIBILITIES}}

**Boundary Diagram:** See Appendix [X]

---

## SECTION 4: PRINCIPAL SERVICE COMMITMENTS AND SYSTEM REQUIREMENTS

### 4.1 Service Level Agreements (SLAs)

#### 4.1.1 Availability Commitment

**Target:** {{AVAILABILITY_TARGET}}% uptime measured monthly

**Measurement Method:**
- Uptime = (Total Minutes in Month - Downtime Minutes) / Total Minutes in Month × 100
- Downtime excludes:
  - Planned maintenance (maximum {{MAINTENANCE_WINDOW}} hours per month with {{NOTICE_PERIOD}} hours notice)
  - Customer-caused outages (misconfigurations, invalid API calls)
  - Force majeure events
  - Third-party service failures beyond our control

**Monitoring:** Real-time status available at {{STATUS_PAGE_URL}}

**Service Credits:** {{SERVICE_CREDITS_POLICY}}

#### 4.1.2 Performance Commitment

**Response Times:**
- Web application page load: {{PAGE_LOAD_TARGET}} (p95)
- API response time: {{API_GET_TARGET}} for GET requests (p95)
- API response time: {{API_POST_TARGET}} for POST/PUT requests (p95)

**Throughput:**
- API rate limits: {{RATE_LIMIT_STANDARD}} (standard tier), {{RATE_LIMIT_ENTERPRISE}} (enterprise tier)

#### 4.1.3 Support Commitment

**Support Hours:** {{SUPPORT_HOURS}}

**Response Times:**
- Critical (P0): {{P0_RESPONSE_TIME}} acknowledgment, {{P0_RESOLUTION_TARGET}} resolution target
- High (P1): {{P1_RESPONSE_TIME}} acknowledgment, {{P1_RESOLUTION_TARGET}} resolution target
- Medium (P2): {{P2_RESPONSE_TIME}} acknowledgment, {{P2_RESOLUTION_TARGET}} resolution target
- Low (P3): {{P3_RESPONSE_TIME}} acknowledgment, {{P3_RESOLUTION_TARGET}} resolution target

### 4.2 Security Commitments

**Data Encryption:**
- All data encrypted in transit (TLS 1.2 minimum, TLS 1.3 preferred)
- All data encrypted at rest (AES-256)
- [All PHI encrypted per HIPAA requirements - if applicable]

**Access Controls:**
- Multi-factor authentication available [required for admin users]
- Role-based access control (RBAC)
- Least privilege principle enforced

**Security Monitoring:**
- 24/7 security monitoring
- Security incident response team
- Vulnerability management program

**Compliance:**
- SOC 2 Type II annual audit
- [HIPAA compliance program - if applicable]
- Regular penetration testing
- Annual security training for all personnel

### 4.3 Recovery Objectives

**Recovery Time Objective (RTO):**
- Critical systems: {{RTO_CRITICAL}}
- Non-critical systems: {{RTO_NON_CRITICAL}}

**Recovery Point Objective (RPO):**
- Critical data: {{RPO_CRITICAL}} (continuous replication)
- Non-critical data: {{RPO_NON_CRITICAL}} (daily backups)

**Backup Frequency:**
- Database: {{DATABASE_BACKUP_FREQUENCY}}
- Files: {{FILE_BACKUP_FREQUENCY}}

### 4.4 Customer Communication

**Methods:**
- Status page: {{STATUS_PAGE_URL}}
- Email notifications: Opt-in for system status
- In-app notifications: For important updates
- Support portal: {{SUPPORT_PORTAL_URL}}

**Notification Triggers:**
- Planned maintenance: {{MAINTENANCE_NOTICE_PERIOD}} advance notice
- Unplanned outage: Immediate notification
- Security incidents affecting customers: Within {{INCIDENT_NOTICE_PERIOD}} of determination
- [HIPAA breach: Within 60 days - if applicable]

### 4.5 Data Retention and Disposal

**Retention:**
- Customer data: Retained while customer account active + {{DATA_RETENTION_PERIOD}} after account closure
- Backup data: {{BACKUP_RETENTION_PERIOD}} rolling retention
- Audit logs: {{LOG_RETENTION_PERIOD}}
- [PHI: Minimum 6 years per state requirements - if applicable]

**Disposal:**
- Secure deletion per data disposal policy
- [Certificates of destruction for disposed storage media]
- [PHI sanitized per NIST 800-88 guidelines - if applicable]

---

## SECTION 5: CONTROL ENVIRONMENT AND CONTROL OBJECTIVES

### 5.1 Control Environment

#### 5.1.1 Governance and Oversight

The Board of Directors provides oversight of the Company's risk management and internal control systems. {{BOARD_OVERSIGHT_DESCRIPTION}}

Management is responsible for designing, implementing, and operating the system of internal controls. The {{SECURITY_LEADER_TITLE}} has primary responsibility for security controls, with support from {{SUPPORTING_ROLES}}.

#### 5.1.2 Risk Assessment

The Company conducts formal risk assessments {{RISK_ASSESSMENT_FREQUENCY}} to identify and evaluate risks to the achievement of security and availability objectives.

**Risk Assessment Process:**
1. Identify assets and threats
2. Assess vulnerabilities
3. Determine likelihood and impact
4. Identify mitigating controls
5. Calculate residual risk
6. Document and report to management

**Risk Register:** Maintained and reviewed {{RISK_REGISTER_REVIEW_FREQUENCY}}

**[For Healthcare: HIPAA Security Rule requires risk analysis - documented as part of security risk assessment process]**

#### 5.1.3 Information and Communication

**Internal Communication:**
- Security policies published on {{POLICY_LOCATION}}
- Security awareness communications {{AWARENESS_FREQUENCY}}
- Incident notifications via {{INTERNAL_COMMUNICATION_TOOLS}}
- Regular security team meetings

**External Communication:**
- Customer security documentation
- Vendor security requirements
- [BAA execution - if healthcare]
- Security incident notifications to customers

#### 5.1.4 Monitoring

**Control Monitoring:**
- Ongoing: Automated monitoring and alerting
- Periodic: Control testing by [internal audit / compliance team]
- Annual: External SOC 2 audit

**Deficiency Management:**
- Control deficiencies tracked in {{TRACKING_SYSTEM}}
- Remediation plans with deadlines
- Escalation to management for significant deficiencies

### 5.2 Control Objectives - Security (Common Criteria)

[For each TSC CC point, document control objectives and related controls]

#### CC1: Control Environment

**Control Objective:** [State objective]

**Controls:**

**Control CC1-001: Code of Conduct**
[Full control description following who/what/when/how/evidence format]

[Continue for all relevant CC1 controls...]

#### CC2: Communication and Information

[Similar structure...]

#### CC3: Risk Assessment

[Similar structure...]

#### CC4: Monitoring Activities

[Similar structure...]

#### CC5: Control Activities

[Similar structure...]

#### CC6: Logical and Physical Access Controls

[Key controls for CC6...]

#### CC7: System Operations

[Key controls for CC7...]

#### CC8: Change Management

[Key controls for CC8...]

#### CC9: Risk Mitigation

[Key controls for CC9...]

### 5.3 Control Objectives - Availability

#### A1.1: Processing Capacity

**Control Objective:** Monitor and manage system capacity to meet availability commitments.

**Controls:**

**Control AV-001: Capacity Monitoring**
[Full control description]

**Control AV-002: Capacity Planning**
[Full control description]

**Control AV-003: Auto-Scaling**
[Full control description]

#### A1.2: Environmental Protections and Backup

**Control Objective:** Maintain backup and recovery infrastructure to support availability.

**Controls:**

**Control AV-004: Automated Backups**
[Full control description]

**Control AV-005: Backup Testing**
[Full control description]

#### A1.3: Recovery and Continuity

**Control Objective:** Provide for recovery and continuity of operations.

**Controls:**

**Control AV-006: Disaster Recovery Plan**
[Full control description]

**Control AV-007: DR Testing**
[Full control description]

**Control AV-008: Business Continuity Plan**
[Full control description]

---

## APPENDICES

### Appendix A: Organizational Chart
[Insert organizational chart showing reporting relationships relevant to controls]

### Appendix B: System Architecture Diagram
[Insert system architecture diagram showing applications, databases, infrastructure]

### Appendix C: Network Diagram
[Insert network diagram showing network segmentation, firewalls, external connections]

### Appendix D: Data Flow Diagram
[Insert data flow diagram showing how data moves through the system]

### Appendix E: Acronym Glossary

| Acronym | Definition |
|---------|------------|
| API | Application Programming Interface |
| AWS | Amazon Web Services |
| BAA | Business Associate Agreement |
| CDN | Content Delivery Network |
| CISO | Chief Information Security Officer |
| DR | Disaster Recovery |
| ePHI | Electronic Protected Health Information |
| HIPAA | Health Insurance Portability and Accountability Act |
| IDS/IPS | Intrusion Detection System / Intrusion Prevention System |
| MFA | Multi-Factor Authentication |
| PHI | Protected Health Information |
| RBAC | Role-Based Access Control |
| RPO | Recovery Point Objective |
| RTO | Recovery Time Objective |
| SIEM | Security Information and Event Management |
| SLA | Service Level Agreement |
| SOC | Service Organization Control |
| SSO | Single Sign-On |
| TLS | Transport Layer Security |
| TSC | Trust Service Criteria |
| VPN | Virtual Private Network |
| WAF | Web Application Firewall |

---

**END OF SYSTEM DESCRIPTION**

---

## SIGN-OFF

This system description has been reviewed and approved by management.

**Chief Executive Officer:**

Signature: _________________________ Date: _____________
{{CEO_NAME}}

**Chief Information Security Officer:**

Signature: _________________________ Date: _____________
{{CISO_NAME}}

---

## INSTRUCTIONS FOR USE:

1. Save a copy of this template with your company name and date
2. Complete all {{PLACEHOLDER}} fields
3. Check all applicable ☐ boxes
4. Expand Section 5 with all your specific controls (this template provides structure)
5. Create and attach all diagrams (Appendices A-D)
6. Remove this instructions section before finalizing
7. Have all stakeholders review
8. Run `scripts/completeness_checker.py` to validate
9. Run `scripts/control_coverage_validator.py` to ensure TSC coverage
10. Obtain management sign-off
11. Version and date the final document
12. Provide to auditor at audit kickoff
