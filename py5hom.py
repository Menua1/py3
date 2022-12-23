#Задайте число. Составьте список чисел Фибоначчи,
#  в том числе для отрицательных индексов.
def Fibon(n):
    if n in [1,2]:
        return 1
    else:
        return Fibon(n-1)+Fibon(n-2)

def NeFibon(n):
    if n==1:
        return 1
    elif n==2:
        return -1
    else:
        num1,num2=1,-1
        for i in range(2,n):
            num1,num2=num2,num1-num2
        return num2
list = [0]
userNumber = int(input('Введите число: '))
for e in range(1, userNumber + 1):
    list.append(Fibon(e))
    list.insert(0, NeFibon(e))
print(list)
