import datetime

def show_groups():
    groups = ["Python Beginners", "JS Intermediate"]
    print("Available groups:")
    for g in groups:
        print(f"- {g}")

def upload_homework():
    student_name = input("Enter your name: ")
    homework = input("Enter your homework text: ")
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    with open("homework_submissions.txt", "a") as f:
        f.write(f"{student_name},{homework},{date}\n")
    print("Homework uploaded successfully.")

def show_attendance():
    attendance_data = {
        "lesson_1": "Present",
        "lesson_2": "Present",
        "lesson_3": "Absent",
    }
    print("Your attendance:")
    for lesson, status in attendance_data.items():
        print(f"{lesson}: {status}")

def show_balance():
    balance = 100  # Placeholder: should be fetched from file/db later
    print(f"Your balance is ${balance}")

def make_payment():
    amount = input("Enter amount to pay: ")
    print(f"Payment of ${amount} completed. Thank you!")
