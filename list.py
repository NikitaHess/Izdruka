#[1 , 2, 2, "teksts", 3.56, [1, "objekts"]] #list(saraksti)

my_list = ['STRING', 100, 23.5, 'soma']
print(my_list)
print(len(my_list))

mylist = ["viens", "divi", "trīs", "četri"]
print(mylist[0]) #elements ar noradito indeksu
print(mylist[1:])

#sarakstu apvienosana (konkatinacija)
cits_list = ["pieci", "cetri"]
print(mylist + cits_list)
jauns_list = mylist + cits_list
print(jauns_list)

#saraksta mainisana
jauns_list[0] = 1 #define konkreta elementa vertibu
print(jauns_list)
jauns_list.append("septini")
print(jauns_list)
jauns_list.append(8)
print(jauns_list)

#elementu nonemsana
pop_elements = jauns_list.pop()
print(pop_elements)
print(jauns_list)
jauns_list.pop(0) #iznem no saraksta elementu ar noradito indeksu
print(jauns_list)

#elementu kartosana
new_list = ['b', 'a', 'e', 'c']
num_list = [4, 1, 8, 3]
new_list.sort()
print(new_list)
num_list.sort()
print(num_list)
#reverse
num_list.reverse()
print(num_list)
new_list.reverse()
print(new_list)

#saraksts saraksta (nested list)
nested_list = [2,4,[5,8]]
print(len(nested_list))
print(nested_list[1])
print(nested_list[1])
