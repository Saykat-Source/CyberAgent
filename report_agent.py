class ReportAgent:
    def __init__(self, name: str):
        self.name = name

    def generate_report(self, results: list) -> None:
        print(f"[{self.name}] Generating final community report...")
        print("\n" + "=" * 60)
        print(" COMMUNITY CYBERSECURITY RISK REPORT ")
        print("=" * 60)

        if not results:
            print("No scan results available.")
            return

        for result in results:
            print("\n" + "-" * 60)
            print(f"Business: {result.get('business_name')}")
            print(f"Decision: {result.get('decision')}")
            print(f"Risk Score: {result.get('risk_score')}")
            print(f"Original URL: {result.get('url')}")
            print(f"Final URL: {result.get('final_url')}")
            print(f"Response Status: {result.get('response_status')}")
            print(f"HTTPS Enabled: {result.get('https_enabled')}")
            print(f"Server Banner: {result.get('server_banner')}")
            print(f"Redirect Count: {result.get('redirect_count')}")
            print(f"robots.txt Exists: {result.get('robots_txt_exists')}")
            print(f"Missing Security Headers: {result.get('missing_security_headers')}")
            print(f"AI Explanation: {result.get('ai_explanation')}")

        print("\n" + "=" * 60)
        print(" END OF REPORT ")
        print("=" * 60)
