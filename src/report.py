"""
This module is responsible for generating human-readable reports from extracted vulnerability data.

It formats and displays vulnerability information in a structured way for easier interpretation and analysis.
"""

def generate_report(vulnerabilities):
    """
    Prints a structured report of vulnerabilities grouped by package.

    Parameters:
        vulnerabilities (list): List of dictionaries containing:
            - package (str)
            - version (str)
            - osv_id (str)
            - cve (str)
            - epss (float)
            - kev (bool) 
    """

    grouped = {}

    # Group vulnerabilities by package
    for item in vulnerabilities:

        key = (item["package"], item["version"])

        if key not in grouped:
            grouped[key] = []

        grouped[key].append(item)

    # Print report
    print("\n" + "=" * 50)

    for (package, version), vulns in grouped.items():

        print(f"\nPackage : {package}")
        print(f"Version : {version}\n")

        print("Vulnerabilities")
        print("-" * 20)

        for v in vulns:
            print(f"OSV ID : {v['osv_id']}")
            print(f"CVE    : {v['cve']}")

            if v["epss"] is not None:
                print(f"EPSS   : {v['epss']:.4f}")
            
            else:
                print("EPSS   : N/A")
            
            if v["kev"]:
                print("KEV    : Yes")
            
            else:
                print("KEV    : No")
            
            print()

        print("\n" + "=" * 50)