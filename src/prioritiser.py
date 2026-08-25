"""
This module assigns a priority to vulnerabilities found by the OSV-Scanner.

The priority is based on the following factors:
- The CVSS score (0.0 to 10.0)
- The EPSS score (0 to 1)
- Whether the vulnerability is listed in the CISA KEV catalogue

Returns:
    dict: The vulnerability record with the calculated risk score and priority.
"""

def assign_priority(vulnerability):

    cvss = vulnerability["cvss"]
    if cvss is None:
        cvss = 0
    
    epss = vulnerability["epss"]
    if epss is None:
        epss = 0

    score = cvss + (epss * 10)

    vulnerability["risk_score"] = round(score,2)
    
    if vulnerability["kev"]:
        vulnerability["priority"] = "Critical"

    elif score >= 15:
        vulnerability["priority"] = "Critical"

    elif score >= 10:
        vulnerability["priority"] = "High"

    elif score >= 7:
        vulnerability["priority"] = "Medium"

    else:
        vulnerability["priority"] = "Low"

    return vulnerability