number_list =[1,2,4,5,7,8,10]
unique =[]
for number in number_list:
    if number not in unique:
      unique.append(number)
print(unique)