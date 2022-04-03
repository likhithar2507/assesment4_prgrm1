import pytest
import prgrm1

@pytest.mark.xfail
@pytest.mark.parametrize("x,result",[(4,2.0),(9,3.0),(10,3)])
def test_square_root(x,result):
    sqrt=prgrm1.square_root(x)
    assert sqrt == result

@pytest.mark.skip(reason="no need")
@pytest.mark.parametrize("a,b,c,result",[(2,3,4,5)])
def test_quadratic_equation(a,b,c,result):
    quatreq=prgrm1.quadratic_equation(a,b,c)
    assert quatreq == result

@pytest.mark.parametrize("celsius,result",[(3,37.4),(4,32.0)])
def test_cels_to_farh(celsius,result):
    cel=prgrm1.cels_to_farh(celsius)
    assert cel == result

@pytest.fixture
def input():
    x=12
    return x
def test_pos_neg_zero(input):
    result=prgrm1.pos_neg_zero(input)
    assert result == "positive"

@pytest.mark.parametrize("num,result",[(16,136),(10,100)])
def test_natural_num(num,result):
    natnum=prgrm1.natural_num(num)
    assert natnum == result