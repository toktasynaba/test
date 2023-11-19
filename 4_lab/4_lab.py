import re

user_list = []

def add_user():
    print("Добавление нового пользователя:")
    user = {}
    user["Name"] = input("Имя: ")
    user["Surname"] = input("Фамилия: ")
    while True:
        try:
            user["Age"] = int(input("Возраст: "))
            break
        except ValueError:
            print("Введите корректный возраст (целое число).")
    user["Address"] = input("Адрес: ")
    user["Username"] = input("Имя пользователя: ")
    while True:
        password = input("Пароль (минимум 8 символов): ")
        if len(password) >= 8:
            user["Password"] = password
            break
        else:
            print("Пароль должен содержать не менее 8 символов.")

    while True:
        user_email = input("Email: ")
        if not any(existing_user.get("Email") == user_email for existing_user in user_list):
            user["Email"] = user_email
            break
        else:
            print("Пользователь с таким email уже существует.")

    user_list.append(user)
    print("Пользователь успешно добавлен!\n")

def edit_user():
    print("Редактирование пользователя:")
    username_to_edit = input("Введите имя пользователя для редактирования: ")

    for user in user_list:
        if user["Username"] == username_to_edit:
            print(f"Текущая информация о пользователе {username_to_edit}: {user}")
            user["Name"] = input("Имя: ")
            user["Surname"] = input("Фамилия: ")
            while True:
                try:
                    user["Age"] = int(input("Возраст: "))
                    break
                except ValueError:
                    print("Введите корректный возраст (целое число).")
            user["Address"] = input("Адрес: ")
            while True:
                password = input("Пароль (минимум 8 символов): ")
                if len(password) >= 8:
                    user["Password"] = password
                    break
                else:
                    print("Пароль должен содержать не менее 8 символов.")

            while True:
                user_email = input("Email: ")
                if not any(existing_user.get("Email") == user_email for existing_user in user_list):
                    user["Email"] = user_email
                    break
                else:
                    print("Пользователь с таким email уже существует.")

            print(f"Информация о пользователе {username_to_edit} успешно обновлена!\n")
            return

    print(f"Пользователь с именем пользователя {username_to_edit} не найден.\n")

def delete_user():
    print("Удаление пользователя:")
    username_to_delete = input("Введите имя пользователя для удаления: ")

    for user in user_list:
        if user["Username"] == username_to_delete:
            user_list.remove(user)
            print(f"Пользователь {username_to_delete} успешно удален!\n")
            return

    print(f"Пользователь с именем пользователя {username_to_delete} не найден.\n")

def view_users():
    print("Список пользователей:")
    for user in user_list:
        print(user)
    print()

def login():
    print("Вход в систему:")
    username = input("Имя пользователя: ")
    password = input("Пароль: ")

    for user in user_list:
        if user["Username"] == username and user["Password"] == password:
            print("Вход выполнен успешно!\n")
            return

    print("Ошибка входа. Проверьте имя пользователя и пароль.\n")

def main():
    while True:
        print("1. Добавить пользователя")
        print("2. Редактировать пользователя")
        print("3. Удалить пользователя")
        print("4. Просмотреть список пользователей")
        print("5. Войти в систему")
        print("6. Выйти из программы")

        choice = input("Выберите действие: ")

        if choice == "1":
            add_user()
        elif choice == "2":
            edit_user()
        elif choice == "3":
            delete_user()
        elif choice == "4":
            view_users()
        elif choice == "5":
            login()
        elif choice == "6":
            print("Программа завершена.")
            break
        else:
            print("Неверный выбор. Пожалуйста, введите число от 1 до 6.")

main()