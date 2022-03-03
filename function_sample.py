# Hozz létre egy is_even nevű függvényt,
# amely True-t ad vissza, ha a paraméterként megadott
# érték páros, egyéb esetben False-t adjon vissza
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

def is_even2(number):
    return number % 2 == 0

print(is_even(4))
print(is_even2(4))
print(is_even(5))
print(is_even2(5))

# Feladat 1
# Hozz létre egy sum_negatives függvényt, mely paraméterül kap egy listát,
# és összegzi a benne szereplő negatív számokat, és azzal tér vissza
def sum_negatives(numbers):
    sum_neg = 0
    for i in numbers:
        if i < 0:
            sum_neg += i
    return sum_neg


list_of_numbers = [1, 3, -1, -10, -7, 3]
print(sum_negatives(list_of_numbers))
# Feladat 2
# Hozz létre egy to_minutes függvényt, mely paraméterül megkapja
# az órák számát, és visszatér a percek számával
def to_minutes(hours):
    return hours * 60


print(to_minutes(6))
print(to_minutes(3))
# Feladat 3
# Hozz létre egy input_number függvényt, melynek legyen egy
# paramétere. A függvény bekér a felhasználótól egy szöveget
# a paraméterrel megadott szöveggel, számmá konvertálja és azt adja vissza
def input_nr2(message):
    return int(input(message))


print(type(input_nr2("Adj meg egy szamot")))

# Feladat 4
# Írjatok egy annotate_every_even_number függvényt, mely kap egy
# számok listáját, és kiírja őket egymás alá, de minden másodikat
# egy karakterrel beljebb ír ki
def annotate_every_even_number(nr_list):
    counter = 1
    for i in nr_list:
        if counter % 2 == 0:            # if is_even(counter): Korábbi fügvény is használható
            print(" "+str(i))
        else:
            print(i)
        counter += 1


annotate_every_even_number([1, 4, 5, 7, 9])

def annotate2(nr_list):
    even_number = False
    for i in nr_list:
        if even_number:            # if is_even(counter): Korábbi fügvény is használható
            print(" "+str(i))
        else:
            print(i)
        even_number = not even_number

annotate2(([1, 4, 5, 7, 9]))
# Feladat 5
# Írj egy concatenate_shorts függvényt, mely paraméterül kap szavak listáját
# és csak a 3 karakternél rövidebb szavakat fűzze össze egy stringbe,
# és ezt adja vissza

def concatenate_shorts(list_of_words):
    concetanated_str = ""
    for word in list_of_words:
        if len(word) < 3:
            concetanated_str +=word
    return concetanated_str


print(concatenate_shorts(["asd", "ls", "cd", "dvd", "gugli"]))
