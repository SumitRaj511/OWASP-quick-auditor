def check_cookies(response):
    findings = []
    for cookie in response.cookies:
        if not cookie.secure:
            findings.append({
                "check": "Cookie Missing Secure Flag",
                "detail": f"Cookie '{cookie.name}' lacks Secure flag",
                "severity": "HIGH",
                "fix_key": "cookie_secure"
            })
        if not cookie.has_nonstandard_attr("HttpOnly"):
            findings.append({
                "check": "Cookie Missing HttpOnly Flag",
                "detail": f"Cookie '{cookie.name}' lacks HttpOnly flag",
                "severity": "HIGH",
                "fix_key": "cookie_httponly"
            })
    return findings
