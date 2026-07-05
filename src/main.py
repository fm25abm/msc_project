"""
This script intializes the Patch Prioritisation Engine.

It calls all the individual modules in the correct order. 

Currently, it invokes the scanner module to analyse a project and generate the vulnerability
report.

Future versions will also call the parser, EPSS, KEV and prioritisation modules.
"""

from scanner import run_scan

def main():

    project_path = "test-projects/python/flask-demo"
    output_file = "output/results.json"

    success = run_scan(project_path, output_file)

    if success:
        print("Results saved to:", output_file)


if __name__ == "__main__":
    main()