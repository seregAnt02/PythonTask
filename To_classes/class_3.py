count_angola = 18
count_new_york = [1, [10, 7]]
count_chicago = 15
count_usa = [count_new_york,count_chicago ]
count_all = [count_angola, count_usa]

# summa = 0

# from array import * 

# input = [[1,1,1,1], [12,12,12,12]]
# # input.insert(1, [1,3,5,7,9]) 
# print("Array after insertion of elements: ") 
# for x in input: 
#     for y in x: 
#         print(y,end = " ")


def sum_number(count_mas) -> int:
    summa = 0
    for items in count_mas:            
        if type(items) is list:
            for y in range(len(items)):
                if type(items[y]) is list:
                    summa += sum_number(items[y])
                else:
                    summa += items[y]
        else:
            summa += items
    return summa
        
print(f'функция рекурсий: {sum_number(count_all)}')
