# Vanta API Integration for ISO 27001 Audits

## Overview

These scripts enable automated retrieval of audit evidence from Vanta using the Vanta Audit API.

**Read-Only Access**: All API operations are read-only. No modifications to Vanta data.

## Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure Credentials

Credentials are already configured in `vanta_config.json`:
- OAuth Client ID: vci_YOUR_CLIENT_ID_HERE
- OAuth Client Secret: (configured)

**Security**: Keep vanta_config.json secure. Add to .gitignore if sharing code.

### 3. Test Connection

```bash
python3 vanta_auth.py
```

Should output: "✓ Connection test successful!"

## Usage

### Retrieve All Audit Data

```bash
python3 retrieve_all.py
```

Exports to `vanta_exports/` directory with:
- policies/ - All policy documents and metadata
- evidence/ - All evidence files organized by control

### Retrieve Policies Only

```bash
python3 retrieve_policies.py
```

### Retrieve Evidence Only

```bash
python3 retrieve_evidence.py
```

### Process Evidence from CSV

```bash
python3 retrieve_evidence.py --csv evidence_urls.csv
```

## API Endpoints Used

**Policies**: `GET /v1/policies`
- Documentation: https://developer.vanta.com/reference/listpolicies
- Returns: List of all policies with metadata

**Evidence**: `GET /v1/audit-evidence-urls`  
- Documentation: https://developer.vanta.com/reference/listauditevidenceurls
- Returns: URLs to evidence files with metadata

## Output Structure

```
vanta_exports/
├── audit_inventory.md          # Master inventory
├── policies/
│   ├── policies_metadata.json  # Full policy data
│   ├── policies_summary.csv    # CSV summary
│   ├── policy_audit_notes.md   # Preliminary findings
│   └── [policy documents]      # Downloaded PDFs/docs
└── evidence/
    ├── evidence_metadata.json  # Full evidence data
    ├── evidence_inventory.csv  # CSV summary
    ├── evidence_audit_notes.md # Preliminary findings
    └── A_8_13/                 # Evidence by control
        └── [evidence files]
```

## Audit Workflow Integration

1. **Pre-Audit**: Run `retrieve_all.py` to get all data
2. **Review**: Read generated `*_audit_notes.md` files for potential findings
3. **Audit**: Use exported data as evidence during audit
4. **Document**: Reference Vanta evidence in audit findings
5. **Report**: Include export inventory in audit report appendices

## Troubleshooting

**Authentication Error**:
- Check client_id and client_secret in vanta_config.json
- Verify Audit API access enabled in Vanta
- Check internet connection

**No Data Retrieved**:
- Verify organization has data in Vanta
- Check API permissions
- Review Vanta Audit API documentation

**Download Failures**:
- Check evidence URLs are accessible
- Verify network allows HTTPS downloads
- Check disk space

## API Rate Limits

Vanta API has rate limits. Scripts include delays to respect limits.
If you encounter rate limit errors, increase `rate_limit_delay` in config.

## Security Best Practices

1. **Keep credentials secure**: Don't commit vanta_config.json to version control
2. **Read-only access**: Audit API cannot modify Vanta data
3. **Audit trail**: All API calls are logged by Vanta
4. **Rotate credentials**: Periodically rotate OAuth client secret in Vanta

## Support

For API issues, consult:
- Vanta API Documentation: https://developer.vanta.com
- Vanta Support: support@vanta.com
- Audit API Setup: https://developer.vanta.com/docs/auditor-application-setup

