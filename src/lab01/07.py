input_info = input("in: ")
first_symbol_id = input_info.find(str([i for i in input_info if i.isupper()][0]))
dot_id = input_info.find(".")
print(f"out: {input_info[first_symbol_id:dot_id+1:3]}")

# test: thisisabracadabraHt1eadljjl12ojh.