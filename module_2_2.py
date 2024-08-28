num1 = int(input("Введите 3 целых числа:"))
first = num1
num2 = int(input("Введите ещё одно число:"))
second=num2
num3 = int(input("Введите последнее число:"))
third =num3
if first==second and first==third and second==third:
    print("Вы ввели три одинаковых числа")
elif first!=second and first!=third and second!=third:
    print("Вы ввели ноль одинаковых чисел")
else:
    print("Вы ввели два одинаковых числа")
