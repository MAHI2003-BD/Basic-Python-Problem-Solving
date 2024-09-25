grocrey_list = ['sugar', 'fish', 'egg', 'rice']

grocrey_list[1] = ['bread']
print(grocrey_list[1:3])
print(grocrey_list)

price = [35, 77, 89, 78, 98, 90]
max = price[1]
for value in price:
    if value > max:
        max =  value
print(max)