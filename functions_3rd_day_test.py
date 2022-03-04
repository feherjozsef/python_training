# Teszt eset == python függvény
from functions_3rd_day import get_max   # Fájl kiterjesztését nem kell odaírni. A file hivatalos elnevezése: "modul"


def test_get_max():
    # given: input adatok
    a = 5
    b = 10
    # when: megkapjuk az aktuális értéket
    result = get_max(a, b)  # Másik file-ban lesz a függvény, ezért importálni kell > rávisszük az egeret és rányomunk az import-ra (A fenti rész automatikusan megjelenik)
    # then: leellenőrizzük, hogy az aktuális érték megegyezik-e a kapott értékkel, ezt az assert-tel tesszük meg
    assert result == 10


def test_get_max_when_first_value_is_greater():
    assert get_max(200, 5) == 200


def test_get_max_equal_values():
    assert get_max(100, 100) == 100


