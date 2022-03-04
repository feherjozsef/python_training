from functions_excercise import word_concat, is_ascending


def test_word_concat():
    assert word_concat("alma", "korte") == "almakorte"

def test_word_concat2():
    assert word_concat("cseresznye", "meggy") == "meggycseresznye"

def test_word_concat3():
    assert word_concat("alma", "haza") == "almahaza"

def test_is_ascending():
    assert is_ascending(1, 3, 6) == True            # Ez lehetne csak simán assert is_ascending(1, 3, 6)

def test_is_ascending2():
    assert is_ascending(1, 10, 20) == True

def test_is_ascending3():
    assert is_ascending(1, 1, 1) == False           # Ez lehetne assert not is_ascending (1, 1, 1)

def test_is_ascending4():
    assert is_ascending(20, 10, 1) == False

def test_is_ascending5():
    assert is_ascending(20, 10, 20) == False