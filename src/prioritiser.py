"""
This script assigns priority to vulnerabilties found by the OSV scanner.

The priority is based on the following factors:
- The CVSS score (0.0 to 10)
- The EPSS score (0 to 1)
- Whether it is actively exploited; through KEV

Returns:
    str: Priority Level
"""

def assign_priority(vulnerability):

    if vulnerability["kev"]:
        vulnerability["priority"] = "Critical"
        return vulnerability
    
    cvss = vulnerability["cvss"]

    if cvss is None:
        cvss = 0
    
    epss = vulnerability["epss"]

    score = cvss + (epss * 10)

    vulnerability["risk_score"] = round(score,2)
    
    if score >= 15:
        vulnerability["priority"] = "Critical"

    elif score >= 10:
        vulnerability["priority"] = "High"
    
    elif score >= 7:
        vulnerability["priority"] = "Medium"
       
    else:
        vulnerability["priority"] = "Low"
