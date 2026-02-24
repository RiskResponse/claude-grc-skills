# Trust Service Criteria - Security (Common Criteria)

## Overview

The Security category addresses the protection of system resources against unauthorized access. Security commitments relate to protecting information and systems from unauthorized access, unauthorized disclosure of information, and damage to systems that could compromise the availability, integrity, confidentiality, and privacy of information or systems.

**Scope**: This document covers the Security Common Criteria (CC) that apply to ALL Trust Service categories (Security, Availability, Confidentiality, Processing Integrity, and Privacy).

## Common Criteria Structure

The Common Criteria are organized into 9 focus areas:
- **CC1**: Control Environment
- **CC2**: Communication and Information
- **CC3**: Risk Assessment
- **CC4**: Monitoring Activities
- **CC5**: Control Activities
- **CC6**: Logical and Physical Access Controls
- **CC7**: System Operations
- **CC8**: Change Management
- **CC9**: Risk Mitigation

Each focus area contains multiple points of focus that must be addressed.

---

## CC1: Control Environment

### CC1.1 - COSO Principle 1: The entity demonstrates a commitment to integrity and ethical values.

**What This Means**:
The organization has established and maintains a culture of integrity and ethics that influences control effectiveness.

**Control Examples**:
- Code of conduct exists and is communicated to all personnel
- Ethics training is provided annually
- Confidentiality and acceptable use agreements are signed
- Disciplinary processes for violations are documented and enforced
- Tone at the top demonstrates ethical behavior

**Evidence**:
- Signed code of conduct acknowledgments
- Ethics training completion records
- Confidentiality agreements
- Disciplinary action log (if applicable)

**SaaS Considerations**:
- Code of conduct should address customer data protection
- Include vendor code of conduct requirements

**Healthcare Considerations**:
- Ethics training should include HIPAA principles
- Conflict of interest policies for PHI access

---

### CC1.2 - COSO Principle 2: The board of directors demonstrates independence from management and exercises oversight of the development and performance of internal control.

**What This Means**:
The board provides objective oversight of management and control effectiveness.

**Control Examples**:
- Board includes independent members
- Regular board meetings with documented minutes
- Board oversight of risk management
- Board audit committee exists (if applicable)
- Board reviews control effectiveness reports

**Evidence**:
- Board composition documentation
- Board meeting minutes
- Audit committee charter
- Reports presented to board

**SaaS Considerations**:
- For startups, may have advisory board or investor oversight
- Document governance structure clearly

**Healthcare Considerations**:
- Board oversight of HIPAA compliance
- Review of breach reports and risk assessments

---

### CC1.3 - COSO Principle 3: Management establishes, with board oversight, structures, reporting lines, and appropriate authorities and responsibilities in the pursuit of objectives.

**What This Means**:
Clear organizational structure exists with defined responsibilities and authorities.

**Control Examples**:
- Organizational chart maintained and current
- Job descriptions include security responsibilities
- Reporting structures clearly defined
- Authority matrices document approval requirements
- Separation of duties implemented

**Evidence**:
- Current organizational chart
- Job descriptions
- Authority matrix/approval policies
- Separation of duties matrix

**SaaS Considerations**:
- Document who owns platform security vs. infrastructure security
- Clear delineation of DevOps responsibilities

**Healthcare Considerations**:
- Privacy officer and security officer roles defined
- Clear responsibility for PHI protection

---

### CC1.4 - COSO Principle 4: The entity demonstrates a commitment to attract, develop, and retain competent individuals in alignment with objectives.

**What This Means**:
The organization ensures personnel have appropriate competence for their roles.

**Control Examples**:
- Background checks performed on employees
- Technical competency requirements defined for roles
- Training programs for security and operations
- Performance evaluations assess competency
- Succession planning for critical roles

**Evidence**:
- Background check policy and completion records
- Training curricula and completion records
- Performance review documentation
- Competency requirements by role

**SaaS Considerations**:
- Specialized training for platform engineering
- DevSecOps competency development

**Healthcare Considerations**:
- HIPAA training for all workforce members
- Additional training for PHI access roles
- Background checks specific to healthcare

---

### CC1.5 - COSO Principle 5: The entity holds individuals accountable for their internal control responsibilities in the pursuit of objectives.

**What This Means**:
There are consequences for not meeting control responsibilities.

**Control Examples**:
- Performance objectives include security responsibilities
- Accountability measures documented
- Control owners identified for each control
- Disciplinary procedures for security violations
- Incentives aligned with security objectives

**Evidence**:
- Performance review criteria
- Control owner assignments
- Disciplinary policy
- Remediation tracking for control deficiencies

**SaaS Considerations**:
- Incident response accountability
- On-call rotation responsibilities

**Healthcare Considerations**:
- Sanctions for HIPAA violations
- Accountability for PHI breaches

---

## CC2: Communication and Information

### CC2.1 - COSO Principle 13: The entity obtains or generates and uses relevant, quality information to support the functioning of internal control.

**What This Means**:
Information needed for controls is identified, captured, and used.

**Control Examples**:
- System logs collected and retained
- Security event monitoring in place
- Performance metrics tracked
- Risk information gathered and analyzed
- Information from external sources considered (threat intelligence)

**Evidence**:
- Log retention policies
- SIEM/monitoring configurations
- Security reports and metrics
- Threat intelligence subscriptions

**SaaS Considerations**:
- Application logs, infrastructure logs, and security logs
- Customer usage metrics for capacity planning

**Healthcare Considerations**:
- Audit logs for PHI access
- Security incident information

---

### CC2.2 - COSO Principle 14: The entity internally communicates information, including objectives and responsibilities for internal control, necessary to support the functioning of internal control.

**What This Means**:
Internal communication channels ensure control-related information reaches appropriate personnel.

**Control Examples**:
- Security policies published and accessible
- Security awareness communications
- Incident notification procedures
- Change communication processes
- Regular team meetings with documented agendas

**Evidence**:
- Policy repository access logs
- Security awareness campaign materials
- Communication distribution lists
- Meeting minutes

**SaaS Considerations**:
- Engineering team security bulletins
- Incident post-mortems shared internally

**Healthcare Considerations**:
- HIPAA policy communication
- Breach notification internal processes

---

### CC2.3 - COSO Principle 15: The entity communicates with external parties regarding matters affecting the functioning of internal control.

**What This Means**:
Communication with external parties (customers, vendors, regulators) is established.

**Control Examples**:
- Customer communication channels for security
- Vendor security requirements communicated
- Regulator reporting procedures
- Incident notification to affected parties
- Third-party assessment sharing (SOC 2 reports)

**Evidence**:
- Customer security documentation
- Vendor contracts with security terms
- Regulatory filings
- Customer incident notifications

**SaaS Considerations**:
- Status page for availability communications
- Security advisory notices to customers
- SOC 2 report sharing process

**Healthcare Considerations**:
- BAA execution with business associates
- HHS breach reporting
- Patient/customer breach notifications

---

## CC3: Risk Assessment

### CC3.1 - COSO Principle 6: The entity specifies objectives with sufficient clarity to enable the identification and assessment of risks relating to objectives.

**What This Means**:
Security and operational objectives are clearly defined.

**Control Examples**:
- Security objectives documented and approved
- Availability targets defined (SLAs)
- Risk appetite statement
- Security strategy aligned with business objectives
- Objectives communicated to relevant personnel

**Evidence**:
- Security objectives documentation
- SLA documentation
- Risk appetite statement
- Board/management approvals

**SaaS Considerations**:
- Availability objectives (e.g., 99.9% uptime)
- Platform security objectives

**Healthcare Considerations**:
- PHI protection objectives
- HIPAA compliance objectives

---

### CC3.2 - COSO Principle 7: The entity identifies risks to the achievement of its objectives across the entity and analyzes risks as a basis for determining how the risks should be managed.

**What This Means**:
A risk assessment process identifies and analyzes risks.

**Control Examples**:
- Annual (minimum) risk assessment performed
- Risk identification methodology
- Risk analysis (likelihood and impact)
- Risk register maintained
- Risk owners assigned

**Evidence**:
- Risk assessment reports
- Risk register
- Risk analysis documentation
- Risk owner assignments

**SaaS Considerations**:
- Cloud infrastructure risks
- Multi-tenant security risks
- Third-party service risks

**Healthcare Considerations**:
- HIPAA Security Rule risk analysis required
- PHI breach risks
- Business associate risks

---

### CC3.3 - COSO Principle 8: The entity considers the potential for fraud in assessing risks to the achievement of objectives.

**What This Means**:
Fraud risks are specifically assessed.

**Control Examples**:
- Fraud risk assessment conducted
- Fraud scenarios identified (internal and external)
- Anti-fraud controls designed
- Whistleblower mechanisms
- Fraud monitoring and detection

**Evidence**:
- Fraud risk assessment
- Whistleblower hotline documentation
- Fraud detection reports

**SaaS Considerations**:
- Account takeover fraud
- Payment fraud
- Insider threats

**Healthcare Considerations**:
- PHI theft or misuse
- Insurance fraud
- Identity theft risks

---

### CC3.4 - COSO Principle 9: The entity identifies and assesses changes that could significantly impact the system of internal control.

**What This Means**:
Changes that affect controls are identified and assessed.

**Control Examples**:
- Change impact assessments include security
- New systems/services trigger security review
- Organizational changes assessed for control impact
- Regulatory changes monitored
- Vendor changes evaluated

**Evidence**:
- Change impact assessment forms
- Security review checklists
- Regulatory change log
- Vendor change notifications

**SaaS Considerations**:
- New cloud services adoption
- Architecture changes
- Major release impact assessments

**Healthcare Considerations**:
- New PHI uses or disclosures
- Regulatory updates (HIPAA, HITECH)
- New business associate arrangements

---

## CC4: Monitoring Activities

### CC4.1 - COSO Principle 16: The entity selects, develops, and performs ongoing and/or separate evaluations to ascertain whether the components of internal control are present and functioning.

**What This Means**:
Controls are monitored to ensure they're working effectively.

**Control Examples**:
- Ongoing monitoring activities (automated alerts, dashboard reviews)
- Periodic control testing
- Internal audits
- Vulnerability assessments
- Penetration testing
- Log reviews

**Evidence**:
- Monitoring dashboards
- Control testing results
- Internal audit reports
- Vulnerability scan reports
- Penetration test reports

**SaaS Considerations**:
- Continuous security monitoring
- Automated vulnerability scanning
- Application security testing

**Healthcare Considerations**:
- PHI access audits
- Security incident review
- Compliance audits

---

### CC4.2 - COSO Principle 17: The entity evaluates and communicates internal control deficiencies in a timely manner to those parties responsible for taking corrective action, including senior management and the board of directors, as appropriate.

**What This Means**:
Control deficiencies are identified, reported, and remediated.

**Control Examples**:
- Deficiency identification process
- Remediation tracking system
- Escalation procedures for significant deficiencies
- Regular reporting to management and board
- Audit findings tracked to closure

**Evidence**:
- Deficiency reports
- Remediation tracking logs
- Management/board reports
- Audit finding closure documentation

**SaaS Considerations**:
- Bug bounty program findings
- Penetration test findings
- Code review findings

**Healthcare Considerations**:
- HIPAA audit findings
- Breach investigation findings
- Corrective action plans

---

## CC5: Control Activities

### CC5.1 - COSO Principle 10: The entity selects and develops control activities that contribute to the mitigation of risks to the achievement of objectives to acceptable levels.

**What This Means**:
Control activities are designed to address identified risks.

**Control Examples**:
- Control activities documented in policies
- Controls mapped to risks
- Mix of preventive and detective controls
- Controls appropriate to risk level
- Compensating controls where needed

**Evidence**:
- Policy documentation
- Risk-control matrices
- Control descriptions
- Compensating control justifications

**SaaS Considerations**:
- Technical controls (automated)
- Operational controls (manual)
- Multi-tenant isolation controls

**Healthcare Considerations**:
- PHI access controls
- Encryption controls
- Audit logging controls

---

### CC5.2 - COSO Principle 11: The entity also selects and develops general control activities over technology to support the achievement of objectives.

**What This Means**:
Technology controls are implemented to support security and operations.

**Control Examples**:
- Access control systems
- Encryption technologies
- Network security controls (firewalls, IDS/IPS)
- Security monitoring tools
- Backup and recovery systems
- Configuration management tools

**Evidence**:
- System configurations
- Technology inventory
- Tool documentation
- Automated control reports

**SaaS Considerations**:
- Cloud security controls (security groups, IAM)
- Container security
- API security controls

**Healthcare Considerations**:
- Encryption at rest and in transit
- Audit log technology
- Access control systems for PHI

---

### CC5.3 - COSO Principle 12: The entity deploys control activities through policies that establish what is expected and in procedures that put policies into action.

**What This Means**:
Policies and procedures document and guide control activities.

**Control Examples**:
- Security policies documented and approved
- Procedures for control execution
- Policies reviewed and updated periodically
- Policies communicated to relevant personnel
- Procedures include step-by-step instructions

**Evidence**:
- Policy documents
- Procedure documents
- Policy review logs
- Communication records
- Policy acknowledgment forms

**SaaS Considerations**:
- Engineering procedures
- Operations runbooks
- Incident response procedures

**Healthcare Considerations**:
- HIPAA policies and procedures
- PHI handling procedures
- Breach response procedures

---

## CC6: Logical and Physical Access Controls

### CC6.1: The entity implements logical access security software, infrastructure, and architectures over protected information assets to protect them from security events to meet the entity's objectives.

**What This Means**:
Logical access controls restrict access to systems and data.

**Control Examples**:
- Authentication systems (SSO, MFA)
- Authorization controls (RBAC)
- Access provisioning process
- Access review process (periodic)
- Password policies
- Privileged access management
- Session management

**Evidence**:
- Access control configurations
- User access lists
- Access review reports
- Authentication logs
- Password policy settings

**SaaS Considerations**:
- Customer identity management
- API authentication
- Service-to-service authentication

**Healthcare Considerations**:
- PHI access controls
- Minimum necessary access
- Emergency access procedures
- Audit logging of PHI access

---

### CC6.2: Prior to issuing system credentials and granting system access, the entity registers and authorizes new internal and external users whose access is administered by the entity. For those users whose access is administered by the entity, user system credentials are removed when user access is no longer authorized.

**What This Means**:
User access is properly authorized before granting and removed when no longer needed.

**Control Examples**:
- Access request and approval workflow
- Background checks for employees
- Onboarding procedures include access provisioning
- Offboarding procedures include access revocation
- Contractor access terms clearly defined
- Access certifications collected

**Evidence**:
- Access request tickets
- Approval records
- Onboarding checklists
- Offboarding checklists
- Background check records

**SaaS Considerations**:
- Engineering access to production
- Customer access to their environments
- Support team access controls

**Healthcare Considerations**:
- Workforce member verification
- Termination procedures for PHI access
- Temporary access for contractors

---

### CC6.3: The entity authorizes, modifies, or removes access to data, software, functions, and other protected information assets based on roles, responsibilities, or the system design and changes, giving consideration to the concepts of least privilege and segregation of duties, to meet the entity's objectives.

**What This Means**:
Access is based on roles, follows least privilege, and enforces segregation of duties.

**Control Examples**:
- Role-based access control (RBAC)
- Least privilege principle enforced
- Segregation of duties matrix
- Access modification procedures
- Regular access recertification
- Privileged access restricted

**Evidence**:
- RBAC configuration
- Segregation of duties matrix
- Access modification logs
- Access recertification reports
- Privileged access logs

**SaaS Considerations**:
- Customer data access segregation
- Development/staging/production separation
- DevOps role definitions

**Healthcare Considerations**:
- Role-based access to PHI
- Minimum necessary standard
- Separation of duties for sensitive functions

---

### CC6.4: The entity restricts physical access to facilities and protected information assets (for example, data center facilities, backup media storage, and other sensitive locations) to authorized personnel to meet the entity's objectives.

**What This Means**:
Physical security controls protect facilities and assets.

**Control Examples**:
- Badge access systems for data centers
- Visitor logs and escort procedures
- Security cameras and monitoring
- Secure storage for backup media
- Clean desk policy
- Physical security for network equipment

**Evidence**:
- Badge access logs
- Visitor logs
- Camera footage retention
- Physical security assessment reports

**SaaS Considerations**:
- For cloud: Rely on provider's physical security (reference their SOC 2)
- Office physical security
- Secure areas for sensitive discussions

**Healthcare Considerations**:
- Physical safeguards for PHI
- Secure storage for backup media
- Workstation security

---

### CC6.5: The entity discontinues logical and physical protections over physical assets only after the ability to read or recover data and software from those assets has been diminished and is no longer required to meet the entity's objectives.

**What This Means**:
Assets are securely disposed of or sanitized before disposal.

**Control Examples**:
- Data destruction policy
- Media sanitization procedures
- Certificate of destruction for disposed assets
- Asset disposal tracking
- Secure disposal of failed hardware

**Evidence**:
- Disposal policy
- Destruction certificates
- Disposal logs
- Asset tracking system records

**SaaS Considerations**:
- Cloud volume deletion procedures
- Container/VM destruction
- Decommissioning procedures

**Healthcare Considerations**:
- PHI destruction requirements
- Media sanitization for PHI
- HIPAA-compliant disposal

---

### CC6.6: The entity implements logical access security measures to protect against threats from sources outside its system boundaries.

**What This Means**:
Perimeter security controls protect against external threats.

**Control Examples**:
- Firewalls configured and maintained
- Network segmentation
- Intrusion detection/prevention systems
- DDoS protection
- Web application firewall (WAF)
- VPN for remote access

**Evidence**:
- Firewall configurations
- Network diagrams
- IDS/IPS alerts and reviews
- WAF configurations

**SaaS Considerations**:
- Cloud security groups
- API rate limiting
- CDN/DDoS protection

**Healthcare Considerations**:
- Network segmentation for PHI systems
- Secure remote access to PHI

---

### CC6.7: The entity restricts the transmission, movement, and removal of information to authorized internal and external users and processes, and protects it during transmission, movement, or removal to meet the entity's objectives.

**What This Means**:
Data in transit is protected and data movement is controlled.

**Control Examples**:
- Encryption for data in transit (TLS/SSL)
- VPN for remote access
- Secure file transfer protocols (SFTP)
- Email encryption
- Data loss prevention (DLP)
- USB port restrictions

**Evidence**:
- Encryption configurations
- Certificate management
- VPN access logs
- DLP policy and alerts

**SaaS Considerations**:
- HTTPS for all web traffic
- API encryption (TLS 1.2+)
- Customer data export controls

**Healthcare Considerations**:
- PHI transmission encryption required
- Secure messaging for PHI
- Email encryption for PHI

---

### CC6.8: The entity implements controls to prevent or detect and act upon the introduction of unauthorized or malicious software to meet the entity's objectives.

**What This Means**:
Malware protection controls are implemented.

**Control Examples**:
- Antivirus/anti-malware software
- Endpoint detection and response (EDR)
- Email filtering and scanning
- Web filtering
- Application whitelisting
- Regular definition updates

**Evidence**:
- Antivirus configurations
- Malware detection reports
- Update logs
- Scan results

**SaaS Considerations**:
- Container image scanning
- Code repository scanning
- Dependency scanning

**Healthcare Considerations**:
- Malware protection for PHI systems
- Ransomware prevention

---

## CC7: System Operations

### CC7.1: To meet its objectives, the entity uses detection and monitoring procedures to identify (1) changes to configurations that result in the introduction of new vulnerabilities, and (2) susceptibilities to newly discovered vulnerabilities.

**What This Means**:
Systems are monitored for vulnerabilities and configuration changes.

**Control Examples**:
- Vulnerability scanning (automated and periodic)
- Configuration management and drift detection
- Patch management process
- Vulnerability disclosure monitoring
- Security advisory subscriptions

**Evidence**:
- Vulnerability scan reports
- Configuration management logs
- Patch application records
- Security advisory reviews

**SaaS Considerations**:
- Container vulnerability scanning
- Dependency vulnerability tracking
- Cloud configuration monitoring

**Healthcare Considerations**:
- PHI system vulnerability management
- Medical device security (if applicable)

---

### CC7.2: The entity monitors system components and the operation of those components for anomalies that are indicative of malicious acts, natural disasters, and errors affecting the entity's ability to meet its objectives; anomalies are analyzed to determine whether they represent security events.

**What This Means**:
Security monitoring detects anomalies and potential security events.

**Control Examples**:
- Security information and event management (SIEM)
- Log aggregation and analysis
- Anomaly detection rules
- Failed login monitoring
- Unusual access pattern detection
- 24/7 monitoring (or clearly defined monitoring hours)

**Evidence**:
- SIEM dashboards and alerts
- Security event logs
- Alert investigation records
- Monitoring coverage documentation

**SaaS Considerations**:
- Application performance monitoring (APM)
- Infrastructure monitoring
- Customer activity monitoring

**Healthcare Considerations**:
- PHI access anomaly detection
- Suspicious activity monitoring
- Audit log review

---

### CC7.3: The entity evaluates security events to determine whether they could or have resulted in a failure of the entity to meet its objectives (security incidents) and, if so, takes actions to prevent or address such failures.

**What This Means**:
Incident response processes handle security events and incidents.

**Control Examples**:
- Incident response plan
- Incident classification and prioritization
- Incident response team defined
- Incident investigation procedures
- Root cause analysis
- Post-incident reviews

**Evidence**:
- Incident response plan
- Incident tickets and logs
- Investigation reports
- Post-incident review reports

**SaaS Considerations**:
- Customer impact assessment
- Customer communication procedures
- Service restoration priorities

**Healthcare Considerations**:
- PHI breach assessment
- Breach notification procedures (HIPAA)
- Risk of harm analysis

---

### CC7.4: The entity responds to identified security incidents by executing a defined incident response program to understand, contain, remediate, and communicate security incidents, as appropriate.

**What This Means**:
A structured incident response program is in place and followed.

**Control Examples**:
- Incident response procedures documented
- Incident containment procedures
- Evidence preservation
- Communication templates
- Escalation procedures
- Lessons learned process

**Evidence**:
- Incident response procedures
- Incident response logs
- Communication records
- Lessons learned documentation

**SaaS Considerations**:
- Customer incident notifications
- Status page updates
- Blameless post-mortems

**Healthcare Considerations**:
- HIPAA breach notification within 60 days
- Risk of harm assessment documentation
- Mitigation of harm procedures

---

### CC7.5: The entity identifies, develops, and implements activities to recover from identified security incidents.

**What This Means**:
Recovery procedures restore normal operations after incidents.

**Control Examples**:
- Incident recovery procedures
- System restoration procedures
- Data recovery from backups
- Service recovery prioritization
- Recovery time testing
- Recovery documentation

**Evidence**:
- Recovery procedures
- Recovery test results
- Actual recovery documentation
- RTO/RPO measurements

**SaaS Considerations**:
- Service recovery procedures
- Database recovery procedures
- Multi-region failover (if applicable)

**Healthcare Considerations**:
- PHI restoration procedures
- Business continuity for patient care
- Emergency mode operations

---

## CC8: Change Management

### CC8.1: The entity authorizes, designs, develops or acquires, configures, documents, tests, approves, and implements changes to infrastructure, data, software, and procedures to meet its objectives.

**What This Means**:
A formal change management process controls changes to systems.

**Control Examples**:
- Change request and approval process
- Change advisory board (CAB)
- Development and testing procedures
- Change documentation requirements
- Rollback procedures
- Change communication

**Evidence**:
- Change tickets/requests
- CAB meeting minutes
- Test plans and results
- Change approvals
- Deployment documentation

**SaaS Considerations**:
- CI/CD pipeline controls
- Feature flag management
- Blue-green deployments
- Rollback capabilities

**Healthcare Considerations**:
- Change impact on PHI systems
- Validation of changes to critical systems
- Change notification to business associates

---

### CC8.2: The entity authorizes, designs, develops or acquires, configures, documents, tests, approves, and implements changes to infrastructure, data, software, and procedures to meet its objectives.

**Note**: This is a continuation/emphasis of CC8.1 focusing on the complete lifecycle.

**Control Examples**:
- Segregation of duties in change process
- Peer review of changes
- Automated testing in pipeline
- Security testing for changes
- Configuration management database (CMDB)

**Evidence**:
- Code review records
- Automated test results
- Security scan results
- CMDB records

---

### CC8.3: The entity manages changes in infrastructure, data, software, and procedures in an emergency, requiring rapid implementation, to meet its objectives.

**What This Means**:
Emergency changes have procedures allowing rapid implementation while maintaining control.

**Control Examples**:
- Emergency change procedures
- Expedited approval process
- Post-implementation review required
- Documentation of emergency rationale
- Emergency change tracking

**Evidence**:
- Emergency change policy
- Emergency change logs
- Post-implementation reviews
- Approval records (even if expedited)

**SaaS Considerations**:
- Hotfix procedures
- Production incident repairs
- Security patch emergency deployment

**Healthcare Considerations**:
- Emergency access procedures for PHI
- Emergency system changes for patient safety
- Documentation of emergency PHI access

---

## CC9: Risk Mitigation

### CC9.1: The entity identifies, selects, and develops risk mitigation activities for risks arising from potential business disruptions.

**What This Means**:
Business continuity and disaster recovery plans address disruption risks.

**Control Examples**:
- Business impact analysis (BIA)
- Business continuity plan (BCP)
- Disaster recovery plan (DRP)
- RTO and RPO defined
- Alternative processing arrangements
- Backup procedures

**Evidence**:
- BIA documentation
- BCP/DRP documents
- RTO/RPO definitions
- Backup policies and logs

**SaaS Considerations**:
- Multi-region architecture
- Automated failover
- Data replication
- Backup restoration testing

**Healthcare Considerations**:
- Contingency plan for PHI systems (required)
- Emergency mode operations
- Patient care continuity

---

### CC9.2: The entity assesses and manages risks associated with vendors and business partners.

**What This Means**:
Third-party risk management program assesses and monitors vendor risks.

**Control Examples**:
- Vendor risk assessment before engagement
- Vendor due diligence (SOC 2, questionnaires)
- Vendor contracts include security requirements
- Ongoing vendor monitoring
- Vendor access controls
- Vendor termination procedures

**Evidence**:
- Vendor risk assessments
- SOC 2 reports from vendors
- Vendor contracts
- Vendor monitoring reports
- Vendor access lists

**SaaS Considerations**:
- Cloud provider risk assessment
- Sub-processor management
- Third-party integration security

**Healthcare Considerations**:
- Business Associate Agreements (BAAs)
- Business associate risk assessment
- PHI access by vendors

---

## Documentation Tips for Security Controls

### Control Description Best Practices

1. **Be Specific**: Use concrete details, not vague terms
2. **Include Frequency**: Daily, weekly, monthly, quarterly, annually, event-driven
3. **Name Responsible Parties**: Specific roles, not "management"
4. **Describe Process**: Step-by-step how control operates
5. **Note Evidence**: What artifacts prove control execution
6. **Address Exceptions**: Document any variances or compensating controls

### Common Pitfalls

- Using "regularly" or "periodically" without defining frequency
- Naming "management" without specifying which manager/role
- Describing aspirational controls (what you plan) instead of actual controls
- Omitting how control effectiveness is verified
- Failing to update control descriptions when processes change

### Mapping Controls to Multiple TSC Points

Many controls address multiple TSC requirements. Document each clearly:

**Example**: Access review control addresses:
- CC6.1 (logical access controls)
- CC6.2 (user access authorization)
- CC6.3 (role-based access)

Map one control to multiple requirements when appropriate.

---

## Resources

- AICPA Trust Services Criteria: [https://www.aicpa.org/interestareas/frc/assuranceadvisoryservices/trustdataintegritytaskforce](Full criteria available from AICPA)
- Templates: See `templates/control_matrix_security.md`
- Examples: See `examples/control_description_samples.md`

