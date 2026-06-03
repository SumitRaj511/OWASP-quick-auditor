import requests

SQLI_PAYLOADS = ["'", "' OR '1'='1", "\" OR \"1\"=\"1", "1; DROP TABLE users--"]
ERROR_SIGNS = ["sql syntax", "mysql_fetch", "ORA-", "syntax error", "unclosed quotation"]

def check_sqli(base_url, params=None):
    findings = []
    if not params:
        return findings
    for param in params:
        for payload in SQLI_PAYLOADS:
            try:
                r = requests.get(base_url, params={param: payload}, timeout=5)
                for sign in ERROR_SIGNS:
                    if sign.lower() in r.text.lower():
                        findings.append({
                            "check": "SQL Injection",
                            "detail": f"Param '{param}' triggered DB error with: {payload}",
                            "severity": "CRITICAL",
                            "fix_key": "sqli"
                        })
                        break
            except:
                pass
    return findings
