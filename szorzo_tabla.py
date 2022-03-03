# Szorzotabla kiirasa
def table():
    for i in range(1, 11):
        for j in range(1, 11):
            if i*j < 10:
                print(" ", end ="")
            print(i * j, end=" ")
            j += 1
        i += 1
        print("")


table()


# Digitek kiírása visszafele
def digits(szam):
    while szam > 10:
        maradek = szam % 10
        print(maradek)
        szam = szam // 10
    print(szam)

digits(654321)

