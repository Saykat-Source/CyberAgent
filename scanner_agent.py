import requests


class ScannerAgent:
    def __init__(self, name: str):
        self.name = name

    def scan_website(self, business: dict) -> dict:
        business_name = business.get("name", "Unknown Business")
        url = business.get("website")

        print(f"[{self.name}] Scanning {business_name}: {url}")

        result = {
            "business_name": business_name,
            "url": url,
            "final_url": "N/A",
            "https_enabled": False,
            "response_status": "ERROR",
            "missing_security_headers": [],
            "missing_security_headers_count": 0,
            "server_banner": "N/A",
            "redirect_count": 0,
            "robots_txt_exists": False,
        }

        if not url:
            print(f"[{self.name}] No website found for {business_name}")
            return result

        try:
            response = requests.get(url, timeout=10, allow_redirects=True)
            headers = response.headers

            security_headers = [
                "Content-Security-Policy",
                "Strict-Transport-Security",
                "X-Frame-Options",
                "X-Content-Type-Options",
                "Referrer-Policy",
            ]

            missing_headers = []
            for header in security_headers:
                if header not in headers:
                    missing_headers.append(header)

            final_url = response.url
            https_enabled = final_url.startswith("https://")
            server_banner = headers.get("Server", "Not disclosed")
            redirect_count = len(response.history)

            robots_url = final_url.rstrip("/") + "/robots.txt"
            robots_exists = False

            try:
                robots_response = requests.get(robots_url, timeout=5)
                if robots_response.status_code == 200:
                    robots_exists = True
            except requests.exceptions.RequestException:
                robots_exists = False

            result.update({
                "final_url": final_url,
                "https_enabled": https_enabled,
                "response_status": response.status_code,
                "missing_security_headers": missing_headers,
                "missing_security_headers_count": len(missing_headers),
                "server_banner": server_banner,
                "redirect_count": redirect_count,
                "robots_txt_exists": robots_exists,
            })

        except requests.exceptions.RequestException as e:
            print(f"[{self.name}] Error scanning {business_name}: {e}")

        return result
