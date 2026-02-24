#!/usr/bin/env python3
"""
SOC 2 System Description Version Comparison

Compares two versions of a system description to identify changes.
Useful for annual updates to track what changed year-over-year.

Usage:
    python3 version_comparison.py old_description.md new_description.md
    python3 version_comparison.py old.md new.md --output changes_report.txt
"""

import sys
import re
import difflib
import argparse
from pathlib import Path
from datetime import datetime


class VersionComparator:
    """Compare two versions of system description."""
    
    def __init__(self, old_file, new_file):
        self.old_file = Path(old_file)
        self.new_file = Path(new_file)
        self.old_content = ""
        self.new_content = ""
        self.changes = []
        
    def load_files(self):
        """Load both files."""
        try:
            with open(self.old_file, 'r', encoding='utf-8') as f:
                self.old_content = f.read()
            with open(self.new_file, 'r', encoding='utf-8') as f:
                self.new_content = f.read()
            return True
        except FileNotFoundError as e:
            print(f"Error: File not found: {e.filename}")
            return False
        except Exception as e:
            print(f"Error reading files: {e}")
            return False
    
    def compare(self):
        """Compare the two files and identify changes."""
        old_lines = self.old_content.splitlines()
        new_lines = self.new_content.splitlines()
        
        # Use difflib to find differences
        diff = difflib.unified_diff(
            old_lines,
            new_lines,
            fromfile=str(self.old_file),
            tofile=str(self.new_file),
            lineterm=''
        )
        
        diff_lines = list(diff)
        
        # Analyze differences
        additions = len([l for l in diff_lines if l.startswith('+')])
        deletions = len([l for l in diff_lines if l.startswith('-')])
        
        return diff_lines, additions, deletions
    
    def identify_significant_changes(self):
        """Identify significant changes like control modifications."""
        significant = []
        
        # Look for control-related changes
        old_controls = re.findall(r'Control\s+(?:ID:\s*)?(\S+)', self.old_content, re.IGNORECASE)
        new_controls = re.findall(r'Control\s+(?:ID:\s*)?(\S+)', self.new_content, re.IGNORECASE)
        
        added_controls = set(new_controls) - set(old_controls)
        removed_controls = set(old_controls) - set(new_controls)
        
        if added_controls:
            significant.append(f"Added Controls ({len(added_controls)}): {', '.join(list(added_controls)[:10])}")
        if removed_controls:
            significant.append(f"Removed Controls ({len(removed_controls)}): {', '.join(list(removed_controls)[:10])}")
        
        # Look for infrastructure changes
        if 'infrastructure' in self.new_content.lower():
            # Check for cloud provider changes
            old_providers = re.findall(r'(AWS|Azure|GCP|Google Cloud)', self.old_content)
            new_providers = re.findall(r'(AWS|Azure|GCP|Google Cloud)', self.new_content)
            if set(old_providers) != set(new_providers):
                significant.append(f"Cloud Provider Change: {set(old_providers)} -> {set(new_providers)}")
        
        return significant
    
    def generate_report(self, diff_lines, additions, deletions, significant):
        """Generate comparison report."""
        report = []
        report.append("=" * 70)
        report.append("SOC 2 SYSTEM DESCRIPTION VERSION COMPARISON")
        report.append("=" * 70)
        report.append(f"Old Version: {self.old_file}")
        report.append(f"New Version: {self.new_file}")
        report.append(f"Comparison Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append("")
        
        report.append("SUMMARY")
        report.append("-" * 70)
        report.append(f"Lines Added: {additions}")
        report.append(f"Lines Deleted: {deletions}")
        report.append(f"Net Change: {additions - deletions} lines")
        
        if significant:
            report.append("\nSIGNIFICANT CHANGES DETECTED")
            report.append("-" * 70)
            for change in significant:
                report.append(f"  - {change}")
        
        if additions == 0 and deletions == 0:
            report.append("\n✓ No changes detected between versions")
        else:
            report.append(f"\n⚠ {additions + deletions} total line changes detected")
        
        # Include unified diff
        if diff_lines:
            report.append("\n\nDETAILED CHANGES (UNIFIED DIFF)")
            report.append("=" * 70)
            report.extend(diff_lines[:200])  # Limit to first 200 lines
            if len(diff_lines) > 200:
                report.append(f"\n... (showing first 200 of {len(diff_lines)} diff lines)")
        
        report.append("\n" + "=" * 70)
        
        return "\n".join(report)
    
    def compare_and_report(self, save_report=None):
        """Execute comparison and generate report."""
        print("=" * 70)
        print("SOC 2 VERSION COMPARISON")
        print("=" * 70)
        print(f"Old: {self.old_file}")
        print(f"New: {self.new_file}")
        print()
        
        if not self.load_files():
            return False
        
        diff_lines, additions, deletions = self.compare()
        significant = self.identify_significant_changes()
        
        report = self.generate_report(diff_lines, additions, deletions, significant)
        print(report)
        
        if save_report:
            try:
                with open(save_report, 'w', encoding='utf-8') as f:
                    f.write(report)
                print(f"\n✓ Report saved to: {save_report}")
            except Exception as e:
                print(f"\n✗ Could not save report: {e}")
        
        return True


def main():
    """Main function."""
    parser = argparse.ArgumentParser(
        description="Compare two versions of SOC 2 system description"
    )
    parser.add_argument('old_file', help='Previous version of system description')
    parser.add_argument('new_file', help='Current version of system description')
    parser.add_argument('--output-report', help='Save comparison report to file')
    
    args = parser.parse_args()
    
    comparator = VersionComparator(args.old_file, args.new_file)
    success = comparator.compare_and_report(save_report=args.output_report)
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()

