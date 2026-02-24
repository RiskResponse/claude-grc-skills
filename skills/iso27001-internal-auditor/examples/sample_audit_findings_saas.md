# Sample Audit Findings for SaaS Company

## Purpose

This document provides real-world examples of audit findings for a SaaS company's ISO 27001:2022 internal audit. Use these as reference for writing your own findings.

---

## EXAMPLE NONCONFORMITIES

### Example 1: Access Review Not Performed (Minor NC)

**Reference**: ISO 27001:2022 Control A.5.18 (Access Rights)

**Requirement**: Access rights shall be reviewed at regular intervals and adjusted when necessary

**Finding**: Quarterly access reviews were not performed for Q2 and Q3 2024. The Access Control Policy (v1.8, approved 2024-01-10) requires quarterly reviews by the IT Security Manager.

**Evidence**:
- Access Control Policy v1.8, Section 4.2: "Access rights shall be reviewed quarterly"
- Shared drive folder "Access Reviews": Contains reviews for Q1 2024 (completed 2024-03-28) and Q4 2023, but missing Q2 and Q3 2024
- Interview with IT Security Manager (2024-11-01): Confirmed reviews not completed due to resource constraints during platform migration
- Vanta Control A.5.18 test history shows last test: 2024-03-28

**Impact**: Without regular access reviews, inappropriate access rights may persist, increasing risk of unauthorized access or privilege escalation.

**Classification**: Minor NC (two quarters missed, but process exists and was previously followed)

---

### Example 2: Risk Treatment Plan Missing (Major NC)

**Reference**: ISO 27001:2022 Clause 6.1.3 (Information Security Risk Treatment)

**Requirement**: The organization shall formulate an information security risk treatment plan and obtain risk owner approval

**Finding**: Three high-severity risks identified in the 2024 annual risk assessment have no treatment plans. These risks remain unaddressed 7 months after assessment.

**Evidence**:
- Vanta Risk Register export (2024-11-01):
  - RISK-2024-012: "Lack of MFA for admin accounts" (Severity: High, Assessed: 2024-04-15, Treatment Plan: None)
  - RISK-2024-018: "Unencrypted database backups" (Severity: High, Assessed: 2024-04-15, Treatment Plan: None)
  - RISK-2024-023: "No DDoS protection" (Severity: High, Assessed: 2024-04-15, Treatment Plan: None)
- Risk Treatment Procedure v1.2, Section 3.1: "All high and critical risks must have treatment plans within 30 days"
- Interview with CISO (2024-11-01): Acknowledged gap, stated "resource priorities shifted to product development"

**Impact**: High-severity security risks remain unmitigated, exposing organization to data breaches, service disruption, and regulatory non-compliance.

**Classification**: Major NC (systematic failure to implement required process, multiple instances, significant security impact)

---

### Example 3: Training Records Missing (Minor NC)

**Reference**: ISO 27001:2022 Clause 7.2 (Competence)

**Requirement**: The organization shall retain documented information as evidence of competence

**Finding**: Security awareness training records are missing for 3 out of 47 employees.

**Evidence**:
- Vanta Personnel module training tracker export (2024-11-01)
- Annual security awareness training completion: 44/47 employees (94%)
- Missing records:
  - Sarah Johnson (hired 2024-09-15) - New hire, training scheduled
  - Mike Chen (hired 2024-10-01) - New hire, onboarding in progress
  - Lisa Martinez (hired 2023-05-20) - No completion record
- Interview with HR Manager (2024-11-01): Confirmed training gap for L. Martinez, investigating
- Training Policy v1.5: "All employees must complete security awareness training within 30 days of hire and annually thereafter"

**Impact**: Employees without proper training may inadvertently cause security incidents.

**Classification**: Minor NC (3 isolated cases, 2 are new hires within 30-day window, 1 is genuine gap)

---

## EXAMPLE OBSERVATIONS

### Observation 1: Backup Monitoring Could Be Enhanced

**Type**: Process Improvement Opportunity

**Description**: While daily backups are performed successfully and tested annually (compliant with policy), there is no automated alerting for backup failures. Backup failures are only detected during monthly manual log reviews.

**Evidence**:
- Vanta Control A.8.13: Daily backup logs show consistent success
- Backup Policy v2.0: Requires daily backups and annual restore testing (both met)
- Interview with IT Operations (2024-11-01): Confirmed manual monthly log review process
- No automated backup monitoring alerts configured in cloud platform

**Recommendation**: Implement automated alerting for backup failures to enable immediate response rather than monthly detection. This would improve RTO/RPO and align with SaaS industry best practices.

**Priority**: Medium

---

### Observation 2: Penetration Test Scope Could Be Expanded

**Type**: Best Practice Gap

**Description**: Annual penetration testing is performed (compliant with policy), but testing scope focuses only on external attack surface. Internal penetration testing and cloud configuration review are not included.

**Evidence**:
- Vanta Evidence: Penetration Test Report 2024 (dated 2024-05-20) - external testing only
- Security Testing Policy v1.3: "Annual penetration testing of production environment"
- Interview with Security Team (2024-11-01): Confirmed internal testing not performed
- Industry best practice for SaaS: Both external and internal testing

**Recommendation**: Expand penetration testing scope to include internal network testing and cloud configuration assessment. Consider bi-annual testing given SaaS critical nature.

**Priority**: Medium

---

## EXAMPLE RECOMMENDATIONS

### Recommendation 1: Implement Automated Policy Review Reminders

**Type**: Efficiency Improvement

**Benefit**: Currently, policy reviews are tracked manually in spreadsheet, leading to occasional missed review dates. Vanta supports automated policy review reminders and workflows.

**Current State**:
- 15 policies manually tracked
- 2 policies found with overdue reviews during this audit
- Manual tracking prone to oversight

**Recommendation**:
- Configure Vanta policy review automation
- Set review reminders 30 days before due date
- Automate review workflow approvals
- Generate dashboard showing review status

**Effort**: Low (Vanta feature configuration)

**Expected Benefit**:
- Eliminate overdue policy reviews
- Reduce administrative burden
- Improve compliance posture
- Better audit readiness

---

### Recommendation 2: Adopt Security Champions Program

**Type**: Security Culture Enhancement

**Benefit**: While security training is completed (compliant), security awareness could be strengthened through a Security Champions program.

**Current State**:
- Annual security training conducted
- Security incidents occasionally occur due to human error
- Security team of 3 serves 50-person company

**Recommendation**:
- Designate security champions in each department (5-7 people)
- Provide enhanced security training to champions
- Champions act as security liaisons and advocates
- Regular champion meetings to discuss security topics

**Effort**: Medium (program setup, ongoing coordination)

**Expected Benefit**:
- Improved security culture
- Faster security question resolution
- Better security awareness across organization
- Reduced security incidents

---

## EXAMPLES: Well-Written vs Poorly-Written Findings

### Poor Finding Example ❌

**Finding**: "The firewall isn't configured right."

**Problems**:
- No specific requirement referenced
- Vague description ("isn't configured right")
- No evidence cited
- No impact stated
- Unclear what needs to be fixed

### Good Finding Example ✅

**Reference**: ISO 27001:2022 Control A.8.20 (Networks Security)

**Requirement**: Networks and network devices shall be secured, managed and controlled to protect information in systems and applications

**Finding**: Production database (PostgreSQL on AWS RDS) is configured to accept connections from any IP address (0.0.0.0/0), rather than restricting access to application servers only as required by the Network Security Policy.

**Evidence**:
- Network Security Policy v2.1, Section 5.3: "Database access shall be restricted to application servers via security group rules"
- AWS RDS security group "prod-db-sg" (screenshot captured 2024-11-01): Inbound rule allows PostgreSQL port 5432 from 0.0.0.0/0
- Interview with DevOps Engineer (2024-11-01): "Set to 0.0.0.0/0 during migration for troubleshooting, forgot to restrict afterward"
- Vanta Control A.8.20 status: "Implemented" - Evidence: Network diagram (doesn't show security group details)

**Impact**: Database exposed to potential unauthorized access from internet. While authentication still required, attack surface unnecessarily expanded. Increases risk of brute force attacks, exploitation attempts, and data breach.

**Why This is Good**:
- Specific requirement cited with policy reference
- Exact technical detail provided (0.0.0.0/0, port, security group name)
- Multiple evidence types (policy, screenshot, interview)
- Clear impact on security
- Actionable - obvious what needs fixing

---

## EXAMPLES: Major vs. Minor NC Classification

### Scenario 1: One Backup Missed

**Situation**: Daily backups required. One backup failed on October 15 due to storage full error. All other backups in October successful.

**Classification**: Minor NC
- Isolated incident
- Not systematic failure
- Process exists and generally works
- Quick resolution possible

---

### Scenario 2: Backups Not Performed for 2 Months

**Situation**: Daily backups required. Due to storage migration, backups were not performed from September 1 to October 31 (61 days).

**Classification**: Major NC
- Systematic failure (two full months)
- Process completely broke down
- Critical control not operating
- Significant data loss risk

---

### Scenario 3: Management Review Not Conducted

**Situation**: Management review required annually per Clause 9.3. No review conducted in 2024.

**Classification**: Major NC
- Complete absence of required activity
- Mandatory ISO 27001 requirement
- No evidence review will occur
- Affects ISMS improvement cycle

---

### Scenario 4: One Training Record Missing

**Situation**: All employees must complete security training annually. 49 out of 50 employees have records. One employee's record missing.

**Classification**: Minor NC (unless...)
- If missing record is for new employee within 30-day window: Observation (not yet NC)
- If missing record is for CISO or person with high-privilege access: Could be Major (critical role)
- If missing record is for regular employee, 6 months overdue: Minor NC

**Context Matters**: Classification depends on severity and circumstances.

---

## SaaS-Specific Finding Examples

### Multi-Tenant Isolation Testing

**Reference**: Control A.8.31 (Separation of development, test and production environments)

**Finding**: Multi-tenant data isolation testing is not performed systematically. While architecture includes tenant ID filtering, no evidence of regular isolation testing.

**Evidence**:
- Multi-Tenancy Architecture Document v1.2: Describes tenant ID filtering approach
- Vanta Control A.8.31: Status "Implemented," Evidence: Architecture diagram only
- Interview with Lead Engineer (2024-11-01): "We test isolation during major releases but not on a schedule"
- No test procedures for isolation testing
- No penetration test reports focusing on tenant isolation

**Impact**: Without regular testing, tenant isolation vulnerabilities could go undetected.

**Classification**: Minor NC (control exists but testing not systematic)

---

### Cloud Configuration Drift

**Reference**: Control A.8.9 (Configuration Management)

**Finding**: Cloud infrastructure configurations are not monitored for drift from approved baselines.

**Evidence**:
- Configuration Management Policy v1.4: Requires monitoring and alerting for configuration changes
- AWS environment: No AWS Config enabled
- Interview with DevOps team (2024-11-01): "We use infrastructure-as-code but don't monitor for manual changes"
- Vanta Control A.8.9: Status "Implemented," Evidence: "Terraform scripts" (shows intended state, not monitoring)

**Impact**: Manual changes to cloud resources could introduce security vulnerabilities without detection.

**Classification**: Minor NC (monitoring required but not implemented)

---

## Key Takeaways

### For Writing NCs:
1. **Be Specific**: Exact details, not generalizations
2. **Cite Evidence**: Multiple sources, specific references
3. **Reference Requirements**: Quote standards and policies
4. **State Impact**: Why does this matter for security?
5. **Be Fair**: If edge case or isolated, classify appropriately

### For Vanta Audits:
1. **Don't Trust Status Alone**: "Implemented" doesn't mean compliant - verify evidence
2. **Check Dates**: Evidence must be recent and within test frequency
3. **Validate Tests**: Review test results, not just that tests exist
4. **Interview**: Vanta shows documents; interviews show understanding and practice
5. **Cross-Reference**: Link Vanta IDs in all findings for traceability

### For Classification:
1. **Minor**: Isolated, doesn't impair ISMS, quick fix
2. **Major**: Systematic, complete absence, multiple related issues, critical control failure
3. **Observation**: Could become NC, best practice gap, potential issue
4. **Recommendation**: Beyond compliance, improvement opportunity

Use these examples as quality benchmarks when documenting your own audit findings.

