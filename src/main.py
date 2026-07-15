"""
This script intializes the Patch Prioritisation Engine.

It calls all the individual modules in a specific order. 

Currently, it:
- Runs Google OSV-Scanner
- Loads and parses the scan results
- Retrieves EPSS scores
- Checks the CISA KEV catalogue
- Generates a vulnerability report

Future versions will also invoke the prioritisation module to rank vulnerabilities based on the collected data.
"""

from scanner import run_scan
from parser import load_results, extract_vulnerabilities
from report import generate_report
from epss import get_epss_score
from kev import is_known_exploited, load_kev_catalog
from prioritiser import assign_priority

def main():

    project = "test-projects/python/flask-demo"
    output = "output/results.json"

    if run_scan(project, output):
        results = load_results(output)
        kev_catalog = load_kev_catalog()

        if results:
            print("Results loaded successfully")

            vulnerabilities = extract_vulnerabilities(results)

            for vulnerability in vulnerabilities:
                vulnerability["epss"] = get_epss_score(vulnerability["cve"])

                vulnerability["kev"] = is_known_exploited(vulnerability["cve"], kev_catalog)

                vulnerability["priority"] = assign_priority(vulnerability)

            generate_report(vulnerabilities)


if __name__ == "__main__":
    main()