from math import sqrt
print("Нулова константа)", None)
print("Перша константа", False)
print("вбудована функція 1 :", chr(98))
print("вбудована функція 2 : 98(10) to 98(2) :", bin(98))
a = 4
if a == 4:
    a += 94
elif a == 5:
    a += 93
else:
    a = 98
print('if/elif/else :', a)
ii = [1,2,3,[1,2,3,[1,1,[12,12],1],4,5,6,7]]
for i1 in ii:
    print('oh',i1)
#bonus
def recursive(i):
    a1 = int()
    for i1 in i:
        if type(i1) == list :
            a1 += recursive(i1)
        else:
            a1 += i1
    return a1
print(recursive(ii))

A = -1
try:
    print("Що буде якщо", sqrt(A), "?")
except Exception as e:
    print(e)
finally:
    print("А вот воно що!")

with open("README.md", "r") as f:
    for line in f:
        print(line)
        break

xax = (lambda x: x + 1)(97)
print(xax)
