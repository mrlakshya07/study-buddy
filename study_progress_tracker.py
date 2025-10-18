from datetime import datetime
import matplotlib.pyplot as plt

def log_study_session():
    while True:
        date_input = input("Enter the date for study session (YYYY-MM-DD) or press Enter for today: ").strip()
        if not date_input:
            current_date = datetime.now().strftime("%Y-%m-%d")
            break
        else:
            try:
                datetime.strptime(date_input, "%Y-%m-%d")
                current_date=date_input
                break
            except ValueError:
                print("Invalid date format. Please enter in YYYY-MM-DD format.")

    while True:
        try:
            hours = float(input("Enter hours studied: "))
            if hours<0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    with open("study_log.txt", "a") as file:
        file.write(f"{current_date},{hours}\n")
    print(f"Study session logged: {current_date}, {hours} hours")


def load_logged_data():
    data = {}
    try:
        with open("study_log.txt","r") as file:
            lines=file.readlines()
            for line in lines:
                parts=line.strip().split(",")
                if len(parts)==2:
                    date, hour = parts[0], float(parts[1])
                    if date in data:
                        data[date].append(hour)
                    else:
                        data[date]=[hour]
    except FileNotFoundError:
        print("No study log file found. Please log study sessions first.")
    return data

def show_all_history(data):
    if not data:
        print("No data available.")
        return
    print("Study Data History:")
    for date in sorted(data):
        hours_list=data[date]
        print(f"{date}: {', '.join(map(str, hours_list))} hours")

def plot_average_study_time(data):
    if not data:
        print("No data available to plot.")
        return
    dates=sorted(data)
    avg_hours=[sum(hours)/len(hours) for hours in (data[date] for date in dates)]
    plt.figure(figsize=(9, 5))
    plt.bar(dates, avg_hours, color="#2F167A")
    plt.xlabel('Date',fontweight='bold')
    plt.ylabel('Average Hours Studied',fontweight='bold')
    plt.title('Average Study Time per Day',fontweight='bold')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def main_menu():
    while True:
        print("\n\t\t\t\tMenu Options:")
        print("\t\t\t1. Input new study session")
        print("\t\t\t2. Load and show all study data")
        print("\t\t\t3. Show average study time visually")
        print("\t\t\t4. Exit")
        choice=input("Enter your choice: ")
        if choice=='1':
            log_study_session()
        elif choice=='2':
            data = load_logged_data()
            show_all_history(data)
        elif choice=='3':
            data = load_logged_data()
            plot_average_study_time(data)
        elif choice=='4':
            print("Thanks for using our service\nGoodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()