
proceeds= int(input("enter revenue: "))
losses = int(input("enter losses:"))
if proceeds > losses:
    profit= proceeds - losses
    profitability = profit / proceeds
    print(f"Congradulation! You make profit={profit} and profitability={profitability:.2f}")
    number_of_workers = int(input("Enter the number of employees of the company: "))
    print(f"Profit per worker ={profit/number_of_workers:.2f}")
elif proceeds <= losses:
    print("Sorry! no profit")

