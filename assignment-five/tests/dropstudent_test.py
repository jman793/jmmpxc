import pytest
import Professor
import json


def test_drop(professorSystem):
    name='yted91'
    course='cloud_computing'
    with open('Data/users.json') as json_file:
        json_obj=json.load(json_file)
    assert json_obj[name]['courses'].get(course,'DNE')!='DNE'
    professorSystem.drop_student(name,course)
    with open('Data/users.json') as json_file:
        json_obj=json.load(json_file)
        assert json_obj[name]['courses'].get(course,'DNE')=='DNE'

        
@pytest.fixture
def professorSystem():
    with open('Data/users.json') as json_file:
        users=json.load(json_file)
    with open('Data/courses.json') as  json_file:
        courses=json.load(json_file)
    professorSystem = Professor.Professor('cmhbf5',users,courses)
    return professorSystem