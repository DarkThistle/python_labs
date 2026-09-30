def format_record(rec: tuple[str, str, float]) -> str:
    if type(rec) != tuple:
        raise TypeError("Прошу умоляю введите кортеж")
    if not 0.0 <= rec[2] <= 5.0 or len(rec) == 0 or rec[0] == "" or rec[1] == "" or len(rec) < 3 or len(rec[0].split()) not in [2, 3] or any([rec[1][i]=="-" for i in [0, -1]]) or not all([i.isalnum() for i in rec[1].split("-")]):
        raise ValueError
    if type(rec[2]) != float or type(rec[0]) != str or type(rec[1]) != str:
        raise TypeError
    name = [i.capitalize() for i in rec[0].split()]
    return f"{name[0]} {" ".join([i[0]+"." for i in name[1:]])}, гр. {rec[1]}, GPA {rec[2]:.02f}"

test1 = ("Иванов Иван Иванович", "BIVT-25", 4.6)
test2 = ("Петров Пётр", "IKBO-12", 5.0)
test3 = ("Петров Пётр Петрович", "IKBO-12", 5.0)
test4 = ("  сидорова  анна   сергеевна ", "ABB-01", 3.999)
print(f"Ввод: {test1}\nВывод: {format_record(test1)}")
