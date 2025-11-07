def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def test_add():
    assert add(1,2) == 3
    assert add(2,2) == 4
    assert add(5,10) == 15

def test_sub():
    assert sub(1,2) == -1
    assert sub(2,2) == 0
    assert sub(5,10) == -5