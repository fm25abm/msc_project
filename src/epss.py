import urllib.request
import json


def get_epss_score(cve_id):

    url = f"https://api.first.org/data/v1/epss?cve={cve_id}"

    try:
        response = urllib.request.urlopen(url)

        data = json.loads(response.read())

        results = data["data"]

        if len(results) > 0:
            return float(results[0]["epss"])

        return None