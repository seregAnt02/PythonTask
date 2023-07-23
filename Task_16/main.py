# Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.

# list_1 = [1, 2, 3, 4, 5]
# k = 6
# 5

list_1 = [1, 12, 6, 7, 8, 15]
k = 11
number = 0
step = k
for i in range(1, len(list_1)):         
    step_left = abs(list_1[i - 1] - k)
    step_right = abs(list_1[i] - k)    
    if step_left < step:
        step = step_left
        number = list_1[i - 1]
    if step_right < step:
        step = step_right 
        number = list_1[i]       
print(number)        
# rint(f"Самый близкий по величине элемент к заданному числу k: {max_number}")
