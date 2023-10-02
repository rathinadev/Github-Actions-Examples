#Sample test

def test(a,b):
    return a*b

def test_mul():
    assert test(3,4) == 12
    assert test(4,5) == 20
