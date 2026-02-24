# Availability Control Matrix (TSC A)

> **TIP**: Refer to `references/common_saas_controls.md` for a library of standard controls you can copy/paste into this matrix.

## Purpose

This control matrix maps your organization's controls to the Availability criteria requirements. Use this to ensure complete coverage and track availability-specific controls beyond the Security Common Criteria.

**Note**: Availability also requires all Security Common Criteria (CC1-CC9). See `control_matrix_security.md` for those requirements.

---

## A1.1: Processing Capacity and Monitoring

| Control Area | Specific Requirement | Your Control(s) | Control Description | Monitoring/Testing | Evidence | Status |
|--------------|---------------------|-----------------|---------------------|-------------------|----------|--------|
| **Capacity Monitoring** | Current capacity monitored | | | | | ☐ |
| | CPU utilization | | | | | ☐ |
| | Memory usage | | | | | ☐ |
| | Disk space | | | | | ☐ |
| | Network bandwidth | | | | | ☐ |
| | Database connections | | | | | ☐ |
| | Application response times | | | | | ☐ |
| **Capacity Planning** | Future needs projected | | | | | ☐ |
| | Growth trends analyzed | | | | | ☐ |
| | Capacity expansion planned | | | | | ☐ |
| **Threshold Management** | Thresholds defined | | | | | ☐ |
| | Alerts configured | | | | | ☐ |
| | Escalation procedures | | | | | ☐ |
| | Auto-scaling (if applicable) | | | | | ☐ |
| **Peak Load** | Load testing performed | | | | | ☐ |
| | Peak capacity validated | | | | | ☐ |
| | Load balancing configured | | | | | ☐ |

**Completion**: __ / 15 capacity controls documented

---

## A1.2: Environmental Protections and Backup

| Control Area | Specific Requirement | Your Control(s) | Control Description | Testing Method | Evidence | Status |
|--------------|---------------------|-----------------|---------------------|----------------|----------|--------|
| **Environmental** | Power redundancy | | | | | ☐ |
| | Climate control | | | | | ☐ |
| | Fire suppression | | | | | ☐ |
| | Environmental monitoring | | | | | ☐ |
| **OR Cloud** | Provider environmental controls | | | | | ☐ |
| | Provider SOC 2 reviewed | | | | | ☐ |
| **Backup** | Automated backup procedures | | | | | ☐ |
| | Backup frequency defined | | | | | ☐ |
| | Backup retention policy | | | | | ☐ |
| | Offsite/off-region backup | | | | | ☐ |
| | Backup encryption | | | | | ☐ |
| | Backup integrity verification | | | | | ☐ |
| **Backup Testing** | Restore testing procedures | | | | | ☐ |
| | Restore tests performed | | | | | ☐ |
| | Restore success measured | | | | | ☐ |
| **Recovery Infrastructure** | Redundant systems | | | | | ☐ |
| | Failover capabilities | | | | | ☐ |
| | Secondary site/region | | | | | ☐ |
| | Recovery infrastructure tested | | | | | ☐ |

**Completion**: __ / 19 backup/environmental controls documented

---

## A1.3: Recovery and Continuity

| Control Area | Specific Requirement | Your Control(s) | Control Description | Testing Method | Evidence | Status |
|--------------|---------------------|-----------------|---------------------|----------------|----------|--------|
| **Business Impact Analysis** | BIA conducted | | | | | ☐ |
| | Critical systems identified | | | | | ☐ |
| | RTO defined per system | | | | | ☐ |
| | RPO defined per system | | | | | ☐ |
| | Impact assessed | | | | | ☐ |
| **Disaster Recovery Plan** | DRP documented | | | | | ☐ |
| | Recovery procedures detailed | | | | | ☐ |
| | Recovery team roles defined | | | | | ☐ |
| | Recovery sequence documented | | | | | ☐ |
| | Communication procedures | | | | | ☐ |
| **Business Continuity Plan** | BCP documented | | | | | ☐ |
| | Alternative work locations | | | | | ☐ |
| | Critical function priorities | | | | | ☐ |
| | Remote work capabilities | | | | | ☐ |
| **DR/BC Testing** | Annual testing (minimum) | | | | | ☐ |
| | Test scenarios documented | | | | | ☐ |
| | Tabletop exercises | | | | | ☐ |
| | Full recovery simulations | | | | | ☐ |
| | Test results documented | | | | | ☐ |
| | Plan updates based on testing | | | | | ☐ |
| **Incident Response** | Availability incident classification | | | | | ☐ |
| | Service restoration procedures | | | | | ☐ |
| | Customer notification | | | | | ☐ |
| | Post-incident reviews | | | | | ☐ |

**Completion**: __ / 24 recovery/continuity controls documented

---

## SLA and Availability Metrics Tracking

| Metric | Target | Measurement Method | Monitoring Frequency | Evidence | Status |
|--------|--------|-------------------|---------------------|----------|--------|
| **Uptime** | __%  | | | | ☐ |
| **Response Time** | __ms (p95) | | | | ☐ |
| **API Availability** | __% | | | | ☐ |
| **RTO** | __ hours | | | | ☐ |
| **RPO** | __ hours/minutes | | | | ☐ |
| **MTTR** | __ hours | | | | ☐ |
| **MTTD** | __ minutes | | | | ☐ |

---

## SUMMARY

**Total Availability Controls:** 58 (15 capacity + 19 backup/environmental + 24 recovery/continuity)

**Documented:** __ / 58

**Coverage Percentage:** __%

**Gaps Identified:**
[List any areas without controls]

**Compensating Controls:**
[Document any compensating controls]

**N/A Items:**
[Document items that don't apply with justification]

---

## AVAILABILITY CONTROL EXAMPLES

### Example: Capacity Monitoring Control

**TSC Point**: A1.1 - Processing Capacity

**Control ID**: AV-001

**Control Description:**
The IT Operations team monitors system capacity metrics in real-time using CloudWatch and DataDog. CPU, memory, disk, and network utilization are monitored with alerts configured at 80% (warning) and 90% (critical) thresholds. Alerts page the on-call engineer via PagerDuty. Weekly capacity reports are generated and reviewed by the Director of Engineering.

**Who**: Automated monitoring; On-call engineer responds to alerts; Director of Engineering reviews weekly reports

**When**: Continuous monitoring; Weekly reporting

**Testing Method**: Inspect monitoring configurations, review sample alerts, review weekly reports

**Evidence**: Monitoring dashboards, alert configuration, PagerDuty logs, weekly capacity reports

---

### Example: DR Testing Control

**TSC Point**: A1.3 - Recovery and Continuity

**Control ID**: AV-007

**Control Description:**
The Company tests disaster recovery procedures annually (minimum) by failing over to the DR region (us-west-2) and validating full system functionality. The test includes database failover, application deployment in DR region, verification of data replication, and validation of RTO/RPO targets. Test results are documented and DR plan updated based on findings.

**Who**: SRE team executes DR test; CTO reviews results; Compliance documents

**When**: Annually (typically in Q3); Ad-hoc when significant infrastructure changes

**Testing Method**: Review DR test reports, validate RTO/RPO measurements

**Evidence**: DR test plans, DR test results, RTO/RPO measurements, plan update records

---

## INTEGRATION WITH SECURITY CONTROLS

Many controls address both Security and Availability:

| Control Area | Security Aspect | Availability Aspect |
|--------------|-----------------|---------------------|
| **Backup** | Protects data integrity | Enables recovery |
| **Incident Response** | Security incidents | Service disruptions |
| **Monitoring** | Security events | Performance and capacity |
| **Vendor Management** | Vendor security risks | Vendor availability/continuity |
| **Change Management** | Security impact assessment | Availability impact assessment |

Document these integrated controls in both matrices with appropriate focus for each TSC category.

---

## VALIDATION

After completing this matrix:
1. Ensure all 58 availability requirements have at least one control
2. Run `scripts/control_coverage_validator.py` for automated validation
3. Review with IT Operations and SRE teams for accuracy
4. Cross-reference with actual monitoring and testing evidence
5. Update as controls change throughout the year

---

**For detailed Availability criteria explanations, see:**
- `references/tsc_availability_criteria.md`
- `references/system_description_requirements.md`

**For Security Common Criteria matrix, see:**
- `templates/control_matrix_security.md`

