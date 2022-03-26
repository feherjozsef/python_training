# Írjatok egy get_max nevű függvényt
# aminek paraméterül át lehet adni két lebegőpontos számot és adja vissza a kettő közül a nagyobbat


def get_max(num1: float, num2: float) -> float:  #Type hint alkalmazható a paraméterekre és a visszatérési értékre. Float-okat várunk és float-tal térünk vissza.
    if num1 > num2:
        return num1
    else:
        return num2

print(get_max(20, 10))
print(type(get_max(20.3, 10.1)))
print(type(get_max(20, 10.1)))


# Írjatok egy beszédes print_square függvényt, ami paraméterül kap két egész számot. Rajzoljon ki egy ekkora téglalapot csillagokból
# 4, 3
# ****
# *  *
# ****

def print_square(width, height):            # Ezt még le kell kezelni 1-re és 0-ra
    if width > 1 or height > 1:
        return
    full_row = "*" * width
    center_row = "*" + (width-2) * " " + "*"
    print(full_row)
    for i in range(0, height-2):
        print(center_row)
    print(full_row)


print_square(4,3)

# String ismétlése kétféleképpen
def repeat_str(s: str, count: int) -> str:
    # return s * count
    result = ""
    for i in range(0, count):
        result +=s
    return result

print(repeat_str("XYZ", 3))
# Írjatok egy függvényt ami paraméterül megkapja a szavak listáját és visszaadja ezeket összefűzve, de mindegyiket gondolatjel között
# -alma--korte--meggy-
def star(words: list) -> str:
    sum_word = ""
    for word in words:
        sum_word += "-" + word + "-"
    return sum_word

print(star(["alma", "korte", "malna"]))