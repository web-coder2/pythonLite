#Подвиг 2. Вводится слово. Необходимо первую букву этого слова
#сделать заглавной, а остальные - малыми.
#Результат отобразить на экране.

str1 = input("input str1 >>> ")

uppered = str1.split(str1[1], 1)[0].upper()
lowered = str1.split(str1[0], 1)[1].lower()

str2 = uppered + lowered
print(str2)


#3.3 Основные методы строк

#Подвиг 3. Вводится строка. Необходимо определить число вхождений
#дефисов (-) в этой строке. На экране отобразить полученное число.

#Sample Input: osnovnye-metody-strok
#Sample Output: 2

str3 = input("input str3 >>> ")

countMinus = 0

for i in range(len(str3)):
    if str3[i] == "-":
        countMinus += 1

print("in str3 count of - = " + str(countMinus))

#3.3 Основные методы строк

#Подвиг 6. Вводится строка. С помощью метода String.find
#найдите в этой строке индекс первого вхождения
#фрагмента "ra". Полученное число выведите на экран.

#Sample Input: abrakadabra
#Sample Output: 2

str4 = input("input str with 'ra' >>> ")

for j in range(len(str4)):
    if str4[j] == "r" and str4[j+1] == "a":
        print(j)
        break
    else:
        pass
