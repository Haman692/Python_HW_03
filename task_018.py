# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
import random
import math

print('Введите размер масива')
size = int(input())
arr = []
for i in range(size):
    randomNum = random.randint(1, 10)
    arr.append(randomNum)
print(arr)

print('Введите искомое число')
number = int(input())
diff = abs(number - arr[0])
if diff == 0:
    diff = 1
desiredNumberA = -1
desiredNumberB = -1
for i  in range(len(arr)):
    if diff > abs(number - arr[i]):
        if number - arr[i] > 0:
            diff = number - arr[i]
            desiredNumberA = arr[i]
        if number - arr[i] < 0:
            diff = abs(number - arr[i])
            desiredNumberB = arr[i]
    if diff == abs(number - arr[i]):
        if number - arr[i] > 0:
            desiredNumberA = arr[i]
        if number - arr[i] < 0:
            desiredNumberB = arr[i]
if desiredNumberB == -1:
    print('Ближайшее число к искомому: ' + str(desiredNumberA))
elif desiredNumberA == -1:
    print('Ближайшее число к искомому: ' + str(desiredNumberB))
else:
    print('Ближайщие числа к искомому: ' + str(desiredNumberA) + ' и ' + str(desiredNumberB))