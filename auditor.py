import requests
import sys
from colorama import Fore, Style, init
from checks.headers import check_headers
from checks.cookies import check_cookies
from checks.directory import check_directory_listing
from checks.xss import check_xss
from checks.sqli import check_sqli
from checks.cors import check_cors
from advisor import get_advice
from reporter import generate_report

init(autoreset=True)

SEVERITY_COLOR = {
    "CRITICAL": Fore.RED,
    "HIGH": Fore.YELLOW,
    "MEDIUM": Fore.CYAN,
    "LOW": Fore.GREEN,
}

def banner():
    print(Fore.GREEN + """
  ██████  ██     ██  █████  ███████ ██████
 ██    ██ ██     ██ ██   ██ ██      ██   ██
 ██    ██ ██  █  ██ ███████ ███████ ██████
 ██    ██ ██ ███ ██ ██   ██      ██ ██
  ██████   ███ ███  ██   ██ ███████ ██
  OWASP Quick Auditor — Learn-as-you-audit
    """)

def run_audit(url, params=None):
    banner()
    print(f"🎯 Target: {url}\n")
    all_findings = []

    try:
        response = requests.get(url, timeout=10)
    except Exception as e:
        print(Fore.RED + f"[ERROR] Could not reach target: {e}")
        sys.exit(1)

    checks = [
        ("Security Headers",    check_headers(response)),
        ("Cookie Flags",        check_cookies(response)),
        ("Directory Listing",   check_directory_listing(url)),
        ("XSS",                 check_xss(url, params)),
        ("SQL Injection",       check_sqli(url, params)),
        ("CORS",                check_cors(url)),
    ]

    for name, findings in checks:
        print(f"\n{'='*50}")
        print(Fore.CYAN + f"[CHECK] {name}")
        if not findings:
            print(Fore.GREEN + "  ✅ No issues found")
        for f in findings:
            color = SEVERITY_COLOR.get(f["severity"], Fore.WHITE)
            print(color + f"  [{f['severity']}] {f['check']}: {f['detail']}")
            advice = get_advice(f["fix_key"])
            print(Fore.WHITE + f"  💡 {advice['why']}")
            if advice["snippet"]:
                print(Fore.LIGHTBLACK_EX + f"  Fix:\n  {advice['snippet'].splitlines()[0]}...")
            f["advice"] = advice
            all_findings.append(f)

    print(f"\n{'='*50}")
    print(f"\n📊 Total findings: {len(all_findings)}")
    generate_report(url, all_findings)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 auditor.py <url> [param1,param2]")
        print("Example: python3 auditor.py http://testphp.vulnweb.com searchFor,artist")
        sys.exit(1)

    target = sys.argv[1]
    params = sys.argv[2].split(",") if len(sys.argv) > 2 else None
    run_audit(target, params)
