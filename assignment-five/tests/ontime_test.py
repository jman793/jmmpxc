import Student
import pytest
import json 

def test_ontime(studentSystem):
    submission_date='2/25/2020'
    due_dateT='2/25/2020'
    due_dateF='2/26/2020'
    assert studentSystem.check_ontime(submission_date,due_dateT)==True
    assert studentSystem.check_ontime(submission_date,due_dateF)==False
    

@pytest.fixture
def studentSystem():
    with open('Data/users.json') as json_file:
        users=json.load(json_file)
    with open('Data/courses.json') as  json_file:
        courses=json.load(json_file)
    professorSystem = Student.Student('yted91',users,courses)
    return professorSystem