# Data Breach Notification Procedures

## Overview

This guide provides step-by-step procedures for responding to data breaches under GDPR and CCPA/CPRA, including assessment, notification requirements, and documentation.

**Critical Timelines:**
- **GDPR:** 72 hours to notify supervisory authority
- **CCPA:** Without unreasonable delay
- **Both:** Immediate internal response required

## What Constitutes a Data Breach

### GDPR Definition (Article 4(12))

"Personal data breach" means breach of security leading to accidental or unlawful:
- Destruction
- Loss
- Alteration
- Unauthorized disclosure
- Unauthorized access

to personal data transmitted, stored, or otherwise processed.

**Key Points:**
- Includes confidentiality, integrity, and availability breaches
- Includes both malicious and accidental incidents
- Applies to data in transit and at rest

### CCPA/CPRA Definition

Unauthorized access and exfiltration, theft, or disclosure resulting from:
- Business's violation of duty to implement and maintain reasonable security procedures
- That compromises security, confidentiality, or integrity of personal information

**Key Points:**
- Only applies to unencrypted/unredacted data
- Requires business's failure to maintain reasonable security
- Focus on unauthorized access, theft, or disclosure

## Types of Data Breaches

### 1. Confidentiality Breach
Unauthorized or accidental disclosure or access to personal data.

**Examples:**
- Hacker gains access to database
- Email sent to wrong recipient
- Lost/stolen laptop with unencrypted data
- Website vulnerability exposing customer data
- Employee accessing records without authorization
- Ransomware attack

### 2. Integrity Breach
Unauthorized or accidental alteration of personal data.

**Examples:**
- Data modified by unauthorized party
- Data corrupted during transfer
- Malware altering records

### 3. Availability Breach
Accidental or unauthorized loss of access or destruction of personal data.

**Examples:**
- Ransomware locking access to data
- Accidental deletion without backup
- DDoS attack preventing access
- Physical destruction (fire, flood)
- System failure with data loss

## Immediate Response (First 24 Hours)

### Step 1: Detect and Confirm (Hour 0)

**Actions:**
- Receive report of potential breach (security team, employee, third party, data subject)
- Assign incident response team
- Assign unique incident ID
- Log date and time of detection

**Document:**
- Who discovered breach
- How breach was discovered
- Initial assessment of severity

### Step 2: Contain the Breach (Hours 0-4)

**Immediate Actions:**
- Isolate affected systems
- Revoke compromised credentials
- Block unauthorized access
- Prevent further data exfiltration
- Preserve evidence (logs, system images)

**Do NOT:**
- Destroy evidence in haste
- Communicate to public before assessment

**Document:**
- Containment actions taken
- Systems isolated
- Time of containment

### Step 3: Preliminary Assessment (Hours 4-24)

**Assess:**
- **What happened?** Nature of breach
- **What data was affected?** Types and categories
- **How many people?** Scale of impact
- **What are the risks?** Likelihood and severity of harm
- **Is notification required?** Under GDPR, CCPA, or both

**Document:**
- Initial findings
- Scope estimate
- Risk assessment
- Regulatory notification requirements

### Step 4: Notify Key Stakeholders (Hours 0-24)

**Internal Notifications:**
- Privacy/DPO team
- Legal counsel
- Senior management/board
- IT security team
- Communications team
- Processor (if they caused breach) or Controller (if you're processor)

**External Notifications (if immediately clear):**
- Law enforcement (if criminal activity)
- Insurance carrier (cyber insurance)

**Document:**
- Who was notified
- When they were notified
- Method of notification

## GDPR Breach Notification Requirements

### Assessment: Must Notify Supervisory Authority?

**YES, if breach likely to result in risk to rights and freedoms of individuals.**

**Consider:**
- Type and sensitivity of data
- Ease of identification of individuals
- Severity of consequences for individuals
- Special characteristics of individuals (children, vulnerable)
- Special characteristics of controller
- Number of affected individuals

**Examples Likely Requiring Notification:**
- Financial information exposed
- Health data exposed
- Children's data exposed
- Login credentials exposed
- Large-scale breach
- Special category data exposed
- Data that could lead to identity theft, fraud, discrimination

**Examples Possibly NOT Requiring Notification:**
- Data already public
- Data encrypted with keys not compromised
- Very limited scale with minimal risk
- Affected only data controller, not individuals

**When in Doubt:** Consult DPO and err on side of notification.

### Notification to Supervisory Authority (Article 33)

**Timeline: Within 72 hours of becoming aware**

**"Becoming aware"** = reasonable degree of certainty that security incident has occurred that compromised personal data.

**How to Notify:**
- Use supervisory authority's designated method
- Most have online reporting forms
- Email or postal mail as backup

**Required Information:**

1. **Nature of breach**
   - Describe what happened
   - Types of breach (confidentiality, integrity, availability)
   - How breach occurred
   - Timeline of breach

2. **Categories and approximate number of data subjects affected**
   - E.g., "Approximately 10,000 customers"
   - Provide range if exact number unknown

3. **Categories and approximate number of personal data records affected**
   - E.g., "Approximately 10,000 customer records containing name, email, and purchase history"

4. **Name and contact details of DPO or other contact point**

5. **Likely consequences of breach**
   - Risk of identity theft
   - Risk of financial loss
   - Risk of discrimination
   - Reputational damage
   - Other consequences

6. **Measures taken or proposed to address breach**
   - Immediate containment actions
   - Long-term remediation
   - Measures to mitigate adverse effects on individuals

**Phased Notification:**
If all information not available within 72 hours:
- Notify with information available
- Explain what information is still being gathered
- Provide remaining information in phases without undue delay

**Documentation Required:**
Document ALL breaches (Article 33(5)), whether or not notified to authority:
- Facts of breach
- Effects of breach
- Remedial action taken

**Lead Authority:**
For cross-border processing, notify lead supervisory authority (one-stop-shop mechanism).

### Notification to Data Subjects (Article 34)

**When Required:**
Breach likely to result in **high risk** to rights and freedoms.

**Higher Threshold than Authority Notification:**
- Authority notification: "risk"
- Data subject notification: "high risk"

**Examples Requiring Data Subject Notification:**
- Sensitive data exposed (health, financial)
- Credentials exposed allowing account takeover
- Large-scale breach of data enabling identity theft
- Children's data exposed with risk of harm

**Timeline:** Without undue delay

**Method:**
- Individual communication (email, letter) preferred
- Clear and plain language
- Direct to affected individuals

**Required Information:**
1. **Nature of breach** (in clear, plain language)
2. **Name and contact details of DPO or other contact point**
3. **Likely consequences**
4. **Measures taken or proposed to address breach and mitigate adverse effects**

**Exceptions (NOT Required If):**

1. **Appropriate technical and organizational protection measures applied**
   - E.g., data encrypted and keys not compromised
   - Encryption must render data unintelligible to unauthorized
   - Must have been in place before breach

2. **Controller took subsequent measures ensuring high risk no longer likely to materialize**
   - E.g., compromised credentials reset before misuse
   - Requires evidence risk eliminated

3. **Would involve disproportionate effort**
   - E.g., contact details not available, would be extremely costly
   - Alternative: public communication or similar measure
   - Must inform individuals equally effectively
   - Report to authority why this exception used

**Supervisory Authority Consultation:**
If considering exception, may be wise to consult authority first.

## CCPA/CPRA Breach Notification Requirements

### Assessment: Must Notify?

**YES, if:**
- Unencrypted and unredacted personal information
- Subject to unauthorized access and exfiltration, theft, or disclosure
- As result of business's violation of duty to implement reasonable security

**NO, if:**
- Data was encrypted or redacted
- Business maintained reasonable security (not legally at fault)
- Only internal access without exfiltration

### What Is "Personal Information" for Breach Purposes?

**Covered Information:**
- Name + (SSN, driver's license number, financial account number + security code, medical information, health insurance information)
- Username/email + password/security question
- Biometric data

**Not Typically Covered:**
- Email address alone
- Encrypted data (if properly encrypted)

### Notification to Consumers

**Timeline:** Without unreasonable delay and consistent with legitimate needs of law enforcement.

**Method:**
- Written notice
- Electronic notice (if primary method of communication)
- Substitute notice (if contact information insufficient)

**Required Content:**

**For California Residents:**
1. **Name and contact information of reporting business**
2. **List of types of personal information breached** (to extent known)
   - Must be specific categories
3. **If information listed in Civil Code §1798.81.5(d)(1)(A):**
   - Toll-free number
   - Toll-free numbers for major credit reporting agencies
   - Relevant websites and toll-free numbers for:
     - Federal Trade Commission
     - California Office of Privacy Protection

**Substitute Notice (if insufficient contact information):**
Required to use if:
- Cost of notice would exceed $250,000, or
- Affected class exceeds 500,000, or
- Insufficient contact information

**Substitute notice must include:**
- Email notice (if email addresses available)
- Conspicuous posting on website
- Notification to major statewide media

**Additional State Laws:**
If breach affects residents of other states, must comply with those states' notification laws.

### Notification to California Attorney General

**Required if:**
- Breach affects more than 500 California residents

**Method:**
- Electronic notification
- Provide sample copy of notice sent to consumers

**Timing:**
- In most expedient time possible and without unreasonable delay

## Other Notification Requirements

### Credit Reporting Agencies

If large-scale breach (typically 1,000+ affected):
- Notify major credit reporting agencies (Equifax, Experian, TransUnion)
- Provide them information to help consumers

### Law Enforcement

If breach involves:
- Criminal activity
- Unauthorized access
- Theft

Coordinate with:
- Local law enforcement
- FBI (for cybercrimes)
- Secret Service (for financial crimes)

May request delay in consumer notification for law enforcement purposes - document request.

### Contractual Obligations

Check contracts with:
- Customers (notification requirements in SLAs)
- Partners
- Processors/controllers

### Sector-Specific Regulators

- Health data: HHS (HIPAA breaches)
- Financial data: OCC, SEC, etc.
- Payment card data: Payment brands (Visa, Mastercard)

### Insurance Carrier

Notify cyber insurance carrier immediately:
- Understand coverage
- Comply with policy requirements
- Get assistance and resources

## Detailed Breach Response Procedures

### Phase 1: Detection and Containment (Day 0-1)

**Hour 0-2: Initial Response**
1. Confirm breach occurred
2. Activate incident response team
3. Assign incident commander
4. Create incident log
5. Preserve evidence

**Hour 2-8: Containment**
1. Isolate affected systems
2. Stop the breach
3. Secure systems
4. Block attacker access
5. Protect evidence for forensics

**Hour 8-24: Initial Assessment**
1. Determine what data affected
2. Determine how many people affected
3. Assess risk level
4. Determine notification requirements
5. Begin internal notifications

**Deliverable:** Preliminary Incident Report

### Phase 2: Investigation and Assessment (Day 1-3)

**Day 1: Detailed Investigation**
1. Forensic analysis of affected systems
2. Review logs and audit trails
3. Determine attack vector
4. Identify root cause
5. Map full scope of compromise

**Day 2: Risk Assessment**
1. Catalog all affected data
2. Identify all affected individuals
3. Assess sensitivity of data
4. Evaluate likelihood of harm
5. Consider special circumstances

**Day 3: Notification Decision**
1. Determine GDPR notification requirement
2. Determine CCPA notification requirement
3. Determine other notification requirements
4. Decide on timing
5. Prepare notification content

**Deliverable:** Full Incident Assessment Report

### Phase 3: Notification (Day 2-7)

**GDPR Authority Notification (by Hour 72)**
1. Draft notification with all required elements
2. Legal and DPO review
3. Submit via appropriate channel
4. Document submission

**Consumer/Data Subject Notification**
1. Draft notification in clear, plain language
2. Legal review
3. Determine method (individual vs. public)
4. Coordinate with communications team
5. Send notifications
6. Document all notifications

**Other Notifications**
1. Attorney General (if 500+ California residents)
2. Credit agencies (if large-scale)
3. Law enforcement
4. Partners and customers (per contracts)
5. Insurance carrier

**Deliverable:** Notification Package (copies of all notifications sent)

### Phase 4: Remediation (Day 1-30)

**Immediate Remediation (Day 1-7)**
1. Fix vulnerability
2. Apply security patches
3. Reset compromised credentials
4. Enhance monitoring
5. Deploy additional security controls

**Long-Term Remediation (Day 7-30)**
1. Security assessment
2. Implement recommendations
3. Update policies and procedures
4. Enhance employee training
5. Review vendor security

**Deliverable:** Remediation Plan and Report

### Phase 5: Follow-Up and Prevention (Day 30+)

**Month 1: Monitoring**
1. Enhanced monitoring for affected individuals
2. Credit monitoring (if appropriate)
3. Identity theft protection services
4. Fraud detection

**Month 1-3: Post-Incident Review**
1. Comprehensive lessons learned
2. Update incident response plan
3. Update security controls
4. Additional training
5. Vendor management review

**Ongoing:**
1. Regular security assessments
2. Penetration testing
3. Employee training
4. Monitoring and logging
5. Incident response drills

**Deliverable:** Post-Incident Review Report

## Documentation Requirements

### Incident Log

**Must Include:**
- Unique incident ID
- Date and time of detection
- Date and time of breach (if different)
- How breach discovered
- Who discovered breach
- Initial assessment
- All actions taken (with timestamps)
- All people involved
- All notifications made
- Cost of response

**Maintain for at least 5 years.**

### Breach Register (GDPR Article 33(5))

**For ALL breaches (whether or not notified), document:**
- Facts of breach
- Effects of breach
- Remedial action taken

**Must be available for supervisory authority inspection.**

### Notification Records

**Keep copies of:**
- All notifications sent (authority, data subjects, others)
- Dates sent
- Method of delivery
- Proof of delivery (if applicable)
- List of recipients

### Assessment Records

**Document decision-making:**
- Risk assessment
- Why notification was/was not required
- Why exceptions applied (if applicable)
- Consultation with DPO
- Legal advice

### Forensic Evidence

**Preserve:**
- System logs
- Audit trails
- Forensic images
- Network traffic captures
- Attacker artifacts
- Timeline of events

**Chain of custody if law enforcement involved.**

## Communication Templates

### Internal Notification to Management

**Subject:** URGENT: Data Security Incident - [Incident ID]

**To:** CEO, General Counsel, DPO, CFO, CTO

**Summary:**
- What happened
- What data affected
- How many people affected
- Risk level
- Notification requirements
- Next steps
- Estimated costs

**Request:** Authorization for notification and remediation expenditures

### Notification to Supervisory Authority (GDPR)

**Use authority's official form or template.**

**Include all required elements per Article 33(3).**

**Language:** Professional, factual, complete

### Notification to Data Subjects (GDPR)

**Subject:** Important Security Notice Regarding Your Personal Data

**Dear [Name]:**

We are writing to inform you of a security incident that may have affected your personal data.

**What Happened:**
[Clear description in plain language]

**What Data Was Affected:**
[List specific data types]

**What We Are Doing:**
[Containment and remediation actions]

**What You Should Do:**
[Specific recommendations for data subject]

**How to Contact Us:**
[Name and contact information of DPO or privacy team]

We sincerely apologize for this incident and are taking steps to prevent future occurrences.

Sincerely,
[Name and Title]

### Notification to Consumers (CCPA)

**Subject:** Notice of Data Security Incident

**To [Name]:**

[Business Name] is providing this notice of a data security incident that may have involved your personal information.

**Types of Personal Information Involved:**
[Specific categories - name, SSN, financial account, etc.]

**What Happened:**
[Description of incident]

**What We Are Doing:**
[Remediation actions]

**What You Can Do:**
[Specific steps]

**Contact Information:**
[Toll-free number]

**Resources:**
- Equifax: 1-800-525-6285, www.equifax.com
- Experian: 1-888-397-3742, www.experian.com
- TransUnion: 1-800-680-7289, www.transunion.com
- Federal Trade Commission: 1-877-ID-THEFT (438-4338), www.ftc.gov/idtheft
- California Office of Privacy Protection: www.privacy.ca.gov

We take the security of your information seriously and apologize for this incident.

Sincerely,
[Name and Title]

## Using the Breach Timeline Checker

The `scripts/breach_timeline_checker.py` tool helps track critical deadlines.

**Usage:**
```bash
python3 breach_timeline_checker.py --breach-date "2025-10-30T14:30:00" --jurisdiction GDPR
```

**Features:**
- Calculates 72-hour GDPR deadline
- Tracks notification status
- Sends reminders
- Documents compliance with deadlines

## Breach Severity Assessment Matrix

### Risk Factors

**High Risk (+):**
- Sensitive/special category data
- Financial data
- Health data
- Children's data
- Credentials/authentication data
- Large-scale (1000+ individuals)
- Vulnerable populations
- Potential for identity theft
- Potential for financial loss
- Potential for discrimination

**Lower Risk (-):**
- Data already public
- De-identified data
- Small scale
- Limited data types
- Low sensitivity
- Strong mitigation in place

### Decision Matrix

**Notification Required:**
- GDPR Authority: Risk present
- GDPR Data Subjects: High risk present
- CCPA: Unencrypted + reasonable security not maintained

**When in Doubt:** Notify. Over-notification is better than under-notification from compliance perspective.

## Post-Breach Obligations

### Offering Credit Monitoring

**Consider offering if:**
- SSN or financial data exposed
- High risk of identity theft
- Large-scale breach

**Duration:** Typically 1-2 years

**Document:** Offer made and acceptance rate

### Setting Up Helpline

**For larger breaches:**
- Dedicated phone line
- Trained staff
- FAQ prepared
- Hours of operation
- Language support

### Regular Updates

**If investigation ongoing:**
- Provide updates to affected individuals
- Update public statements
- Update regulators

### Media Relations

**Coordinate with communications team:**
- Consistent messaging
- Designated spokesperson
- Media monitoring
- Social media response

## Preventing Future Breaches

### Security Enhancements

1. **Access Controls:** Least privilege, MFA, regular review
2. **Encryption:** At rest and in transit
3. **Monitoring:** SIEM, anomaly detection, 24/7 SOC
4. **Patching:** Regular updates, vulnerability management
5. **Network Segmentation:** Limit lateral movement
6. **Data Minimization:** Reduce data holdings
7. **Vendor Management:** Assess third-party security

### Training and Awareness

1. **Security awareness training** for all employees
2. **Phishing simulations**
3. **Incident response drills**
4. **Role-specific training** (developers, IT, privacy team)

### Testing

1. **Penetration testing** (annual or more)
2. **Vulnerability scanning** (continuous)
3. **Red team exercises**
4. **Incident response tabletop exercises**

### Governance

1. **Information security policies**
2. **Incident response plan** (review annually)
3. **Business continuity and disaster recovery**
4. **Privacy by design** in new projects
5. **Regular risk assessments**

## Common Mistakes to Avoid

1. **Delay in detecting breach** - Implement robust monitoring
2. **Inadequate containment** - Have plan ready
3. **Destroying evidence** - Preserve first, clean up later
4. **Missing 72-hour deadline** - Start clock correctly, track carefully
5. **Unclear communication** - Use plain language, be specific
6. **Over-promising** - Don't promise what you can't deliver
7. **Inadequate remediation** - Fix root cause, not just symptoms
8. **Insufficient documentation** - Document everything
9. **Ignoring processors** - Coordinate with processors/controllers
10. **No follow-through** - Complete remediation, provide updates

## Regulatory Guidance References

- **GDPR:** Articles 33-34, Recitals 85-88
- **EDPB Guidelines 01/2021:** Examples of data breach notification
- **CCPA/CPRA:** Cal. Civ. Code §1798.150 (private right of action for breaches)
- **California Data Breach Notification Law:** Cal. Civ. Code §§1798.29, 1798.82
- **FTC:** Data Breach Response: A Guide for Business

## Checklist: Breach Response

### Immediate (Hour 0-24)
- [ ] Detect and confirm breach
- [ ] Assign incident response team
- [ ] Create incident log with unique ID
- [ ] Contain breach (isolate systems, revoke access)
- [ ] Preserve evidence
- [ ] Notify key internal stakeholders
- [ ] Preliminary assessment

### Day 1-3
- [ ] Detailed forensic investigation
- [ ] Comprehensive risk assessment
- [ ] Determine all affected data and individuals
- [ ] Decide notification requirements
- [ ] Draft notifications
- [ ] Legal and DPO review

### Day 2-7
- [ ] Notify supervisory authority (if GDPR, within 72 hours)
- [ ] Notify affected individuals (if required)
- [ ] Notify California AG (if 500+ CA residents)
- [ ] Notify law enforcement (if criminal)
- [ ] Notify credit agencies (if large-scale)
- [ ] Notify partners/processors/controllers
- [ ] Issue public statement (if appropriate)

### Day 1-30
- [ ] Implement immediate fixes
- [ ] Enhanced monitoring
- [ ] Provide credit monitoring (if appropriate)
- [ ] Set up helpline (if appropriate)
- [ ] Ongoing investigation
- [ ] Comprehensive remediation plan
- [ ] Update security controls

### Month 1-3
- [ ] Post-incident review
- [ ] Update incident response plan
- [ ] Additional security measures
- [ ] Employee training
- [ ] Vendor review
- [ ] Regulatory follow-up (if requested)

### Ongoing
- [ ] Monitor for affected individuals
- [ ] Long-term security enhancements
- [ ] Regular testing and exercises
- [ ] Update policies and procedures
- [ ] Maintain all documentation (5+ years)

