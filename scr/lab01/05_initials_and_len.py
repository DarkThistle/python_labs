name = [i for i in input("ФИО: ").split()]
print(f'Инициалы: {"".join(i[0] for i in name)}.\nДлина (символов): {sum(len(i) for i in name)+(len(name)-1)}')
