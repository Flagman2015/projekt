my_list = input("list: ")
list = my_list.split(' ')

for i in range(len(list) // 2):
     k1, k2 = 2 * i,  2 * i +1
     list[k1], list[k2] = list[k2], list[k1]

print(list)


