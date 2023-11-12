def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Ошибка: деление на ноль"

def square_root(a):
    if a >= 0:
        return a ** 0.5
    else:
        return "Ошибка: невозможно извлечь корень из отрицательного числа"


while True:
    print("\nВыберите операцию:\n"
          "1. Сложение \n"
          "2. Вычитание\n"
          "3. Умножение\n"
          "4. Деление\n"
          "5. Извлечение корня\n"
          "6. Выход из калькулятора")

    operation = input("Введите номер операции: ")

    if operation == '6':
        print("Выход из калькулятора.")
        break

    if operation in ['1', '2', '3', '4']:
        try:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
        except ValueError:
            print("Ошибка: вы ввели строку. Введите число, чтобы продолжить пользоваться калькулятором.")
            continue
    elif operation == '5':
        try:
            num1 = float(input("Введите число: "))
        except ValueError:
            print("Ошибка: вы ввели строку. Введите число, чтобы продолжить пользоваться калькулятором.")
            continue
    else:
        print("Неверный выбор. Пожалуйста, введите число от 1 до 5.")
        continue
    if operation == '1':
        print("Результат: ", add(num1, num2))
    elif operation == '2':
        print("Результат: ", subtract(num1, num2))
    elif operation == '3':
        print("Результат: ", multiply(num1, num2))
    elif operation == '4':
        print("Результат: ", divide(num1, num2))
    elif operation == '5':
        print("Результат: ", square_root(num1))
    else:
        print("Неверный выбор. Пожалуйста, введите число от 1 до 5.")