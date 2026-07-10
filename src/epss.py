"""
This script retrieves EPSS (Exploit Prediction Scoring System) scores
for vulnerabilities extracted from the OSV-Scanner report.

Parameters:
    cve (str): CVE identifier

Returns:
    float: EPSS score if found
"""

import json
import urllib.request


def get_epss_score(cve):

    if cve is None:
        return None

    url = f"https://api.first.org/data/v1/epss?cve={cve}"

    try:

        response = urllib.request.urlopen(url)

        data = json.loads(response.read())

        if len(data["data"]) > 0:
            return float(data["data"][0]["epss"])

        return None

    except Exception:
        return None
