#!/usr/bin/env python3
"""
Data Subject Request (DSR) Tracker

Tracks data subject rights requests (GDPR) and consumer rights requests (CCPA),
monitors deadlines, and generates compliance reports.

Usage:
    # Create new request
    python3 dsr_tracker.py --add --type access --email user@example.com --regulation GDPR
    
    # List all requests
    python3 dsr_tracker.py --list
    
    # List only pending requests
    python3 dsr_tracker.py --list --status pending
    
    # Update request status
    python3 dsr_tracker.py --update DSR-2025-001 --status completed
    
    # Check overdue requests
    python3 dsr_tracker.py --check-overdue
    
    # Generate compliance report
    python3 dsr_tracker.py --report monthly
"""

import sys
import argparse
import json
from datetime import datetime, timedelta
from pathlib import Path
from collections import defaultdict


class DSRTracker:
    """Track and manage data subject/consumer rights requests."""
    
    REQUEST_TYPES = [
        'access', 'delete', 'rectification', 'correction', 'portability',
        'restriction', 'object', 'opt-out', 'limit-use', 'automated-decision'
    ]
    
    REQUEST_STATUSES = [
        'pending', 'in_progress', 'verification_needed', 'completed',
        'denied', 'extended', 'cancelled'
    ]
    
    def __init__(self, data_file='dsr_tracker.json'):
        self.data_file = Path(data_file)
        self.requests = self.load_requests()
    
    def load_requests(self):
        """Load existing requests from file."""
        if self.data_file.exists():
            try:
                with open(self.data_file, 'r') as f:
                    return json.load(f)
            except:
                return {}
        return {}
    
    def save_requests(self):
        """Save requests to file."""
        try:
            with open(self.data_file, 'w') as f:
                json.dump(self.requests, f, indent=2)
            return True
        except Exception as e:
            print(f"Error: Could not save requests: {e}")
            return False
    
    def generate_request_id(self):
        """Generate unique request ID."""
        today = datetime.now()
        date_str = today.strftime('%Y-%m')
        
        # Count requests from this month
        count = sum(1 for r in self.requests.values() 
                   if r['request_id'].startswith(f'DSR-{date_str}'))
        
        return f"DSR-{date_str}-{count + 1:03d}"
    
    def calculate_deadline(self, received_date, regulation, extended=False):
        """Calculate response deadline based on regulation."""
        received_dt = datetime.fromisoformat(received_date)
        
        if regulation == 'GDPR':
            days = 30 if not extended else 90  # 30 days + 60 day extension
        elif regulation == 'CCPA':
            days = 45 if not extended else 90  # 45 days + 45 day extension
        else:
            days = 30  # Default
        
        deadline = received_dt + timedelta(days=days)
        return deadline.isoformat()
    
    def add_request(self, request_type, email, regulation, name='', description='', 
                    received_date=None):
        """Add new data subject request."""
        if request_type not in self.REQUEST_TYPES:
            print(f"Error: Invalid request type. Must be one of: {', '.join(self.REQUEST_TYPES)}")
            return None
        
        if regulation not in ['GDPR', 'CCPA']:
            print("Error: Regulation must be GDPR or CCPA")
            return None
        
        request_id = self.generate_request_id()
        received_date = received_date or datetime.now().isoformat()
        deadline = self.calculate_deadline(received_date, regulation)
        
        request = {
            'request_id': request_id,
            'type': request_type,
            'email': email,
            'name': name,
            'regulation': regulation,
            'description': description,
            'received_date': received_date,
            'deadline': deadline,
            'extended': False,
            'status': 'pending',
            'verification_status': 'not_verified',
            'notes': [],
            'history': [
                {
                    'date': datetime.now().isoformat(),
                    'action': 'created',
                    'user': 'system',
                }
            ]
        }
        
        self.requests[request_id] = request
        self.save_requests()
        
        print(f"\n✓ Created new request: {request_id}")
        print(f"  Type: {request_type}")
        print(f"  Email: {email}")
        print(f"  Regulation: {regulation}")
        print(f"  Received: {received_date}")
        print(f"  Deadline: {deadline}")
        print(f"  Days to respond: {self.calculate_days_remaining(deadline)}")
        
        return request_id
    
    def update_request(self, request_id, status=None, extended=None, note=None):
        """Update request status or add notes."""
        if request_id not in self.requests:
            print(f"Error: Request {request_id} not found")
            return False
        
        request = self.requests[request_id]
        
        if status:
            if status not in self.REQUEST_STATUSES:
                print(f"Error: Invalid status. Must be one of: {', '.join(self.REQUEST_STATUSES)}")
                return False
            
            request['status'] = status
            request['history'].append({
                'date': datetime.now().isoformat(),
                'action': f'status_changed_to_{status}',
                'user': 'system',
            })
            
            if status == 'completed':
                request['completed_date'] = datetime.now().isoformat()
            
            print(f"✓ Updated status to: {status}")
        
        if extended is not None:
            request['extended'] = extended
            if extended:
                # Recalculate deadline
                request['deadline'] = self.calculate_deadline(
                    request['received_date'], 
                    request['regulation'], 
                    extended=True
                )
                request['history'].append({
                    'date': datetime.now().isoformat(),
                    'action': 'deadline_extended',
                    'user': 'system',
                })
                print(f"✓ Deadline extended to: {request['deadline']}")
        
        if note:
            request['notes'].append({
                'date': datetime.now().isoformat(),
                'note': note,
            })
            print(f"✓ Added note")
        
        self.save_requests()
        return True
    
    def calculate_days_remaining(self, deadline):
        """Calculate days remaining until deadline."""
        deadline_dt = datetime.fromisoformat(deadline)
        now = datetime.now()
        diff = (deadline_dt - now).days
        return diff
    
    def list_requests(self, status_filter=None, regulation_filter=None):
        """List all requests with optional filtering."""
        requests = list(self.requests.values())
        
        if status_filter:
            requests = [r for r in requests if r['status'] == status_filter]
        
        if regulation_filter:
            requests = [r for r in requests if r['regulation'] == regulation_filter]
        
        if not requests:
            print("No requests found matching criteria.")
            return
        
        # Sort by deadline
        requests.sort(key=lambda r: r['deadline'])
        
        print("\n" + "=" * 80)
        print("DATA SUBJECT REQUESTS")
        print("=" * 80)
        print(f"Total: {len(requests)} requests")
        print()
        
        for request in requests:
            days_remaining = self.calculate_days_remaining(request['deadline'])
            
            # Status indicator
            if request['status'] == 'completed':
                indicator = "✓"
            elif days_remaining < 0:
                indicator = "❌ OVERDUE"
            elif days_remaining <= 5:
                indicator = "⚠ URGENT"
            else:
                indicator = "•"
            
            print(f"{indicator} {request['request_id']}")
            print(f"   Type: {request['type']} | Regulation: {request['regulation']}")
            print(f"   Email: {request['email']}")
            if request.get('name'):
                print(f"   Name: {request['name']}")
            print(f"   Status: {request['status']}")
            print(f"   Received: {request['received_date']}")
            print(f"   Deadline: {request['deadline']}")
            
            if days_remaining >= 0:
                print(f"   Days Remaining: {days_remaining}")
            else:
                print(f"   OVERDUE by: {abs(days_remaining)} days")
            
            if request['extended']:
                print(f"   ⏰ Extended deadline")
            
            if request.get('notes'):
                print(f"   Notes: {len(request['notes'])} note(s)")
            
            print()
    
    def check_overdue(self):
        """Check for overdue requests."""
        now = datetime.now()
        overdue = []
        urgent = []
        
        for request in self.requests.values():
            if request['status'] in ['completed', 'cancelled', 'denied']:
                continue
            
            deadline_dt = datetime.fromisoformat(request['deadline'])
            days_remaining = (deadline_dt - now).days
            
            if days_remaining < 0:
                overdue.append((request, abs(days_remaining)))
            elif days_remaining <= 5:
                urgent.append((request, days_remaining))
        
        if not overdue and not urgent:
            print("\n✓ No overdue or urgent requests")
            return
        
        if overdue:
            print("\n" + "=" * 80)
            print(f"❌ OVERDUE REQUESTS ({len(overdue)})")
            print("=" * 80)
            for request, days_overdue in sorted(overdue, key=lambda x: x[1], reverse=True):
                print(f"\n{request['request_id']} - OVERDUE by {days_overdue} days")
                print(f"  Type: {request['type']}")
                print(f"  Email: {request['email']}")
                print(f"  Deadline was: {request['deadline']}")
                print(f"  Regulation: {request['regulation']}")
        
        if urgent:
            print("\n" + "=" * 80)
            print(f"⚠ URGENT REQUESTS ({len(urgent)}) - Due within 5 days")
            print("=" * 80)
            for request, days_left in sorted(urgent, key=lambda x: x[1]):
                print(f"\n{request['request_id']} - {days_left} days remaining")
                print(f"  Type: {request['type']}")
                print(f"  Email: {request['email']}")
                print(f"  Deadline: {request['deadline']}")
                print(f"  Regulation: {request['regulation']}")
    
    def generate_report(self, period='monthly'):
        """Generate compliance report."""
        now = datetime.now()
        
        if period == 'monthly':
            start_date = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
            period_name = start_date.strftime('%B %Y')
        elif period == 'quarterly':
            quarter = (now.month - 1) // 3
            start_date = now.replace(month=quarter * 3 + 1, day=1, hour=0, minute=0, second=0, microsecond=0)
            period_name = f"Q{quarter + 1} {now.year}"
        else:  # yearly
            start_date = now.replace(month=1, day=1, hour=0, minute=0, second=0, microsecond=0)
            period_name = str(now.year)
        
        # Filter requests by period
        period_requests = [
            r for r in self.requests.values()
            if datetime.fromisoformat(r['received_date']) >= start_date
        ]
        
        if not period_requests:
            print(f"\nNo requests for {period_name}")
            return
        
        print("\n" + "=" * 80)
        print(f"DATA SUBJECT REQUEST COMPLIANCE REPORT - {period_name}")
        print("=" * 80)
        
        # Statistics by type
        by_type = defaultdict(int)
        by_regulation = defaultdict(int)
        by_status = defaultdict(int)
        
        completed_on_time = 0
        completed_late = 0
        extended_requests = 0
        denied_requests = 0
        
        for request in period_requests:
            by_type[request['type']] += 1
            by_regulation[request['regulation']] += 1
            by_status[request['status']] += 1
            
            if request['extended']:
                extended_requests += 1
            
            if request['status'] == 'completed':
                completed_date = datetime.fromisoformat(request['completed_date'])
                deadline_date = datetime.fromisoformat(request['deadline'])
                if completed_date <= deadline_date:
                    completed_on_time += 1
                else:
                    completed_late += 1
            elif request['status'] == 'denied':
                denied_requests += 1
        
        # Summary
        print(f"\nTOTAL REQUESTS: {len(period_requests)}")
        print("-" * 80)
        
        print(f"\nBY TYPE:")
        for req_type, count in sorted(by_type.items()):
            pct = (count / len(period_requests)) * 100
            print(f"  {req_type:20} {count:3} ({pct:5.1f}%)")
        
        print(f"\nBY REGULATION:")
        for regulation, count in sorted(by_regulation.items()):
            pct = (count / len(period_requests)) * 100
            print(f"  {regulation:20} {count:3} ({pct:5.1f}%)")
        
        print(f"\nBY STATUS:")
        for status, count in sorted(by_status.items()):
            pct = (count / len(period_requests)) * 100
            print(f"  {status:20} {count:3} ({pct:5.1f}%)")
        
        print(f"\nCOMPLIANCE METRICS:")
        print("-" * 80)
        total_completed = completed_on_time + completed_late
        if total_completed > 0:
            on_time_pct = (completed_on_time / total_completed) * 100
            print(f"Completed on time:    {completed_on_time:3} / {total_completed:3} ({on_time_pct:5.1f}%)")
            print(f"Completed late:       {completed_late:3} / {total_completed:3} ({100-on_time_pct:5.1f}%)")
        
        print(f"Deadline extensions:  {extended_requests:3}")
        print(f"Denied requests:      {denied_requests:3}")
        
        # Current status
        pending = by_status.get('pending', 0) + by_status.get('in_progress', 0)
        if pending > 0:
            print(f"\nCURRENT PENDING:      {pending:3}")
        
        # Overdue check
        now = datetime.now()
        overdue_count = sum(1 for r in period_requests 
                           if r['status'] not in ['completed', 'cancelled', 'denied']
                           and datetime.fromisoformat(r['deadline']) < now)
        if overdue_count > 0:
            print(f"⚠ OVERDUE REQUESTS:  {overdue_count:3}")
        
        print("\n" + "=" * 80)


def main():
    """Main function."""
    parser = argparse.ArgumentParser(
        description="Data Subject Request (DSR) Tracker"
    )
    
    # Actions
    parser.add_argument('--add', action='store_true', help='Add new request')
    parser.add_argument('--list', action='store_true', help='List all requests')
    parser.add_argument('--update', metavar='REQUEST_ID', help='Update request')
    parser.add_argument('--check-overdue', action='store_true', help='Check for overdue requests')
    parser.add_argument('--report', choices=['monthly', 'quarterly', 'yearly'], help='Generate report')
    
    # Request details (for --add)
    parser.add_argument('--type', choices=DSRTracker.REQUEST_TYPES, help='Request type')
    parser.add_argument('--email', help='Data subject email')
    parser.add_argument('--name', help='Data subject name')
    parser.add_argument('--regulation', choices=['GDPR', 'CCPA'], help='Applicable regulation')
    parser.add_argument('--description', help='Request description')
    parser.add_argument('--received-date', help='Date received (ISO format)')
    
    # Update options (for --update)
    parser.add_argument('--status', choices=DSRTracker.REQUEST_STATUSES, help='New status')
    parser.add_argument('--extend-deadline', action='store_true', help='Extend deadline')
    parser.add_argument('--note', help='Add note to request')
    
    # List filters
    parser.add_argument('--status-filter', choices=DSRTracker.REQUEST_STATUSES, help='Filter by status')
    parser.add_argument('--regulation-filter', choices=['GDPR', 'CCPA'], help='Filter by regulation')
    
    args = parser.parse_args()
    
    tracker = DSRTracker()
    
    # Add new request
    if args.add:
        if not all([args.type, args.email, args.regulation]):
            print("Error: --add requires --type, --email, and --regulation")
            parser.print_help()
            sys.exit(1)
        
        tracker.add_request(
            args.type,
            args.email,
            args.regulation,
            name=args.name or '',
            description=args.description or '',
            received_date=args.received_date
        )
        return
    
    # Update request
    if args.update:
        tracker.update_request(
            args.update,
            status=args.status,
            extended=args.extend_deadline if args.extend_deadline else None,
            note=args.note
        )
        return
    
    # List requests
    if args.list:
        tracker.list_requests(
            status_filter=args.status_filter,
            regulation_filter=args.regulation_filter
        )
        return
    
    # Check overdue
    if args.check_overdue:
        tracker.check_overdue()
        return
    
    # Generate report
    if args.report:
        tracker.generate_report(period=args.report)
        return
    
    # No action specified
    parser.print_help()
    print("\nCommon commands:")
    print("  # Add new request")
    print('  python3 dsr_tracker.py --add --type access --email user@example.com --regulation GDPR')
    print("\n  # List all pending requests")
    print('  python3 dsr_tracker.py --list --status-filter pending')
    print("\n  # Update request status")
    print('  python3 dsr_tracker.py --update DSR-2025-10-001 --status completed')
    print("\n  # Check for overdue requests")
    print('  python3 dsr_tracker.py --check-overdue')
    print("\n  # Generate monthly report")
    print('  python3 dsr_tracker.py --report monthly')


if __name__ == "__main__":
    main()

