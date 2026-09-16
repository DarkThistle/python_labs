m = int(input("Минуты: "))
hours, mins = m//60, m%60
print(f"{hours}:{mins:02d}")