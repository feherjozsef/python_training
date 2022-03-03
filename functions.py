# Függvény definíciója
def print_employee_data():
    """Ez a függvény kiírja az alkamazott nevét és életkorát""" # Dokumentáció, ha rávisszük az egeret a hívás helyén a függvényre, akkor ezt kiírja
    # DRY = Don't Repeat Yourself
    name = "John"
    age = 30
    print("Az alkalmazott neve:", name)
    print("Az alkalmazott kora:", age)
    # A függvény végén a paraméterek törlődnek, nincs többé name és age

# Függvény meghívása
print_employee_data()   # Függvény debug-olása > Bug search > F7-et kell hasznalni F8 helyett (belép a függvénybe)

# Függvény paraméterezése
def print_employee_new(name, age):      # Csak a parameterek nevet kell megadni
    print("Az alkalmazott neve:", name)
    print("Az alkalmazott kora:", age)

print_employee_new("Jozsi", 13)         # Parameter ertekek
# Az átmásolás sorrendben történik, ez a sorrendi kötés
print_employee_new("Pista", 80)
print_employee_new("Feca", 30)

def print_dog_name(name):
    print("A kutya neve", name)


print_dog_name("Kutymuty")
print_dog_name("Vauvau")

# Függvény írása ami 2 számot vár parameternek és kiírja a két szám összegét
def print_sum(a, b):
    print("A ket szam osszege", a + b)


print_sum(3, 4)

number1 = int(input("Adj meg 1 szamot"))
number2 = int(input("Adj meg 1 masik szamot"))
print_sum(number1, number2)