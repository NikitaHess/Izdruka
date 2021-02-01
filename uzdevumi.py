
x = input("Ievadi teikumu: ")
print(len(x)) # 1 uzd

x = input("Ievadi vārdu: ")
print(x[0]) # 2 uzd      

x = "Sveika, Pasaule!"
print(x[-6:-1]) # 3 uzd

x = input("Ievadi teikumu: ")
print("Tavs ievadītais teikums ir " + (x.upper())) # 4 uzd

x = input("Ievadi teikumu: ")
print("Tavs ievadītais teikums ir " + (x.lower())) # 5 uzd

vards = "samērcēt"
ped_burti = vards[1:]
print("p" + ped_burti) # 6 uzd

x = "    Sveika, Pasaule!    "
print(x.strip())  # 7 uzd



#8 Uzdevums
#Izveidot programmu, kura vārdam nomaina pirmo burtu uz mazo
#Piemērs:

#Ievade: Nikita
#Izvade: nikita
vards = input('Ievadi savu vārdu: ')
vards =vards[0].lower()+ vards[1:]
print(vards)


vards = str(input('Ievadi vārdu: '))
first = vards[0]
vards = vards.lower()
vards = vards[::-1]
vards = vards.capitalize()
print(vards+". Pamatīgs juceklis, vai ne,",first) # 9 uzd