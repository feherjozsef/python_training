# Visszatérési értékkel rendelkező függvény
def calculate_sum(a, b):                # A fv definíciójában lévő értékeket "formális paraméter"-eknek hívják
    return a + b


print(calculate_sum(8, 10))             # A hívás helyén lévő értékeket "aktuális paraméter"-nek hívják
# Függvény híváskor az aktuális paraméterek értékei átmásolódnak a formális paraméterekbe
result = calculate_sum(1, 2)
print(result)

# Függvény paraméterei lehetnek további függvények, illetve kifejezések. Akár a függvény saját magát is meghívhatja paraméternek
print(6 + calculate_sum(7, 9))
print(calculate_sum(1+2, 3*4))

print(calculate_sum(len("alma"), calculate_sum(10, 8+2)))