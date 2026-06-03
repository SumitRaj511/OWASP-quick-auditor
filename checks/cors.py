import requests

def check_cors(base_url):
    findings = []
    try:
        headers = {"Origin": "https://evil.com"}
        r = requests.get(base_url, headers=headers, timeout=5)
        acao = r.headers.get("Access-Control-Allow-Origin", "")
        acac = r.headers.get("Access-Control-Allow-Credentials", "")
        if acao == "*":
            findings.append({
                "check": "CORS Misconfiguration",
                "detail": "Access-Control-Allow-Origin: * (wildcard)",
                "severity": "MEDIUM",
                "fix_key": "cors_wildcard"
            })
        if "evil.com" in acao and acac.lower() == "true":
            findings.append({
                "check": "CORS + Credentials Leak",
                "detail": "Reflects evil origin AND allows credentials",
                "severity": "CRITICAL",
                "fix_key": "cors_credentials"
            })
    except:
        pass
    return findings
