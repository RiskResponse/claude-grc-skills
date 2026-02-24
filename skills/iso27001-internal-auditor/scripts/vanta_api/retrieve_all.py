#!/usr/bin/env python3
"""
Retrieve All Audit Data from Vanta

Orchestrates retrieval of all audit-relevant data:
- Policies
- Controls
- Evidence
- Risks
- Test results

Creates organized export structure for ISO 27001 internal audit.
"""

import sys
from pathlib import Path
from datetime import datetime
from vanta_auth import VantaAuth
from retrieve_policies import PolicyRetriever
from retrieve_evidence import EvidenceRetriever


def main():
    """Retrieve all audit data from Vanta."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Retrieve all audit data from Vanta for ISO 27001 internal audit"
    )
    parser.add_argument('--export-dir', default='vanta_exports',
                       help='Base directory for all exports')
    parser.add_argument('--quick', action='store_true',
                       help='Metadata only, skip file downloads for faster export')
    
    args = parser.parse_args()
    
    export_base = Path(args.export_dir)
    export_base.mkdir(parents=True, exist_ok=True)
    
    print("=" * 70)
    print("VANTA AUDIT DATA RETRIEVAL")
    print("=" * 70)
    print(f"Export Directory: {export_base.absolute()}")
    print(f"Export Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)
    print()
    
    # Test authentication first
    print("Step 1: Testing Vanta API connection...")
    try:
        auth = VantaAuth()
        if not auth.test_connection():
            print("\n✗ Authentication failed. Cannot proceed with data retrieval.")
            print("  Check your vanta_config.json file has correct credentials.")
            sys.exit(1)
    except Exception as e:
        print(f"\n✗ Authentication error: {e}")
        sys.exit(1)
    
    print("\n" + "-" * 70)
    
    # List audits first - required for audit-scoped API
    print("\nStep 1.5: Listing available audits...")
    print("-" * 70)
    from list_audits import AuditLister
    audit_lister = AuditLister()
    audits = audit_lister.list_audits()
    
    if not audits:
        print("\n✗ No audits found. Cannot retrieve evidence without an audit.")
        print("  Evidence is scoped to specific audits in Vanta Auditor API.")
        sys.exit(1)
    
    audit_lister.display_audits(audits)
    
    # Use the most recent audit
    latest_audit = audit_lister.get_latest_audit(audits)
    audit_id = latest_audit.get('id')
    audit_name = latest_audit.get('name', 'Unknown')
    
    print(f"\n→ Using latest audit: {audit_name} (ID: {audit_id})")
    print("  To use a different audit, run list_audits.py and specify --audit-id")
    
    print("\n" + "-" * 70)
    
    # Retrieve policies
    print("\nStep 2: Retrieving policies...")
    print("-" * 70)
    policy_retriever = PolicyRetriever(export_dir=export_base / 'policies')
    policies = policy_retriever.export_policies(download_documents=not args.quick)
    print(f"✓ Policies: {len(policies)} retrieved")
    
    print("\n" + "-" * 70)
    
    # Retrieve evidence for the selected audit
    print(f"\nStep 3: Retrieving audit evidence for audit {audit_id}...")
    print("-" * 70)
    evidence_retriever = EvidenceRetriever(export_dir=export_base / 'evidence')
    evidence = evidence_retriever.export_all_evidence(audit_id)
    print(f"✓ Evidence: {len(evidence)} items retrieved")
    
    print("\n" + "-" * 70)
    
    # Note: Controls and Risks endpoints would require additional API access
    # These may not be available in Audit API - document this limitation
    print("\nStep 4: Additional data (if API access available)...")
    print("-" * 70)
    print("ℹ Controls, Risks, and Tests may require full Vanta API access.")
    print("  Audit API provides policies and evidence.")
    print("  For complete data, export manually from Vanta or use MCP Server.")
    
    # Generate master audit inventory
    print("\n" + "-" * 70)
    print("\nGenerating audit inventory...")
    generate_audit_inventory(export_base, policies, evidence)
    
    print("\n" + "=" * 70)
    print("RETRIEVAL COMPLETE")
    print("=" * 70)
    print(f"\nAll audit data exported to: {export_base.absolute()}")
    print("\nExported:")
    print(f"  - {len(policies)} policies")
    print(f"  - {len(evidence)} evidence items")
    print("\nGenerated Files:")
    print(f"  - {export_base}/audit_inventory.md - Master inventory")
    print(f"  - {export_base}/policies/policies_summary.csv")
    print(f"  - {export_base}/policies/policy_audit_notes.md")
    print(f"  - {export_base}/evidence/evidence_inventory.csv")
    print(f"  - {export_base}/evidence/evidence_audit_notes.md")
    print("\nNext Steps:")
    print("  1. Review audit_inventory.md for overview")
    print("  2. Review *_audit_notes.md files for potential findings")
    print("  3. Begin document review using exported materials")
    print("  4. Create audit checklist based on evidence gaps")
    print("=" * 70)


def generate_audit_inventory(export_dir, policies, evidence):
    """Generate master audit inventory document."""
    inventory_file = export_dir / 'audit_inventory.md'
    
    with open(inventory_file, 'w') as f:
        f.write("# Vanta Audit Data Inventory\n\n")
        f.write(f"**Export Date**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write("---\n\n")
        
        f.write("## Summary\n\n")
        f.write(f"- **Policies Retrieved**: {len(policies)}\n")
        f.write(f"- **Evidence Items Retrieved**: {len(evidence)}\n\n")
        
        f.write("---\n\n")
        
        f.write("## Policies Overview\n\n")
        f.write("| Policy Name | Version | Last Reviewed | Status |\n")
        f.write("|-------------|---------|---------------|--------|\n")
        for policy in policies:
            name = policy.get('name', 'Unknown')
            version = policy.get('version', '-')
            reviewed = policy.get('lastReviewed', 'Not recorded')
            status = policy.get('status', 'unknown')
            f.write(f"| {name} | {version} | {reviewed} | {status} |\n")
        
        f.write("\n---\n\n")
        
        f.write("## Evidence by Control\n\n")
        # Group evidence by control
        by_control = {}
        for item in evidence:
            control_id = item.get('controlId', 'Unassigned')
            if control_id not in by_control:
                by_control[control_id] = []
            by_control[control_id].append(item)
        
        for control_id in sorted(by_control.keys()):
            items = by_control[control_id]
            f.write(f"### {control_id} ({len(items)} evidence items)\n\n")
            for item in items:
                f.write(f"- {item.get('evidenceType')}: {item.get('description')}\n")
            f.write("\n")
        
        f.write("---\n\n")
        f.write("## File Locations\n\n")
        f.write(f"- Policies: `{export_dir}/policies/`\n")
        f.write(f"- Evidence: `{export_dir}/evidence/`\n")
        f.write(f"- Audit Notes: `*_audit_notes.md` files in each directory\n")
    
    print(f"✓ Master inventory generated: {inventory_file}")


if __name__ == "__main__":
    main()

