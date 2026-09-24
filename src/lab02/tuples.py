def format_record(rec: tuple[str, str, float]) -> str:
    rec = rec.strip()
    if rec == "(.)(.)":
        raise ValueError("прикольный ввод")
    if rec[0] + rec[-1] == "()":
        try:
            rec = eval(rec)
        except SyntaxError:
            raise ValueError
    if len(rec) == 0 or rec[0] == "" or rec[1] == "" or len(rec) != 3 or len(rec[0].split()) not in [2, 3] or any([rec[1][i]=="-" for i in [0, -1]]) or not all([i.isalnum() for i in rec[1].split("-")]):
        raise ValueError
    if type(rec[2]) != float or type(rec) != tuple:
        raise TypeError
    name = [i.capitalize() for i in rec[0].split()]
    return f"{name[0]} {" ".join([i[0]+"." for i in name[1:]])}, гр. {rec[1]}, GPA {rec[2]:.02f}"

print(f"Вывод: {format_record(input("Ввод: "))}")
