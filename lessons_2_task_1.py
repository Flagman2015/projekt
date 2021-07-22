my_list = [12, 'None', -77, 'True', 'false', 9.5, [1, 2, 7], (9, 2)]
def my_type(el):
     for el in range(len(my_list)):
         print(type(my_list[el]))
     return
my_type(my_list)