revenue = float(input("Введите выручку фирмы - "))
cost = float(input("Введите издержки фирмы - "))
if revenue > cost:
    income = revenue - cost
    profitability = revenue / cost
    print(
        f"Поздравляем, ваша фирма работает с прибылью - {income:.2f}! Рентабельность вашей выручки {profitability:.2f}")
    staff = int(input("Введите количество сотрудников фирмы"))
    profit_per_staff = income / staff
    print(f"Прибыль фирмы в расчете на одного сотрудника {profit_per_staff:.2f}")
elif revenue == cost:
    print("Ваша фирма пока работает без прибыли, но покрывает издержки")
else:
    print("К сожалению, ваша фирма убыточна и не покрывает издержки")