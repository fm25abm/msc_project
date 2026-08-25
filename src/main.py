"""
This script initializes the Patch Prioritisation Engine.

It calls all the individual modules in a specific order:

- Runs Google OSV-Scanner
- Loads and parses the scan results
- Retrieves EPSS scores
- Checks the CISA KEV catalogue
- Assigns vulnerability priorities
- Generates a vulnerability report

"""

import os
from scanner import run_scan
from parser import load_results, extract_vulnerabilities
from report import generate_report
from epss import get_epss_score
from kev import is_known_exploited, load_kev_catalog
from prioritiser import assign_priority
from exporter import export_results

def main():

    project = "evaluation/real-world-projects/Portfolio-Flask/requirements.txt"
    project_name = os.path.basename(os.path.dirname(project))
    output = f"evaluation/results/raw-osv-results/{project_name}.json"
    processed_path = f"evaluation/results/processed-ppe-results/{project_name}.json"

    if run_scan(project, output):
        results = load_results(output)
        kev_catalog = load_kev_catalog()

        if results:
            print("Results loaded successfully")

            vulnerabilities = extract_vulnerabilities(results)

            for vulnerability in vulnerabilities:
                vulnerability["epss"] = get_epss_score(vulnerability["cve"])

                vulnerability["kev"] = is_known_exploited(vulnerability["cve"], kev_catalog)

                assign_priority(vulnerability)
            
            export_results(vulnerabilities, processed_path)
            generate_report(vulnerabilities, project)


if __name__ == "__main__":
    main()