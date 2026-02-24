# GDPR Comprehensive Reference Guide

## Overview

The General Data Protection Regulation (GDPR) is the EU's comprehensive data protection law that came into effect on May 25, 2018. It applies to any organization processing personal data of individuals in the EU, regardless of where the organization is located.

**Official Citation**: Regulation (EU) 2016/679

## Scope and Applicability

### Territorial Scope (Article 3)

GDPR applies to:

1. **Establishment Criterion**: Organizations established in the EU, regardless of where processing occurs
2. **Targeting Criterion**: Organizations outside the EU if they:
   - Offer goods or services to EU data subjects (even if free)
   - Monitor behavior of EU data subjects

### Material Scope

GDPR applies to:
- Processing of personal data wholly or partly by automated means
- Processing of personal data in structured filing systems

**Exceptions:**
- Personal or household activities
- Law enforcement activities (covered by separate directive)
- National security activities

## Key Definitions

### Personal Data (Article 4(1))

Any information relating to an identified or identifiable natural person ("data subject").

**Examples:**
- Name, email, phone number
- IP address, cookie identifiers
- Location data
- Financial information
- Photos, audio recordings
- Genetic data, biometric data
- Health data
- Racial/ethnic origin
- Political opinions, religious beliefs
- Trade union membership
- Sexual orientation

**Special Categories (Article 9)** - requires explicit consent or other specific legal basis:
- Racial or ethnic origin
- Political opinions
- Religious or philosophical beliefs
- Trade union membership
- Genetic data
- Biometric data (for identification)
- Health data
- Sex life or sexual orientation

### Processing (Article 4(2))

Any operation performed on personal data:
- Collection, recording, organization
- Structuring, storage, adaptation
- Retrieval, consultation, use
- Disclosure, dissemination, alignment
- Restriction, erasure, destruction

### Data Controller (Article 4(7))

Entity that determines the purposes and means of processing personal data.

**Responsibilities:**
- Determines "why" and "how" to process data
- Bears primary compliance obligations
- Must implement appropriate technical and organizational measures
- Must execute DPAs with processors

### Data Processor (Article 4(8))

Entity that processes personal data on behalf of the controller.

**Responsibilities:**
- Follows controller's documented instructions
- Must execute DPA with controller (Article 28)
- Can only engage sub-processors with controller approval
- Maintains records of processing activities
- Cooperates with supervisory authorities

### Data Protection Officer (DPO) (Article 37)

Required when:
- Processing carried out by public authority
- Core activities require regular and systematic monitoring on large scale
- Core activities involve large-scale processing of special categories or criminal data

**Responsibilities:**
- Inform and advise on GDPR obligations
- Monitor compliance
- Advise on Data Protection Impact Assessments
- Serve as contact point for supervisory authority
- Must be independent and report to highest management

## Principles of Data Processing (Article 5)

### 1. Lawfulness, Fairness, Transparency

**Lawfulness:**
- Must have legal basis under Article 6
- Must comply with other laws

**Fairness:**
- Process data in ways data subjects reasonably expect
- Do not process in ways that are detrimental or misleading
- Balance organization's interests with individual's rights

**Transparency:**
- Provide clear information about processing at collection
- Use clear, plain language
- Make privacy information easily accessible

### 2. Purpose Limitation

- Specify purposes before collection
- Purposes must be explicit and legitimate
- Do not process for incompatible purposes
- Further processing for archiving, scientific research, or statistical purposes is not incompatible (with safeguards)

### 3. Data Minimization

- Collect only data adequate, relevant, and necessary for purposes
- Regularly review data collected
- Delete data fields that are not necessary
- Consider pseudonymization or anonymization

### 4. Accuracy

- Take reasonable steps to ensure accuracy
- Rectify or erase inaccurate data without delay
- Consider source reliability
- Keep data up-to-date where necessary

### 5. Storage Limitation

- Retain data only as long as necessary for purposes
- Define and document retention periods
- Implement regular review and deletion procedures
- May retain longer for archiving, research, or statistical purposes (with safeguards)

### 6. Integrity and Confidentiality

- Implement appropriate security measures
- Protect against unauthorized or unlawful processing
- Protect against accidental loss, destruction, or damage
- Consider state of the art, costs, and nature of risks

### 7. Accountability

- Controller must demonstrate compliance
- Maintain documentation (records of processing, DPIAs, breach records)
- Implement appropriate policies
- Conduct regular audits and reviews

## Legal Bases for Processing (Article 6)

Must have at least one legal basis before processing personal data:

### 1. Consent (Article 6(1)(a))

**Requirements:**
- Freely given, specific, informed, unambiguous
- Clear affirmative action
- Separate from other terms and conditions
- Easy to withdraw (as easy as giving consent)
- Cannot be condition of service if not necessary
- For children under 16 (or lower age set by member state), need parental consent

**Documentation:**
- Who consented
- When they consented
- What they were told
- How they consented
- Whether they have withdrawn consent

### 2. Contract (Article 6(1)(b))

Processing necessary to:
- Perform a contract with the data subject
- Take steps before entering into contract at request of data subject

**Examples:**
- Processing delivery address to ship product
- Processing payment information to charge for service
- Processing account information to provide access

**Limitations:**
- Must be genuinely necessary for contract performance
- Cannot use for peripheral purposes

### 3. Legal Obligation (Article 6(1)(c))

Processing necessary to comply with legal obligation to which controller is subject.

**Examples:**
- Tax reporting requirements
- Employment law obligations
- Legal discovery in litigation
- Regulatory reporting

**Requirements:**
- Must be EU or member state law
- Must be clear and foreseeable
- Must have appropriate basis

### 4. Vital Interests (Article 6(1)(d))

Processing necessary to protect vital interests of data subject or another person.

**Use Cases:**
- Medical emergencies
- Humanitarian crises
- Situations where consent cannot be obtained

**Limitations:**
- Should be used sparingly
- Only when no other legal basis is appropriate
- "Vital interests" means life or death situations

### 5. Public Task (Article 6(1)(e))

Processing necessary for performance of task carried out in public interest or in exercise of official authority.

**Typically Used By:**
- Government agencies
- Public authorities
- Bodies performing official functions

### 6. Legitimate Interests (Article 6(1)(f))

Processing necessary for legitimate interests pursued by controller or third party, except where overridden by interests or fundamental rights of data subject.

**Not available for public authorities in performance of tasks.**

**Three-Part Test:**
1. **Purpose Test**: Is there a legitimate interest?
2. **Necessity Test**: Is processing necessary for that interest?
3. **Balancing Test**: Do individual's interests override legitimate interest?

**Legitimate Interest Assessment (LIA) Must Document:**
- What is the legitimate interest?
- Is processing necessary or could you achieve it another way?
- What is the impact on individuals?
- Can you adopt safeguards to reduce impact?
- Do interests of individuals override your legitimate interest?

**Examples of Legitimate Interests:**
- Fraud prevention
- Network and information security
- Direct marketing (with opt-out)
- Intragroup transfers
- Employee monitoring (with balancing)

## Data Subject Rights

### Right of Access (Article 15)

**What Data Subjects Can Request:**
- Confirmation whether personal data is being processed
- Copy of personal data being processed
- Information about:
  - Purposes of processing
  - Categories of data
  - Recipients or categories of recipients
  - Retention period
  - Rights (rectification, erasure, restriction, objection, complaint)
  - Source of data (if not collected from data subject)
  - Existence of automated decision-making
  - Safeguards for international transfers

**Controller Obligations:**
- Provide first copy free of charge
- May charge reasonable fee for additional copies or manifestly unfounded/excessive requests
- Respond within 30 days (extendable by 2 months)
- Provide in commonly used electronic format if requested electronically

**Restrictions:**
- May refuse if manifestly unfounded or excessive
- May refuse if adversely affects rights of others
- Must justify refusal and inform of complaint rights

### Right to Rectification (Article 16)

**What Data Subjects Can Request:**
- Correction of inaccurate personal data
- Completion of incomplete personal data

**Controller Obligations:**
- Rectify without undue delay
- Communicate rectification to recipients unless impossible or disproportionate effort
- Inform data subject of recipients if requested

### Right to Erasure / "Right to Be Forgotten" (Article 17)

**When Erasure Required:**
- Data no longer necessary for purposes
- Withdrawal of consent (if no other legal basis)
- Objection to processing (and no overriding grounds)
- Data processed unlawfully
- Compliance with legal obligation
- Data collected from children for information society services

**Exceptions (Article 17(3)):**
- Exercise of freedom of expression and information
- Compliance with legal obligation
- Public interest in public health
- Archiving, scientific, historical research, or statistical purposes
- Establishment, exercise, or defense of legal claims

**Controller Obligations:**
- Erase without undue delay
- If data made public, take reasonable steps to inform other controllers to erase links, copies
- Communicate erasure to recipients unless impossible or disproportionate effort

### Right to Restriction of Processing (Article 18)

**When Restriction Applies:**
- Accuracy contested (for period enabling verification)
- Processing unlawful but data subject opposes erasure
- Controller no longer needs data but data subject needs it for legal claims
- Object to processing (pending verification of legitimate grounds)

**Effect of Restriction:**
- Data can only be stored
- Processing only with consent, for legal claims, to protect rights of others, or important public interest

**Controller Obligations:**
- Communicate restriction to recipients unless impossible or disproportionate effort
- Inform data subject before lifting restriction

### Right to Data Portability (Article 20)

**When It Applies:**
- Processing based on consent or contract
- Processing carried out by automated means

**What Data Subjects Can Request:**
- Receive personal data in structured, commonly used, machine-readable format
- Transmit data to another controller without hindrance
- Have data transmitted directly to another controller (where technically feasible)

**Scope:**
- Only data provided by data subject (not inferred or derived data)
- Should not adversely affect rights of others

**Formats:**
- JSON, XML, CSV commonly used
- Should include metadata if necessary

### Right to Object (Article 21)

**General Right to Object:**
- Object to processing based on legitimate interests or public task
- Controller must stop unless demonstrates compelling legitimate grounds overriding interests of data subject

**Absolute Right to Object:**
- Direct marketing: must stop upon objection, no exceptions
- Scientific/historical research or statistics (unless necessary for public interest task)

**Notification:**
- Right to object must be explicitly brought to attention at latest at first communication
- Must be presented clearly and separately

### Rights Related to Automated Decision-Making (Article 22)

**Right Not to Be Subject To:**
- Decision based solely on automated processing
- That produces legal effects or similarly significantly affects data subject

**Exceptions (Automated Decision-Making Permitted If):**
- Necessary for contract
- Authorized by EU or member state law with safeguards
- Based on explicit consent

**Safeguards Required:**
- Right to obtain human intervention
- Right to express point of view
- Right to contest decision
- Must not process special categories (except with explicit consent or substantial public interest with safeguards)

## Data Protection by Design and by Default (Article 25)

### Data Protection by Design

Implement appropriate technical and organizational measures to:
- Integrate data protection into processing
- Consider state of the art, costs, nature, scope, context, and purposes
- Implement measures like pseudonymization

**Examples:**
- Privacy impact assessments at project start
- Privacy-friendly default settings
- Minimize data collection
- Encrypt data
- Implement access controls
- Regular security testing

### Data Protection by Default

Ensure that by default, only personal data necessary for each specific purpose is processed.

**Applies To:**
- Amount of data collected
- Extent of processing
- Period of storage
- Accessibility

**Examples:**
- Collect minimum data by default
- Limit access to data by default
- Short retention periods by default
- Privacy-friendly settings by default

## Data Protection Impact Assessment (DPIA) (Article 35)

### When Required

Required when processing likely to result in high risk to rights and freedoms, particularly when:
- Systematic and extensive evaluation based on automated processing (including profiling)
- Large-scale processing of special categories or criminal conviction data
- Systematic monitoring of publicly accessible area on large scale

**Supervisory authorities must publish list of processing requiring DPIA.**

### DPIA Must Contain

1. Systematic description of processing operations and purposes
2. Assessment of necessity and proportionality
3. Assessment of risks to rights and freedoms
4. Measures to address risks and demonstrate compliance

### Process

1. Describe processing systematically
2. Assess necessity and proportionality
3. Identify and assess risks
4. Identify mitigation measures
5. Consult DPO
6. Consult data subjects or representatives (where appropriate)
7. Document DPIA
8. Review and update when changes occur

### Consultation with Supervisory Authority

Required when DPIA indicates high risk and controller cannot sufficiently mitigate.

**Authority must respond within 8 weeks** (extendable by 6 weeks for complex cases).

## Processor Requirements (Article 28)

### Data Processing Agreement (DPA) Required

Controller must only use processors providing sufficient guarantees and must execute written agreement.

### DPA Must Include

**Subject matter, duration, nature, purpose** of processing

**Type of personal data** and categories of data subjects

**Obligations and rights of controller**

**Processor Obligations:**
1. Process only on documented instructions (including international transfers)
2. Ensure confidentiality of persons authorized to process
3. Implement appropriate security measures (Article 32)
4. Respect conditions for engaging sub-processors
5. Assist controller with data subject rights
6. Assist controller with security, breach notification, and DPIA
7. Delete or return data at end of services
8. Make available information necessary to demonstrate compliance
9. Allow and contribute to audits

### Sub-Processors

- Processor must not engage sub-processor without prior authorization
- Authorization can be general or specific
- Must inform controller of changes with opportunity to object
- Same obligations through contract or other legal act
- Processor remains fully liable to controller

## Security of Processing (Article 32)

### Risk-Based Approach

Implement appropriate technical and organizational measures considering:
- State of the art
- Costs of implementation
- Nature, scope, context, and purposes of processing
- Risk of varying likelihood and severity

### Appropriate Measures May Include

1. **Pseudonymization and encryption** of personal data
2. **Ability to ensure ongoing confidentiality, integrity, availability, and resilience** of systems
3. **Ability to restore availability and access** in timely manner after incident
4. **Regular testing, assessment, and evaluation** of effectiveness

### Organizational Measures

- Security policies and procedures
- Staff training and awareness
- Incident response plan
- Access control procedures
- Change management procedures
- Vendor management

### Technical Measures

- Encryption (in transit and at rest)
- Access controls and authentication
- Network security
- Logging and monitoring
- Secure development practices
- Regular patching and updates
- Backup and disaster recovery

## Data Breach Notification

### Notification to Supervisory Authority (Article 33)

**Timeline: 72 hours** from becoming aware of breach

**"Becoming aware"** means controller has reasonable degree of certainty incident has occurred.

**Notification Must Include:**
1. Nature of breach
2. Categories and approximate number of data subjects affected
3. Categories and approximate number of records affected
4. Contact details of DPO or other contact point
5. Likely consequences of breach
6. Measures taken or proposed to address breach

**Phased Notification:**
If information not available within 72 hours, may provide initially available information and supplement later.

**Documentation:**
Must document all breaches (whether or not reported) including facts, effects, and remedial action.

### Notification to Data Subjects (Article 34)

**When Required:**
Breach likely to result in high risk to rights and freedoms.

**Timeline:** Without undue delay

**Notification Must Include:**
1. Nature of breach in clear and plain language
2. Contact details of DPO or other contact point
3. Likely consequences
4. Measures taken or proposed

**Exceptions (Not Required If):**
1. Appropriate technical/organizational protection applied (e.g., encryption)
2. Controller took subsequent measures ensuring high risk no longer likely to materialize
3. Disproportionate effort (then public communication)

### Processor Obligations (Article 33(2))

Processor must notify controller without undue delay after becoming aware of breach.

## International Data Transfers (Chapter V)

### General Principle

Cannot transfer personal data outside EU/EEA unless:
- Adequate level of protection ensured
- Appropriate safeguards in place
- Specific derogation applies

### Adequacy Decisions (Article 45)

**European Commission determines** adequacy of third country or international organization.

**Current adequate jurisdictions include:**
- Andorra, Argentina, Canada (commercial), Faroe Islands, Guernsey, Israel, Isle of Man, Japan, Jersey, New Zealand, Republic of Korea, Switzerland, United Kingdom, Uruguay
- EU-U.S. Data Privacy Framework

**Effect:**
Transfers can flow freely without further authorization.

### Appropriate Safeguards (Article 46)

When no adequacy decision, can transfer if appropriate safeguards are in place:

**Standard Contractual Clauses (SCCs):**
- Adopted by European Commission
- New SCCs adopted June 2021
- Must assess if destination country law undermines protection

**Binding Corporate Rules (BCRs):**
- For intra-group transfers
- Require approval from lead supervisory authority

**Other Mechanisms:**
- Approved codes of conduct with binding enforcement
- Approved certification mechanisms with binding enforcement
- Ad-hoc contractual clauses (require authority approval)

**Transfer Impact Assessment:**
For SCCs and BCRs, must assess:
- Laws and practices in destination country
- Whether they impinge on protection
- Supplementary measures needed

### Derogations (Article 49)

In absence of adequacy or safeguards, transfers permitted for:
- Explicit consent (after informing of risks)
- Performance of contract
- Important reasons of public interest
- Establishment, exercise, or defense of legal claims
- Vital interests
- Transfers from public register
- Compelling legitimate interests (limited and occasional)

## Supervisory Authorities (Article 51-59)

### Independence

Each member state establishes independent supervisory authority.

**Independence means:**
- Free from external influence
- Adequate resources and powers
- Members appointed for fixed terms

### Powers

**Investigative:**
- Order controller/processor to provide information
- Conduct investigations and audits
- Access premises and equipment
- Obtain access to all personal data

**Corrective:**
- Issue warnings and reprimands
- Order compliance
- Limit or ban processing
- Order erasure
- Impose administrative fines

**Advisory:**
- Advise government and parliament
- Raise public awareness
- Issue guidelines

### Cooperation

**European Data Protection Board (EDPB):**
- Ensures consistent application across EU
- Issues guidelines, recommendations, best practices
- Handles cross-border cases

**One-Stop-Shop:**
For cross-border processing, lead supervisory authority handles case with cooperation of other authorities.

## Administrative Fines (Article 83)

### Two-Tier System

**Up to €10 million or 2% of worldwide annual turnover** (whichever higher):
- Controller/processor obligations (Articles 8, 11, 25-39, 42, 43)
- Certification body obligations (Articles 42, 43)
- Monitoring body obligations (Article 41(4))

**Up to €20 million or 4% of worldwide annual turnover** (whichever higher):
- Basic principles (Articles 5, 6, 7, 9)
- Data subject rights (Articles 12-22)
- International transfers (Articles 44-49)
- Member state law obligations (Article 9(2))
- Non-compliance with authority orders

### Factors Considered

- Nature, gravity, duration of infringement
- Intentional or negligent character
- Actions taken to mitigate damage
- Degree of responsibility
- Previous infringements
- Degree of cooperation with authority
- Categories of data affected
- How authority became aware
- Compliance with prior orders
- Approved codes of conduct or certification

### Application

Fines must be:
- Effective
- Proportionate
- Dissuasive

In each individual case.

## Records of Processing Activities (Article 30)

### Controller Records Must Include

1. Name and contact details of controller (and DPO)
2. Purposes of processing
3. Categories of data subjects
4. Categories of personal data
5. Categories of recipients
6. International transfers and safeguards
7. Retention periods
8. Security measures

### Processor Records Must Include

1. Name and contact details of processor (and DPO)
2. Name and contact details of each controller
3. Categories of processing
4. International transfers and safeguards
5. Security measures

### Exception

Organizations with fewer than 250 employees exempt unless:
- Processing likely to result in risk to rights and freedoms
- Processing not occasional
- Processing includes special categories or criminal conviction data

### Best Practice

Even if exempt, maintain records to demonstrate compliance.

## Penalties and Enforcement

### Supervisory Authority Actions

- Warnings
- Reprimands
- Orders to comply
- Temporary or permanent processing bans
- Data erasure orders
- Administrative fines
- Suspension of data flows

### Right to Lodge Complaint (Article 77)

Data subjects can lodge complaint with supervisory authority.

**Authority must:**
- Inform complainant of progress and outcome
- Inform of right to judicial remedy

### Right to Judicial Remedy (Articles 78-82)

**Against Supervisory Authority (Article 78):**
Can challenge legally binding decision or lack of action.

**Against Controller/Processor (Article 79):**
Can seek judicial remedy for infringement of rights.

**Right to Compensation (Article 82):**
Can receive compensation for material or non-material damage from GDPR infringement.

**Burden of Proof:**
Controller/processor must prove not responsible for damage.

### Criminal Sanctions

Member states may establish additional criminal penalties for certain infringements.

## Compliance Checklist

### Governance
- [ ] Designate DPO (if required)
- [ ] Implement privacy governance structure
- [ ] Adopt privacy policies and procedures
- [ ] Establish breach response procedures
- [ ] Implement staff training program

### Processing
- [ ] Maintain records of processing activities
- [ ] Identify legal bases for all processing
- [ ] Conduct DPIAs for high-risk processing
- [ ] Implement privacy by design and default
- [ ] Ensure data quality and minimization

### Data Subject Rights
- [ ] Implement procedures for all rights
- [ ] Provide privacy notices at collection
- [ ] Establish response timelines (30 days)
- [ ] Train staff on handling requests
- [ ] Document all requests and responses

### Security
- [ ] Conduct risk assessments
- [ ] Implement appropriate technical measures
- [ ] Implement appropriate organizational measures
- [ ] Regular testing and evaluation
- [ ] Document security measures

### Vendors and Processors
- [ ] Inventory all processors
- [ ] Execute DPAs with all processors
- [ ] Conduct vendor due diligence
- [ ] Monitor processor compliance
- [ ] Review sub-processor arrangements

### International Transfers
- [ ] Inventory all international transfers
- [ ] Ensure adequate safeguards
- [ ] Execute SCCs or other mechanisms
- [ ] Conduct transfer impact assessments
- [ ] Monitor destination country developments

### Documentation
- [ ] Maintain records of processing
- [ ] Document legal bases
- [ ] Maintain DPIA records
- [ ] Document all breaches
- [ ] Maintain consent records
- [ ] Document data subject requests
- [ ] Retain copies of DPAs

### Review and Audit
- [ ] Regular compliance audits
- [ ] Review processing activities
- [ ] Update privacy notices
- [ ] Review vendor compliance
- [ ] Monitor regulatory developments
- [ ] Update policies and procedures

