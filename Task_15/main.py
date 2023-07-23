# Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи. Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. Но вот незадача: арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!

# Входные данные
# В первой строке входного файла INPUT.TXT задано одно число N – количество арбузов. Вторая строка содержит N чисел, записанных через пробел. Здесь каждое число – это масса соответствующего арбуза. Все числа натуральные и не превышают 30000.

# Выходные данные
# В выходной файл OUTPUT.TXT нужно вывести два числа через пробел: массу арбуза, который Иван Васильевич купит теще и массу арбуза, который он купит себе.

# Input: 5 -> 5 1 6 5 9
# Output: 1 9

n1 = input('Input watermelon 1:')
n2 = input('Input watermelon 2:')
n3 = input('Input watermelon 3:')
n4 = input('Input watermelon 4:')
n5 = input('Input watermelon 5:')

watermelonArr = [n1, n2, n3, n4, n5]

min = n1
i = 0
while i < len(watermelonArr):
    if min > watermelonArr[i]:
        min = watermelonArr[i]
    i +=1
print(f"Watermelon with min weight is {min}")

max = n1
i = 0
while i < len(watermelonArr):
    if max < watermelonArr[i]:
        max = watermelonArr[i]
    i +=1
print(f"Watermelon with max weight is {max}")
