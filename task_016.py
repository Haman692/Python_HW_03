# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
import random


print('Введите размер масива')
size = int(input())
array = []
for i in range(size):
    randomNumber = random.randint(1, 10)
    array.append(randomNumber)
print(array)
print('Введите искомое число')
desiredNumber = int(input())
counter = 0
for i in range(len(array)):
    if int(array[i]) == desiredNumber:
        counter += 1
print('Искомое число нашлось ' + str(counter) + ' раз')