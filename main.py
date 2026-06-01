from coordinator import CoordinatorAgent


def main():
    coordinator = CoordinatorAgent("CoordinatorAgent")

    street_name = input("Enter street name: ").strip()

    coordinator.run(
        "Assess the security posture of businesses on a given street using a multi-agent system",
        street_name
    )


if __name__ == "__main__":
    main()
