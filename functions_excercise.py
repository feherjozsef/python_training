# Írj egy is_ascending, amely paraméterül kap 3 egész számot
# A függvény True-t ad vissza, ha a számok szigorúan növekvő sorrendben vannak.
# Ellenkező esetben, visszaad egy False értéket.
# Test esetek
# 1, 3, 6 -> True
# 1, 10, 20 -> True
# 1, 1, 1 -> False
# 20, 10, 1 -> False
# 20, 10, 20 -> False

def is_ascending(a, b, c):
    if a < b < c:               # Ez rövidíthető is return a < b < c -vel (Ez false vagy true lesz
        return True
    else:
        return False


# Írj egy word_concat függvényt, mely két szót kap paraméterként és visszaadja őket összefűzve úgy, hogy a rövidebb legyen elöl
# Test esetek
# "alma", "korte" -> "almakorte"
# "cseresznye", "meggy" -> "meggycseresznye"

def word_concat(a, b):
    if len(a) <= len(b):
        return a+b
    else:
        return b+a
