"""
This module generates human-readable text reports from processed vulnerability data and saves them to the ppe-reports directory.

It formats vulnerability information in a structured way, grouped by package and version, for easier interpretation and analysis.
"""
import os

def write_line(text, report_file):
    """
    This function writes to the report file.
    """
    report_file.write(text + "\n")

def generate_report(vulnerabilities, project):

    project_name = os.path.basename(os.path.dirname(project))
    report_path = f"evaluation/results/ppe-reports/{project_name}.txt"

    print("Generating report...")

    with open(report_path, "w", encoding="utf-8") as report_file:
        grouped = {}

        # Group vulnerabilities by package
        for item in vulnerabilities:

            key = (item["package"], item["version"])

            if key not in grouped:
                grouped[key] = []

            grouped[key].append(item)

        # Write report
        write_line("\n" + "=" * 50, report_file)

        for (package, version), vulns in grouped.items():

            write_line(f"\nPackage : {package}", report_file)
            write_line(f"Version : {version}\n", report_file)
            write_line("Vulnerabilities", report_file)
            write_line("-" * 20,report_file)

            for v in vulns:

                write_line(f"OSV ID : {v['osv_id']}", report_file)

                write_line(f"CVE    : {v['cve']}", report_file)

                write_line(f"CVSS   : {v['cvss']}", report_file)

                if v["epss"] is not None:
                    write_line(f"EPSS   : {v['epss']:.4f}", report_file)
            
                else:
                    write_line("EPSS   : N/A", report_file)
            
                if v["kev"]:
                    write_line("KEV    : Yes", report_file)
            
                else:
                    write_line("KEV    : No", report_file)

                if "risk_score" in v:
                    write_line(f"Risk Score : {v['risk_score']}", report_file)
            
                write_line(f"Priority : {v['priority']}", report_file)
            
                write_line("", report_file)
        
            write_line("\n" + "=" * 50, report_file)
    print(f"\nReport saved to {report_path}")