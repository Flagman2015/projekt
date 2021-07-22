a = int(input("Enter time in seconds:"))
if a < 60:
    print(f"00:00:{a:02}")
elif a < 3600:
    print(f"00:{a // 60:02}:{a % 60:02}")
else:
    print(f"{a // 3600:02}:{(a % 3600)// 60:02}:{a % 60:02}")

