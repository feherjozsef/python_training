#Kérd be a felhasználótól hogy hány számot szeretne megadni
#Kér be tőle pont annyi számot amennyit megadott
#Összegezzük a felhasználó által megadott csak pozitív számokat

sum = 0
count = int(input("Add meg hany szamot szeretnel megadni"))
for i in range(0, count):
    number = int(input("Add meg a " + str(i+1) + ". szamot"))
    if number > 0:
        sum +=number
print("A pozitiv szamok osszege", sum)


#While-os megoldas
# number =int(input("Add meg hany darab szammal szeretnel dolgozni: "))
# value=0
# sum =0
# counter =1
# while counter <=number:
#     value =int(input("Addj meg egy szamot: "))
#     if value > 0:
#         sum+=value
#     counter+=1
# print("paros szamok osszege: ", sum)