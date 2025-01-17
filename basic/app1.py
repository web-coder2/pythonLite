import math

num = float(input("input a num >>> "))

def nummer(number):
    if number < 0:
        return number * -1
    else:
        return number

print(nummer(num))


a = float(input("katet a >>> "))
b = float(input("katet b >>> "))

def hypotenuze(a, b):
    c = ((a ** 2) + (b ** 2)) ** 0.5
    return c

print(hypotenuze(a, b))
        
#Подвиг 8. Гелевая ручка стоит x рублей. Сегодня магазин предоставляет скидку в 10%
#на каждую купленную ручку. Какое наибольшее количество таких ручек можно будет купить
#на 500 рублей? Результат выведите в консоль в виде целого числа

sale = int(input("sale of the pen >>> "))
skidka = 0.1
afterSale = sale - (sale * skidka)
cash = 500
kolvo = math.floor(cash / afterSale)
print(kolvo)
