# Vanta MCP Server Setup Guide

## Overview

The Vanta MCP (Model Context Protocol) Server enables Claude to directly query Vanta for audit evidence during conversations. This provides real-time access to policies, controls, risks, and other compliance data.

**Repository**: [github.com/VantaInc/vanta-mcp-server](https://github.com/VantaInc/vanta-mcp-server)

**Benefits for Auditors**:
- Interactive evidence retrieval during audits
- Real-time Vanta data access
- Natural language queries
- No manual export/import needed
- Maintains context across audit conversation

---

## Prerequisites

- Node.js 18 or higher
- Vanta account with appropriate access
- Claude Desktop app or MCP-compatible client
- Vanta API credentials (OAuth or API key)

---

## Installation

### Step 1: Install Vanta MCP Server

```bash
# Using npx (recommended - always uses latest version)
npx @vanta/mcp-server

# Or install globally
npm install -g @vanta/mcp-server
```

### Step 2: Configure Authentication

The Vanta MCP Server supports multiple authentication methods:

**Option A: OAuth (Recommended for Auditors)**

Use the provided Audit API credentials:
- Client ID: `vci_YOUR_CLIENT_ID_HERE`
- Client Secret: `vcs_YOUR_CLIENT_SECRET_HERE` (configured in setup)

**Option B: API Key**

Alternative if you have a Vanta API key.

### Step 3: Configure Claude Desktop

Add Vanta MCP Server to your Claude Desktop configuration:

**Location**: 
- macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
- Windows: `%APPDATA%\Claude\claude_desktop_config.json`

**Configuration**:

```json
{
  "mcpServers": {
    "vanta": {
      "command": "npx",
      "args": [
        "@vanta/mcp-server"
      ],
      "env": {
        "VANTA_CLIENT_ID": "vci_YOUR_CLIENT_ID_HERE",
        "VANTA_CLIENT_SECRET": "vcs_YOUR_CLIENT_SECRET_HERE"
      }
    }
  }
}
```

**Security Note**: Configuration file contains credentials. Secure appropriately.

### Step 4: Restart Claude Desktop

Close and restart Claude Desktop app to load the MCP server.

### Step 5: Verify Connection

In Claude Desktop, you should see the Vanta MCP Server listed as connected.

Test with a simple query:
> "Using the Vanta MCP server, list all policies"

If configured correctly, Claude will query Vanta and return policy list.

---

## Troubleshooting

### MCP Server Not Appearing

**Check**:
1. Configuration file syntax correct (valid JSON)
2. Node.js 18+ installed (`node --version`)
3. Claude Desktop fully restarted
4. No typos in configuration

**Solution**:
- Review Claude Desktop logs for errors
- Validate JSON configuration
- Reinstall MCP server

### Authentication Errors

**Symptoms**:
- "Failed to authenticate with Vanta"
- "Invalid credentials"

**Check**:
1. Client ID and Secret correct
2. Credentials not expired
3. Network connectivity

**Solution**:
- Verify credentials in Vanta dashboard
- Test credentials with API scripts first
- Rotate credentials if needed

### No Data Returned

**Symptoms**:
- MCP server connects but returns empty results

**Check**:
1. Organization has data in Vanta
2. API permissions include audit access
3. Query syntax correct

**Solution**:
- Verify data exists in Vanta web interface
- Check API scope/permissions
- Review Vanta MCP Server documentation

---

## Available MCP Tools

Once configured, the Vanta MCP Server provides these tools (check repository for latest):

**Policy Tools**:
- List all policies
- Get policy details
- Check policy approval status
- Review policy versions

**Control Tools**:
- List controls
- Get control implementation status
- Review control evidence
- Check test results

**Risk Tools**:
- List risks
- Get risk assessments
- Review treatment plans
- Check risk owners

**Evidence Tools**:
- List evidence by control
- Get evidence metadata
- Check evidence currency

**Note**: Exact tool names and capabilities depend on MCP server version. Refer to [Vanta MCP Server documentation](https://github.com/VantaInc/vanta-mcp-server) for details.

---

## Security Considerations

1. **Credential Storage**: Credentials in Claude config file - secure your system
2. **Read-Only Access**: MCP server uses Audit API (read-only by design)
3. **Audit Trail**: All MCP queries logged by Vanta
4. **Session Management**: Tokens managed automatically by MCP server
5. **Data in Claude**: Be aware Vanta data is sent to Claude/Anthropic

---

## Next Steps

After setup, proceed to `mcp_audit_workflow.md` to learn how to conduct audits using the MCP server.

