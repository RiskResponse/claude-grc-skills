#!/usr/bin/env python3
"""
Vanta API Authentication Helper

Uses OAuth 2.0 client credentials flow for Vanta Audit API.
ALL OPERATIONS ARE READ-ONLY - Audit API provides read-only access.

Security Notes:
- Credentials stored in config file (vanta_config.json)
- Config file should be added to .gitignore
- OAuth tokens expire and are refreshed automatically
- Audit API has read-only permissions by design
"""

import os
import json
import requests
from pathlib import Path
from datetime import datetime, timedelta


class VantaAuth:
    """Handle Vanta API authentication using OAuth 2.0 client credentials."""
    
    def __init__(self, config_file='vanta_config.json'):
        """
        Initialize authentication.
        
        Args:
            config_file: Path to configuration file containing OAuth credentials
        """
        self.config_file = Path(config_file)
        self.config = self.load_config()
        self.client_id = self.config.get('client_id')
        self.client_secret = self.config.get('client_secret')
        self.access_token = None
        self.token_expires_at = None
        
        if not self.client_id or not self.client_secret:
            raise ValueError(
                "Missing OAuth credentials. Please configure vanta_config.json "
                "with client_id and client_secret from Vanta Audit API."
            )
    
    def load_config(self):
        """Load configuration from JSON file."""
        if not self.config_file.exists():
            # Create template config if doesn't exist
            template = {
                "client_id": "vci_YOUR_CLIENT_ID",
                "client_secret": "vcs_YOUR_CLIENT_SECRET",
                "api_base_url": "https://api.vanta.com",
                "export_directory": "./vanta_exports",
                "rate_limit_delay": 1
            }
            with open(self.config_file, 'w') as f:
                json.dump(template, f, indent=2)
            raise FileNotFoundError(
                f"Config file created at {self.config_file}. "
                "Please update with your Vanta OAuth credentials."
            )
        
        with open(self.config_file, 'r') as f:
            return json.load(f)
    
    def authenticate(self):
        """
        Authenticate with Vanta API using OAuth 2.0 client credentials flow.
        
        Returns:
            str: Access token
        """
        token_url = f"{self.config['api_base_url']}/oauth/token"
        
        payload = {
            'grant_type': 'client_credentials',
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'scope': 'auditor-api.audit:read auditor-api.auditor:read'
        }
        
        try:
            response = requests.post(token_url, data=payload)
            response.raise_for_status()
            
            token_data = response.json()
            self.access_token = token_data['access_token']
            
            # Calculate token expiration (typically 1 hour)
            expires_in = token_data.get('expires_in', 3600)
            self.token_expires_at = datetime.now() + timedelta(seconds=expires_in)
            
            print(f"✓ Authenticated successfully. Token expires at {self.token_expires_at}")
            return self.access_token
            
        except requests.exceptions.RequestException as e:
            print(f"✗ Authentication failed: {e}")
            if hasattr(e.response, 'text'):
                print(f"  Response: {e.response.text}")
            raise
    
    def get_headers(self):
        """
        Get authorization headers for API requests.
        Automatically refreshes token if expired.
        
        Returns:
            dict: Headers including authorization token
        """
        # Refresh token if expired or doesn't exist
        if not self.access_token or (self.token_expires_at and datetime.now() >= self.token_expires_at):
            self.authenticate()
        
        return {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
    
    def test_connection(self):
        """Test API connection and credentials."""
        try:
            self.authenticate()
            print("✓ Connection test successful!")
            print(f"  Client ID: {self.client_id[:20]}...")
            print(f"  API Base URL: {self.config['api_base_url']}")
            return True
        except Exception as e:
            print(f"✗ Connection test failed: {e}")
            return False


def main():
    """Test authentication when run directly."""
    print("=" * 70)
    print("VANTA API AUTHENTICATION TEST")
    print("=" * 70)
    
    try:
        auth = VantaAuth()
        if auth.test_connection():
            print("\n✓ Ready to use Vanta API for audit evidence retrieval")
        else:
            print("\n✗ Authentication failed. Check your credentials in vanta_config.json")
    except Exception as e:
        print(f"\n✗ Error: {e}")


if __name__ == "__main__":
    main()

