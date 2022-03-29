import fa

import pytest

@pytest.mark.xfail
@pytest.mark.parametrize("a,b",[(1,True),(2,True),(153,True),(11,True),(12,True),(15,True)])
def test_Armstrong(a,b):
    b = fa.Armstrong(a)
    assert b == True

@pytest.mark.parametrize("asign,result",[(8,True),(16,True),(24,True),(30,True),(41,True)])
def test_Divisiblity(asign,result):
    result = fa.divisible(asign)
    assert result == True
@pytest.mark.skip
@pytest.mark.parametrize("a,b,c,answer",[(1,5,7,7),(9,7,5,9),(4,5,8,4),(6,4,8,4)])
def test_Largest(a,b,c,answer):
    answer = fa.largest(a,b,c)
    assert answer == True

@pytest.mark.parametrize("a,result",[(8,True),(26,True),(60,True),(15,True),(7,True)])
def test_Palindrome(a,result):
    result = fa.even(a)
    assert result == True