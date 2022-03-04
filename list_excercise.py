# Írj egy függvényt amely paraméterül kap egy listát amiben nevek vannak és visszaad egy másik listát.
# A másik listába azok a nevek kerüljenek bele, amelyek John-nal kezdődnek.

def filter_johns(wordlist):
    result = []
    for name in wordlist:
        if "John" in name and name.index("John") == 0:
            result.append(name)
    return result

print(filter_johns(["John Smith", "Jane Smith", "Jack Done", "John Doe", "Jack John Man", "Johny Joe"]))
