import subprocess


class LLMAgent:
    def __init__(self, name: str, model: str = "gemma:2b"):
        self.name = name
        self.model = model

    def generate_explanation(self, scan_result: dict) -> str:
        print(f"[{self.name}] Generating AI explanation...")

        prompt = f"""
You are a cybersecurity assistant.

Explain this website security result in simple words.

Business: {scan_result.get('business_name')}
HTTPS Enabled: {scan_result.get('https_enabled')}
Missing Security Headers: {scan_result.get('missing_security_headers')}
Server Banner: {scan_result.get('server_banner')}
Risk Score: {scan_result.get('risk_score')}
Decision: {scan_result.get('decision')}

Keep the answer short and simple.
"""

        try:
            result = subprocess.run(
                ["ollama", "run", self.model],
                input=prompt,
                text=True,
                capture_output=True
            )

            return result.stdout.strip()

        except Exception as e:
            return f"Error generating explanation: {e}"

