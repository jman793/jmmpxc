import pytest
import System
import Student
import json 

def test_login(loginSystem):
    name='akend3'
    password='123454321'
    loginSystem.login(name,password)
    with open('Data/users.json') as json_file:
        json_obj=json.load(json_file)
    users=json_obj
    with open('Data/courses.json') as json_file:
        json_obj=json.load(json_file)
    courses=json_obj
    studentobj=Student.Student(name,users,courses)
    assert studentobj.name==loginSystem.usr.name

    


@pytest.fixture
def loginSystem():
    loginSystem = System.System()
    loginSystem.load_data()
    return loginSystem