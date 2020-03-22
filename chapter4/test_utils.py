from utils import str_to_int

def test_str_to_int():
    assert str_to_int("52") == 52

def test_str_to_int_float():
    assert str_to_int("52.2") == 52

def test_str_to_int_comma():
    assert str_to_int("52,2") == 52

def test_str_to_int_commas():
    assert str_to_int("1,100,700.54") == 1100700

#def test_str_to_int_commas_non_decimal():
#    assert str_to_int("1,100,700") == 1100700

