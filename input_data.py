#Kérjük be a fehl nevét, ha üres a mező, akkor írjuk ki hogy nem lehet üres értéket megadni és kérjük be mégegyszer
#Ha viszont nem üres írjuk ki hogy köszönöm

name = ""
while name =="":
    name=input("Add meg a neved")
    if name =="":
        print("Nem jo, adj meg egy nevet")
print("koszonom")