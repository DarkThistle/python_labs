def format_record(rec: tuple[str, str, float]) -> str:
    name = [i.capitalize() for i in rec[0].split()]
    return f"{name[0]} {" ".join([i[0]+"." for i in name[1:]])}, гр. {rec[1]}, GPA {rec[2]:.02f}"
print(format_record(eval(input())))