from agents.llm_agent import LLMAgent


class AnalysisAgent:
    def __init__(self, name: str):
        self.name = name
        self.llm_agent = LLMAgent("LLMAgent")

    def assess_risk(self, scan_result: dict) -> dict:
        business_name = scan_result.get("business_name", "Unknown Business")
        print(f"[{self.name}] Evaluating risk for {business_name}...")

        response_status = scan_result.get("response_status")
        https_enabled = scan_result.get("https_enabled", False)
        missing_headers_count = scan_result.get("missing_security_headers_count", 0)
        server_banner = scan_result.get("server_banner", "N/A")

        if response_status == "ERROR":
            scan_result["risk_score"] = 0
            scan_result["decision"] = "SCAN FAILED"
            scan_result["ai_explanation"] = "No website available to analyze."
            return scan_result

        risk_score = 0

        if not https_enabled:
            risk_score += 40

        risk_score += missing_headers_count * 8

        if server_banner not in ["N/A", "Not disclosed", "", None]:
            risk_score += 5

        if risk_score >= 50:
            decision = "HIGH RISK"
        elif risk_score >= 20:
            decision = "MEDIUM RISK"
        else:
            decision = "LOW RISK"

        scan_result["risk_score"] = risk_score
        scan_result["decision"] = decision

        scan_result["ai_explanation"] = self.llm_agent.generate_explanation(scan_result)

        return scan_result
