price_all = 0
while True:
    try:
        tickets = int(input("Сколько Вам необходимо билетов?"))
        if type(tickets) == int:
            break
    except ValueError:
        print("Введите целое число")
for i in range(tickets):
    i += 1
    while True:
        try:
            age = int(input(f"Для какого возраста билет № {i}"))
            if age < 18:
                print("Вход бесплатно")
            elif 18 <= age <= 25:
                price_all += 990
                print("Стоимость билета 990р")
            else:
                price_all += 1390
                print("Стоимость билета 1390р")
            if type (age) == int:
                break
        except ValueError:
            print("Введите целое число")
if tickets >= 3:
    price_all = price_all / 100 * 90
    print(f"Сумма к оплате {price_all} рублей")
else:
    print(f"Сумма к оплате {price_all} рублей")
