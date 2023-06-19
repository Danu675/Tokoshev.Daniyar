date = int(input("Введите день вашего рождения = "))
month = int(input("Введите месяц вашего рождения = "))
year = int(input("Введите год вашего рождения = "))
if (date >= 21 and date <= 31 and month == 3) or (month == 4 and date <= 20 and date >= 1):
    print("ваш знак зодиака Овен")
elif (date >= 21 and date <= 30 and month == 4) or (month == 5 and date <= 21 and date >= 1):
    print("ваш знак зодиака Телец")
elif (date >= 22 and date <= 31 and month == 5) or (month == 6 and date <= 21 and date >= 1):
    print("Ваш знак зодиака Близнецы")
elif (date >= 22 and date <= 30 and month == 6) or (month == 7 and date <= 22 and date >= 1):
    print("Ваш знак зодиака Рак")
elif (date >= 23 and date <= 31 and month == 7) or (month == 8 and date <= 21 and date >= 1):
    print("Ваш знак зодиака Лев")
elif (date >= 22 and date <= 31 and month == 8) or (month == 9 and date <= 23 and date >= 1):
    print("Ваш знак зодиака Дева")
elif (date >= 24 and date <= 30 and month == 9) or (month == 10 and date <= 23 and date >= 1):
    print("Ваш знак зодиака Весы")
elif (date >= 24 and date <= 31 and month == 10) or (month == 11 and date <= 22 and date >= 1):
    print("Ваш знак зодиака Скорпион")
elif (date >= 23 and date <= 30 and month == 11) or (month == 12 and date <= 22 and date >= 1):
    print("ваш знак Зодиака Стрелец")
elif (date >= 23 and date <= 31 and month == 12) or (month == 1 and date <= 20 and date >= 1):
    print("Ваш знак Зодиака Козерог")
elif (date >= 21 and date <= 31 and month == 1) or (month == 2 and date <= 19 and date >= 1):
    print("Ваш знак Зодиака Водолей")
elif (date >= 20 and date <= 28 and month == 2) or (month == 3 and date <= 20 and date >= 1):
    print("Ваш знак Зодиака Рыбы")
else:
    print("Ошибка , Введите коректные значения !!!")