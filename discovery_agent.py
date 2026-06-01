import csv


class DiscoveryAgent:
    def __init__(self, name: str, csv_file: str = "businesses.csv"):
        self.name = name
        self.csv_file = csv_file

    def discover_businesses(self, street_name: str) -> list:
        print(f"[{self.name}] Discovering businesses for: {street_name}")

        street_key = street_name.strip().lower()
        businesses = []

        try:
            with open(self.csv_file, mode="r", encoding="utf-8") as file:
                reader = csv.DictReader(file)

                for row in reader:
                    csv_street = row.get("street", "").strip().lower()

                    if csv_street == street_key:
                        businesses.append({
                            "name": row.get("name", "").strip(),
                            "website": row.get("website", "").strip(),
                        })

        except FileNotFoundError:
            print(f"[{self.name}] Error: CSV file '{self.csv_file}' not found.")
            return []

        if not businesses:
            print(f"[{self.name}] No businesses found for this street.")
        else:
            print(f"[{self.name}] Found {len(businesses)} businesses.")

        return businesses
