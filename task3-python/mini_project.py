# Вариант 4. Функция для ввода статей (доходов или расходов)

def input_items(category, count):
    # category - строка, например "доходов" или "расходов"
    # count - количество статей
    # Возвращает список статей (каждая - кортеж (название, сумма)) и общую сумму.

    items = []                # список для хранения статей
    total = 0.0               # общая сумма
    print(f"\nВведите {count} статей {category}:")
    for i in range(1, count + 1):
        name = input(f"  Название {i}: ")          # строка
        amount = float(input(f"  Сумма {i}: "))    # число с плавающей точкой
        items.append((name, amount))
        total += amount
    return items, total

# Основная часть программы
print("=== Учёт доходов и расходов ===")

# Запрос количества статей (целое число)
n = int(input("Сколько статей доходов/расходов вы хотите ввести? "))

# Ввод доходов
income_items, total_income = input_items("доходов", n)

# Ввод расходов
expense_items, total_expense = input_items("расходов", n)

# Расчёт остатка
balance = total_income - total_expense

# Определение статуса (условие if/else)
if balance >= 0:
    status = "профицит"
    is_profit = True          # булева переменная для демонстрации
else:
    status = "дефицит"
    is_profit = False

# Вывод результатов
print("\n--- Итоги ---")
print(f"Общий доход: {total_income:.2f} руб.")
print(f"Общий расход: {total_expense:.2f} руб.")
print(f"Остаток: {balance:.2f} руб.")
print(f"Статус бюджета: {status}")

# Дополнительный цикл for для вывода списка статей (по желанию)
print("\nДетализация доходов:")
for name, amount in income_items:
    print(f"  {name}: {amount:.2f} руб.")

print("Детализация расходов:")
for name, amount in expense_items:
    print(f"  {name}: {amount:.2f} руб.")

print("\nПрограмма завершена.")