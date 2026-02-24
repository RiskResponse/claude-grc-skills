#!/usr/bin/env python3
"""
List Audits from Vanta

Lists all audits accessible via Vanta Auditor API.
This is the first step - you must select an audit before retrieving evidence.

Endpoint: GET /v1/audits
Documentation: https://developer.vanta.com/reference/listaudits
"""

import requests
import json
from pathlib import Path
from datetime import datetime
from vanta_auth import VantaAuth


class AuditLister:
    """List and select audits from Vanta."""
    
    def __init__(self):
        """Initialize audit lister."""
        self.auth = VantaAuth()
        self.base_url = self.auth.config['api_base_url']
    
    def list_audits(self, page_size=100):
        """
        Retrieve list of all audits with pagination.
        
        Args:
            page_size: Number of audits per page (max 100)
            
        Returns:
            list: All audit objects
        """
        url = f"{self.base_url}/v1/audits"
        all_audits = []
        cursor = None
        page_num = 1
        
        try:
            while True:
                params = {'pageSize': min(page_size, 100)}
                if cursor:
                    params['cursor'] = cursor
                
                response = requests.get(url, headers=self.auth.get_headers(), params=params)
                response.raise_for_status()
                
                response_data = response.json()
                
                # Extract audits from paginated response
                if 'data' in response_data:
                    audits = response_data['data']
                    page_info = response_data.get('pageInfo', {})
                elif 'results' in response_data and isinstance(response_data['results'], dict):
                    audits = response_data['results'].get('data', [])
                    page_info = response_data['results'].get('pageInfo', {})
                else:
                    audits = []
                    page_info = {}
                
                all_audits.extend(audits)
                print(f"  Retrieved page {page_num}: {len(audits)} audits")
                
                # Check for next page
                if not page_info.get('hasNextPage'):
                    break
                
                cursor = page_info.get('endCursor')
                page_num += 1
            
            print(f"\n✓ Retrieved {len(all_audits)} total audits from Vanta\n")
            return all_audits
            
        except requests.exceptions.RequestException as e:
            print(f"✗ Failed to retrieve audits: {e}")
            if hasattr(e, 'response') and e.response is not None:
                print(f"  Response: {e.response.text}")
            return all_audits  # Return what we got so far
    
    def display_audits(self, audits):
        """Display audits in readable format."""
        if not audits:
            print("No audits found.")
            return
        
        print("=" * 70)
        print("AVAILABLE AUDITS")
        print("=" * 70)
        print()
        
        for i, audit in enumerate(audits, 1):
            # Handle both string IDs and full audit objects
            if isinstance(audit, str):
                # Just an ID
                print(f"{i}. Audit ID: {audit}")
                print()
            else:
                # Full audit object
                audit_id = audit.get('id', 'unknown')
                name = audit.get('name', 'Unnamed audit')
                framework = audit.get('framework', 'Unknown')
                status = audit.get('status', 'unknown')
                created = audit.get('createdAt', '')
                
                print(f"{i}. {name}")
                print(f"   ID: {audit_id}")
                print(f"   Framework: {framework}")
                print(f"   Status: {status}")
                print(f"   Created: {created}")
                print()
    
    def save_audit_list(self, audits, filename='vanta_exports/audits_list.json'):
        """Save audit list to file."""
        filepath = Path(filename)
        filepath.parent.mkdir(parents=True, exist_ok=True)
        
        with open(filepath, 'w') as f:
            json.dump(audits, f, indent=2)
        
        print(f"✓ Audit list saved to {filepath}")
    
    def get_latest_audit(self, audits):
        """Get the most recent audit."""
        if not audits:
            return None
        
        # If audits are just strings (IDs), return the first one
        if isinstance(audits[0], str):
            return audits[0]
        
        # If full objects, sort by creation date
        sorted_audits = sorted(
            audits,
            key=lambda a: a.get('createdAt', ''),
            reverse=True
        )
        
        return sorted_audits[0] if sorted_audits else None


def main():
    """Main function for standalone execution."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="List all audits from Vanta"
    )
    parser.add_argument('--save', action='store_true',
                       help='Save audit list to JSON file')
    parser.add_argument('--latest', action='store_true',
                       help='Show only the latest audit')
    
    args = parser.parse_args()
    
    print("=" * 70)
    print("VANTA AUDIT LISTER")
    print("=" * 70)
    print()
    
    lister = AuditLister()
    audits = lister.list_audits()
    
    if args.latest and audits:
        latest = lister.get_latest_audit(audits)
        print("LATEST AUDIT:")
        print("=" * 70)
        lister.display_audits([latest])
        print(f"\nTo retrieve evidence for this audit, run:")
        print(f"  python3 retrieve_evidence.py --audit-id {latest.get('id')}")
    else:
        lister.display_audits(audits)
        
        if audits:
            print("=" * 70)
            print("\nTo retrieve evidence for an audit, run:")
            print("  python3 retrieve_evidence.py --audit-id <AUDIT_ID>")
    
    if args.save and audits:
        lister.save_audit_list(audits)
    
    print("\n" + "=" * 70)


if __name__ == "__main__":
    main()

