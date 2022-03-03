year = int(input("Add meg a szuletesi eved"))
min_year = 1900
actual_year = 2022
if year > actual_year or year < min_year:
    print("Helytelen szuletesi ev")
else:
    print("Az eletkorod", actual_year - year, "év")