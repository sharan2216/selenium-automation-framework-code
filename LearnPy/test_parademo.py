import pytest


# # 1st example------
@pytest.fixture(params=["a", "b"])
def demo_fixture(request):
    print(request.param)


def testLogin(demo_fixture):
    print("Login Successful")


# 2nd example------
@pytest.mark.parametrize("a,b,final", [(2, 6, 8), (5, 10, 15), (5, 10, 15)])
def testAdd(a, b, final):
    assert a + b == final
