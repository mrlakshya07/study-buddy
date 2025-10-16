import time
import winsound

def pomodoro(minutes):
    total_seconds = minutes * 60
    for remaining in range(total_seconds, 0, -1):
        print(f"Time left: {remaining} sec", end="\r")
        time.sleep(1)
    print()  # Move to next line after countdown

    # Play beep sound at the end (frequency=1000Hz, duration=2000ms)
    winsound.Beep(1000, 2000)
    print("Time's up! Take a break.")

mins = int(input("Enter the time in minutes: "))
pomodoro(mins)