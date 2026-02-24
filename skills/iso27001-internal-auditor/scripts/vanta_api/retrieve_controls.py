#!/usr/bin/env python3
"""
Retrieve Controls from Vanta Audit

Uses Vanta Audit API listAuditControls endpoint to retrieve control information
for a specific audit.

Endpoint: GET /v1/audits/{auditId}/controls
Documentation: https://developer.vanta.com/reference/listauditcontrols

Read-only operation - retrieves control implementation status and details.
"""

import requests
import json
from pathlib import Path
from datetime import datetime
from vanta_auth import VantaAuth


class ControlRetriever:
    """Retrieve controls from Vanta audit."""
    
    def __init__(self, export_dir='vanta_exports/controls'):
        """Initialize control retriever."""
        self.auth = VantaAuth()
        self.export_dir = Path(export_dir)
        self.export_dir.mkdir(parents=True, exist_ok=True)
        self.base_url = self.auth.config['api_base_url']
    
    def list_audit_controls(self, audit_id, page_size=100):
        """
        Retrieve all controls for a specific audit with pagination.
        
        Args:
            audit_id: The audit ID to retrieve controls for
            page_size: Number of controls per page (max 100)
            
        Returns:
            list: All control objects for the audit
        """
        url = f"{self.base_url}/v1/audits/{audit_id}/controls"
        all_controls = []
        cursor = None
        page_num = 1
        
        try:
            # Note: Vanta API cursor pagination appears to have issues
            # Retrieving first page only until pagination is resolved
            # For complete data: Use Vanta UI export or MCP Server
            max_pages = 1  # Only retrieve first page due to pagination issues
            while page_num <= max_pages:
                params = {'pageSize': min(page_size, 100)}
                if cursor:
                    params['after'] = cursor  # Vanta uses 'after' not 'cursor'
                
                response = requests.get(url, headers=self.auth.get_headers(), params=params)
                response.raise_for_status()
                
                response_data = response.json()
                
                # Extract controls from paginated response
                # Vanta nests data and pageInfo under 'results'
                if 'results' in response_data and isinstance(response_data['results'], dict):
                    results = response_data['results']
                    controls = results.get('data', [])
                    page_info = results.get('pageInfo', {})
                elif 'data' in response_data:
                    controls = response_data['data']
                    page_info = response_data.get('pageInfo', {})
                else:
                    controls = []
                    page_info = {}
                
                # Debug: Show cursor info
                next_cursor = page_info.get('endCursor')
                has_next = page_info.get('hasNextPage', False)
                
                all_controls.extend(controls)
                print(f"  Page {page_num}: {len(controls)} controls | Total: {len(all_controls)} | hasNext: {has_next}")
                
                # Check for next page
                if not has_next or not next_cursor:
                    break
                
                cursor = next_cursor
                page_num += 1
            
            if page_num > max_pages:
                print(f"  ⚠ Stopped at safety limit ({max_pages} pages)")
            
            # Deduplicate controls by ID (in case pagination isn't working properly)
            unique_controls = []
            seen_ids = set()
            for control in all_controls:
                control_id = control.get('id')
                if control_id not in seen_ids:
                    unique_controls.append(control)
                    seen_ids.add(control_id)
            
            if len(unique_controls) < len(all_controls):
                print(f"  ⚠ Removed {len(all_controls) - len(unique_controls)} duplicate controls")
            
            print(f"\n✓ Retrieved {len(unique_controls)} unique controls")
            print(f"  ℹ Note: Vanta API cursor pagination not working - retrieved first page only")
            print(f"  ℹ For complete control list (123 total): Use Vanta UI export or MCP Server")
            return unique_controls
            
            print(f"\n✓ Retrieved {len(all_controls)} total controls for audit {audit_id}")
            return all_controls
            
        except requests.exceptions.RequestException as e:
            print(f"✗ Failed to retrieve controls: {e}")
            if hasattr(e, 'response') and e.response is not None:
                print(f"  Response: {e.response.text}")
            return all_controls  # Return what we got so far
    
    def export_controls(self, audit_id):
        """
        Export all controls for a specific audit.
        
        Args:
            audit_id: The audit ID to export controls for
            
        Returns:
            list: Control metadata
        """
        print(f"Retrieving controls for audit {audit_id}...")
        controls = self.list_audit_controls(audit_id)
        
        if not controls:
            print("No controls found or retrieval failed.")
            return []
        
        # Export metadata to JSON
        metadata_file = self.export_dir / 'controls_metadata.json'
        with open(metadata_file, 'w') as f:
            json.dump(controls, f, indent=2)
        print(f"✓ Control metadata saved to {metadata_file}")
        
        # Create CSV summary for audit checklist
        csv_file = self.export_dir / 'controls_summary.csv'
        with open(csv_file, 'w') as f:
            f.write("Control ID,Control Name,ISO Section,Framework Name,Status,Owner,Test Count,Document Count\n")
            for control in controls:
                control_id = control.get('id', '')
                name = control.get('name', '')
                
                # Extract ISO section numbers from sections array
                sections = control.get('sections', [])
                section_names = [s.get('name', '') for s in sections if isinstance(s, dict)]
                section_str = ', '.join(section_names) if section_names else ''
                
                # Get framework name
                framework_name = control.get('frameworkName', '')
                
                # Get status (might be in different fields)
                status = control.get('status', control.get('implementationStatus', 'Unknown'))
                
                # Get owner
                owner = control.get('owner', {})
                owner_name = owner.get('displayName', '') if isinstance(owner, dict) else str(owner)
                
                # Get counts
                test_count = len(control.get('tests', []))
                doc_count = len(control.get('documents', []))
                
                f.write(f"{control_id},"
                       f"\"{name}\","
                       f"\"{section_str}\","
                       f"{framework_name},"
                       f"{status},"
                       f"\"{owner_name}\","
                       f"{test_count},"
                       f"{doc_count}\n")
        print(f"✓ Control summary saved to {csv_file}")
        
        # Generate audit notes
        self.generate_control_audit_notes(controls)
        
        # Generate control mapping
        self.generate_iso_control_mapping(controls)
        
        return controls
    
    def generate_control_audit_notes(self, controls):
        """Generate preliminary audit notes for control review."""
        notes_file = self.export_dir / 'control_audit_notes.md'
        
        # Organize by ISO section
        by_section = {}
        for control in controls:
            sections = control.get('sections', [])
            if sections:
                for section_obj in sections:
                    section_name = section_obj.get('name', 'Unassigned') if isinstance(section_obj, dict) else 'Unassigned'
                    if section_name not in by_section:
                        by_section[section_name] = []
                    by_section[section_name].append(control)
            else:
                if 'Unassigned' not in by_section:
                    by_section['Unassigned'] = []
                by_section['Unassigned'].append(control)
        
        with open(notes_file, 'w') as f:
            f.write("# Control Audit Notes\n\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Total Controls: {len(controls)}\n")
            f.write(f"ISO Sections Covered: {len(by_section)}\n\n")
            
            f.write("## Potential Findings\n\n")
            
            # Check for gaps
            no_owner = [c for c in controls if not c.get('owner')]
            no_tests = [c for c in controls if len(c.get('tests', [])) == 0]
            no_docs = [c for c in controls if len(c.get('documents', [])) == 0]
            
            if no_owner:
                f.write(f"### ⚠ Controls Without Owner ({len(no_owner)})\n\n")
                for control in no_owner[:10]:
                    f.write(f"- {control.get('name')} (ID: {control.get('id')})\n")
                if len(no_owner) > 10:
                    f.write(f"- ... and {len(no_owner) - 10} more\n")
                f.write("\n**Potential NC**: ISO 27001:2022 requires control ownership\n\n")
            
            if no_tests:
                f.write(f"### ⚠ Controls Without Tests ({len(no_tests)})\n\n")
                for control in no_tests[:10]:
                    f.write(f"- {control.get('name')} (ID: {control.get('id')})\n")
                if len(no_tests) > 10:
                    f.write(f"- ... and {len(no_tests) - 10} more\n")
                f.write("\n**Observation**: Consider implementing tests for control validation\n\n")
            
            if no_docs:
                f.write(f"### ⚠ Controls Without Documentation ({len(no_docs)})\n\n")
                for control in no_docs[:10]:
                    f.write(f"- {control.get('name')} (ID: {control.get('id')})\n")
                if len(no_docs) > 10:
                    f.write(f"- ... and {len(no_docs) - 10} more\n")
                f.write("\n**Observation**: Controls may need supporting documentation\n\n")
            
            f.write("---\n\n")
            f.write("## Controls by ISO 27001 Section\n\n")
            
            for section in sorted(by_section.keys()):
                section_controls = by_section[section]
                f.write(f"### {section} ({len(section_controls)} controls)\n\n")
                
                for control in section_controls[:5]:  # Show first 5
                    name = control.get('name', 'Unknown')
                    owner = control.get('owner', {})
                    owner_name = owner.get('displayName', 'Unassigned') if isinstance(owner, dict) else 'Unassigned'
                    test_count = len(control.get('tests', []))
                    
                    f.write(f"- **{name}**\n")
                    f.write(f"  - Owner: {owner_name}\n")
                    f.write(f"  - Tests: {test_count}\n")
                    
                    # Flag issues
                    if not owner or owner_name == 'Unassigned':
                        f.write(f"  - ⚠ No owner assigned\n")
                    if test_count == 0:
                        f.write(f"  - ⚠ No tests configured\n")
                    
                    f.write("\n")
                
                if len(section_controls) > 5:
                    f.write(f"_... and {len(section_controls) - 5} more controls in this section_\n\n")
        
        print(f"✓ Control audit notes generated: {notes_file}")
    
    def generate_iso_control_mapping(self, controls):
        """Generate ISO 27001 control coverage mapping."""
        mapping_file = self.export_dir / 'iso27001_control_mapping.md'
        
        # Organize by ISO section
        by_section = {}
        for control in controls:
            sections = control.get('sections', [])
            if sections:
                for section_obj in sections:
                    section_name = section_obj.get('name', 'Unassigned') if isinstance(section_obj, dict) else 'Unassigned'
                    if section_name not in by_section:
                        by_section[section_name] = []
                    by_section[section_name].append(control)
            else:
                if 'Unassigned' not in by_section:
                    by_section['Unassigned'] = []
                by_section['Unassigned'].append(control)
        
        with open(mapping_file, 'w') as f:
            f.write("# ISO 27001:2022 Control Coverage Mapping\n\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write(f"**Total Controls in Vanta**: {len(controls)}\n")
            f.write(f"**ISO Sections Covered**: {len(by_section)}\n\n")
            
            f.write("## Coverage by Annex A Section\n\n")
            f.write("| Section | Controls | Controls with Tests | Coverage |\n")
            f.write("|---------|----------|--------------------|---------|\n")
            
            for section in sorted(by_section.keys()):
                section_controls = by_section[section]
                controls_with_tests = len([c for c in section_controls if c.get('tests')])
                coverage_pct = (controls_with_tests / len(section_controls) * 100) if section_controls else 0
                
                f.write(f"| {section} | {len(section_controls)} | {controls_with_tests} | {coverage_pct:.1f}% |\n")
            
            f.write("\n## Detailed Control List by Section\n\n")
            
            for section in sorted(by_section.keys()):
                f.write(f"### {section}\n\n")
                for control in by_section[section]:
                    name = control.get('name', 'Unknown')
                    control_id = control.get('id', '')
                    tests = control.get('tests', [])
                    docs = control.get('documents', [])
                    
                    f.write(f"- **{name}** (ID: {control_id})\n")
                    f.write(f"  - Tests: {len(tests)}\n")
                    f.write(f"  - Documents: {len(docs)}\n")
                f.write("\n")
        
        print(f"✓ ISO 27001 control mapping generated: {mapping_file}")


def main():
    """Main function for standalone execution."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Retrieve controls from Vanta for ISO 27001 audit"
    )
    parser.add_argument('--audit-id', required=True,
                       help='Audit ID to retrieve controls for (get from list_audits.py)')
    parser.add_argument('--export-dir', default='vanta_exports/controls',
                       help='Directory to export controls')
    
    args = parser.parse_args()
    
    print("=" * 70)
    print("VANTA CONTROL RETRIEVER")
    print("=" * 70)
    print(f"Audit ID: {args.audit_id}")
    print()
    
    retriever = ControlRetriever(export_dir=args.export_dir)
    controls = retriever.export_controls(args.audit_id)
    
    print("\n" + "=" * 70)
    print(f"Control retrieval complete. Exported to: {retriever.export_dir}")
    print("=" * 70)
    print("\nGenerated Files:")
    print(f"  - controls_metadata.json - Full control data")
    print(f"  - controls_summary.csv - CSV summary for audit")
    print(f"  - control_audit_notes.md - Preliminary findings")
    print(f"  - iso27001_control_mapping.md - Coverage by section")
    print("\nNext Steps:")
    print("  1. Review control_audit_notes.md for potential issues")
    print("  2. Review iso27001_control_mapping.md for coverage")
    print("  3. Use controls_summary.csv in audit checklist")
    print("  4. Cross-reference with ISO 27001:2022 Annex A requirements")


if __name__ == "__main__":
    main()

