# Задача №7. Решение в группах
# Дано натуральное число. Требуется определить,
# является ли год с данным номером високосным. Если
# год является високосным, то выведите YES, иначе
# выведите NO. Напомним, что в соответствии с
# григорианским календарем, год является
# високосным, если его номер кратен 4, но не кратен
# 100, а также если он кратен 400.
# Input: 2016
# Output: YES


age = int(input("Введите год: "))
if (age % 4 == 0 and age % 100 != 0 or age % 400 == 0):
    print("Yes")
else:
    print("No")
