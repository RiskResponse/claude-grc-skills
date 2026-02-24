# Trust Service Criteria - Availability

## Overview

The Availability category addresses the accessibility of the system, products, or services as stipulated by a contract or service level agreement (SLA). Availability relates to whether the system, product, or service is available for operation and use as committed or agreed.

**Key Focus**: System uptime, performance, capacity, and recovery capabilities.

## Availability Criteria Structure

Availability criteria build upon the Security Common Criteria (CC1-CC9) and add specific availability-focused points of focus:

- **A1.1**: The entity maintains, monitors, and evaluates current processing capacity and use of system components
- **A1.2**: The entity authorizes, designs, develops or acquires, implements, operates, approves, maintains, and monitors environmental protections, software, data backup processes, and recovery infrastructure
- **A1.3**: The entity provides for recovery and continuity of operations

Note: Availability ALSO requires compliance with all Common Criteria (CC1-CC9) documented in `tsc_security_criteria.md`.

---

## A1.1: Current Processing Capacity

### The entity maintains, monitors, and evaluates current processing capacity and use of system components (infrastructure, data, and software) to manage capacity demand and to enable the implementation of additional capacity to help meet its objectives.

**What This Means**:
The organization actively monitors and manages system capacity to ensure availability commitments are met.

### Control Objectives

#### A1.1.1 - Capacity Monitoring

**What This Means**:
Current capacity utilization is continuously monitored.

**Control Examples**:
- CPU utilization monitoring with alerting
- Memory usage monitoring
- Disk space monitoring
- Network bandwidth monitoring
- Database connection pool monitoring
- Application performance monitoring (APM)
- Queue depth monitoring

**Evidence**:
- Monitoring dashboards
- Capacity reports
- Alert configurations and history
- Trending analysis

**SaaS Considerations**:
- Per-tenant resource monitoring
- API rate limiting and monitoring
- Auto-scaling configurations
- Container/pod resource limits

**Healthcare Considerations**:
- System availability for patient care operations
- Peak usage during business hours
- Emergency access capacity

---

#### A1.1.2 - Capacity Planning

**What This Means**:
Future capacity needs are identified and planned for.

**Control Examples**:
- Capacity trend analysis
- Growth projections based on business plans
- Capacity planning reviews (quarterly/annually)
- Infrastructure scaling procedures
- Budget allocation for capacity expansion

**Evidence**:
- Capacity planning documents
- Trend analysis reports
- Infrastructure expansion approvals
- Scaling procedures

**SaaS Considerations**:
- Customer onboarding capacity planning
- Feature launch capacity assessment
- Geographic expansion capacity planning
- Seasonal traffic pattern planning

**Healthcare Considerations**:
- Patient volume growth planning
- New service capacity requirements
- Emergency surge capacity

---

#### A1.1.3 - Capacity Threshold Management

**What This Means**:
Thresholds are defined and monitored to trigger capacity actions.

**Control Examples**:
- Capacity thresholds defined (e.g., 80% CPU triggers alert)
- Escalation procedures when thresholds exceeded
- Automated scaling based on thresholds
- Threshold review and adjustment process
- Capacity incident response

**Evidence**:
- Threshold documentation
- Alert configurations
- Auto-scaling rules
- Capacity incident tickets

**SaaS Considerations**:
- Dynamic scaling thresholds
- Customer-specific capacity limits
- Rate limiting thresholds

**Healthcare Considerations**:
- Critical system priority thresholds
- Emergency capacity triggers

---

#### A1.1.4 - Peak Load Management

**What This Means**:
System can handle peak loads and traffic spikes.

**Control Examples**:
- Load testing (performance and stress testing)
- Peak capacity validation
- Load balancing configurations
- Traffic shaping and rate limiting
- Capacity buffer maintained (headroom)

**Evidence**:
- Load test reports
- Peak usage metrics
- Load balancer configurations
- Capacity buffer documentation

**SaaS Considerations**:
- Black Friday / peak event planning
- Product launch load testing
- Multi-region load distribution

**Healthcare Considerations**:
- Peak patient volume handling
- Emergency department surge capacity
- Flu season / pandemic surge planning

---

## A1.2: Environmental Protections and Backup Processes

### The entity authorizes, designs, develops or acquires, implements, operates, approves, maintains, and monitors environmental protections, software, data backup processes, and recovery infrastructure to meet its objectives.

**What This Means**:
Physical environmental controls and backup systems ensure system availability.

### Control Objectives

#### A1.2.1 - Environmental Controls

**What This Means**:
Physical environmental protections maintain system availability.

**Control Examples**:
- Redundant power supplies and UPS systems
- Temperature and humidity monitoring and control (HVAC)
- Fire suppression systems
- Water detection and protection
- Environmental monitoring with alerting

**Evidence**:
- Data center specifications
- Environmental monitoring reports
- Maintenance records
- Testing records

**SaaS Considerations**:
- For cloud: Rely on provider's environmental controls
- Reference cloud provider's SOC 2 report
- For on-premise: Document own controls

**Healthcare Considerations**:
- Backup power for critical patient care systems
- Environmental monitoring for PHI storage
- Generator testing documentation

---

#### A1.2.2 - Backup Processes

**What This Means**:
Data is backed up regularly to enable recovery.

**Control Examples**:
- Automated backup procedures
- Backup frequency defined (daily, hourly, continuous)
- Backup retention policy
- Offsite/off-region backup storage
- Backup encryption
- Backup integrity verification

**Evidence**:
- Backup policies and procedures
- Backup schedules and logs
- Backup success/failure monitoring
- Integrity verification results

**SaaS Considerations**:
- Database automated backups
- Application state backups
- Customer data backup procedures
- Multi-region backup replication

**Healthcare Considerations**:
- PHI backup procedures
- HIPAA-compliant backup storage
- Backup encryption for PHI
- Retention aligned with legal requirements

---

#### A1.2.3 - Backup Testing

**What This Means**:
Backups are tested to ensure they can be successfully restored.

**Control Examples**:
- Regular backup restoration testing
- Test restore procedures documented
- Restoration success metrics
- Failed restore investigations
- Annual (minimum) full recovery test

**Evidence**:
- Test restore procedures
- Test results and reports
- Restoration success logs
- Annual test documentation

**SaaS Considerations**:
- Automated restore testing
- Database point-in-time recovery testing
- Customer data restoration validation

**Healthcare Considerations**:
- PHI restoration testing
- Critical system restore priority
- Restoration time measurement

---

#### A1.2.4 - Recovery Infrastructure

**What This Means**:
Infrastructure to support recovery is maintained and ready.

**Control Examples**:
- Secondary site or region availability
- Failover capabilities
- Redundant systems
- Recovery infrastructure testing
- Recovery infrastructure capacity

**Evidence**:
- Infrastructure diagrams
- Failover configurations
- Redundancy documentation
- Recovery capacity assessments

**SaaS Considerations**:
- Multi-region deployment
- Active-active or active-passive configuration
- Automated failover mechanisms
- Cross-region database replication

**Healthcare Considerations**:
- Backup site for critical operations
- Emergency mode operations capability
- Critical system redundancy

---

## A1.3: Recovery and Continuity

### The entity provides for recovery and continuity of operations in the event of a disaster or other significant disruption that could affect its ability to meet its objectives.

**What This Means**:
Disaster recovery and business continuity plans ensure operations can continue or be restored after disruptions.

### Control Objectives

#### A1.3.1 - Business Impact Analysis

**What This Means**:
The impact of disruptions is analyzed to inform recovery planning.

**Control Examples**:
- Business impact analysis (BIA) conducted
- Critical systems and processes identified
- RTO (Recovery Time Objective) defined for each system
- RPO (Recovery Point Objective) defined for each system
- Impact assessment (financial, operational, reputational)

**Evidence**:
- BIA documentation
- Criticality assessments
- RTO/RPO definitions
- Impact analysis reports

**SaaS Considerations**:
- Customer-facing systems typically most critical
- Data loss tolerance (RPO) for customer data
- Service restoration priorities

**Healthcare Considerations**:
- Patient care system criticality
- PHI system recovery priorities
- Emergency vs. non-emergency operations

---

#### A1.3.2 - Disaster Recovery Plan (DRP)

**What This Means**:
A documented plan guides technical recovery of IT systems.

**Control Examples**:
- Disaster recovery plan documented
- Recovery procedures for each critical system
- Recovery team roles and responsibilities
- Recovery sequence and dependencies
- Communication procedures during recovery
- Vendor contact information for recovery

**Evidence**:
- DRP documentation
- Recovery procedures
- Team contact lists
- Recovery playbooks

**SaaS Considerations**:
- Database failover procedures
- Application failover procedures
- DNS failover procedures
- Customer communication during DR events

**Healthcare Considerations**:
- HIPAA contingency plan requirement
- PHI system recovery procedures
- Emergency mode operations
- Patient care continuity procedures

---

#### A1.3.3 - Business Continuity Plan (BCP)

**What This Means**:
A documented plan guides overall business continuity beyond just IT.

**Control Examples**:
- Business continuity plan documented
- Alternative work locations identified
- Critical business functions prioritized
- Communication procedures
- Supplier/vendor alternate arrangements
- Remote work capabilities

**Evidence**:
- BCP documentation
- Alternative site agreements
- Communication plans
- Remote access capabilities

**SaaS Considerations**:
- Support team continuity
- Engineering team continuity
- Management communication procedures

**Healthcare Considerations**:
- Patient care continuity
- Emergency operations procedures
- Alternative care delivery arrangements

---

#### A1.3.4 - DR/BC Testing

**What This Means**:
Disaster recovery and business continuity plans are regularly tested.

**Control Examples**:
- Annual (minimum) DR/BC testing
- Test scenarios documented
- Tabletop exercises
- Full recovery simulations
- Test results documented
- Plan updates based on test findings

**Evidence**:
- Test plans
- Test results and reports
- Tabletop exercise documentation
- Plan update records
- Lessons learned documentation

**SaaS Considerations**:
- Failover testing (manual and automated)
- Restore testing from backups
- Cross-region failover drills
- Customer communication testing

**Healthcare Considerations**:
- Emergency mode operation testing
- PHI system recovery testing
- Patient care continuity drills

---

#### A1.3.5 - Incident Response Integration

**What This Means**:
Incident response procedures address availability incidents.

**Control Examples**:
- Availability incident classification
- Incident escalation procedures
- Service restoration procedures
- Customer notification procedures
- Post-incident reviews for availability events

**Evidence**:
- Incident response procedures
- Availability incident logs
- Customer notifications
- Post-incident review reports

**SaaS Considerations**:
- Status page updates
- Incident severity definitions (P0, P1, etc.)
- Customer SLA impact assessment
- Blameless post-mortems

**Healthcare Considerations**:
- Patient care impact assessment
- Emergency notification procedures
- System restoration priorities

---

## Integration with Security Common Criteria

Availability builds upon the Security Common Criteria. Key integration points:

### CC7 (System Operations) + Availability

**Monitoring**:
- CC7.2 focuses on security anomalies
- Availability adds performance and capacity monitoring
- Combined: Comprehensive system health monitoring

**Incident Response**:
- CC7.3/7.4 handle security incidents
- Availability adds service outage response
- Combined: All incidents (security and availability) managed

### CC9 (Risk Mitigation) + Availability

**Business Continuity**:
- CC9.1 addresses business disruptions
- Availability expands with specific RTO/RPO
- Combined: Complete continuity and recovery program

**Vendor Management**:
- CC9.2 addresses vendor security risks
- Availability adds vendor availability SLAs
- Combined: Comprehensive third-party risk management

---

## Availability Control Documentation Best Practices

### Define Measurable Commitments

**Good Example**:
> "The application maintains 99.9% uptime during business hours (6 AM - 10 PM PST, Monday-Friday), measured monthly. Uptime is calculated as: (Total Minutes in Month - Downtime Minutes) / Total Minutes in Month. Planned maintenance windows (announced 72 hours in advance) are excluded from calculations."

**Poor Example**:
> "The system is highly available."

### Document Recovery Objectives

**Good Example**:
> "Critical production databases have an RTO of 1 hour and RPO of 15 minutes. Recovery procedures are documented in DR Runbook v3.2. Recovery is tested quarterly with last test completed on 2024-09-15 achieving RTO of 47 minutes and RPO of 10 minutes."

**Poor Example**:
> "Systems can be recovered quickly if needed."

### Describe Monitoring and Alerting

**Good Example**:
> "CPU utilization is monitored every 60 seconds. Alerts trigger when:
> - Warning: CPU > 80% for 5 consecutive minutes
> - Critical: CPU > 90% for 3 consecutive minutes
> Alerts page the on-call engineer via PagerDuty. Response SLA: Critical alerts acknowledged within 15 minutes."

**Poor Example**:
> "Systems are monitored for performance issues."

---

## Availability Metrics and SLAs

### Common Availability Metrics

**Uptime Percentage**:
- 99% = 7.2 hours downtime/month
- 99.9% = 43 minutes downtime/month
- 99.95% = 21 minutes downtime/month
- 99.99% = 4.3 minutes downtime/month
- 99.999% = 26 seconds downtime/month

**Response Times**:
- API response time (e.g., p95 < 200ms, p99 < 500ms)
- Page load time
- Transaction processing time

**Recovery Metrics**:
- Mean Time To Detect (MTTD)
- Mean Time To Respond (MTTR)
- Recovery Time Objective (RTO)
- Recovery Point Objective (RPO)

### SLA Documentation

**Components of Good SLA**:
1. **Service Definition**: What's covered
2. **Availability Target**: Specific percentage or uptime hours
3. **Measurement Method**: How uptime is calculated
4. **Exclusions**: Planned maintenance, customer-caused outages
5. **Consequences**: Service credits or penalties for non-compliance
6. **Monitoring**: How customers can view real-time status

**Example SLA Statement**:
> "Customer Portal Service Level Agreement:
> - Target Availability: 99.9% measured monthly
> - Measurement: Total available minutes / total minutes in month
> - Exclusions: Planned maintenance (max 4 hours/month with 72-hour notice), customer configuration errors, external service failures beyond our control
> - Service Credits: If availability < 99.9%, customer receives 10% monthly credit; if < 99%, customer receives 25% monthly credit
> - Status Monitoring: Real-time status available at status.company.com"

---

## SaaS-Specific Availability Considerations

### Multi-Tenant Architecture

**Address**:
- Tenant isolation failures don't cascade
- Resource limits per tenant prevent noisy neighbor
- Tenant-specific availability monitoring
- Degraded mode operations

**Control Examples**:
- Resource quotas per tenant
- Circuit breakers to isolate failing tenants
- Per-tenant health checks
- Graceful degradation

### API Availability

**Address**:
- API uptime SLAs
- Rate limiting doesn't affect availability SLA
- API versioning and deprecation
- Webhook reliability

**Control Examples**:
- API health endpoints
- API response time monitoring
- Rate limit design (not overly restrictive)
- API status communication

### Geographic Distribution

**Address**:
- Multi-region deployment
- Regional failover
- Data residency requirements
- Cross-region latency

**Control Examples**:
- Active-active or active-passive regions
- Geographic load balancing
- Regional health checks
- Failover automation

---

## Healthcare-Specific Availability Considerations

### Patient Care Impact

**Address**:
- Critical systems for patient care
- Emergency access procedures
- Downtime notification to clinicians
- Backup/manual procedures

**Control Examples**:
- Critical system designation
- Emergency mode operations
- Downtime procedures for clinical staff
- Alternative access methods

### HIPAA Contingency Plan Requirements

**HIPAA Requires**:
- Data backup plan (§ 164.308(a)(7)(ii)(A))
- Disaster recovery plan (§ 164.308(a)(7)(ii)(B))
- Emergency mode operation plan (§ 164.308(a)(7)(ii)(C))
- Testing and revision procedures (§ 164.308(a)(7)(ii)(D))
- Applications and data criticality analysis (§ 164.308(a)(7)(ii)(E))

**Integration with SOC 2**:
- SOC 2 Availability criteria align well with HIPAA contingency requirements
- Document how SOC 2 controls satisfy HIPAA requirements
- Reference HIPAA-required testing in DR/BC testing

### PHI System Prioritization

**Address**:
- PHI systems recovery priority
- PHI backup procedures
- PHI system failover
- PHI access during downtime

**Control Examples**:
- PHI system criticality ranking
- PHI backup segregation
- PHI emergency access procedures
- Audit logging during recovery

---

## Availability Control Matrix Example

| Control ID | Control Description | TSC Criteria | Testing Method | Evidence |
|-----------|-------------------|--------------|----------------|----------|
| AV-001 | CPU monitoring with 80% threshold alert | A1.1 | Inspect monitoring config, review alerts | Monitoring dashboard, alert config |
| AV-002 | Daily automated database backups | A1.2 | Review backup logs, test restore | Backup policy, backup logs |
| AV-003 | Quarterly DR test | A1.3 | Review test results | DR test report |
| AV-004 | 99.9% uptime SLA monitored monthly | A1.1, A1.3 | Review uptime reports | Uptime reports, SLA calculations |

---

## Resources and Templates

- **Control Matrix Template**: `templates/control_matrix_availability.md`
- **Section 4 Template** (SLAs and commitments): `templates/section_4_commitments.md`
- **Availability Control Examples**: `examples/control_description_samples.md`
- **Security Common Criteria**: `references/tsc_security_criteria.md` (required foundation)

---

## Key Takeaways

1. **Quantify Everything**: Use specific percentages, times, and metrics
2. **Test Regularly**: Backup, restore, failover, and DR testing are required
3. **Monitor Continuously**: Real-time monitoring with defined thresholds
4. **Document RTO/RPO**: Be specific about recovery objectives
5. **Align SLAs**: System description SLAs must match customer contracts
6. **Consider All Scenarios**: Plan for various failure modes
7. **Build on Security**: Availability requires all CC1-CC9 controls plus availability-specific controls
8. **Healthcare Focus**: Emergency procedures, patient care continuity, HIPAA contingency requirements

Availability is about keeping promises to customers. Every commitment in the system description should be measurable, monitored, and testable.

