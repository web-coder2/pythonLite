string = input("input 2 words >>")
s1 = string.split(" ", 1)[0]
s2 = string.split(" ", 1)[1]

if s1 in s2:
    print("first word was in second word")
else:
    print("first word dont into second word")

print(s1 == s2)
print(s1 < s2)
print(s1 > s2)


#3.2 Индексы и срезы строк

#Подвиг 1. Напишите программу ввода строки и отображения на экране
#ее первого и последнего символа в виде одной строки.

#Sample Input: I love Python
#Sample Output: In

text = input("input a text with spaces >>> ")
textSym1 = text[0]
textSymLast = text[len(text) - 1]

print(textSym1, " ", textSymLast)


#3.2 Индексы и срезы строк

#Подвиг 4. Напишите программу отображения первых четырех символов
#из введенной строки. Будем полагать, что строка гарантированно
#длиной не менее четырех символов.

#Sample Input: panda
#Sample Output: pand

checkStatus = True

while checkStatus:
    teta = input("input a word where her length > 4 symbols >>> ")
    if len(teta) < 4:
        checkStatus = True
    else:
        print(teta[0], teta[1], teta[2], teta[3])
        checkStatus = False
