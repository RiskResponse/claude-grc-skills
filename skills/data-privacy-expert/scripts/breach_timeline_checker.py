#!/usr/bin/env python3
"""
Data Breach Timeline Checker

Calculates important deadlines for data breach notifications under GDPR and CCPA,
and tracks breach response progress.

Usage:
    python3 breach_timeline_checker.py --breach-date "2025-10-30T14:30:00" --jurisdiction GDPR
    python3 breach_timeline_checker.py --breach-date "2025-10-30T14:30:00" --jurisdiction CCPA
    python3 breach_timeline_checker.py --breach-date "2025-10-30T14:30:00" --jurisdiction BOTH
    
    # Check status of existing breach
    python3 breach_timeline_checker.py --breach-id "BR-2025-001"
"""

import sys
import argparse
from datetime import datetime, timedelta
import json
from pathlib import Path


class BreachTimelineChecker:
    """Tracks breach notification deadlines and progress."""
    
    def __init__(self):
        self.breach_log_file = Path("breach_log.json")
        self.breaches = self.load_breaches()
    
    def load_breaches(self):
        """Load existing breach records."""
        if self.breach_log_file.exists():
            try:
                with open(self.breach_log_file, 'r') as f:
                    return json.load(f)
            except:
                return {}
        return {}
    
    def save_breaches(self):
        """Save breach records."""
        try:
            with open(self.breach_log_file, 'w') as f:
                json.dump(self.breaches, f, indent=2)
        except Exception as e:
            print(f"Warning: Could not save breach log: {e}")
    
    def calculate_gdpr_deadlines(self, breach_datetime):
        """Calculate GDPR breach notification deadlines."""
        # 72 hours for supervisory authority notification
        authority_deadline = breach_datetime + timedelta(hours=72)
        
        return {
            "authority_notification": {
                "deadline": authority_deadline,
                "requirement": "Notify supervisory authority within 72 hours (GDPR Article 33)",
                "status": "CRITICAL" if datetime.now() < authority_deadline else "OVERDUE",
                "hours_remaining": (authority_deadline - datetime.now()).total_seconds() / 3600,
            },
            "data_subject_notification": {
                "deadline": None,  # Without undue delay, context-dependent
                "requirement": "Notify data subjects without undue delay if high risk (GDPR Article 34)",
                "status": "ASSESS",
                "note": "Required only if breach likely to result in high risk to rights and freedoms",
            }
        }
    
    def calculate_ccpa_deadlines(self, breach_datetime):
        """Calculate CCPA breach notification deadlines."""
        # CCPA: "without unreasonable delay" - no specific timeline
        # Best practice: within 30-60 days
        suggested_deadline = breach_datetime + timedelta(days=30)
        
        return {
            "consumer_notification": {
                "deadline": suggested_deadline,
                "requirement": "Notify consumers without unreasonable delay (CCPA)",
                "status": "PENDING",
                "note": "No specific timeline, but should be prompt. Coordinate with law enforcement if needed.",
            },
            "attorney_general_notification": {
                "deadline": suggested_deadline,
                "requirement": "Notify CA Attorney General if 500+ residents affected",
                "status": "PENDING",
                "note": "Required if breach affects 500 or more California residents",
            }
        }
    
    def create_breach_record(self, breach_id, breach_datetime, jurisdiction, description=""):
        """Create new breach record."""
        deadlines = {}
        
        if jurisdiction in ["GDPR", "BOTH"]:
            deadlines["GDPR"] = self.calculate_gdpr_deadlines(breach_datetime)
        
        if jurisdiction in ["CCPA", "BOTH"]:
            deadlines["CCPA"] = self.calculate_ccpa_deadlines(breach_datetime)
        
        breach_record = {
            "breach_id": breach_id,
            "breach_datetime": breach_datetime.isoformat(),
            "detected_datetime": datetime.now().isoformat(),
            "jurisdiction": jurisdiction,
            "description": description,
            "deadlines": deadlines,
            "notifications_sent": [],
            "status": "ACTIVE",
        }
        
        self.breaches[breach_id] = breach_record
        self.save_breaches()
        
        return breach_record
    
    def print_timeline(self, breach_record):
        """Print breach timeline and deadlines."""
        print("\n" + "=" * 70)
        print("BREACH TIMELINE AND DEADLINES")
        print("=" * 70)
        print(f"Breach ID: {breach_record['breach_id']}")
        print(f"Breach Occurred: {breach_record['breach_datetime']}")
        print(f"Detected: {breach_record['detected_datetime']}")
        print(f"Jurisdiction: {breach_record['jurisdiction']}")
        
        if breach_record.get('description'):
            print(f"Description: {breach_record['description']}")
        
        print("\n" + "-" * 70)
        
        for jurisdiction, deadlines in breach_record['deadlines'].items():
            print(f"\n{jurisdiction} REQUIREMENTS:")
            print("-" * 70)
            
            for notification_type, details in deadlines.items():
                print(f"\n{notification_type.replace('_', ' ').title()}:")
                print(f"  Requirement: {details['requirement']}")
                
                if details['deadline']:
                    deadline_dt = datetime.fromisoformat(details['deadline']) if isinstance(details['deadline'], str) else details['deadline']
                    print(f"  Deadline: {deadline_dt.strftime('%Y-%m-%d %H:%M:%S')}")
                    
                    # Calculate time remaining
                    now = datetime.now()
                    if now < deadline_dt:
                        time_diff = deadline_dt - now
                        hours = time_diff.total_seconds() / 3600
                        if hours < 24:
                            print(f"  ⚠ Time Remaining: {hours:.1f} hours")
                        else:
                            days = hours / 24
                            print(f"  Time Remaining: {days:.1f} days")
                        
                        # Alert if critical deadline approaching
                        if jurisdiction == "GDPR" and notification_type == "authority_notification":
                            if hours < 24:
                                print(f"  🚨 CRITICAL: Less than 24 hours remaining!")
                            elif hours < 48:
                                print(f"  ⚠ WARNING: Less than 48 hours remaining!")
                    else:
                        print(f"  ❌ OVERDUE by {-time_diff.days} days")
                
                print(f"  Status: {details['status']}")
                
                if 'note' in details:
                    print(f"  Note: {details['note']}")
        
        # Show notifications sent
        if breach_record.get('notifications_sent'):
            print("\n" + "-" * 70)
            print("NOTIFICATIONS SENT:")
            for notification in breach_record['notifications_sent']:
                print(f"  - {notification['type']}: {notification['date']}")
        
        print("\n" + "=" * 70)
    
    def print_checklist(self, breach_record):
        """Print breach response checklist."""
        breach_dt = datetime.fromisoformat(breach_record['breach_datetime'])
        now = datetime.now()
        hours_elapsed = (now - breach_dt).total_seconds() / 3600
        
        print("\n" + "=" * 70)
        print("BREACH RESPONSE CHECKLIST")
        print("=" * 70)
        print(f"Time Since Breach: {hours_elapsed:.1f} hours ({hours_elapsed/24:.1f} days)")
        print()
        
        # Immediate response (0-24 hours)
        print("IMMEDIATE RESPONSE (0-24 hours):")
        print("  [ ] Detect and confirm breach")
        print("  [ ] Assign incident response team")
        print("  [ ] Create incident log")
        print("  [ ] Contain the breach (isolate systems, revoke access)")
        print("  [ ] Preserve evidence")
        print("  [ ] Preliminary assessment (what, when, how many)")
        print("  [ ] Notify key internal stakeholders")
        print("  [ ] Notify processor/controller (if applicable)")
        
        # Day 1-3
        print("\nINVESTIGATION (Day 1-3):")
        print("  [ ] Detailed forensic analysis")
        print("  [ ] Determine full scope of compromise")
        print("  [ ] Risk assessment")
        print("  [ ] Determine notification requirements")
        print("  [ ] Document findings")
        
        # Day 2-7 (GDPR: within 72 hours)
        print("\nNOTIFICATION PHASE:")
        
        if "GDPR" in breach_record['jurisdiction']:
            authority_deadline = datetime.fromisoformat(
                breach_record['deadlines']['GDPR']['authority_notification']['deadline']
            ) if isinstance(
                breach_record['deadlines']['GDPR']['authority_notification']['deadline'], str
            ) else breach_record['deadlines']['GDPR']['authority_notification']['deadline']
            
            if now < authority_deadline:
                hours_left = (authority_deadline - now).total_seconds() / 3600
                print(f"  [GDPR] Notify supervisory authority (⚠ {hours_left:.1f} hours remaining):")
            else:
                print(f"  [GDPR] Notify supervisory authority (❌ OVERDUE):")
            
            print("    [ ] Prepare notification with all required elements")
            print("    [ ] Submit via authority's designated method")
            print("    [ ] Document submission")
        
        if "GDPR" in breach_record['jurisdiction']:
            print("  [GDPR] Notify data subjects (if high risk):")
            print("    [ ] Assess if high risk to individuals")
            print("    [ ] Draft notification in clear language")
            print("    [ ] Send individual notifications")
            print("    [ ] Document notifications sent")
        
        if "CCPA" in breach_record['jurisdiction']:
            print("  [CCPA] Notify consumers:")
            print("    [ ] Prepare notification per CCPA requirements")
            print("    [ ] Send to affected California residents")
            print("    [ ] Notify CA Attorney General (if 500+ residents)")
            print("    [ ] Document notifications sent")
        
        print("\nOTHER NOTIFICATIONS:")
        print("  [ ] Law enforcement (if criminal activity)")
        print("  [ ] Credit reporting agencies (if large-scale)")
        print("  [ ] Insurance carrier")
        print("  [ ] Business partners/customers (per contracts)")
        
        print("\nREMEDIATION (Day 1-30):")
        print("  [ ] Fix vulnerability")
        print("  [ ] Apply security patches")
        print("  [ ] Reset compromised credentials")
        print("  [ ] Enhanced monitoring")
        print("  [ ] Deploy additional security controls")
        print("  [ ] Update policies and procedures")
        
        print("\nDOCUMENTATION:")
        print("  [ ] Incident log maintained")
        print("  [ ] All actions documented with timestamps")
        print("  [ ] Copies of all notifications saved")
        print("  [ ] Evidence preserved")
        print("  [ ] Costs tracked")
        
        print("\n" + "=" * 70)
    
    def mark_notification_sent(self, breach_id, notification_type, date=None):
        """Mark a notification as sent."""
        if breach_id not in self.breaches:
            print(f"Error: Breach {breach_id} not found")
            return False
        
        if date is None:
            date = datetime.now().isoformat()
        
        notification = {
            "type": notification_type,
            "date": date,
        }
        
        self.breaches[breach_id]['notifications_sent'].append(notification)
        self.save_breaches()
        print(f"✓ Marked '{notification_type}' notification as sent for breach {breach_id}")
        return True
    
    def list_active_breaches(self):
        """List all active breaches."""
        active = [b for b in self.breaches.values() if b.get('status') == 'ACTIVE']
        
        if not active:
            print("No active breaches recorded.")
            return
        
        print("\n" + "=" * 70)
        print("ACTIVE BREACHES")
        print("=" * 70)
        
        for breach in active:
            print(f"\nBreach ID: {breach['breach_id']}")
            print(f"Date: {breach['breach_datetime']}")
            print(f"Jurisdiction: {breach['jurisdiction']}")
            
            # Check for overdue notifications
            for jurisdiction, deadlines in breach['deadlines'].items():
                for notification_type, details in deadlines.items():
                    if details['deadline']:
                        deadline_dt = datetime.fromisoformat(details['deadline']) if isinstance(details['deadline'], str) else details['deadline']
                        if datetime.now() > deadline_dt:
                            print(f"  ❌ OVERDUE: {notification_type}")
                        elif (deadline_dt - datetime.now()).total_seconds() / 3600 < 24:
                            print(f"  ⚠ URGENT: {notification_type} due in < 24 hours")
            
            print("-" * 70)


def main():
    """Main function."""
    parser = argparse.ArgumentParser(
        description="Data Breach Timeline Checker - Track breach notification deadlines"
    )
    
    parser.add_argument('--breach-date', help='Date/time breach occurred (ISO format: YYYY-MM-DDTHH:MM:SS)')
    parser.add_argument('--jurisdiction', choices=['GDPR', 'CCPA', 'BOTH'], help='Applicable jurisdiction')
    parser.add_argument('--description', help='Brief description of breach')
    parser.add_argument('--breach-id', help='Check status of existing breach by ID')
    parser.add_argument('--list', action='store_true', help='List all active breaches')
    parser.add_argument('--mark-sent', help='Mark notification as sent (requires --breach-id and --notification-type)')
    parser.add_argument('--notification-type', help='Type of notification sent')
    
    args = parser.parse_args()
    
    checker = BreachTimelineChecker()
    
    # List active breaches
    if args.list:
        checker.list_active_breaches()
        return
    
    # Mark notification sent
    if args.mark_sent and args.breach_id and args.notification_type:
        checker.mark_notification_sent(args.breach_id, args.notification_type)
        return
    
    # Check existing breach
    if args.breach_id:
        if args.breach_id in checker.breaches:
            checker.print_timeline(checker.breaches[args.breach_id])
            checker.print_checklist(checker.breaches[args.breach_id])
        else:
            print(f"Error: Breach {args.breach_id} not found")
            print("\nAvailable breaches:")
            for bid in checker.breaches.keys():
                print(f"  - {bid}")
        return
    
    # Create new breach record
    if not args.breach_date or not args.jurisdiction:
        parser.print_help()
        print("\nExample usage:")
        print('  python3 breach_timeline_checker.py --breach-date "2025-10-30T14:30:00" --jurisdiction GDPR')
        sys.exit(1)
    
    try:
        breach_datetime = datetime.fromisoformat(args.breach_date)
    except ValueError:
        print(f"Error: Invalid date format: {args.breach_date}")
        print("Use ISO format: YYYY-MM-DDTHH:MM:SS")
        print("Example: 2025-10-30T14:30:00")
        sys.exit(1)
    
    # Generate breach ID
    breach_id = f"BR-{breach_datetime.strftime('%Y-%m-%d-%H%M')}"
    
    # Create breach record
    breach_record = checker.create_breach_record(
        breach_id,
        breach_datetime,
        args.jurisdiction,
        args.description or ""
    )
    
    print(f"\n✓ Created breach record: {breach_id}")
    
    # Display timeline and checklist
    checker.print_timeline(breach_record)
    checker.print_checklist(breach_record)
    
    print(f"\nTo check status later, run:")
    print(f"  python3 breach_timeline_checker.py --breach-id {breach_id}")


if __name__ == "__main__":
    main()

