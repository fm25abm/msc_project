"""
This script assigns priority to vulnerabilties found by the OSV scanner.

The priority is based on two factors:
- The EPSS score
- Whether it is actively exploited; through KEV

Returns:
    str: Priority Level
"""

def assign_priority(vulnerability):

    if vulnerability["kev"]:
        return "Critical"
    
    if vulnerability["epss"] >= 0.70:
        return "High"

    if vulnerability["epss"] >= 0.30:
        return "Medium"
    
    else:
        return "Low"

if __name__ == "__main__":

    vulnerability = {
        "epss": 0.82,
        "kev": False
    }

    print(assign_priority(vulnerability))