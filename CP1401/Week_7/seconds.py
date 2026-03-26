def main():
    for i in range(0, 3176, 635):
        print(f"{i} seconds is {format_seconds(i)}")

    favourite_duration = int(input("Favourite duration in seconds: "))
    print(f"You love {format_seconds(favourite_duration)}")


def format_seconds(seconds):
    """Convert seconds to minutes and seconds string."""
    minutes = seconds // 60
    sec = seconds % 60
    return f"{minutes}m {sec}s"


main()