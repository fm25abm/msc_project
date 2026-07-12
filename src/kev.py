"""
This script checks whether a vulnerability exists in the CISA Known Exploited Vulnerabilities catalogue.

Parameters:
    cve (str): CVE identifier.

Returns:
    bool: True if the CVE is listed in the KEV catalogue, otherwise False.
"""

import json
import urllib.request


def is_known_exploited(cve):

    if cve is None:
        return False

    url = "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"

    try:

        response = urllib.request.urlopen(url)

        data = json.loads(response.read())

        for vulnerability in data["vulnerabilities"]:

            if vulnerability["cveID"] == cve:
                return True

        return False

    except Exception:
        return False


if __name__ == "__main__":
    main()