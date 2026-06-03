import requests

XSS_PAYLOADS = [
    "<script>alert(1)</script>",
    '"><img src=x onerror=alert(1)>',
    "';alert(1)//",
]

def check_xss(base_url, params=None):
    findings = []
    if not params:
        return findings
    for param in params:
        for payload in XSS_PAYLOADS:
            try:
                r = requests.get(base_url, params={param: payload}, timeout=5)
                if payload in r.text:
                    findings.append({
                        "check": "Reflected XSS",
                        "detail": f"Param '{param}' reflects payload: {payload}",
                        "severity": "CRITICAL",
                        "fix_key": "xss"
                    })
                    break
            except:
                pass
    return findings
