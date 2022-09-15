# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#
# Пример:
#
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
numbers = list(map(float, input().split()))
fraction_numbers = []
def fraction(n):
    decimal = divmod(n, 1)
    return round(list(decimal)[1], 10)
for i in range(0, len(numbers)):
    fraction_numbers.append(fraction(numbers[i]))
print(fraction_numbers)
max = 0
min = 1
for i in range(0, len(fraction_numbers)):
    if fraction_numbers[i] < min and fraction_numbers[i] != 0:
        min = fraction_numbers[i]
    if fraction_numbers[i] > max:
        max = fraction_numbers[i]
print(numbers, "=>", max - min)





