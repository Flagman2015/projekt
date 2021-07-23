my_list = [7, 5, 4, 3, 3, 3, 2, 1]

rat = int(input("Введите число  "))
inserted = False
for i, e in enumerate(my_list):
    if rat > e:
       my_list.insert(i, rat)
       inserted = True
       break

if not inserted:
    my_list.append(rat)

print(my_list)




