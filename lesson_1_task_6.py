
a = int(input("start day result: "))
b = int(input("achieved result: "))
day = 1
if a > b:
    print("no progress")
while a<= b:
    a = a + a/10
    day += 1
print  (f"day: {day}")






