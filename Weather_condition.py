def display_weather(season):
    """
    This function displays the typical weather for a given season.
    :param season: The season (autumn or spring)
    """
    if season.lower() == "autumn":
        print("Autumn: Cooler temperatures, shorter days, and colorful falling leaves.")
    elif season.lower() == "spring":
        print("Spring: Warmer temperatures, blooming flowers, and occasional rain.")
    else:
        print("Invalid season. Please enter 'autumn' or 'spring'.")

# Example usage:
season = input("Enter the season (autumn or spring): ")
display_weather(season)
