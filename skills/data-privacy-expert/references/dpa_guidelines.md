# Data Processing Addendum (DPA) Guidelines

## Overview

A Data Processing Addendum (DPA) is a legally binding contract between a data controller and a data processor that governs the processor's handling of personal data on behalf of the controller. DPAs are required under GDPR Article 28 and recommended under CCPA/CPRA.

**Purpose:**
- Define roles and responsibilities
- Ensure processor complies with data protection laws
- Protect controller from processor's non-compliance
- Establish liability and audit rights

## When a DPA Is Required

### GDPR (Article 28)

**Required whenever:**
- Controller engages processor to process personal data on controller's behalf
- Processor engages sub-processor

**"Processing on behalf"** means:
- Processor acts under controller's instructions
- Processor does not determine purposes and means
- Relationship exists to provide service to controller

### CCPA/CPRA

**Required for service providers and contractors**

Service provider/contractor relationship requires written contract prohibiting:
- Retention, use, or disclosure outside performing services
- Selling or sharing personal information
- Retaining, using, or disclosing outside direct business relationship

## Controller vs Processor Determination

### Data Controller

Entity that:
- Determines **why** to process data (purposes)
- Determines **how** to process data (means)
- Makes strategic decisions about data use
- Bears primary legal compliance obligations

**Examples:**
- Company collecting customer data for own business
- Employer collecting employee data
- Website operator collecting visitor data

### Data Processor

Entity that:
- Processes data **on behalf of** controller
- Follows controller's documented **instructions**
- Provides service **to** controller
- Does not make independent decisions about data use

**Examples:**
- Cloud hosting provider storing customer data
- Payroll service provider processing employee data
- Email marketing platform sending campaigns
- Customer support platform accessing customer records
- Analytics provider processing website data

### Joint Controllers

When two or more entities **jointly** determine purposes and means:
- Must arrange responsibilities through transparent arrangement
- Each can be held fully liable
- Must inform data subjects of arrangement

## Essential DPA Clauses

### 1. Parties and Effective Date

**Must Identify:**
- Legal name of controller
- Legal name of processor
- Addresses and contact information
- Effective date of agreement
- Relationship to underlying service agreement

**Best Practice:**
- Reference master service agreement
- Specify that DPA supplements (not replaces) main agreement
- Define precedence if conflicts arise

### 2. Definitions

**Key Terms to Define:**
- Personal Data / Personal Information
- Processing
- Data Subject / Consumer
- Controller / Business
- Processor / Service Provider
- Sub-processor
- Supervisory Authority
- Data Breach / Security Incident
- Applicable Laws (GDPR, CCPA, other)

**Best Practice:**
- Use regulatory definitions where possible
- Define jurisdiction-specific terms if processing in multiple regions
- Include definitions annex if lengthy

### 3. Subject Matter and Duration

**Must Specify:**
- What services processor will provide
- Duration of processing (term of agreement, or specific period)
- Scope of processing activities

**Example:**
"Processor shall process Personal Data for the duration of the Service Agreement to provide [cloud hosting services / payment processing / customer support] as described in Schedule A."

### 4. Nature and Purpose of Processing

**Must Describe:**
- Types of processing activities (collection, storage, analysis, etc.)
- Business purpose or function
- Why processing is necessary

**Example:**
"Processor will store, retrieve, and transmit customer contact information and order history for the purpose of enabling Controller to deliver products and provide customer support."

**Best Practice:**
- Be specific about what processor can and cannot do
- Align with controller's purposes in privacy notice
- Limit to what is necessary

### 5. Type of Personal Data

**Must Specify:**
- Categories of personal data processed
- Whether special categories or sensitive data included

**Examples:**
- Contact information (name, email, phone, address)
- Account credentials (usernames, hashed passwords)
- Transaction data (order history, payment information)
- Usage data (logs, analytics, interactions)
- Special categories: health data, biometric data, etc.
- Sensitive PI (CCPA): financial account numbers, precise geolocation, etc.

**Best Practice:**
- List all categories actually processed
- Identify special categories / sensitive PI separately
- Update if data types change

### 6. Categories of Data Subjects

**Must Specify:**
- Who the data relates to

**Examples:**
- Customers / consumers
- Website visitors
- Employees
- Business contacts
- Children (if applicable, note age ranges)

**Best Practice:**
- Be comprehensive
- Note if includes vulnerable groups (children, employees)

### 7. Controller Obligations and Rights

**Controller Must:**
- Ensure it has lawful basis for processing
- Provide necessary information and instructions to processor
- Ensure processor is capable of complying
- Monitor processor's compliance
- Maintain records of processing activities

**Controller Rights:**
- Issue reasonable documented instructions
- Audit processor's compliance (or engage independent auditor)
- Require processor to assist with compliance
- Terminate for breach

**Best Practice:**
- Specify how instructions will be communicated
- Define audit rights clearly (frequency, notice, scope)
- Address costs of audits

### 8. Processor Obligations

#### 8.1 Process Only on Instructions

Processor must:
- Process only on documented instructions from controller
- Inform controller if instructions violate applicable law
- Not process for own purposes

**Example Clause:**
"Processor shall process Personal Data only on documented written instructions from Controller, including with regard to transfers of Personal Data to a third country or international organization, unless required to do so by EU or Member State law."

#### 8.2 Confidentiality

Processor must:
- Ensure persons authorized to process are under confidentiality obligation
- Implement confidentiality agreements or statutory obligations

**Example Clause:**
"Processor shall ensure that all personnel authorized to process Personal Data have committed themselves to confidentiality or are under an appropriate statutory obligation of confidentiality."

#### 8.3 Security Measures

Processor must implement appropriate technical and organizational measures, considering:
- State of the art
- Costs of implementation
- Nature, scope, context, and purposes
- Risk to data subjects

**Measures typically include:**
- Pseudonymization and encryption
- Ability to ensure ongoing confidentiality, integrity, availability, resilience
- Ability to restore availability after incident
- Regular testing and evaluation

**Example Clause:**
"Processor shall implement and maintain appropriate technical and organizational security measures as set out in Schedule [X] to protect Personal Data against accidental or unlawful destruction, loss, alteration, unauthorized disclosure, or access."

**Best Practice:**
- Attach security measures as schedule/annex
- Specify security standards (ISO 27001, SOC 2, etc.)
- Address encryption (in transit and at rest)
- Include access controls, monitoring, incident response

#### 8.4 Sub-Processors

Processor must:
- Not engage sub-processor without authorization
- Obtain prior specific or general written authorization
- Inform controller of changes with opportunity to object
- Impose same obligations through contract
- Remain fully liable to controller

**General Authorization:**
If general authorization given, processor must:
- Notify controller of intended changes (additions/replacements)
- Allow controller to object
- Maintain list of current sub-processors

**Example Clause:**
"Controller provides general authorization for Processor to engage sub-processors. Processor shall inform Controller of any intended changes concerning addition or replacement of sub-processors at least [30] days in advance, giving Controller opportunity to object. Processor shall maintain a current list of sub-processors at [URL/location]."

**Best Practice:**
- Require written list of current sub-processors
- Specify objection period (e.g., 30 days)
- Define process for objecting
- Address consequences of valid objection (termination, alternative arrangements)
- Require flow-down of all DPA obligations

#### 8.5 Assistance with Data Subject Rights

Processor must assist controller in responding to data subject requests:
- Right of access
- Right to rectification
- Right to erasure
- Right to restriction
- Right to data portability
- Right to object

**Must specify:**
- How processor will assist (technical means, information provision)
- Timeline for assistance
- Compensation for assistance (if chargeable)

**Example Clause:**
"Taking into account the nature of the processing, Processor shall assist Controller by implementing appropriate technical and organizational measures, insofar as possible, for fulfillment of Controller's obligation to respond to data subject requests. Processor shall notify Controller within [5] business days of receiving data subject request and shall provide assistance within [10] business days unless Controller specifies shorter timeframe."

**Best Practice:**
- Specify response times
- Define scope of assistance (free vs. chargeable)
- Clarify who responds to data subject
- Establish communication protocol

#### 8.6 Assistance with Compliance

Processor must assist controller with:
- Security of processing (Article 32)
- Data breach notification (Articles 33-34)
- Data protection impact assessments (Article 35)
- Prior consultation with supervisory authority (Article 36)

**Must account for:**
- Nature of processing
- Information available to processor

**Example Clause:**
"Processor shall assist Controller in ensuring compliance with Controller's obligations under [Articles 32 to 36] of GDPR, taking into account the nature of processing and information available to Processor. Such assistance shall include [providing relevant information about processing, conducting security assessments, participating in DPIA as needed]."

**Best Practice:**
- Be specific about what assistance entails
- Address compensation if significant effort required
- Set expectations for timelines

### 9. Data Breach Notification

Processor must:
- Notify controller without undue delay after becoming aware of breach
- Provide sufficient information for controller to meet notification obligations

**Notification must include:**
- Nature of breach
- Categories and approximate number of data subjects affected
- Categories and approximate number of records affected
- Likely consequences
- Measures taken or proposed to address breach

**Timeline:**
- GDPR: Controller must notify authority within 72 hours
- Processor should notify controller immediately (specify: within 24-48 hours)

**Example Clause:**
"Processor shall notify Controller without undue delay and in any event within [24] hours after becoming aware of a Personal Data Breach. Notification shall include all information specified in Article 33(3) GDPR and shall be delivered to [designated contact] via [email/phone]. Processor shall provide reasonable cooperation and assistance regarding breach investigation and notification."

**Best Practice:**
- Define "without undue delay" (e.g., 24 hours)
- Specify notification method and contact
- Address ongoing cooperation during incident
- Clarify what constitutes "awareness" of breach

### 10. Data Deletion and Return

Upon termination or expiry of services, processor must:
- Delete all personal data (including copies), or
- Return all personal data to controller, and
- Delete existing copies (unless storage required by law)

**Must specify:**
- Method of return (format, encryption)
- Certification of deletion
- Exception for legal retention requirements
- Timeline for deletion/return

**Example Clause:**
"Upon termination of Services or upon Controller's written request, Processor shall, at Controller's choice, delete or return all Personal Data to Controller, and delete existing copies unless EU or Member State law requires storage. Processor shall certify in writing to Controller that it has complied with this requirement within [30] days of termination."

**Best Practice:**
- Specify format for data return
- Address backup tapes and archival copies
- Require written certification
- Allow for legal retention with documentation

### 11. Audit Rights

Controller must have right to audit processor's compliance.

**Must specify:**
- Frequency of audits (e.g., annual, on reasonable notice)
- Notice period required
- Scope of audit
- Access to facilities, records, personnel
- Who bears costs
- Confidentiality obligations
- Can engage independent auditor

**Example Clause:**
"Controller shall have the right to conduct audits (including inspections) of Processor's processing activities, upon reasonable advance written notice of at least [30] days, during normal business hours, no more than [once per year], to verify compliance with this DPA. Controller may engage independent third-party auditor bound by confidentiality. Processor shall provide reasonable cooperation and access to information, facilities, and personnel. Each party shall bear its own costs unless audit reveals material non-compliance."

**Best Practice:**
- Balance controller's need with processor's operational burden
- Limit frequency (e.g., once per year, plus for-cause)
- Address costs (especially if frequent audits or no issues found)
- Allow substitution of certifications (SOC 2, ISO 27001) in lieu of on-site audit
- Protect confidentiality of processor's systems and other clients

### 12. International Data Transfers

If processing involves transfers outside EU/EEA (GDPR) or to third parties outside original collection context:

**Must address:**
- Where data will be processed/stored
- Legal mechanism for transfer
- Additional safeguards

**GDPR Transfer Mechanisms:**
- Adequacy decision (Article 45)
- Standard Contractual Clauses (Article 46)
- Binding Corporate Rules (Article 47)
- Derogations (Article 49) - limited use

**Example Clause:**
"Processor shall not transfer Personal Data outside the European Economic Area unless (a) the transfer is to a country subject to an adequacy decision, or (b) Processor has implemented appropriate safeguards such as Standard Contractual Clauses as approved by European Commission. Where SCCs are used, they are incorporated by reference and Controller and Processor shall execute them as separate agreement or as Schedule [X] to this DPA."

**Best Practice:**
- List all countries where processing will occur
- Attach Standard Contractual Clauses if needed
- Conduct and document Transfer Impact Assessment
- Address governmental access to data
- Specify that processor will notify of changes in processing locations

### 13. Term and Termination

**Must specify:**
- When DPA becomes effective
- Duration (typically tied to service agreement)
- Survival provisions (e.g., confidentiality, deletion obligations)

**Termination provisions:**
- Termination for material breach
- Effect of termination (deletion/return of data)
- Survival of certain obligations

**Example Clause:**
"This DPA shall commence on the Effective Date and remain in force for the duration of the Service Agreement. Either party may terminate this DPA with immediate effect if the other party materially breaches this DPA and fails to remedy within [30] days of written notice. Upon termination, Processor shall delete or return all Personal Data as specified in Section [X]. Sections [confidentiality, limitation of liability, governing law] shall survive termination."

### 14. Liability and Indemnification

**GDPR Requirements:**
- Processor liable for damage only if failed to comply with GDPR processor obligations or acted outside/contrary to lawful instructions
- Processor exempt if proves not responsible for damage
- Where controller and processor involved in same processing, each liable for entire damage (then internal allocation)

**Must address:**
- Scope of liability
- Limitations of liability (if any)
- Indemnification obligations
- Relationship to main agreement

**Example Clause:**
"Each party's liability under this DPA shall be subject to the limitation of liability provisions in the Service Agreement, except that neither party's liability shall be limited with respect to data subject claims under [Article 82] GDPR. Processor shall indemnify Controller against claims arising from Processor's breach of this DPA or failure to comply with Controller's lawful documented instructions."

**Best Practice:**
- Align with main agreement but consider regulatory requirements
- GDPR may override contractual liability limits for data subject claims
- Consider insurance requirements

### 15. Governing Law and Jurisdiction

**Must specify:**
- Which law governs the DPA
- Jurisdiction for disputes

**GDPR Consideration:**
- DPA should be governed by law of EU member state
- If controller in EU, typically controller's jurisdiction
- Cannot contract out of GDPR obligations

**Example Clause:**
"This DPA shall be governed by the laws of [EU Member State], without regard to conflict of law principles. Any disputes shall be subject to the exclusive jurisdiction of the courts of [location]."

### 16. Order of Precedence

**Must clarify:**
- Relationship between DPA and main service agreement
- What prevails in case of conflict

**Example Clause:**
"In the event of conflict between this DPA and the Service Agreement with respect to processing of Personal Data, this DPA shall prevail. In all other matters, the Service Agreement shall govern."

## CCPA-Specific Provisions

### Service Provider Certification

**Required:**
Service provider must certify that it understands restrictions and will comply with them.

**Example Clause:**
"Service Provider certifies that it understands the restrictions in California Civil Code Section 1798.140(ag) and will comply with them."

### Prohibition on Selling/Sharing

**Must include:**
- Prohibition on selling or sharing personal information
- Prohibition on retaining, using, or disclosing outside performing services

**Example Clause:**
"Service Provider shall not: (a) sell or share Personal Information as those terms are defined in CCPA; (b) retain, use, or disclose Personal Information for any purpose other than performing the Services specified in this Agreement; (c) retain, use, or disclose Personal Information outside the direct business relationship between Business and Service Provider."

### Business Purpose Limitation

**Must specify:**
- Specific business purposes for which service provider may use data

**Example Clause:**
"Service Provider may process Personal Information only for the following business purposes: [list specific purposes: payment processing, customer support, hosting services, etc.]."

### Assistance with Consumer Requests

**Must address:**
- How service provider will assist with consumer rights requests

**Example Clause:**
"Service Provider shall, upon Business's request, provide reasonable assistance to enable Business to respond to consumer requests to exercise their rights under CCPA, including requests to know, delete, correct, and opt-out."

### Right to Take Corrective Action

**Must include:**
- Business's right to take reasonable and appropriate steps if service provider cannot comply

**Example Clause:**
"If Service Provider determines it cannot meet its obligations under this Agreement, it shall promptly notify Business. Business shall have the right to take reasonable and appropriate steps to stop and remediate unauthorized use of Personal Information."

## DPA Best Practices

### Structure and Organization

1. **Clear Hierarchy**: Main agreement + DPA + Schedules/Annexes
2. **Modular Approach**: Use schedules for details that may change
3. **Version Control**: Date and version DPA, track updates

### Schedules/Annexes to Include

**Schedule A: Description of Processing**
- Subject matter and duration
- Nature and purpose
- Types of personal data
- Categories of data subjects

**Schedule B: Security Measures**
- Technical measures (encryption, access controls, etc.)
- Organizational measures (policies, training, incident response)
- Compliance certifications (ISO 27001, SOC 2)

**Schedule C: Sub-Processors**
- Current list of sub-processors
- Location and services provided
- Contact information
- Update: Should be living document

**Schedule D: Standard Contractual Clauses** (if international transfers)
- Module 2 (Controller to Processor) typically used
- Complete all required sections
- Execute properly

**Schedule E: Additional Terms** (jurisdiction-specific)
- UK Addendum (if UK processing)
- Swiss provisions (if Swiss processing)
- Other regional requirements

### Negotiation Tips

**For Controllers:**
- Ensure broad audit rights
- Limit sub-processor discretion (require approval or advance notice)
- Require security certifications
- Ensure timely breach notification (specify hours, not "undue delay")
- Require annual attestations of compliance

**For Processors:**
- Limit audit frequency and burden
- General authorization for pre-approved sub-processors
- Clarify scope of "assistance" and when fees apply
- Reasonable liability caps (aligned with service agreement)
- Specify acceptable deletion methods

### Common Pitfalls to Avoid

1. **Boilerplate without customization**: Tailor to actual processing
2. **Inconsistency with privacy notice**: Ensure alignment
3. **Vague security obligations**: Be specific
4. **No sub-processor list**: Maintain current list
5. **Forgetting about backups**: Address deletion of backups
6. **Inadequate breach notification**: Specify short timeline
7. **No provision for law changes**: Include mechanism to update DPA
8. **Missing international transfer safeguards**: Execute SCCs if needed
9. **Ignoring CCPA if processing California data**: Include service provider provisions
10. **No review trigger**: Update when processing changes

## DPA Checklist

Before executing DPA, verify:

### Parties and Roles
- [ ] Parties correctly identified (legal entities)
- [ ] Roles properly classified (controller/processor)
- [ ] Effective date specified
- [ ] Relationship to main agreement clear

### Processing Details
- [ ] Subject matter described
- [ ] Duration specified
- [ ] Nature and purpose defined
- [ ] Types of personal data listed
- [ ] Categories of data subjects identified
- [ ] Special categories/sensitive data noted

### Obligations
- [ ] Process only on instructions - covered
- [ ] Confidentiality obligations - included
- [ ] Security measures - specified (with schedule)
- [ ] Sub-processor requirements - addressed
- [ ] Data subject rights assistance - covered
- [ ] Compliance assistance - included
- [ ] Breach notification - specified with timeline
- [ ] Data deletion/return - addressed
- [ ] Audit rights - defined

### Special Considerations
- [ ] International transfers addressed (if applicable)
- [ ] SCCs attached (if needed)
- [ ] Transfer Impact Assessment conducted (if needed)
- [ ] CCPA provisions included (if California data)
- [ ] Service provider certification included (if CCPA)
- [ ] Other jurisdiction requirements addressed

### Legal Terms
- [ ] Liability and indemnification addressed
- [ ] Governing law specified
- [ ] Dispute resolution defined
- [ ] Term and termination covered
- [ ] Survival provisions included

### Schedules/Annexes
- [ ] Schedule A: Description of processing
- [ ] Schedule B: Security measures
- [ ] Schedule C: Sub-processor list
- [ ] Schedule D: SCCs (if applicable)
- [ ] Schedule E: Additional jurisdiction terms (if applicable)

### Execution
- [ ] Authorized signatories
- [ ] Proper corporate authority
- [ ] Dated signatures
- [ ] Copies distributed to relevant teams
- [ ] DPA filed with main agreement
- [ ] Review schedule set (annual or when changes occur)

## Updating DPAs

### When to Update

DPAs should be reviewed and updated when:
- Changes in processing activities
- New sub-processors added
- Changes in security measures
- Changes in data types processed
- Changes in applicable law
- New jurisdictions involved
- Material changes to service agreement

### Update Process

1. **Assess Changes**: Determine impact on DPA
2. **Draft Amendment**: Create amendment or new version
3. **Internal Review**: Legal and privacy teams review
4. **Negotiate**: Work with other party
5. **Execute**: Properly signed and dated
6. **Distribute**: Provide to relevant stakeholders
7. **File**: Maintain with original DPA

**Best Practice:**
Include provision in DPA requiring periodic review and update mechanism.

## Sample DPA Structure

```
DATA PROCESSING ADDENDUM

1. DEFINITIONS
2. SCOPE AND APPLICABILITY
3. ROLES AND RESPONSIBILITIES
4. PROCESSING DETAILS
   4.1 Subject Matter and Duration
   4.2 Nature and Purpose
   4.3 Types of Personal Data
   4.4 Categories of Data Subjects
5. CONTROLLER OBLIGATIONS
6. PROCESSOR OBLIGATIONS
   6.1 Process Only on Instructions
   6.2 Confidentiality
   6.3 Security Measures
   6.4 Sub-Processors
   6.5 Data Subject Rights
   6.6 Compliance Assistance
7. DATA BREACH NOTIFICATION
8. DATA DELETION AND RETURN
9. AUDIT RIGHTS
10. INTERNATIONAL DATA TRANSFERS
11. LIABILITY AND INDEMNIFICATION
12. TERM AND TERMINATION
13. GENERAL PROVISIONS
14. GOVERNING LAW
15. SIGNATURES

SCHEDULES:
Schedule A: Description of Processing
Schedule B: Technical and Organizational Security Measures
Schedule C: List of Sub-Processors
Schedule D: Standard Contractual Clauses (if applicable)
Schedule E: Additional Terms by Jurisdiction
```

## Resources

- GDPR Article 28: Processor requirements
- Standard Contractual Clauses (2021): For international transfers
- EDPB Guidelines 07/2020: On concepts of controller and processor
- California Civil Code §1798.140(ag): Service provider definition
- CCPA Regulations §7002: Service provider requirements
- Template DPA: See `templates/data_processing_addendum.md`

