"""
This script intializes the Patch Prioritisation Engine.

It calls all the individual modules in the correct order. 

Currently, it invokes the scanner module to analyse a project and generate the vulnerability
report.

Future versions will also call the parser, EPSS, KEV and prioritisation modules.
"""

from scanner import run_scan
from parser import load_results, extract_vulnerabilities
from report import generate_report

def main():

    project = "test-projects/python/flask-demo"
    output = "output/results.json"

    if run_scan(project, output):
        results = load_results(output)

        if results:
            print("Results loaded successfully")

            vulnerabilities = extract_vulnerabilities(results)
            
            generate_report(vulnerabilities)


if __name__ == "__main__":
    main()