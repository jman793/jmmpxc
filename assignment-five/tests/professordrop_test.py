import pytest
import Professor
import json


def test_prof(professorSystem):
    name='hdjsr7'
    course='cloud_computing'
    professorSystem.drop_student(name,course)
    #THIS STATEMENT SHOULD PASS IF THE SYSTEM WORKS CORRECTLY
    #THE REASON BEING THAT SAAB SHOULD NOT BE ABLE TO DROP STUDENTS FROM CLOUD COMPUTING
    with open('Data/users.json') as json_file:
        json_obj=json.load(json_file)
    assert json_obj[name]['courses'].get(course,'DNE')!='DNE'


@pytest.fixture
def professorSystem():
    with open('Data/users.json') as json_file:
        users=json.load(json_file)
    with open('Data/courses.json') as  json_file:
        courses=json.load(json_file)
    professorSystem = Professor.Professor('saab',users,courses)
    return professorSystem