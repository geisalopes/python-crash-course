def make_sandwiches(*fillings):
    """Make a sandwich with the given fillings"""
    print("\nMaking a sandwich with the following fillings:")
    for filling in fillings:
        print(f"- {filling}")


make_sandwiches("meat balls", "pomodoro sauce")
make_sandwiches("tuna", "cream cheese", "capers")
make_sandwiches("chicken", "corn")
