#!/usr/bin/env python3
"""
SOC 2 Control Coverage Validator

Validates that a SOC 2 system description adequately covers all
Trust Service Criteria points for Security and Availability.

Usage:
    python3 control_coverage_validator.py system_description.md
    python3 control_coverage_validator.py system_description.md --criteria both
    python3 control_coverage_validator.py system_description.md --criteria security
    python3 control_coverage_validator.py system_description.md --criteria availability
"""

import sys
import re
import argparse
from pathlib import Path


class ControlCoverageValidator:
    """Validates TSC control coverage."""
    
    # Security Common Criteria points
    SECURITY_CC_POINTS = [
        "CC1.1", "CC1.2", "CC1.3", "CC1.4", "CC1.5",
        "CC2.1", "CC2.2", "CC2.3",
        "CC3.1", "CC3.2", "CC3.3", "CC3.4",
        "CC4.1", "CC4.2",
        "CC5.1", "CC5.2", "CC5.3",
        "CC6.1", "CC6.2", "CC6.3", "CC6.4", "CC6.5", "CC6.6", "CC6.7", "CC6.8",
        "CC7.1", "CC7.2", "CC7.3", "CC7.4", "CC7.5",
        "CC8.1", "CC8.2", "CC8.3",
        "CC9.1", "CC9.2",
    ]
    
    # Availability criteria points
    AVAILABILITY_POINTS = [
        "A1.1", "A1.2", "A1.3",
    ]
    
    CC_DESCRIPTIONS = {
        "CC1": "Control Environment",
        "CC2": "Communication and Information",
        "CC3": "Risk Assessment",
        "CC4": "Monitoring Activities",
        "CC5": "Control Activities",
        "CC6": "Logical and Physical Access Controls",
        "CC7": "System Operations",
        "CC8": "Change Management",
        "CC9": "Risk Mitigation",
    }
    
    AVAILABILITY_DESCRIPTIONS = {
        "A1.1": "Processing Capacity and Monitoring",
        "A1.2": "Environmental Protections and Backup",
        "A1.3": "Recovery and Continuity",
    }
    
    def __init__(self, file_path):
        self.file_path = Path(file_path)
        self.content = ""
        self.coverage_results = {}
        
    def load_file(self):
        """Load system description."""
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                self.content = f.read()
            return True
        except:
            return False
    
    def check_point_coverage(self, point):
        """Check if a TSC point is mentioned in the description."""
        # Look for the point mentioned
        pattern = re.escape(point)
        if re.search(pattern, self.content):
            return True
        return False
    
    def validate_security_coverage(self):
        """Validate Security (CC) coverage."""
        print("\n" + "=" * 70)
        print("SECURITY COMMON CRITERIA COVERAGE")
        print("=" * 70)
        
        covered = []
        missing = []
        
        current_cc = None
        for point in self.SECURITY_CC_POINTS:
            cc_prefix = point[:3]  # e.g., "CC1"
            
            # Print header for each CC section
            if cc_prefix != current_cc:
                current_cc = cc_prefix
                print(f"\n{cc_prefix}: {self.CC_DESCRIPTIONS.get(cc_prefix, '')}")
            
            if self.check_point_coverage(point):
                print(f"  ✓ {point}")
                covered.append(point)
            else:
                print(f"  ✗ {point} - NOT DOCUMENTED")
                missing.append(point)
        
        total = len(self.SECURITY_CC_POINTS)
        coverage_pct = (len(covered) / total) * 100
        
        print(f"\n{'-' * 70}")
        print(f"Coverage: {len(covered)} / {total} ({coverage_pct:.1f}%)")
        
        self.coverage_results['security'] = {
            'total': total,
            'covered': len(covered),
            'missing': missing,
            'percentage': coverage_pct
        }
        
        return len(missing) == 0
    
    def validate_availability_coverage(self):
        """Validate Availability criteria coverage."""
        print("\n" + "=" * 70)
        print("AVAILABILITY CRITERIA COVERAGE")
        print("=" * 70)
        
        # Check if Availability is even in scope
        if not re.search(r'availability', self.content, re.IGNORECASE):
            print("ℹ Availability not detected in document")
            print("  (Skip this check if Availability not in scope)")
            return True
        
        covered = []
        missing = []
        
        for point in self.AVAILABILITY_POINTS:
            desc = self.AVAILABILITY_DESCRIPTIONS.get(point, '')
            if self.check_point_coverage(point):
                print(f"✓ {point}: {desc}")
                covered.append(point)
            else:
                print(f"✗ {point}: {desc} - NOT DOCUMENTED")
                missing.append(point)
        
        total = len(self.AVAILABILITY_POINTS)
        coverage_pct = (len(covered) / total) * 100 if total > 0 else 0
        
        print(f"\n{'-' * 70}")
        print(f"Coverage: {len(covered)} / {total} ({coverage_pct:.1f}%)")
        
        self.coverage_results['availability'] = {
            'total': total,
            'covered': len(covered),
            'missing': missing,
            'percentage': coverage_pct
        }
        
        return len(missing) == 0
    
    def print_summary(self):
        """Print overall summary."""
        print("\n" + "=" * 70)
        print("OVERALL COVERAGE SUMMARY")
        print("=" * 70)
        
        total_points = 0
        total_covered = 0
        
        for criteria, results in self.coverage_results.items():
            total_points += results['total']
            total_covered += results['covered']
            print(f"{criteria.upper():20} {results['covered']:3} / {results['total']:3} ({results['percentage']:5.1f}%)")
        
        if total_points > 0:
            overall_pct = (total_covered / total_points) * 100
            print(f"{'TOTAL':20} {total_covered:3} / {total_points:3} ({overall_pct:5.1f}%)")
            
            print(f"\n{'-' * 70}")
            if overall_pct == 100:
                print("✓ COMPLETE COVERAGE - All TSC points documented")
            elif overall_pct >= 90:
                print("⚠ MOSTLY COMPLETE - Review missing points")
            elif overall_pct >= 75:
                print("⚠ PARTIAL COVERAGE - Significant gaps remain")
            else:
                print("✗ INCOMPLETE - Major gaps in TSC coverage")
        
        # List all missing points
        all_missing = []
        for results in self.coverage_results.values():
            all_missing.extend(results['missing'])
        
        if all_missing:
            print(f"\n{'-' * 70}")
            print(f"MISSING TSC POINTS ({len(all_missing)}):")
            for point in all_missing:
                print(f"  - {point}")
            print("\nRefer to references/tsc_security_criteria.md and")
            print("tsc_availability_criteria.md for requirements.")


def main():
    """Main function."""
    parser = argparse.ArgumentParser(
        description="SOC 2 Control Coverage Validator"
    )
    parser.add_argument('file', help='System description file to validate')
    parser.add_argument('--criteria', choices=['security', 'availability', 'both'], 
                       default='both', help='Which criteria to validate (default: both)')
    parser.add_argument('--output-report', help='Save report to file')
    
    args = parser.parse_args()
    
    validator = ControlCoverageValidator(args.file)
    
    if not validator.load_file():
        print(f"Error: Could not load file: {args.file}")
        sys.exit(1)
    
    print(f"Validating TSC Coverage: {args.file}")
    
    all_pass = True
    
    if args.criteria in ['security', 'both']:
        if not validator.validate_security_coverage():
            all_pass = False
    
    if args.criteria in ['availability', 'both']:
        if not validator.validate_availability_coverage():
            all_pass = False
    
    validator.print_summary()
    
    sys.exit(0 if all_pass else 1)


if __name__ == "__main__":
    main()

