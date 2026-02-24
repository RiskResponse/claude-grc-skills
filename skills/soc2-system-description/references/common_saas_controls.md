# Common SaaS Controls Library
## Purpose
This library provides pre-written, high-quality control descriptions for standard SaaS technology stacks (AWS, GitHub, Jira, etc.). Use these as a starting point and customize them to match the organization's specific implementation.

**Format**: `[Control ID]` | `[TSC Mapping]` | `[Description]`

> **Note for Drata Users**: Drata automatically monitors many of these controls (e.g., "Infrastructure Monitoring", "Vulnerability Scanning") via integrations. When using these descriptions, you can reference Drata as the "compliance monitoring platform" that collects evidence.

---

## CC6: Logical and Physical Access (Identity & Access Management)

### Access Provisioning
**IAM-001** | **CC6.1, CC6.2**
**Access Provisioning**
User accounts are provisioned based on the principle of least privilege. Access requests are submitted via [Ticket System e.g. Jira], approved by the user's manager and the system owner, and provisioned by the IT/Security team. Access is granted only for the resources necessary for the user's role.
**Evidence:** Jira tickets showing approval and provisioning; IAM user creation logs.
> **Drata Mapping**: Corresponds to Drata Control "DC-16: Access Provisioning" (Personnel). Drata automates evidence collection via IdP integration.

### Access Termination
**IAM-002** | **CC6.1, CC6.2, CC6.5**
**Access Termination**
Upon notification of employee termination from HR (via [HR System]), the IT team revokes access to all systems and applications within 24 hours (immediate revocation for involuntary termination). This includes removing SSO access, disabling AWS IAM users, and removing Github organization membership.
**Evidence:** Termination checklists; Jira tickets; SSO access logs showing deactivation time.
> **Drata Mapping**: Corresponds to Drata Control "DC-14: Access Termination". Drata monitors IdP for terminated users.

### Review of User Access
**IAM-003** | **CC6.1, CC6.3**
**User Access Review**
The Security team conducts a quarterly review of all user access to production systems (AWS, Database, Identity Provider). A list of current users and their roles is generated and reviewed by system owners to ensure access is still appropriate. Inappropriate access is revoked immediately.
**Evidence:** Quarterly access review tickets; spreadsheets showing sign-off; evidence of remediation for any findings.

### Multi-Factor Authentication
**IAM-004** | **CC6.1**
**Multi-Factor Authentication (MFA)**
MFA is enforced for all users accessing the corporate Identity Provider (e.g., Okta/Google Workspace) and for all root/IAM user access to the production cloud environment (AWS/GCP/Azure).
**Evidence:** Identity provider configuration screenshots showing MFA enforcement policy; AWS IAM report showing MFA enabled for all users.
> **Drata Mapping**: Corresponds to Drata Control "DC-17: MFA on Identity Provider". Drata continuously monitors MFA status.

---

## CC7: System Operations (Monitoring & Incident Response)

### Vulnerability Scanning
**OPS-001** | **CC7.1**
**Vulnerability Scanning**
Automated vulnerability scanning is performed [Daily/Weekly] on all production containers/instances using [Tool Name, e.g., AWS Inspector/Trivy/Snyk]. Critical and High vulnerabilities are alerted to the engineering team for remediation within [30] days.
**Evidence:** Vulnerability scan reports; Jira tickets for remediation of identified vulnerabilities.

### Security Monitoring
**OPS-002** | **CC7.2**
**Security Monitoring & Alerting**
Logs from production systems (CloudTrail, VPC Flow Logs, Application Logs) are aggregated into [SIEM/Logging Tool e.g., Splunk/DataDog]. Automated alerts are configured for suspicious activities (e.g., root login, repeated failed auth, security group changes). Alerts notify the security team via [PagerDuty/Slack].
**Evidence:** Logging tool configuration; list of active alerts; sample alert notifications.

### Incident Response
**OPS-003** | **CC7.3, CC7.4, CC7.5**
**Incident Response**
The company maintains an Incident Response Plan (IRP) that is tested annually. Incidents are tracked in [Jira/ServiceNow], classified by severity, and managed through containment, eradication, and recovery phases. Post-incident reviews are conducted for all High/Critical incidents.
**Evidence:** Incident Response Plan; Incident tickets; Post-mortem reports.

---

## CC8: Change Management (SDLC)

### Change Approval
**DEV-001** | **CC8.1, CC8.2**
**Change Management & Code Review**
All changes to production code are managed via [GitHub/GitLab]. Code changes require a pull request (PR) with at least one peer review and approval before merging. The main branch is protected to prevent direct commits.
**Evidence:** GitHub branch protection settings; sample Pull Requests showing peer review and approval.
> **Drata Mapping**: Corresponds to Drata Control "DC-87: SDLC - Code Review". Drata monitors GitHub/GitLab for branch protection and PR approvals.

### Automated Testing
**DEV-002** | **CC8.1**
**CI/CD Pipeline & Testing**
A Continuous Integration/Continuous Deployment (CI/CD) pipeline (e.g., GitHub Actions/CircleCI) automatically builds and tests all code commits. Changes must pass all automated unit and integration tests before they can be deployed to production.
**Evidence:** CI/CD configuration files; build logs showing successful test execution.

### Deployment to Production
**DEV-003** | **CC8.1**
**Restricted Deployment**
Only authorized CI/CD tools and designated engineering leads have permissions to deploy changes to the production environment. Deployments are triggered automatically after merging to the main branch (or manually gated for release).
**Evidence:** Deployment logs; IAM policy restricting deployment permissions.

---

## A1: Availability (Backups & Capacity)

### Data Backups
**AVL-001** | **A1.2**
**Database Backups**
Production databases (e.g., AWS RDS) are configured to take automated daily snapshots with a retention period of [30] days. Transaction logs are backed up every [5] minutes to support point-in-time recovery.
**Evidence:** RDS backup configuration screenshots; list of available snapshots.
> **Drata Mapping**: Corresponds to Drata Control "DC-56: Database Backups". Drata monitors AWS RDS backup settings.

### Backup Testing
**AVL-002** | **A1.2**
**Backup Restoration Testing**
A backup restoration test is performed [Quarterly/Annually] to verify data integrity and the ability to meet the RTO/RPO. The test involves restoring a production backup to a non-production environment and validating data availability.
**Evidence:** Backup restoration test report; tickets documenting the test results.

### Capacity Monitoring
**AVL-003** | **A1.1**
**Infrastructure Capacity Monitoring**
Key system metrics (CPU, Memory, Disk, Network) are monitored via [DataDog/CloudWatch]. Alerts are triggered if utilization exceeds [80%] for a sustained period. Auto-scaling groups are configured to automatically add resources during high load.
**Evidence:** Monitoring dashboard screenshots; auto-scaling configuration.

### Disaster Recovery Plan
**AVL-004** | **A1.3**
**Disaster Recovery Testing**
A Disaster Recovery (DR) test is conducted annually to simulate a catastrophic failure (e.g., region loss). The test validates the failover process, communication plan, and recovery time. Results are documented and used to update the DR plan.
**Evidence:** DR Plan document; DR test execution report.

