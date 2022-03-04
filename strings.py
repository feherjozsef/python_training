name = "John Doe"

# A str Immutable - módosíthatatlan

print(name.upper())         # Nagybetűsíti a nevet > Ez a függvény egy újabb string-et ad vissza és az kerül kiírásra (nem módosítja a régi string-et)
print(name.lower())

print(name[0])              # Kiírja az első karaktert 0. index
print(name[6])

# Ha a string változó értékét meg szeretnénk változtatni, akkor felül kell írni a régi változót:
name = name.upper()
print(name)

# Karakterek bejárása a string-ben
for c in name:
    print(c)

# String hossza
print(len(name))

# String szeletelése
print(name[2:5])        # Balról zárt és jobbról nyílt 2-es 3-as 4-es karaktert adja vissza > substring

print(name[2:])         # 2-től a string végéig
print(name[:6])         # 0. karaktertől a 6-osig
print(name[0:7:2])      # 0. karaktertől a 7. karakterig kiad minden második karaktert
print(name[::-1])       # Visszafele adja ki a string-et
print(name[:-1])        # utolsó karaktert elhagyja, hátulról indexelünk
print(name[0:3] + name[4:6])

filename = "doomdoom.exe"
print(filename[-3:])    # Az utolsó 3 karaktert adja vissza
ip = "192.168.0.1"
print(ip[-1:])


print("alma" == "alma")
print("alma" == "korte")
# ABC szerint hasonlítja össze
print("alma" > "korte")
print("alma" < "korte")

print("a" in "alma")    # Megnézi, hogy benne van-e a string-ben
print("al" in "alma")
print("la" in "alma")
print("alma" in "alma")
print("b" in "alma")


# Írj egy olyan függvényt ami megszámolja, hogy hány darab "a" betű van 1 szóban.

def is_a_in_string(word):
    count = 0
    for c in word:
        if c == 'a':
            count += 1
    return count

# def test_is_a_in_string():
#     assert is_a_in_string("alma") == 2
#
# def test_is_a_in_string2():
#     assert is_a_in_string("paplanja") == 3
#
# def test_is_a_in_string3():
#     assert is_a_in_string("cold") == 0


# Írj egy olyan függvényt, amely paraméterül kap 1 szót és megszámolja, hogy hány magánhangzó van benne

def char_counter(word: str) -> int:
    counter = 0
    for c in word:
        if c in "aeiou":
            counter += 1
    return counter

# def test_char_counter():
#     assert char_counter("almakolabuborek") == 7
#
# def test_char_counter2():
#     assert char_counter("mlmnmj") == 0
#
# def test_char_counter3():
#     assert char_counter("aaabbeecckkiiuukllko") == 10




# Írj egy függvényt, amely kap egy szót és visszaadja a benne szereplő betűket *-gal elválasztva
# Az utolsó  karakter után ne legyen csillag

def star(word):
    star_word = ""
    for c in word:
        star_word += c + "*"
    return star_word[:-1]

# def test_star():
#     assert star("XYZ") == "X*Y*Z"
#
# def test_star2():
#     assert star("kalap") == "k*a*l*a*p"
#
# def test_star3():
#     assert star("roka") != "r*o*k*a*"

# Írj egy függvényt amely visszaadja, hogy a paraméterként átadott szó palindrom-e

def palindrom(word):
    return word == word[::-1]

# def test_palindrom():
    # assert palindrom("indulagorogaludni")
#
# def test_palindrom2():
#     assert not palindrom("indul a gorog aludni")
#
# def test_palindrom3():
#     assert not palindrom("kutya")
#
# def test_palindrom4():
#     assert palindrom("anna")

# Írj egy függvényt ami a paraméterként átadott szóból kiveszi a szóközöket és azt adja vissza

def space_killer(word):
    word_without_space = ""
    for c in word:
        if c != " ":
            word_without_space += c
    return word_without_space

# def test_space_killer():
#     assert space_killer("indul a gorog aludni") == "indulagorogaludni"
#
# def test_space_killer2():
#     assert space_killer("alma ") == "alma"

# def test_space_killer3():
#     assert space_killer(" alma ") == "alma"

# Megkeresi az indexét az stringen belül
name = "John Doe"
print(name.index("Doe"))
print(name.index("J"))


print("alma korte barack".split())  #szétszedi listába a string-et (alap elválasztó character a space

fruits = "alma korte barack"
fruit_list = fruits.split()
print(fruit_list)

for n in fruit_list:
    print(n)

names = "john doe jack doe jane doe"
print(names.upper()[4:15].split())

ip = "192.168.1.1"
print("192.168.1.1".split("."))

for number in ip.split("."):
    print(int(number))

