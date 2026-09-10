import datetime
import time

def display_current_datetime():
    current = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current Date and Time: {current}")

def calculate_date_difference():
    date1_str = input("Enter the first date (YYYY-MM-DD): ")
    date2_str = input("Enter the second date (YYYY-MM-DD): ")
    try:
        d1 = datetime.datetime.strptime(date1_str, "%Y-%m-%d")
        d2 = datetime.datetime.strptime(date2_str, "%Y-%m-%d")
        diff = abs((d2 - d1).days)
        print(f"Difference: {diff} days")
    except ValueError:
        print("Invalid date format.")

def format_custom_date():
    dt = datetime.datetime.now()
    print("Formatted Date:", dt.strftime("%B %d, %Y"))

def run_stopwatch():
    input("Press Enter to start stopwatch...")
    start = time.time()
    input("Press Enter to stop stopwatch...")
    elapsed = time.time() - start
    print(f"Elapsed Time: {elapsed:.2f} seconds")

def run_countdown_timer():
    try:
        seconds = int(input("Enter countdown time in seconds: "))
        for i in range(seconds, 0, -1):
            print(f"Countdown: {i}s", end="\r")
            time.sleep(1)
        print("Time's up!                ")
    except ValueError:
        print("Please enter a valid integer.")
        