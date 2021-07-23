a= input("введите строку ")
b = []
num = 1
for el in range(a.count(' ') + 1):
     b = a.split()
     if len(str(b)) <= 10:
         print(f" {num} {my_word [el]}")
         num += 1
     else:
         print(f" {num} {b [el] [0:10]}")
         num += 1