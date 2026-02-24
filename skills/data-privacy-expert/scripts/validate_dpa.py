#!/usr/bin/env python3
"""
DPA Validation Script

Validates Data Processing Addendums (DPAs) for completeness and compliance
with GDPR Article 28 requirements and CCPA service provider provisions.

Usage:
    python3 validate_dpa.py path/to/dpa.md
    python3 validate_dpa.py path/to/dpa.md --output-report validation_report.txt
"""

import sys
import re
from pathlib import Path
from datetime import datetime


class DPAValidator:
    """Validates DPA documents for required clauses and completeness."""
    
    # Required GDPR Article 28 elements
    GDPR_REQUIRED_ELEMENTS = [
        ("Subject matter and duration", r"(subject matter|duration|term)"),
        ("Nature and purpose of processing", r"(nature|purpose).*processing"),
        ("Types of personal data", r"(type|categor).*personal data"),
        ("Categories of data subjects", r"categor.*data subject"),
        ("Process only on instructions", r"(process.*instruct|documented.*instruct)"),
        ("Confidentiality obligations", r"confidentiality"),
        ("Security measures", r"(security measures|technical.*organizational)"),
        ("Sub-processor provisions", r"(sub-processor|subprocessor)"),
        ("Assistance with data subject rights", r"(assist.*data subject|data subject.*rights)"),
        ("Assistance with compliance", r"(assist.*compliance|breach notification|DPIA)"),
        ("Deletion or return of data", r"(delet.*return|return.*delet)"),
        ("Audit rights", r"audit"),
    ]
    
    # Recommended additional clauses
    RECOMMENDED_ELEMENTS = [
        ("International data transfers", r"(international.*transfer|Standard Contractual Clauses|SCC)"),
        ("Liability and indemnification", r"(liability|indemnif)"),
        ("Term and termination", r"(termination|term of agreement)"),
        ("Governing law", r"governing law"),
        ("Schedules/Annexes", r"(schedule|annex|appendix)"),
    ]
    
    # CCPA-specific requirements
    CCPA_REQUIRED_ELEMENTS = [
        ("Service provider certification", r"(certif.*understand.*restrict|Section 1798\.140)"),
        ("Prohibition on selling/sharing", r"(not sell|prohibit.*sell|not.*share)"),
        ("Business purpose limitation", r"business purpose"),
        ("Right to take corrective action", r"(corrective action|remediate)"),
    ]
    
    def __init__(self, dpa_path):
        """Initialize validator with DPA file path."""
        self.dpa_path = Path(dpa_path)
        self.content = ""
        self.findings = []
        self.warnings = []
        self.missing_elements = []
        
    def load_dpa(self):
        """Load DPA content from file."""
        try:
            with open(self.dpa_path, 'r', encoding='utf-8') as f:
                self.content = f.read()
            return True
        except FileNotFoundError:
            self.findings.append(f"ERROR: File not found: {self.dpa_path}")
            return False
        except Exception as e:
            self.findings.append(f"ERROR: Could not read file: {e}")
            return False
    
    def check_element(self, element_name, pattern, case_sensitive=False):
        """Check if a required element is present in the DPA."""
        flags = 0 if case_sensitive else re.IGNORECASE
        if re.search(pattern, self.content, flags):
            return True
        return False
    
    def validate_gdpr_elements(self):
        """Validate presence of GDPR Article 28 required elements."""
        print("\n=== GDPR Article 28 Requirements ===")
        missing = []
        
        for element_name, pattern in self.GDPR_REQUIRED_ELEMENTS:
            if self.check_element(element_name, pattern):
                print(f"✓ {element_name}")
                self.findings.append(f"PASS: {element_name}")
            else:
                print(f"✗ {element_name} - MISSING")
                self.findings.append(f"FAIL: {element_name} - Required by GDPR Article 28")
                missing.append(element_name)
                self.missing_elements.append(element_name)
        
        return len(missing) == 0
    
    def validate_recommended_elements(self):
        """Validate presence of recommended elements."""
        print("\n=== Recommended Elements ===")
        missing = []
        
        for element_name, pattern in self.RECOMMENDED_ELEMENTS:
            if self.check_element(element_name, pattern):
                print(f"✓ {element_name}")
                self.findings.append(f"PASS: {element_name}")
            else:
                print(f"⚠ {element_name} - Consider adding")
                self.warnings.append(f"WARNING: {element_name} - Recommended for completeness")
                missing.append(element_name)
        
        return len(missing) == 0
    
    def validate_ccpa_elements(self):
        """Validate presence of CCPA service provider requirements."""
        # Check if CCPA applies (look for CCPA references)
        if not re.search(r"(CCPA|California Consumer Privacy Act|California.*privacy)", 
                        self.content, re.IGNORECASE):
            print("\n=== CCPA Requirements ===")
            print("ℹ CCPA provisions not detected - Skip if not processing California data")
            self.findings.append("INFO: CCPA provisions not detected")
            return True
        
        print("\n=== CCPA Requirements ===")
        missing = []
        
        for element_name, pattern in self.CCPA_REQUIRED_ELEMENTS:
            if self.check_element(element_name, pattern):
                print(f"✓ {element_name}")
                self.findings.append(f"PASS: {element_name}")
            else:
                print(f"✗ {element_name} - MISSING")
                self.findings.append(f"FAIL: {element_name} - Required by CCPA")
                missing.append(element_name)
                self.missing_elements.append(element_name)
        
        return len(missing) == 0
    
    def check_placeholders(self):
        """Check for unfilled placeholders."""
        print("\n=== Placeholder Check ===")
        placeholder_patterns = [
            r'\[INSERT[^\]]*\]',
            r'\[SPECIFY[^\]]*\]',
            r'\[DESCRIBE[^\]]*\]',
            r'\[LIST[^\]]*\]',
            r'\[TODO[^\]]*\]',
            r'\[FILL[^\]]*\]',
            r'\[ADD[^\]]*\]',
            r'\[COMPLETE[^\]]*\]',
        ]
        
        unfilled = []
        for pattern in placeholder_patterns:
            matches = re.findall(pattern, self.content, re.IGNORECASE)
            unfilled.extend(matches)
        
        if unfilled:
            print(f"⚠ Found {len(unfilled)} unfilled placeholders")
            for placeholder in set(unfilled):  # Unique placeholders
                print(f"  - {placeholder}")
                self.warnings.append(f"WARNING: Unfilled placeholder: {placeholder}")
        else:
            print("✓ No unfilled placeholders detected")
            self.findings.append("PASS: No unfilled placeholders")
        
        return len(unfilled) == 0
    
    def check_dates(self):
        """Check for dates and effective date."""
        print("\n=== Date Check ===")
        
        # Check for effective date
        if re.search(r'(effective date|dated|entered.*on)', self.content, re.IGNORECASE):
            print("✓ Effective date section found")
            self.findings.append("PASS: Effective date section present")
        else:
            print("⚠ Effective date not clearly specified")
            self.warnings.append("WARNING: Effective date should be clearly specified")
        
        # Check for any date format (YYYY-MM-DD, MM/DD/YYYY, etc.)
        date_patterns = [
            r'\d{4}-\d{2}-\d{2}',
            r'\d{2}/\d{2}/\d{4}',
            r'(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},?\s+\d{4}',
        ]
        
        dates_found = False
        for pattern in date_patterns:
            if re.search(pattern, self.content):
                dates_found = True
                break
        
        if not dates_found:
            print("⚠ No dates found - Ensure DPA is dated when executed")
            self.warnings.append("WARNING: No dates found in DPA")
    
    def check_signatures(self):
        """Check for signature blocks."""
        print("\n=== Signature Check ===")
        
        if re.search(r'(signature|signed by|authorized signatory)', 
                    self.content, re.IGNORECASE):
            print("✓ Signature section found")
            self.findings.append("PASS: Signature section present")
        else:
            print("⚠ Signature section not detected")
            self.warnings.append("WARNING: DPA should include signature blocks for both parties")
    
    def generate_report(self):
        """Generate validation report."""
        report = []
        report.append("=" * 70)
        report.append("DPA VALIDATION REPORT")
        report.append("=" * 70)
        report.append(f"File: {self.dpa_path}")
        report.append(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append("")
        
        # Summary
        total_findings = len(self.findings)
        total_warnings = len(self.warnings)
        failures = len([f for f in self.findings if f.startswith("FAIL")])
        
        report.append("SUMMARY")
        report.append("-" * 70)
        report.append(f"Total Checks: {total_findings}")
        report.append(f"Failures: {failures}")
        report.append(f"Warnings: {total_warnings}")
        
        if failures == 0 and total_warnings == 0:
            report.append("\n✓ DPA VALIDATION PASSED - All required elements present")
        elif failures == 0:
            report.append(f"\n⚠ DPA VALIDATION PASSED WITH WARNINGS - Review {total_warnings} warnings")
        else:
            report.append(f"\n✗ DPA VALIDATION FAILED - {failures} required elements missing")
        
        # Detailed findings
        report.append("\n\nDETAILED FINDINGS")
        report.append("-" * 70)
        for finding in self.findings:
            report.append(finding)
        
        # Warnings
        if self.warnings:
            report.append("\n\nWARNINGS")
            report.append("-" * 70)
            for warning in self.warnings:
                report.append(warning)
        
        # Recommendations
        if self.missing_elements:
            report.append("\n\nRECOMMENDATIONS")
            report.append("-" * 70)
            report.append("Add the following missing elements to the DPA:")
            for i, element in enumerate(self.missing_elements, 1):
                report.append(f"{i}. {element}")
            report.append("\nRefer to references/dpa_guidelines.md for detailed guidance on each clause.")
        
        report.append("\n" + "=" * 70)
        
        return "\n".join(report)
    
    def validate(self, save_report=None):
        """Run complete validation."""
        print("=" * 70)
        print("DPA VALIDATOR")
        print("=" * 70)
        print(f"Validating: {self.dpa_path}")
        
        if not self.load_dpa():
            print("\nValidation failed: Could not load DPA file")
            return False
        
        print(f"File size: {len(self.content)} characters")
        
        # Run all validations
        gdpr_pass = self.validate_gdpr_elements()
        recommended_pass = self.validate_recommended_elements()
        ccpa_pass = self.validate_ccpa_elements()
        
        # Additional checks
        self.check_placeholders()
        self.check_dates()
        self.check_signatures()
        
        # Generate and display report
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
        
        # Return True if all required elements present
        return gdpr_pass and ccpa_pass


def main():
    """Main function."""
    if len(sys.argv) < 2:
        print("Usage: python3 validate_dpa.py <dpa_file> [--output-report <report_file>]")
        print("\nExample:")
        print("  python3 validate_dpa.py my_dpa.md")
        print("  python3 validate_dpa.py my_dpa.md --output-report validation_report.txt")
        sys.exit(1)
    
    dpa_file = sys.argv[1]
    report_file = None
    
    # Check for output report option
    if '--output-report' in sys.argv:
        try:
            report_idx = sys.argv.index('--output-report')
            report_file = sys.argv[report_idx + 1]
        except (IndexError, ValueError):
            print("Error: --output-report requires a file name")
            sys.exit(1)
    
    # Run validation
    validator = DPAValidator(dpa_file)
    success = validator.validate(save_report=report_file)
    
    # Exit with appropriate code
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()

