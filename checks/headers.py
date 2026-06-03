REQUIRED_HEADERS = [
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Strict-Transport-Security",
    "Referrer-Policy",
    "Permissions-Policy",
]

def check_headers(response):
    findings = []
    for header in REQUIRED_HEADERS:
        if header not in response.headers:
            findings.append({
                "check": "Missing Security Header",
                "detail": f"{header} is missing",
                "severity": "MEDIUM",
                "fix_key": f"header_{header.lower().replace('-','_')}"
            })
    return findings
