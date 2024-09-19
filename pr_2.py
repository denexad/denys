hello = "Hello, World!"
name = "Denis"
last_name = "Panasiyk"
year = 16

print(type (hello), type (name), type (last_name), type (year)) 

type_lst = (type (hello), type (name), type (last_name), type (year)) 

values = [ hello, name, last_name, year]

types = [type(value) for value in values]

type_count = {}
for t in types :
    if t in type_count:
        type_count[t] += 1
    else:
        type_count[t] = 1

most_common_type = max(type_count, key=type_count.get)

print("Найчастіше зустрічається тип даних: {most_common_type.__name__}, кількість повторень: {type_count[most_common_type]}")
