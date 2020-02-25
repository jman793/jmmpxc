import Student
import pytest
import json 

def test_submit(studentSystem):
    name='yted91'
    course='software_engineering'
    assignment_name='assignment1'
    submission='blah'
    submission_date='2/25/2020'

    studentSystem.submit_assignment(course,assignment_name,submission,submission_date)
    with open('Data/users.json') as json_file:
        jsob_obj=json.load(json_file)
    assert jsob_obj[name]['courses'][course].get(assignment_name,'DNE')!='DNE'
    assert jsob_obj[name]['courses'][course][assignment_name]['submission']==submission
    assert jsob_obj[name]['courses'][course][assignment_name]['submission_date']==submission_date
    

@pytest.fixture
def studentSystem():
    with open('Data/users.json') as json_file:
        users=json.load(json_file)
    with open('Data/courses.json') as  json_file:
        courses=json.load(json_file)
    professorSystem = Student.Student('yted91',users,courses)
    return professorSystem