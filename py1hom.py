#Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на позиции с нечетным индексом.

t=[1,3,5,6,2,3,41,23,2]
sum=0
for i in range (1,len(t),2):
        sum+=t[i]
print(f'Сумма элементов с нечетными индексами равна = {sum}')