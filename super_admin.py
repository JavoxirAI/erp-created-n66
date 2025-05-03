from file_manager import read, write
from datetime import datetime


def show_all_admins():
    users = read("user.csv")
    if not users:
        print("Adminlar topilmadi.")
        return

    for user in users:
        if user[3] == "admin":
            print(f"ID: {user[0]}, Username: {user[1]}, Yaratilgan sana: {user[4]}")


def create_admin():
    users = read("user.csv")

    if len(users) > 1:
        last_id = int(users[-1][0])
    else:
        last_id = 0

    new_id = last_id + 1
    username = input("Yangi admin username: ")
    password = input("Parol: ")
    created_at = datetime.now().strftime("%Y-%m-%d")

    new_admin = [str(new_id), username, password, "admin", created_at]

    write("user.csv", new_admin, mode="a")
    print("Admin muvaffaqiyatli yaratildi!")




def delete_admin():
    users = read("user.csv")

    if len(users) <= 1:
        print("Adminlar mavjud emas.")
        return

    admin_id = input("O'chirmoqchi bo'lgan admin ID sini kiriting: ")

    new_users = [users[0]]
    found = False

    for user in users[1:]:
        if user[0] == admin_id and user[3] == "admin":
            found = True
            continue
        new_users.append(user)

    if found:
        write("user.csv", new_users, mode="w")
        print("Admin muvaffaqiyatli o‘chirildi.")
    else:
        print("Bunday ID li admin topilmadi.")


def show_statistics():
    users = read("user.csv")
    if len(users) <= 1:
        print("Hech qanday foydalanuvchi mavjud emas.")
        return

    total_users = 0
    admin_count = 0
    teacher_count = 0
    student_count = 0

    for user in users[1:]:
        role = user[3]
        total_users += 1
        if role == "admin":
            admin_count += 1
        elif role == "teacher":
            teacher_count += 1
        elif role == "student":
            student_count += 1

    print(f"\nStatistika:")
    print(f"Jami foydalanuvchilar: {total_users}")
    print(f"Adminlar soni: {admin_count}")
    print(f"Teacherlar soni: {teacher_count}")
    print(f"Studentlar soni: {student_count}")

