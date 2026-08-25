"""
This module loads the CISA Known Exploited Vulnerabilities catalogue and checks whether a CVE is listed in it.

Parameters:
    cve (str): CVE identifier.
    kev_catalog (list): Vulnerabilities loaded from the CISA KEV catalogue.

Returns:
    bool: True if the CVE is listed in the KEV catalogue, otherwise False.
"""

import json
import urllib.request

def load_kev_catalog():

    url = "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"

    try:

        response = urllib.request.urlopen(url)

        data = json.loads(response.read())

        return data["vulnerabilities"]

    except Exception:

        return []


def is_known_exploited(cve, kev_catalog):

    if cve is None:
        return False

    url = "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"

    try:

        for vulnerability in kev_catalog:

            if vulnerability["cveID"] == cve:
                return True

        return False

    except Exception:
        return False