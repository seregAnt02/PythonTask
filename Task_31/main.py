
# Последовательностью Фибоначчи называется последовательность чисел
# a0, a1, ..., an, ..., где a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).

# Требуется найти N-е число Фибоначчи

# Input: 7
# Output: 21

# Задание необходимо решать через рекурсию



n = int(input('Введите порядковый номер числа Фибоначчи: '))


def fib(n):           # создаем метод (рекурсию)
    if n in (0,1):    # базис рекурсии - кортеж а не список, т.к. он быстрее работает
        return 1
    return fib(n-1) + fib(n-2) # сама рекурсия (формула расчета)
print(f'Порядковому номеру {n} соответствует значение {fib(n)}')
