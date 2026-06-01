from dashboard_generator import generate_dashboard
from agents.discovery_agent import DiscoveryAgent
from agents.scanner_agent import ScannerAgent
from agents.analysis_agent import AnalysisAgent
from agents.report_agent import ReportAgent


class CoordinatorAgent:
    def __init__(self, name: str):
        self.name = name
        self.goal = None

        self.discovery_agent = DiscoveryAgent("DiscoveryAgent")
        self.scanner_agent = ScannerAgent("ScannerAgent")
        self.analysis_agent = AnalysisAgent("AnalysisAgent")
        self.report_agent = ReportAgent("ReportAgent")

    def set_goal(self, goal: str) -> None:
        self.goal = goal
        print(f"[{self.name}] Goal set: {self.goal}")

    def run(self, goal: str, street_name: str) -> None:
        self.set_goal(goal)

        businesses = self.discovery_agent.discover_businesses(street_name)

        if not businesses:
            print(f"[{self.name}] No businesses to scan.")
            return

        final_results = []

        for business in businesses:
            scan_result = self.scanner_agent.scan_website(business)
            analyzed_result = self.analysis_agent.assess_risk(scan_result)
            final_results.append(analyzed_result)

        self.report_agent.generate_report(final_results)
        generate_dashboard(final_results)
  
