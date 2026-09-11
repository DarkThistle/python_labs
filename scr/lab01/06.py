n = int(input())
ochno = 0
za_ochno = 0
for i in range(n):
    user = input(f"id_{i+1}: ").split()
    if user[-1] == "True":
        ochno += 1
    elif user[-1] == "False":
        za_ochno += 1
print(f"out: {ochno} {za_ochno}")

# Тестовые данные
# 1337
# Максимов Максим 18 True
# Геннадьев Геннадий 17 False
# Алексеев Алексей 17 True