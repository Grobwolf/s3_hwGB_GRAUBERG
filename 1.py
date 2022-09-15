# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#
# Пример:
#
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

numbers = list(map(int, input().split()))
print(numbers)
result = numbers[1]
for i in range(3, len(numbers)):
    if i % 2 != 0:
        result += numbers[i]
print(result)