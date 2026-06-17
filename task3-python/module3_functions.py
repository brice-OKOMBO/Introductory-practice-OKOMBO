# ========== Упражнение 1. calculate_profit ==========
# Функция принимает выручку и затраты, возвращает прибыль.
def calculate_profit(revenue, costs):
    # revenue - выручка (доход)
    # costs - затраты (расходы)
    profit = revenue - costs   # прибыль = доход - расход
    return profit              # возвращаем результат

# Вызываем функцию с тремя парами значений
print("=== Упражнение 1 ===")
p1 = calculate_profit(100000, 70000)
print("Прибыль при 100000 и 70000:", p1)
p2 = calculate_profit(50000, 60000)
print("Прибыль при 50000 и 60000:", p2)
p3 = calculate_profit(200000, 200000)
print("Прибыль при 200000 и 200000:", p3)
print()

# ========== Упражнение 2. calculate_vat ==========
# Функция принимает цену и ставку НДС (по умолчанию 20% = 0.2),
# возвращает сумму налога.
def calculate_vat(price, vat_rate=0.20):
    # price - цена товара
    # vat_rate - ставка (по умолчанию 20%)
    vat = price * vat_rate   # налог = цена × ставка
    return vat

print("=== Упражнение 2 ===")
# Вызов с явной ставкой (10%)
vat1 = calculate_vat(1000, 0.10)
print("НДС 10% от 1000 руб.:", vat1)
# Вызов со стандартной ставкой (20%) — второй параметр не пишем
vat2 = calculate_vat(1000)
print("НДС 20% от 1000 руб.:", vat2)
# Ещё один пример
vat3 = calculate_vat(2500)
print("НДС 20% от 2500 руб.:", vat3)
print()

# ========== Упражнение 3. get_category ==========
# Функция возвращает категорию бизнеса по годовой выручке.
def get_category(revenue):
    # revenue - годовая выручка
    if revenue < 1_000_000:
        return "Микробизнес"
    elif revenue < 10_000_000:
        return "Малый бизнес"
    elif revenue < 100_000_000:
        return "Средний бизнес"
    else:
        return "Крупный бизнес"

print("=== Упражнение 3 ===")
# Тестируем на 4 разных значениях
print("500000 руб. ->", get_category(500000))
print("5 млн руб. ->", get_category(5_000_000))
print("50 млн руб. ->", get_category(50_000_000))
print("200 млн руб. ->", get_category(200_000_000))
print()

# ========== Упражнение 4. compound_interest ==========
# Функция принимает капитал, годовую ставку (%) и срок (лет),
# возвращает итоговую сумму по формуле сложного процента.
def compound_interest(capital, rate_percent, years):
    # capital - начальная сумма
    # rate_percent - процентная ставка (например, 7 для 7%)
    # years - количество лет
    multiplier = 1 + rate_percent / 100   # коэффициент роста (например, 1.07)
    total = capital * (multiplier ** years)  # возводим в степень years
    return total

print("=== Упражнение 4 ===")
start = 100000   # начальный капитал 100 000 руб.
rate = 7         # 7% годовых
# Выводим для 3, 5 и 10 лет
for years in (3, 5, 10):
    result = compound_interest(start, rate, years)
    print(f"Через {years} лет: {result:.2f} руб.")
print()

# ========== Упражнение 5. apply_discount ==========
# Функция принимает цену и процент скидки, возвращает новую цену.
def apply_discount(price, discount_percent):
    # price - исходная цена
    # discount_percent - скидка в процентах (например, 15 для 15%)
    new_price = price * (1 - discount_percent / 100)  # цена со скидкой
    return new_price

print("=== Упражнение 5 ===")
# Список из 5 товаров (цены)
prices = [1200, 3500, 500, 8000, 250]
discount = 15   # 15% скидка
print(f"Скидка {discount}% на все товары:")
for i, price in enumerate(prices, start=1):
    discounted = apply_discount(price, discount)
    print(f"Товар {i}: {price} руб. -> {discounted:.2f} руб.")