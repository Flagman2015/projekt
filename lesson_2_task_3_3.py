list = ['winter', 'spring', 'summer', 'autumn']
month = int(input("Введите месяц по номеру "))
if month ==1 or month == 12 or month == 2:
    print(seasons_list[0])
elif month == 3 or month == 4 or month ==5:
    print(list[1])
elif month == 6 or month == 7 or month == 8:
    print(list[2])
elif month == 9 or month == 10 or month == 11:
    print(list[3])
else:
    print("Такого месяца не существует")