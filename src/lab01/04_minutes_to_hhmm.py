m = int(input("Минуты: "))
hours, mins = (m//60)%24, m%60

print(f"{hours:02d}:{mins:02d}")