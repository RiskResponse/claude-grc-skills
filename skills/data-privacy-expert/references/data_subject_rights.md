# Data Subject Rights Comprehensive Guide

## Overview

Data protection regulations grant individuals significant rights over their personal information. This guide provides detailed procedures for handling all data subject rights requests under GDPR and consumer rights requests under CCPA/CPRA.

**Key Timelines:**
- GDPR: 30 days (extendable by 2 months)
- CCPA: 45 days (extendable by 45 days once)

## General Request Handling Procedures

### 1. Receive and Log Request

**Record:**
- Date and time received
- Method of receipt (email, web form, phone, mail)
- Full text of request
- Data subject/consumer contact information
- Type of request (access, deletion, rectification, etc.)
- Unique request ID for tracking

**Tools:**
- Use `scripts/dsr_tracker.py` to log and track requests
- Create ticket in privacy management system
- Assign to designated privacy team member

### 2. Verify Identity

**GDPR Requirements:**
- Must be certain of requester's identity
- Can request additional information if reasonable doubts
- Proportionate to request (stricter for deletion/sensitive data)

**CCPA Requirements:**
- Must use reasonable method to verify identity
- Match at least 2-3 data points with information already maintained
- Higher standard for sensitive data

**Verification Methods:**
- Email confirmation (for email-based accounts)
- Account login verification
- Government ID verification (for high-risk requests)
- Phone verification
- Challenge questions based on data already held

**Documentation:**
- Record verification method used
- Date identity confirmed
- By whom verified

**Red Flags:**
- Request from non-account email
- Mismatch in details provided
- Unusual patterns (multiple requests for different people)
- Request for another person without authorization

### 3. Classify Request Type

Determine which right(s) are being exercised:

**GDPR:**
- Access (Article 15)
- Rectification (Article 16)
- Erasure (Article 17)
- Restriction (Article 18)
- Data Portability (Article 20)
- Objection (Article 21)
- Automated Decision-Making (Article 22)

**CCPA:**
- Right to Know (categories or specific pieces)
- Right to Delete
- Right to Correct
- Right to Opt-Out
- Right to Limit Use of Sensitive Personal Information

### 4. Assess Validity

**Determine:**
- Do we process this person's data?
- Is request valid under applicable law?
- Are there any exemptions or exceptions?
- Do we need clarification from requester?

**If Invalid:**
- Document reason
- Notify requester within timeline
- Explain rights to complain (GDPR) or appeal (CCPA)

### 5. Search for Data

**Comprehensive Search Required:**
- All databases and systems
- Production and non-production environments
- Backups and archives
- Data held by processors
- Paper records
- Employee devices (if applicable)
- Third parties to whom disclosed

**Documentation:**
- List all systems searched
- Date of search
- Results from each system
- Person conducting search

### 6. Review Data

**Before Providing/Deleting:**
- Check for third-party rights or confidential information
- Redact information about others (unless necessary for exercising right)
- Confirm legal basis for retention (if denying deletion)
- Assess impact on business operations

### 7. Respond to Data Subject/Consumer

**Response Must Include:**
- Acknowledgment of request
- Action taken (or reason for refusal)
- Information requested (if access request)
- Confirmation of action (if deletion/correction)
- Explanation of rights (complain to authority, judicial remedy)
- Contact information for questions

**Response Timing:**
- Start clock from receipt of valid request (after identity verification if needed)
- Provide response within regulatory deadline
- If extending deadline, inform within original deadline period

### 8. Document Everything

**Maintain Records:**
- Copy of original request
- Identity verification performed
- Systems searched
- Data found
- Action taken
- Response sent
- Date completed
- Any extensions or clarifications

**Retention:**
- Keep records for at least 3 years (CCPA)
- Keep for 5-7 years (GDPR best practice)
- Necessary to demonstrate compliance

## Right of Access

### GDPR Right of Access (Article 15)

#### What Data Subject Can Request

1. **Confirmation** of whether personal data is being processed
2. **Copy** of personal data undergoing processing
3. **Information** about processing:
   - Purposes of processing
   - Categories of personal data
   - Recipients or categories of recipients
   - Retention period (or criteria)
   - Rights (rectification, erasure, restriction, objection, complain)
   - Source of data (if not collected from data subject)
   - Existence of automated decision-making (including profiling) and logic involved
   - Safeguards for international transfers (if applicable)

#### How to Respond

**Step 1: Gather Information**
- Search all systems for personal data
- Compile list of processing activities involving requester
- Identify all recipients of data

**Step 2: Prepare Response**
- Provide copy in structured, commonly used format
- If requested electronically, provide in commonly used electronic format (unless other format requested)
- Organize clearly (not raw database dumps)
- Include all required information listed above

**Step 3: Review for Exemptions**
- Redact information about third parties (unless they consent or reasonable to disclose)
- Withhold privileged or confidential business information if justified
- Consider adversely affecting rights and freedoms of others

**Step 4: Deliver Response**
- First copy: Free of charge
- Additional copies: Reasonable fee based on administrative costs
- Send via secure method
- Within 30 days (extendable by 2 months if complex)

#### Format Examples

**Structured Presentation:**
```
SUBJECT ACCESS RESPONSE

Data Subject: [Name]
Request Date: [Date]
Response Date: [Date]

1. CONFIRMATION
We confirm that we process your personal data.

2. PERSONAL DATA
[Organized by category]
- Contact Information: [list data]
- Account Information: [list data]
- Transaction History: [list data]

3. PROCESSING INFORMATION
Purposes: [list purposes]
Legal Basis: [list legal bases]
Recipients: [list recipients]
Retention: [retention periods]
Source: [if not from data subject]

4. YOUR RIGHTS
[List all rights and how to exercise]

5. CONTACT INFORMATION
[Privacy team contact]
```

### CCPA Right to Know (§1798.100, §1798.110)

#### What Consumer Can Request

**Two Types:**

**1. Right to Know Categories:**
- Categories of personal information collected
- Categories of sources
- Business/commercial purposes for collection
- Categories of third parties with whom shared
- Categories sold or shared (if any)

**2. Right to Know Specific Pieces:**
- Specific pieces of personal information collected

#### How to Respond

**For Categories Request:**
Provide disclosure covering preceding 12 months:
```
CATEGORIES OF INFORMATION:
- Identifiers (name, email, IP address)
- Commercial information (purchase history)
- Internet activity (browsing history on our site)

CATEGORIES OF SOURCES:
- Directly from you (account creation, purchases)
- Automatically (website cookies)
- Third parties (data brokers)

BUSINESS PURPOSES:
- Fulfill orders and provide services
- Improve website and services
- Communicate with customers

CATEGORIES OF THIRD PARTIES:
- Service providers (hosting, payment processing)
- Analytics providers
- Advertising networks

CATEGORIES SOLD OR SHARED:
- None [or specify categories]
```

**For Specific Pieces Request:**
- Provide actual data (like GDPR access request)
- Organize clearly by category
- Provide in portable and readily usable format

**Verification:**
- Higher standard for specific pieces than categories
- Match at least 2-3 data points

**Response Timeline:**
- 45 days (extendable by 45 days once)
- Inform of extension within 45 days

**Frequency Limitation:**
May require only 2 verifiable requests per 12-month period for specific pieces.

## Right to Deletion/Erasure

### GDPR Right to Erasure (Article 17)

#### When Deletion Required

Must delete when:
1. Data no longer necessary for purposes
2. Withdrawal of consent (and no other legal basis)
3. Data subject objects and no overriding legitimate grounds
4. Data processed unlawfully
5. Compliance with legal obligation
6. Data collected from child for information society services

#### Exceptions (When Can Refuse)

May refuse deletion if necessary for:
1. Exercise of freedom of expression and information
2. Compliance with legal obligation
3. Public interest in public health
4. Archiving, scientific, historical research, or statistical purposes (with safeguards)
5. Establishment, exercise, or defense of legal claims

#### How to Process Deletion

**Step 1: Verify Grounds**
- Confirm one of the grounds for deletion applies
- Check if any exceptions apply
- Document analysis

**Step 2: Delete from All Systems**
- Production databases
- Development/test environments
- Backups (or document backup deletion schedule)
- Analytics platforms
- CRM systems
- Email marketing platforms
- Third-party processors
- Paper records

**Step 3: Notify Recipients**
Unless impossible or disproportionate effort:
- Notify all recipients to whom data disclosed
- Inform of deletion request
- Request they also delete (including links, copies)

**Step 4: Confirm to Data Subject**
- Acknowledge deletion completed
- Specify what was deleted
- Note any exceptions (with justification)
- Inform of right to complain

**Step 5: Issue Certificate of Deletion**
- Use `templates/certificate_of_deletion.md`
- Document what was deleted, when, how
- Obtain authorized signature
- Provide to data subject
- Retain copy for compliance

**Special Consideration - Backups:**
Three approaches:
1. **Immediate deletion from backups** (if technically feasible)
2. **Flagging for deletion** when backup restored
3. **Retention until backup expires** (if short retention period)

Document approach taken and justify.

### CCPA Right to Delete (§1798.105)

#### When Deletion Required

Must delete (and direct service providers to delete) when consumer requests.

#### Exceptions (When Can Refuse)

May refuse if necessary to:
1. Complete transaction, provide goods/services, fulfill contract
2. Detect security incidents, protect against illegal activity
3. Debug to identify and repair errors
4. Exercise free speech or another right
5. Comply with California Electronic Communications Privacy Act
6. Engage in research in public interest (with safeguards, if consumer provided informed consent)
7. Enable solely internal uses reasonably aligned with consumer expectations
8. Comply with legal obligation
9. Make internal lawful uses compatible with context provided

#### How to Process Deletion

**Step 1: Verify Identity**
- Use reasonable verification method
- Higher standard if includes sensitive personal information

**Step 2: Assess Exceptions**
- Review if any exceptions apply
- Document justification if denying

**Step 3: Delete from Records**
- Business's own records
- Direct service providers and contractors to delete
- Document confirmation from service providers

**Step 4: Respond to Consumer**
- Confirm deletion
- Specify if any data retained (and exception relied upon)
- Inform of right to appeal to CPPA

**Timeline:**
- 45 days (extendable by 45 days once)

## Right to Rectification/Correction

### GDPR Right to Rectification (Article 16)

#### What Can Be Rectified

- Correction of inaccurate personal data
- Completion of incomplete personal data

#### How to Process

**Step 1: Verify Inaccuracy**
- Request evidence/documentation if needed
- Assess whether data actually inaccurate
- May consider source and purpose of data

**Step 2: Correct Data**
- Update in all systems
- Verify correction propagated

**Step 3: Notify Recipients**
- Inform all recipients to whom disclosed
- Unless impossible or disproportionate effort
- Inform data subject of recipients (if requested)

**Step 4: Confirm to Data Subject**
- Acknowledge rectification
- Specify what was corrected
- Confirm completeness if applicable

**Timeline:**
- Without undue delay
- Within 30 days (extendable by 2 months)

### CCPA Right to Correct (§1798.106)

#### How to Process

**Step 1: Verify Identity**

**Step 2: Assess Request**
- Determine if information is indeed inaccurate
- Use commercially reasonable efforts to correct

**Step 3: Correct Data**
- Correct in business's records
- Notify service providers and contractors to correct

**Step 4: Respond to Consumer**
- Confirm correction made
- Specify what was corrected

**Timeline:**
- 45 days (extendable by 45 days once)

## Right to Restriction

### GDPR Right to Restriction of Processing (Article 18)

#### When Restriction Applies

Must restrict processing when:
1. Accuracy contested (during verification period)
2. Processing unlawful but data subject opposes erasure (requests restriction)
3. Controller no longer needs data but data subject needs it for legal claims
4. Objection pending (pending verification whether legitimate grounds override)

#### What Restriction Means

Data can only be:
- Stored
- Processed with consent
- Processed for legal claims
- Processed to protect rights of another person
- Processed for important public interest

#### How to Implement

**Step 1: Apply Restriction**
- Flag record in all systems
- Implement technical controls to prevent processing
- Document restriction applied

**Step 2: Notify Recipients**
- Inform all recipients
- Unless impossible or disproportionate effort

**Step 3: Lift Restriction**
- Only when conditions no longer apply
- Inform data subject before lifting restriction

**Timeline:**
- Without undue delay
- Within 30 days (extendable by 2 months)

## Right to Data Portability

### GDPR Right to Data Portability (Article 20)

#### When It Applies

- Processing based on consent or contract
- Processing carried out by automated means

#### What Must Be Provided

Data that:
- Data subject provided to controller
- In structured, commonly used, machine-readable format
- Transmitted directly to another controller (if technically feasible)

#### What Is Not Included

- Inferred or derived data
- Data not provided by data subject

#### Formats

**Commonly used formats:**
- JSON (preferred for structured data)
- XML
- CSV
- API access

**Include:**
- Data values
- Metadata (if necessary for understanding)
- Schema or field descriptions

#### How to Process

**Step 1: Identify Portable Data**
- Only data provided by data subject
- Exclude derived or inferred data

**Step 2: Prepare Data**
- Export in machine-readable format
- Organize logically
- Include schema/documentation

**Step 3: Transmit Data**
- Directly to another controller (if technically feasible and requested)
- Otherwise, provide to data subject

**Step 4: Verify**
- Ensure format is actually usable
- Test if possible

**Timeline:**
- Without undue delay
- Within 30 days (extendable by 2 months)

**Example JSON Structure:**
```json
{
  "export_date": "2025-10-30",
  "data_subject": "user@example.com",
  "account_data": {
    "username": "user123",
    "created_date": "2023-01-15",
    "email": "user@example.com",
    "preferences": { ... }
  },
  "transactions": [
    {
      "date": "2024-05-20",
      "amount": 49.99,
      "items": [ ... ]
    }
  ]
}
```

## Right to Object

### GDPR Right to Object (Article 21)

#### General Right to Object

Data subject can object to processing based on:
- Legitimate interests (Article 6(1)(f))
- Performance of task in public interest (Article 6(1)(e))

**Controller must stop unless:**
- Demonstrates compelling legitimate grounds overriding interests of data subject
- Processing for establishment, exercise, or defense of legal claims

#### Absolute Right to Object

**Direct Marketing:**
- Must stop upon objection
- No exceptions
- Also applies to profiling related to direct marketing

**Scientific/Historical Research or Statistics:**
- Must stop unless necessary for public interest task

#### How to Process

**Step 1: Receive Objection**
- Log and classify type of objection

**Step 2: Assess Grounds**
- **For direct marketing:** Stop immediately
- **For legitimate interests:** Assess whether compelling grounds exist
- Document balancing test

**Step 3: Stop Processing (if no overriding grounds)**
- Cease processing for objected purpose
- Flag record to prevent future processing
- May retain for other lawful purposes

**Step 4: Notify Data Subject**
- Confirm processing stopped
- Or explain compelling grounds (if continuing)
- Inform of right to complain

**Timeline:**
- Direct marketing: Immediately
- Others: Within 30 days (extendable by 2 months)

**Proactive Measure:**
Right to object must be explicitly brought to attention at latest at first communication and presented clearly, separately from other information (Article 21(4)).

## Right to Opt-Out (CCPA)

### Right to Opt-Out of Sale/Sharing (§1798.120)

#### How to Process

**Step 1: Receive Opt-Out**
- Via "Do Not Sell or Share" link
- Via Global Privacy Control (GPC) signal
- Via other method

**Step 2: Process Immediately**
- Stop selling/sharing personal information
- Flag consumer record
- Wait at least 12 months before requesting opt-in

**Step 3: Direct Third Parties**
- Notify third parties who received data
- Instruct to stop selling/sharing

**Step 4: Respect Going Forward**
- Apply to all future collection
- Honor across devices/browsers if possible

**No Response Required:**
Opt-out processed automatically, no need to confirm (unless consumer requests confirmation).

### Right to Limit Use of Sensitive Personal Information (§1798.121)

#### When It Applies

Business uses or discloses sensitive personal information for purposes beyond:
- Performing services reasonably expected
- Specific enumerated purposes (security, quality control, etc.)

#### How to Process

**Step 1: Receive Request**
- Via "Limit Use of My Sensitive Personal Information" link
- Via opt-out preference signal

**Step 2: Limit Use**
- Restrict use to permitted purposes only
- Flag consumer record
- Apply going forward

**Step 3: Direct Service Providers**
- Instruct to limit use
- Confirm compliance

**Timeline:**
- Implement immediately

## Rights Related to Automated Decision-Making

### GDPR (Article 22)

#### Right Not to Be Subject To

Decision based solely on automated processing (including profiling) that:
- Produces legal effects, or
- Similarly significantly affects data subject

#### Exceptions (Permitted If)

1. Necessary for contract
2. Authorized by EU/member state law with safeguards
3. Based on explicit consent

#### Safeguards Required

- Right to obtain human intervention
- Right to express point of view
- Right to contest decision

#### How to Process Objection

**Step 1: Receive Objection**
- Classify as automated decision-making objection

**Step 2: Assess**
- Is decision solely automated?
- Does it produce legal/significant effects?
- Is exception applicable?

**Step 3: Provide Safeguards**
- Human review of decision
- Opportunity for data subject to provide input
- Explanation of decision
- Ability to contest

**Step 4: Respond**
- Explain decision-making process
- Provide outcome of human review
- Address data subject's objections

### CCPA ADMT (Starting 2027)

#### Rights

- Pre-use notice of ADMT
- Opt-out of ADMT
- Access to logic involved
- Ability to appeal decision
- Opportunity for human review

#### How to Process Opt-Out

**Step 1: Receive Opt-Out**
- Via "Limit Use of ADMT" mechanism

**Step 2: Process Within 15 Business Days**
- Stop using ADMT for consumer
- Flag record
- Implement alternative process

**Step 3: Confirm**
- Notify consumer of opt-out processed

## Complex Scenarios

### Multiple Rights in Single Request

**Example:** "Delete all my data and tell me what you had"

**Approach:**
1. Clarify with requester which right takes precedence
2. If both wanted: Provide access first, then delete
3. Document both actions

### Requests for Another Person

**General Rule:** Must verify authority

**Acceptable:**
- Parent on behalf of child
- Legal guardian/power of attorney (with documentation)
- Executor of estate (with documentation)
- Authorized agent (with written authorization)

**Verification:**
- Request proof of authority
- Verify identity of both requester and data subject

### Excessive or Unfounded Requests

**GDPR:**
- May charge reasonable fee or refuse if manifestly unfounded or excessive
- Must justify

**CCPA:**
- May limit to 2 verifiable requests per 12 months (for specific pieces)
- May charge reasonable fee for additional requests

**Documentation Required:**
- Explain why excessive or unfounded
- Provide information on right to complain/appeal

### Data Subject Deceased

**GDPR:**
- Member states may provide for rules regarding deceased persons' rights
- Check national law

**CCPA:**
- Generally, rights do not extend to deceased
- May be exercised by executor/administrator in some cases
- Emerging area, check CPPA guidance

### B2B Contacts

**GDPR:**
- Applies to business contacts (they are individuals)
- All rights apply

**CCPA:**
- Limited exemption until January 1, 2023 (now expired)
- Applies to B2B contacts as of January 1, 2023

## Tracking and Reporting

### Metrics to Track

- Total requests received (by type)
- Average response time
- Requests completed on time
- Requests extended
- Requests denied (with reasons)
- Verifications failed
- Complaints escalated

### Reporting

**Internal:**
- Monthly/quarterly reports to management
- KPIs and trends

**External:**
- May be required for audits
- CPPA may request data

**Use:**
- `scripts/dsr_tracker.py` for automated tracking and reporting

## Staff Training

### Essential Training Topics

1. **Recognizing Requests**
   - Requests may not use legal terminology
   - "Delete my account" = deletion request
   - "What do you know about me?" = access request

2. **Initial Response**
   - Acknowledge promptly
   - Route to privacy team
   - Do not delete/modify data until verified

3. **Identity Verification**
   - When required
   - Methods available
   - Escalation if suspicious

4. **Timelines**
   - Regulatory deadlines
   - Internal SLAs
   - Consequences of delays

5. **Escalation**
   - When to involve legal
   - When to involve DPO
   - Red flag situations

## Templates

For response templates, see:
- `templates/data_subject_request_response.md` - Standard response letters
- `templates/certificate_of_deletion.md` - Deletion confirmation

## Compliance Checklist

- [ ] Written procedures for all rights
- [ ] At least 2 methods for submitting requests
- [ ] Identity verification process documented
- [ ] Staff trained on recognizing and routing requests
- [ ] Privacy team designated and resourced
- [ ] Systems identified for data search
- [ ] Processor agreements address assistance with requests
- [ ] Response templates created
- [ ] Tracking system implemented (`dsr_tracker.py`)
- [ ] Escalation procedures defined
- [ ] Regular audits of request handling
- [ ] Metrics tracked and reported

## Common Pitfalls

1. **Failing to recognize request** - Train staff to spot requests even without legal language
2. **Inadequate verification** - Balance security with accessibility
3. **Incomplete data search** - Search ALL systems, including backups
4. **Missing deadline** - Track carefully, extend proactively if needed
5. **Not notifying processors** - Required to tell processors to delete/correct
6. **Retaining after deletion** - Ensure actually deleted from all systems
7. **Inadequate documentation** - Record every step
8. **No exception analysis** - Always check if exceptions apply
9. **Poor communication** - Explain clearly to data subjects
10. **Ignoring processor requests** - When acting as processor, respond to controller's instructions promptly

