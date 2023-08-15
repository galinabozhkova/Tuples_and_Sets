text = input()
dict_symbols = {}
for el in text:
    if el not in dict_symbols:
        dict_symbols[el] = 0
    dict_symbols[el]+=1

sorted_dict = sorted(dict_symbols.items(), key = lambda x: x[0])

for el in sorted_dict:
    print(f'{el[0]}: {el[1]} time/s')