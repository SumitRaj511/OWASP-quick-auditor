import requests

COMMON_DIRS = ["/admin", "/backup", "/config", "/.git", "/uploads", "/test"]

def check_directory_listing(base_url):
    findings = []
    for path in COMMON_DIRS:
        try:
            r = requests.get(base_url + path, timeout=5)
            if r.status_code == 200 and "Index of" in r.text:
                findings.append({
                    "check": "Directory Listing Enabled",
                    "detail": f"Open directory at {base_url + path}",
                    "severity": "HIGH",
                    "fix_key": "directory_listing"
                })
        except:
            pass
    return findings
