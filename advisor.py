FIXES = {
    "cookie_secure": {
        "why": "Cookies sent without HTTPS can be intercepted.",
        "impact": "Session hijacking and account takeover.",
        "fix": "Enable the Secure flag on cookies.",
        "snippet": 'response.set_cookie("session", value, secure=True)',
        "time": "2 minutes",
        "question": "What does the Secure flag do?",
        "answer": "It ensures cookies are only transmitted over HTTPS."
    },

    "cookie_httponly": {
        "why": "JavaScript can read cookies if HttpOnly is missing.",
        "impact": "XSS attacks can steal user sessions.",
        "fix": "Enable HttpOnly on cookies.",
        "snippet": 'Set-Cookie: sessionid=abc; HttpOnly; Secure',
        "time": "2 minutes",
        "question": "What is HttpOnly?",
        "answer": "It prevents JavaScript from accessing cookies."
    },

    "xss": {
        "why": "Attackers may inject JavaScript into your pages.",
        "impact": "Session theft, phishing and account compromise.",
        "fix": "Escape output and implement CSP.",
        "snippet": 'from markupsafe import escape\nsafe = escape(user_input)',
        "time": "15 minutes",
        "question": "What is XSS and how can it be prevented?",
        "answer": "XSS executes attacker-controlled JavaScript in a victim browser. Prevent it using output encoding and CSP."
    },

    "sqli": {
        "why": "User input may modify database queries.",
        "impact": "Database leakage, authentication bypass.",
        "fix": "Use parameterized queries.",
        "snippet": 'cursor.execute("SELECT * FROM users WHERE id=?", (user_id,))',
        "time": "10 minutes",
        "question": "What is SQL Injection?",
        "answer": "SQL Injection manipulates backend queries using malicious input."
    },

    "directory_listing": {
        "why": "Attackers can browse server directories.",
        "impact": "Sensitive files may be exposed.",
        "fix": "Disable directory listing.",
        "snippet": 'Options -Indexes',
        "time": "5 minutes",
        "question": "Why disable directory listing?",
        "answer": "It prevents attackers from discovering files and folders."
    },

    "cors_wildcard": {
        "why": "Any website can access your API.",
        "impact": "Sensitive data exposure.",
        "fix": "Allow only trusted origins.",
        "snippet": 'Access-Control-Allow-Origin: https://yourdomain.com',
        "time": "5 minutes",
        "question": "Why is wildcard CORS dangerous?",
        "answer": "It allows any website to read responses from your API."
    },

    "cors_credentials": {
        "why": "Credentials are shared with arbitrary origins.",
        "impact": "Account compromise and data theft.",
        "fix": "Whitelist trusted origins only.",
        "snippet": 'Never reflect Origin blindly.',
        "time": "10 minutes",
        "question": "Why is CORS with credentials dangerous?",
        "answer": "It may expose authenticated sessions to attackers."
    }
}

for h in [
    "content_security_policy",
    "x_frame_options",
    "x_content_type_options",
    "strict_transport_security",
    "referrer_policy",
    "permissions_policy"
]:
    FIXES[f"header_{h}"] = {
        "why": f"{h.replace('_',' ').title()} protects browsers against common attacks.",
        "impact": "Reduced browser-side security.",
        "fix": f"Add {h.replace('_','-').title()} header.",
        "snippet": f"{h.replace('_','-').title()}: <value>",
        "time": "5 minutes",
        "question": f"What is {h.replace('_',' ').upper()}?",
        "answer": f"It is a security header used to improve browser security."
    }

def get_advice(fix_key):
    return FIXES.get(
        fix_key,
        {
            "why": "Review OWASP documentation.",
            "impact": "Unknown",
            "fix": "Review secure configuration.",
            "snippet": "",
            "time": "Unknown",
            "question": "N/A",
            "answer": "N/A"
        }
    )
