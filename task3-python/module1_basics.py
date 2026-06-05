# Упражнение №1. Карточка сотрудника
# Создание переменных разных типов для карточки сотрудника
employee_name = "Алексей Смирнов"           # тип str
employee_age = 34                           # тип int
employee_salary = 87500.50                  # тип float
is_employee_active = True                   # тип bool

# Вывод информации
print("=" * 50)
print("КАРТОЧКА СОТРУДНИКА")
print("=" * 50)
print("Имя сотрудника:", employee_name)
print("Возраст:", employee_age, "лет")
print("Зарплата:", employee_salary, "руб.")
print("Работает в настоящее время:", is_employee_active)
print("=" * 50)
print()  # пустая строка для разделения упражнений

# Упражнение №2. Приветствие
# Запрос имени и города у пользователя
user_name = input("Введите имя сотрудника: ")
user_city = input("Введите название города, где работает сотрудник: ")

# Форматированный вывод приветствия
print("\nРезультат:")
print(f"Сотрудник {user_name} работает в офисе {user_city}")
print()  # пустая строка для разделения упражнений

# Упражнение №4. Доход по вкладу
# Запрос исходных данных для расчёта дохода по вкладу
deposit_amount = float(input("Введите сумму вклада (руб.): "))
annual_interest_rate = float(input("Введите годовую процентную ставку (%): "))

# Расчёт годового дохода
yearly_income = deposit_amount * (annual_interest_rate / 100)

# Вывод результата с пояснением
print("\nРезультат:")
print(f"Сумма вклада: {deposit_amount:.2f} руб.")
print(f"Годовая ставка: {annual_interest_rate:.2f}%")
print(f"Доход за год: {yearly_income:.2f} руб.")
print()  # пустая строка для разделения упражнений