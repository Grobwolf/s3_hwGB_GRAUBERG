# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#
# Пример:
#
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
fib1 = fib2 = 1
n = int(input())
fib_list = []
for i in range(2, n+3):
    fib1, fib2 = fib2, fib1 - fib2
    fib_list.append(fib2)
sfib_list = fib_list.copy()
i = 0
i2 = -1
while i < len(fib_list) / 2:
    sfib_list[i], sfib_list[i2] = sfib_list[i2], sfib_list[i]
    i += 1
    i2 -= 1
for i in range(1, len(fib_list)):
    if fib_list[i] < 0:
        fib_list[i] *= -1
    sfib_list.append(fib_list[i])
print(sfib_list)
