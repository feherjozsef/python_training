#program gyak
name=input("Add meg a neved")
count=input("Hanyszor irjam ki a neved:") # bevitelkor is lehet integerre alakitani count=int(input("mivan"))
for i in range(0,int(count)):       #for i in range(1, count+1): VAGY for i in range(count): ekkor default-ban 0-tol indul
    print(str(i+1) + " " + name)    #print(i+1, name)

for name in ["john", "jack", "jane"]:   #listát nem legeneráltatom a range-gel hanem megadom konkrétan
    print(name)

for i in [2, 4, 6, 8, 10]:              #a ciklus változó felveszi a lista értékeit
    print(i)

