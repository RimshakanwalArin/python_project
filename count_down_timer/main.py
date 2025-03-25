import time

def timer(countdown_seconds):
    """Countdown timer function"""
    while countdown_seconds:
        mins, secs = divmod(countdown_seconds, 60)  # Convert seconds into minutes:seconds format
        print(f"Time Remaining: {mins:02d}:{secs:02d}", end="\r")  # Overwrites the line
        time.sleep(1)  # Wait for 1 second
        countdown_seconds -= 1
    
    print("\nTime's up!")  # Print when the countdown reaches zero

def main():
    try:
        countdown_time = int(input("Enter countdown time in seconds: "))  # User input for countdown
        timer(countdown_time)
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
