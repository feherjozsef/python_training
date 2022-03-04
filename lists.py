names = []              # Üres lista
print(names)

# Listához hozzáadhatóak az elemek
names.append("John Doe")
print(names)
names.append("Jack Doe")
print(names)
names.append("Joc")
print(names)

print(names[2])
print(names[0:2])
print(names[::-1])

names[1] = "Jack Smith"
print(names)

names.remove("Jack Smith")
print(names)

numbers = [1, 2, 3]
print(numbers)

employee = ["John Doe", 20]
print(employee)
print(employee[0])
print(employee[1])

# Lista hossza = lista elemeinek száma
print(len(employee))

# Listában is megnézhető, hogy egy adott érték megtalálható-e benne
print(names)
print("John Doe" in names)
print("Coco Jambo" in names)
print("J" in names)
