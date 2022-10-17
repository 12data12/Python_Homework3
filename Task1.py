# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

import random
numbers = [round(random.uniform (-99.99, 100), 2) for x in range (10)]
print(f'List of random real numbers: {numbers}')
print (f'The sum of the list elements having odd indexes is {round((sum(numbers[::2]) if numbers else 0),2)}')