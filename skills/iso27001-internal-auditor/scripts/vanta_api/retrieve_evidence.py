#!/usr/bin/env python3
"""
Retrieve Audit Evidence from Vanta

Uses Vanta Audit API listAuditEvidenceUrls endpoint to retrieve evidence URLs
and download evidence files.

Documentation: https://developer.vanta.com/reference/listauditevidenceurls

Supports:
- Listing all evidence URLs
- Downloading evidence files
- Processing CSV files with evidence URLs
- Organizing evidence by control/requirement
"""

import requests
import json
import csv
from pathlib import Path
from datetime import datetime
from urllib.parse import urlparse
from vanta_auth import VantaAuth


class EvidenceRetriever:
    """Retrieve and download audit evidence from Vanta."""
    
    def __init__(self, export_dir='vanta_exports/evidence'):
        """Initialize evidence retriever."""
        self.auth = VantaAuth()
        self.export_dir = Path(export_dir)
        self.export_dir.mkdir(parents=True, exist_ok=True)
        self.base_url = self.auth.config['api_base_url']
    
    def list_audit_evidence(self, audit_id, page_size=100):
        """
        Retrieve all evidence for a specific audit with pagination.
        
        Args:
            audit_id: The audit ID to retrieve evidence for
            page_size: Number of items per page (max 100)
            
        Returns:
            list: All evidence objects for the audit
        """
        url = f"{self.base_url}/v1/audits/{audit_id}/evidence"
        all_evidence = []
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
                
                # Extract evidence from paginated response
                # Vanta nests data under 'results'
                if 'results' in response_data and isinstance(response_data['results'], dict):
                    results = response_data['results']
                    evidence_items = results.get('data', [])
                    page_info = results.get('pageInfo', {})
                elif 'data' in response_data:
                    evidence_items = response_data['data']
                    page_info = response_data.get('pageInfo', {})
                else:
                    evidence_items = []
                    page_info = {}
                
                # Debug: Show cursor info
                next_cursor = page_info.get('endCursor')
                has_next = page_info.get('hasNextPage', False)
                
                all_evidence.extend(evidence_items)
                print(f"  Page {page_num}: {len(evidence_items)} items | Total: {len(all_evidence)} | hasNext: {has_next}")
                
                # Check for next page
                if not has_next or not next_cursor:
                    break
                
                cursor = next_cursor
                page_num += 1
            
            if page_num > max_pages:
                print(f"  ⚠ Stopped at safety limit ({max_pages} pages)")
            
            # Deduplicate evidence by ID (in case pagination isn't working properly)
            unique_evidence = []
            seen_ids = set()
            for item in all_evidence:
                item_id = item.get('id')
                if item_id not in seen_ids:
                    unique_evidence.append(item)
                    seen_ids.add(item_id)
            
            if len(unique_evidence) < len(all_evidence):
                print(f"  ⚠ Removed {len(all_evidence) - len(unique_evidence)} duplicate evidence items")
            
            print(f"\n✓ Retrieved {len(unique_evidence)} unique evidence items")
            print(f"  ℹ Note: Vanta API cursor pagination not working - retrieved first page only")
            print(f"  ℹ For complete evidence: Use Vanta UI export or MCP Server")
            return unique_evidence
            
            print(f"\n✓ Retrieved {len(all_evidence)} total evidence items for audit {audit_id}")
            return all_evidence
            
        except requests.exceptions.RequestException as e:
            print(f"✗ Failed to retrieve evidence: {e}")
            if hasattr(e, 'response') and e.response is not None:
                print(f"  Response: {e.response.text}")
            return all_evidence  # Return what we got so far
    
    def get_evidence_urls(self, audit_id, evidence_id):
        """
        Get download URLs for specific evidence.
        
        Args:
            audit_id: The audit ID
            evidence_id: The evidence ID
            
        Returns:
            list: URLs for downloading evidence files
        """
        url = f"{self.base_url}/v1/audits/{audit_id}/evidence/{evidence_id}/urls"
        
        try:
            response = requests.get(url, headers=self.auth.get_headers())
            response.raise_for_status()
            
            data = response.json()
            urls = data.get('results', data.get('urls', []))
            
            return urls
            
        except requests.exceptions.RequestException as e:
            print(f"  ✗ Failed to get URLs for evidence {evidence_id}: {e}")
            return []
    
    def download_evidence_file(self, evidence_url, control_id, evidence_type, description=''):
        """
        Download evidence file from URL.
        
        Args:
            evidence_url: URL to evidence file
            control_id: Control this evidence relates to
            evidence_type: Type of evidence
            description: Description of evidence
            
        Returns:
            bool: Success status
        """
        try:
            response = requests.get(evidence_url, timeout=30)
            response.raise_for_status()
            
            # Create control-specific directory
            control_dir = self.export_dir / control_id.replace('.', '_')
            control_dir.mkdir(exist_ok=True)
            
            # Determine filename from URL or description
            parsed_url = urlparse(evidence_url)
            original_filename = Path(parsed_url.path).name
            if not original_filename:
                original_filename = f"{evidence_type}_{datetime.now().strftime('%Y%m%d')}"
            
            # Ensure unique filename
            filename = control_dir / original_filename
            counter = 1
            while filename.exists():
                stem = Path(original_filename).stem
                suffix = Path(original_filename).suffix
                filename = control_dir / f"{stem}_{counter}{suffix}"
                counter += 1
            
            # Download file
            with open(filename, 'wb') as f:
                f.write(response.content)
            
            print(f"  ✓ {control_id}: {filename.name}")
            return True
            
        except Exception as e:
            print(f"  ✗ Failed to download {evidence_url}: {e}")
            return False
    
    def process_evidence_csv(self, csv_file):
        """
        Process CSV file containing evidence URLs and download all.
        
        CSV Format: control_id,evidence_type,evidence_url,description
        
        Args:
            csv_file: Path to CSV file with evidence URLs
            
        Returns:
            int: Number of files successfully downloaded
        """
        csv_path = Path(csv_file)
        if not csv_path.exists():
            print(f"✗ CSV file not found: {csv_file}")
            return 0
        
        downloaded = 0
        with open(csv_path, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                control_id = row.get('control_id', 'unknown')
                evidence_type = row.get('evidence_type', 'evidence')
                evidence_url = row.get('evidence_url', '')
                description = row.get('description', '')
                
                if evidence_url:
                    if self.download_evidence_file(evidence_url, control_id, evidence_type, description):
                        downloaded += 1
        
        print(f"\n✓ Downloaded {downloaded} evidence files from CSV")
        return downloaded
    
    def export_all_evidence(self, audit_id):
        """
        Export all evidence for a specific audit and download files.
        
        Args:
            audit_id: The audit ID to export evidence for
            
        Returns:
            list: Evidence metadata
        """
        evidence_items = self.list_audit_evidence(audit_id)
        
        if not evidence_items:
            print("No evidence found or retrieval failed.")
            return []
        
        # Export metadata to JSON
        metadata_file = self.export_dir / 'evidence_metadata.json'
        with open(metadata_file, 'w') as f:
            json.dump(evidence_items, f, indent=2)
        print(f"✓ Evidence metadata saved to {metadata_file}")
        
        # Create CSV for audit reference
        csv_file = self.export_dir / 'evidence_inventory.csv'
        with open(csv_file, 'w') as f:
            f.write("Evidence ID,Name,Evidence Type,Status,Test Status,Related Controls,Creation Date\n")
            for item in evidence_items:
                # Extract control IDs from relatedControls
                controls = item.get('relatedControls', [])
                control_ids = ', '.join([
                    '/'.join(ctrl.get('sectionNames', [])) 
                    for ctrl in controls
                ]) if controls else ''
                
                f.write(f"{item.get('id', '')},"
                       f"\"{item.get('name', '')}\"," 
                       f"{item.get('evidenceType', '')},"
                       f"{item.get('status', '')},"
                       f"{item.get('testStatus', '')},"
                       f"\"{control_ids}\","
                       f"{item.get('creationDate', '')}\n")
        print(f"✓ Evidence inventory saved to {csv_file}")
        
        # Download evidence files
        print("\nDownloading evidence files...")
        downloaded = 0
        for item in evidence_items:
            evidence_id = item.get('id')
            control_id = item.get('controlId', 'unknown')
            evidence_type = item.get('type', 'evidence')
            description = item.get('description', '')
            
            # Get URLs for this evidence
            urls = self.get_evidence_urls(audit_id, evidence_id)
            
            for url_obj in urls:
                url = url_obj.get('url') if isinstance(url_obj, dict) else url_obj
                if url:
                    if self.download_evidence_file(url, control_id, evidence_type, description):
                        downloaded += 1
        
        print(f"\n✓ Downloaded {downloaded} evidence files")
        
        # Generate audit notes
        self.generate_evidence_notes(evidence_items)
        
        return evidence_items
    
    def generate_evidence_notes(self, evidence_items):
        """Generate audit notes for evidence review."""
        notes_file = self.export_dir / 'evidence_audit_notes.md'
        
        # Organize by control
        by_control = {}
        for item in evidence_items:
            control_id = item.get('controlId', 'Unassigned')
            if control_id not in by_control:
                by_control[control_id] = []
            by_control[control_id].append(item)
        
        with open(notes_file, 'w') as f:
            f.write("# Evidence Audit Notes\n\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Total Evidence Items: {len(evidence_items)}\n")
            f.write(f"Controls with Evidence: {len(by_control)}\n\n")
            
            f.write("## Evidence by Control\n\n")
            
            for control_id in sorted(by_control.keys()):
                items = by_control[control_id]
                f.write(f"### {control_id}\n\n")
                f.write(f"Evidence Count: {len(items)}\n\n")
                
                for item in items:
                    f.write(f"- **Type**: {item.get('evidenceType')}\n")
                    f.write(f"  - Upload Date: {item.get('uploadDate')}\n")
                    f.write(f"  - Uploaded By: {item.get('uploadedBy')}\n")
                    f.write(f"  - Description: {item.get('description')}\n")
                    
                    # Check evidence age
                    upload_date_str = item.get('uploadDate')
                    if upload_date_str:
                        try:
                            upload_date = datetime.fromisoformat(upload_date_str.replace('Z', '+00:00'))
                            days_old = (datetime.now() - upload_date.replace(tzinfo=None)).days
                            if days_old > 90:
                                f.write(f"  - ⚠ Evidence is {days_old} days old - verify still current\n")
                        except:
                            pass
                    
                    f.write("\n")
                
                f.write("\n")
        
        print(f"✓ Evidence audit notes generated: {notes_file}")


def main():
    """Main function for standalone execution."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Retrieve audit evidence from Vanta for ISO 27001 audit"
    )
    parser.add_argument('--audit-id', required=True,
                       help='Audit ID to retrieve evidence for (get from list_audits.py)')
    parser.add_argument('--csv', help='Process evidence URLs from CSV file')
    parser.add_argument('--export-dir', default='vanta_exports/evidence',
                       help='Directory to export evidence')
    parser.add_argument('--metadata-only', action='store_true',
                       help='Retrieve metadata only, do not download files')
    
    args = parser.parse_args()
    
    print("=" * 70)
    print("VANTA EVIDENCE RETRIEVER")
    print("=" * 70)
    print(f"Audit ID: {args.audit_id}")
    print()
    
    retriever = EvidenceRetriever(export_dir=args.export_dir)
    
    if args.csv:
        # Process CSV file
        retriever.process_evidence_csv(args.csv)
    else:
        # Export all evidence for the audit
        retriever.export_all_evidence(args.audit_id)
    
    print("\n" + "=" * 70)
    print(f"Evidence retrieval complete. Exported to: {retriever.export_dir}")
    print("=" * 70)


if __name__ == "__main__":
    main()

