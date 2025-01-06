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
