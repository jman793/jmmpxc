import pytest
import System

def test_login(loginSystem):
    name='akend3'
    password='wrong password'
    #THIS SHOULD FAIL BECAUSE THE PASSWORD IS WRONG
    assert loginSystem.check_password(name,password)
    
    


@pytest.fixture
def loginSystem():
    loginSystem = System.System()
    loginSystem.load_data()
    return loginSystem