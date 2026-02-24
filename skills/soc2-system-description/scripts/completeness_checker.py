#!/usr/bin/env python3
"""
SOC 2 System Description Completeness Checker

Validates that a SOC 2 system description includes all required sections
and components per AICPA standards.

Usage:
    python3 completeness_checker.py system_description.md
    python3 completeness_checker.py system_description.md --output-report report.txt
"""

import sys
import re
from pathlib import Path
from datetime import datetime


class CompletenessChecker:
    """Validates SOC 2 system description completeness."""
    
    # Required sections per AICPA
    REQUIRED_SECTIONS = [
        ("Section 1: Overview", r"(section\s*1|overview of.*system)"),
        ("Section 2: System Components", r"(section\s*2|system components)"),
        ("Section 3: Boundaries", r"(section\s*3|boundaries)"),
        ("Section 4: Service Commitments", r"(section\s*4|service commitments|system requirements)"),
        ("Section 5: Control Environment", r"(section\s*5|control environment|control objectives)"),
    ]
    
    # Required components in Section 2
    SECTION_2_COMPONENTS = [
        ("Infrastructure", r"infrastructure"),
        ("Software", r"software"),
        ("People", r"people|personnel|staff|organizational|roles"),
        ("Procedures", r"procedures|processes"),
        ("Data", r"data|information"),
    ]
    
    # Important elements to check
    IMPORTANT_ELEMENTS = [
        ("Examination period", r"examination period"),
        ("Description date", r"(description as of|as of date)"),
        ("Trust Service Criteria specified", r"(trust service|security|availability|confidentiality)"),
        ("Organizational chart or structure", r"(organizational chart|organizational structure)"),
        ("System boundaries defined", r"(system boundaries|in-scope|out-of-scope)"),
        ("SLA or commitments", r"(SLA|service level|availability.*commitment|uptime)"),
        ("Third-party services", r"(third-party|vendors|service providers)"),
    ]
    
    # Common placeholders that should be filled
    PLACEHOLDER_PATTERNS = [
        r'\[INSERT[^\]]*\]',
        r'\[COMPANY[^\]]*\]',
        r'\[FILL[^\]]*\]',
        r'\[TODO[^\]]*\]',
        r'\[SPECIFY[^\]]*\]',
        r'\[DESCRIBE[^\]]*\]',
        r'\[LIST[^\]]*\]',
        r'{{[^}]*}}',  # New format: {{PLACEHOLDER}}
    ]
    
    def __init__(self, file_path):
        self.file_path = Path(file_path)
        self.content = ""
        self.findings = []
        self.warnings = []
        self.missing = []
        
    def load_file(self):
        """Load system description file."""
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                self.content = f.read()
            return True
        except FileNotFoundError:
            print(f"ERROR: File not found: {self.file_path}")
            return False
        except Exception as e:
            print(f"ERROR: Could not read file: {e}")
            return False
    
    def check_sections(self):
        """Check for required sections."""
        print("\n=== Required Sections (AICPA) ===")
        
        for section_name, pattern in self.REQUIRED_SECTIONS:
            if re.search(pattern, self.content, re.IGNORECASE):
                print(f"✓ {section_name}")
                self.findings.append(f"PASS: {section_name}")
            else:
                print(f"✗ {section_name} - MISSING")
                self.findings.append(f"FAIL: {section_name} - Required by AICPA")
                self.missing.append(section_name)
        
        return len(self.missing) == 0
    
    def check_section_2_components(self):
        """Check that Section 2 includes all five required components."""
        print("\n=== Section 2 Components ===")
        
        for component_name, pattern in self.SECTION_2_COMPONENTS:
            if re.search(pattern, self.content, re.IGNORECASE):
                print(f"✓ {component_name}")
                self.findings.append(f"PASS: Section 2 includes {component_name}")
            else:
                print(f"✗ {component_name} - MISSING from Section 2")
                self.findings.append(f"FAIL: {component_name} - Required in Section 2")
                self.missing.append(f"Section 2: {component_name}")
        
        return len([m for m in self.missing if m.startswith("Section 2")]) == 0
    
    def check_important_elements(self):
        """Check for important elements."""
        print("\n=== Important Elements ===")
        
        for element_name, pattern in self.IMPORTANT_ELEMENTS:
            if re.search(pattern, self.content, re.IGNORECASE):
                print(f"✓ {element_name}")
                self.findings.append(f"PASS: {element_name}")
            else:
                print(f"⚠ {element_name} - Consider adding")
                self.warnings.append(f"WARNING: {element_name} - Recommended")
    
    def check_placeholders(self):
        """Check for unfilled placeholders."""
        print("\n=== Placeholder Check ===")
        
        unfilled = []
        for pattern in self.PLACEHOLDER_PATTERNS:
            matches = re.findall(pattern, self.content, re.IGNORECASE)
            unfilled.extend(matches)
        
        if unfilled:
            print(f"⚠ Found {len(unfilled)} unfilled placeholders")
            unique_placeholders = set(unfilled)
            for placeholder in list(unique_placeholders)[:10]:  # Show first 10
                print(f"  - {placeholder}")
            if len(unique_placeholders) > 10:
                print(f"  ... and {len(unique_placeholders) - 10} more")
            self.warnings.append(f"WARNING: {len(unfilled)} unfilled placeholders found")
        else:
            print("✓ No unfilled placeholders detected")
            self.findings.append("PASS: No placeholders remaining")
    
    def estimate_completeness(self):
        """Estimate overall completeness percentage."""
        print("\n=== Document Analysis ===")
        
        # Count sections, controls, etc.
        word_count = len(self.content.split())
        print(f"Document size: {word_count} words")
        
        # Typical system description is 15-40 pages, roughly 5,000-15,000 words
        if word_count < 3000:
            print("⚠ Document may be too brief (typical: 5,000-15,000 words)")
            self.warnings.append("WARNING: Document may lack sufficient detail")
        elif word_count > 20000:
            print("⚠ Document may be overly detailed")
        else:
            print("✓ Document length appropriate")
        
        # Check for controls
        control_matches = re.findall(r'\bcontrol\b', self.content, re.IGNORECASE)
        print(f"'Control' mentioned: {len(control_matches)} times")
        
        if len(control_matches) < 20:
            print("⚠ May need more control documentation")
            self.warnings.append("WARNING: Limited control documentation detected")
    
    def generate_report(self):
        """Generate completeness report."""
        report = []
        report.append("=" * 70)
        report.append("SOC 2 SYSTEM DESCRIPTION COMPLETENESS REPORT")
        report.append("=" * 70)
        report.append(f"File: {self.file_path}")
        report.append(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append("")
        
        # Summary
        required_items = len(self.REQUIRED_SECTIONS) + len(self.SECTION_2_COMPONENTS)
        missing_items = len(self.missing)
        completeness_pct = ((required_items - missing_items) / required_items) * 100
        
        report.append("SUMMARY")
        report.append("-" * 70)
        report.append(f"Required Sections: {len(self.REQUIRED_SECTIONS)}")
        report.append(f"Required Section 2 Components: {len(self.SECTION_2_COMPONENTS)}")
        report.append(f"Missing Items: {missing_items}")
        report.append(f"Completeness: {completeness_pct:.1f}%")
        report.append(f"Warnings: {len(self.warnings)}")
        
        if missing_items == 0:
            report.append("\n✓ ALL REQUIRED SECTIONS PRESENT")
        else:
            report.append(f"\n✗ INCOMPLETE - {missing_items} required items missing")
        
        # Missing items
        if self.missing:
            report.append("\n\nMISSING REQUIRED ITEMS")
            report.append("-" * 70)
            for item in self.missing:
                report.append(f"✗ {item}")
        
        # Warnings
        if self.warnings:
            report.append("\n\nWARNINGS")
            report.append("-" * 70)
            for warning in self.warnings:
                report.append(f"⚠ {warning}")
        
        # Recommendations
        if self.missing:
            report.append("\n\nRECOMMENDATIONS")
            report.append("-" * 70)
            report.append("Add the following missing sections/components:")
            for i, item in enumerate(self.missing, 1):
                report.append(f"{i}. {item}")
            report.append("\nRefer to templates/system_description_complete.md for structure.")
        
        report.append("\n" + "=" * 70)
        
        return "\n".join(report)
    
    def validate(self, save_report=None):
        """Run complete validation."""
        print("=" * 70)
        print("SOC 2 SYSTEM DESCRIPTION COMPLETENESS CHECKER")
        print("=" * 70)
        print(f"Checking: {self.file_path}\n")
        
        if not self.load_file():
            return False
        
        # Run all checks
        sections_complete = self.check_sections()
        components_complete = self.check_section_2_components()
        self.check_important_elements()
        self.check_placeholders()
        self.estimate_completeness()
        
        # Generate report
        report = self.generate_report()
        print("\n" + report)
        
        # Save report if requested
        if save_report:
            try:
                with open(save_report, 'w', encoding='utf-8') as f:
                    f.write(report)
                print(f"\n✓ Report saved to: {save_report}")
            except Exception as e:
                print(f"\n✗ Could not save report: {e}")
        
        return sections_complete and components_complete


def main():
    """Main function."""
    if len(sys.argv) < 2:
        print("Usage: python3 completeness_checker.py <system_description_file> [--output-report <report_file>]")
        print("\nExample:")
        print("  python3 completeness_checker.py system_description.md")
        print("  python3 completeness_checker.py system_description.md --output-report completeness_report.txt")
        sys.exit(1)
    
    file_path = sys.argv[1]
    report_file = None
    
    if '--output-report' in sys.argv:
        try:
            report_idx = sys.argv.index('--output-report')
            report_file = sys.argv[report_idx + 1]
        except (IndexError, ValueError):
            print("Error: --output-report requires a file name")
            sys.exit(1)
    
    checker = CompletenessChecker(file_path)
    success = checker.validate(save_report=report_file)
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()

