import pytest
import System

#Tests if the program can handle a wrong username
def test_pass(loginSystem):
    name='akend3'
    password='123454321'
    assert loginSystem.check_password(name,password)
    


@pytest.fixture
def loginSystem():
    loginSystem = System.System()
    loginSystem.load_data()
    return loginSystem