#Logikai = boolean (True vagy False lehet az értéke) > ezek is literal-ok > értékül adható változóknak

are_you_a_boy=True
print(are_you_a_boy)
print(type(are_you_a_boy))

# Összehasonlító operátorok
result = 10 < 20
print("result = 10 < 20 is", result)
result = 20 < 10
print(result)
result = 10 >= 20
print(result)
result = 10 == 10
print(result)
result = 10 == 20
print(result)
print("alma" == "korte")
print("alma"=="alma")

while False:                #egyszersem fut le
    print("Hello ciklus")

# while True:               vegtelen ciklus
#     print("Hello man")

count=0
while count < 10:
    print("Hello ", count)
    count = count + 1
print("Program vege")