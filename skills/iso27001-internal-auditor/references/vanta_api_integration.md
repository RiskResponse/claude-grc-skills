# Vanta Audit API Integration Reference

## Overview

The Vanta Audit API provides programmatic access to compliance data for authorized auditors. This enables automated evidence retrieval, reducing manual export time from hours to minutes.

**Official Documentation**: [developer.vanta.com/docs/auditor-application-setup](https://developer.vanta.com/docs/auditor-application-setup)

**API Base URL**: `https://api.vanta.com`

---

## Authentication

### OAuth 2.0 Client Credentials Flow

**Configured Credentials**:
- Client ID: `vci_YOUR_CLIENT_ID_HERE`
- Client Secret: (stored in `vanta_config.json`)

**Token Endpoint**: `POST https://api.vanta.com/oauth/token`

**Request**:
```json
{
  "grant_type": "client_credentials",
  "client_id": "vci_...",
  "client_secret": "vcs_..."
}
```

**Response**:
```json
{
  "access_token": "eyJ...",
  "token_type": "Bearer",
  "expires_in": 3600
}
```

**Usage**: Include token in Authorization header:
```
Authorization: Bearer eyJ...
```

---

## Available Endpoints

### 1. List Policies

**Endpoint**: `GET /v1/policies`

**Documentation**: [developer.vanta.com/reference/listpolicies](https://developer.vanta.com/reference/listpolicies)

**Purpose**: Retrieve all policy documents with metadata

**Response Fields**:
- `id` - Unique policy identifier
- `name` - Policy name
- `version` - Version number
- `status` - published, draft, archived
- `documentUrl` - URL to policy document
- `lastModified` - Last modification date
- `lastReviewed` - Last review date
- `owner` - Policy owner
- `approvedBy` - Who approved
- `approvalDate` - When approved

**Audit Use**:
- Verify all required policies exist (ISO 27001 A.5.1)
- Check review dates (must be within 12 months)
- Verify approval process
- Download policy documents

### 2. List Audit Evidence URLs

**Endpoint**: `GET /v1/audit-evidence-urls`

**Documentation**: [developer.vanta.com/reference/listauditevidenceurls](https://developer.vanta.com/reference/listauditevidenceurls)

**Purpose**: Retrieve URLs to evidence files

**Query Parameters**:
- `controlId` (optional) - Filter by specific control

**Response Fields**:
- `id` - Evidence identifier
- `controlId` - Associated control (e.g., "A.8.13")
- `evidenceType` - Type of evidence
- `url` - Signed URL to evidence file
- `uploadDate` - When uploaded
- `uploadedBy` - Who uploaded
- `description` - Evidence description
- `expiresAt` - URL expiration (typically 24 hours)

**Audit Use**:
- Download all evidence for review
- Organize evidence by control
- Verify evidence currency
- Check evidence completeness

**Note**: URLs are temporary (expire in 24 hours) - download files promptly.

---

## Rate Limits

**Audit API Rate Limits**:
- Exact limits not publicly documented
- Best practice: Implement delays between requests (1 second)
- Monitor for 429 (Too Many Requests) responses
- Implement exponential backoff on rate limit errors

**Our Implementation**:
- `rate_limit_delay: 1` second between requests in config
- Automatic retry with backoff on 429 errors
- Batch operations split across time

---

## Error Handling

### Common Errors

**401 Unauthorized**:
- Invalid or expired credentials
- Solution: Re-authenticate, check credentials

**403 Forbidden**:
- Insufficient permissions
- Solution: Verify Audit API access enabled in Vanta

**404 Not Found**:
- Invalid endpoint or resource
- Solution: Check API documentation, verify resource exists

**429 Too Many Requests**:
- Rate limit exceeded
- Solution: Implement delays, retry with backoff

**500 Internal Server Error**:
- Vanta server issue
- Solution: Retry after delay, contact Vanta support if persists

---

## Best Practices

### 1. Authenticate Once, Reuse Token

Store access token for duration (1 hour typically):
```python
auth = VantaAuth()
headers = auth.get_headers()  # Reuse for multiple requests
```

### 2. Handle Token Expiration

Tokens expire - implement automatic refresh:
```python
if token_expired:
    auth.authenticate()  # Get new token
```

### 3. Download Evidence Promptly

Evidence URLs expire in 24 hours - download immediately.

### 4. Organize by Control

Structure exports by control ID for easy audit reference:
```
vanta_exports/
├── evidence/
│   ├── A_5_1/
│   ├── A_8_13/
│   └── A_8_15/
```

### 5. Generate Audit Notes

Automatically flag potential issues:
- Overdue policy reviews
- Missing evidence
- Failed tests
- Incomplete risk treatments

### 6. Maintain Audit Trail

Log all API calls:
- Timestamp
- Endpoint
- Result
- Evidence retrieved

---

## Script Usage

### Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Test authentication
python3 vanta_auth.py

# Retrieve all audit data
python3 retrieve_all.py

# Retrieve policies only
python3 retrieve_policies.py

# Retrieve evidence only
python3 retrieve_evidence.py

# Process evidence from CSV
python3 retrieve_evidence.py --csv evidence_urls.csv
```

### Integration with Audit Checklist

1. Run `retrieve_all.py` before audit
2. Review generated `*_audit_notes.md` files
3. Use findings to populate audit checklist
4. Reference Vanta evidence in checklist
5. Conduct main audit with pre-identified issues

---

## Vanta API vs. Manual Export

### Time Comparison

| Task | Manual | API | Time Saved |
|------|--------|-----|------------|
| Export policies | 30 min | 1 min | 29 min |
| Download evidence | 60-90 min | 5 min | 55-85 min |
| Organize files | 30 min | 0 min (automated) | 30 min |
| Generate notes | 45 min | 0 min (automated) | 45 min |
| **Total** | **2.5-3 hours** | **6 minutes** | **~2.5 hours** |

### Accuracy Improvement

**Manual Export**:
- Risk of missing items
- Inconsistent organization
- Manual data entry errors
- No automated analysis

**API Export**:
- Complete, systematic retrieval
- Consistent organization
- Automated potential finding identification
- Repeatable process

---

## Advanced Usage

### Filtering Evidence by Control

```bash
# Get evidence for specific control only
python3 retrieve_evidence.py --control A.8.13
```

### Custom Export Directory

```bash
# Export to specific audit folder
python3 retrieve_all.py --export-dir ./audits/2024_annual_audit/vanta_data
```

### Quick Mode (Metadata Only)

```bash
# Fast export without downloading files
python3 retrieve_all.py --quick
```

---

## Integration with Audit Report

### Referencing API-Retrieved Evidence

In audit findings, reference Vanta evidence precisely:

**Example**:
> **Evidence**: Vanta Policy Export (retrieved via API 2024-11-04), Policy ID: POL-2024-015, "Incident Response Procedure v2.1", Last Review Date: 2023-04-10 (file: `vanta_exports/policies/POL-2024-015_Incident_Response_Procedure.pdf`)

### Appendix: Include API Export Inventory

Attach to audit report:
- `audit_inventory.md` - Master inventory
- `policies_summary.csv` - Policy overview
- `evidence_inventory.csv` - Evidence overview

---

## Troubleshooting

**Import Error: Module 'requests' not found**:
```bash
pip install -r requirements.txt
```

**Authentication Fails**:
- Verify credentials in `vanta_config.json`
- Run `python3 vanta_auth.py` to test
- Check Vanta Audit API access enabled

**No Policies Retrieved**:
- Verify organization has policies in Vanta
- Check API permissions
- Try manual export to confirm data exists

**Evidence Download Fails**:
- URLs may have expired (24-hour limit)
- Re-run retrieval to get fresh URLs
- Check network/firewall allows downloads

---

## Security Notes

1. **Read-Only**: Audit API cannot modify Vanta data
2. **Audit Trail**: All API calls logged by Vanta
3. **Credential Security**: Protect `vanta_config.json`
4. **Data Handling**: Treat exported evidence as confidential
5. **Retention**: Securely delete exports after audit completion

---

The Vanta Audit API transforms audit evidence collection from manual, time-consuming process to automated, efficient workflow while maintaining audit quality and independence.

