from numb3rs import validate


def test_valid_ips():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True
    assert validate("192.168.1.1") == True


def test_invalid_range():
    assert validate("275.3.6.28") == False
    assert validate("255.255.255.256") == False
    assert validate("512.512.512.512") == False


def test_invalid_format():
    assert validate("cat") == False
    assert validate("1.2.3") == False
    assert validate("1.2.3.4.5") == False
    assert validate("1.2.3.cat") == False


def test_edge_cases():
    assert validate("255.0.0.0") == True
    assert validate("0.255.0.0") == True
    assert validate("256.1.1.1") == False
    assert validate("1.256.1.1") == False
