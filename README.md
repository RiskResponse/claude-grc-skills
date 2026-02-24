# GRC Plugin for Claude

A Claude plugin providing Governance, Risk, and Compliance (GRC) skills for compliance professionals, auditors, and privacy teams. Built by [Risk & Response](https://riskandresponse.com).

## Skills Included

### ISO 27001 Internal Auditor

Comprehensive guidance for conducting ISO 27001:2022 internal audits with Vanta platform integration. Covers the complete 7-step audit process from planning through corrective action follow-up, all 93 Annex A controls, evidence analysis, nonconformity classification, and audit reporting for SaaS companies.

### SOC 2 System Description Expert

Expert guidance for writing and updating SOC 2 system descriptions that comply with AICPA Trust Services Criteria. Focuses on Security (Common Criteria - SEC) and Availability (Common Criteria - A) controls with industry-specific templates for SaaS and Healthcare organizations, including HIPAA alignment and validation scripts.

### Data Privacy Expert

Comprehensive guidance on GDPR and CCPA/CPRA compliance, including data subject rights management, Data Processing Addendum (DPA) drafting, Certificates of Deletion, breach notification procedures, and privacy risk assessments.

## Installation

### Claude Code

```bash
claude plugin install grc
```

Or load locally for development:

```bash
claude --plugin-dir ./claude-grc-skills
```

### Claude Cowork

Install from the Plugin Directory within Claude Cowork.

## Usage

Once installed, skills are invoked automatically by Claude based on task context, or manually:

```
/grc:iso27001-internal-auditor
/grc:soc2-system-description
/grc:data-privacy-expert
```

### Example Use Cases

**ISO 27001 Auditing**: "Conduct an internal audit of our access control policies against ISO 27001:2022 Annex A controls A.5.15 through A.5.18. Review the evidence exported from Vanta and classify any findings."

**SOC 2 Documentation**: "Draft a system description for our SaaS platform covering Security and Availability trust service criteria. We process healthcare data so include HIPAA alignment."

**Privacy Compliance**: "We received a GDPR data subject access request from an EU customer. Walk me through the response process, required timelines, and help me draft the response documentation."

## Plugin Structure

```
claude-grc-skills/
├── .claude-plugin/
│   └── plugin.json
├── skills/
│   ├── iso27001-internal-auditor/
│   │   ├── SKILL.md
│   │   ├── examples/
│   │   ├── mcp/
│   │   ├── references/
│   │   ├── scripts/
│   │   └── templates/
│   ├── soc2-system-description/
│   │   ├── SKILL.md
│   │   ├── examples/
│   │   ├── references/
│   │   ├── scripts/
│   │   └── templates/
│   └── data-privacy-expert/
│       ├── SKILL.md
│       ├── references/
│       ├── scripts/
│       └── templates/
├── LICENSE
└── README.md
```

## License

Apache 2.0 — see [LICENSE](./LICENSE).

## Disclaimer

These skills are provided for informational and productivity purposes only. They do not constitute legal, audit, or compliance advice. Always consult qualified professionals for compliance decisions and verify all outputs against current regulatory requirements.
