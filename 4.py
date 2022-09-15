# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#
# Пример:
#
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

number = int(input())
bin_number = ""
while number > 0:
    bin_number = str(number % 2) + bin_number
    number = number // 2
print(number, "->", bin_number)