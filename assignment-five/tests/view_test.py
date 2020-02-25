import Student
import pytest
import json 

def test_view(studentSystem):
    name='yted91'
    course='cloud_computing'

    functionview=studentSystem.view_assignments(course)
    with open('Data/courses.json') as json_file:
        json_obj=json.load(json_file)
    courseassign=json_obj[course]['assignments']
    assignments = []
    for key in courseassign:
        assignments.append([key,courseassign[key]['due_date']])
    assert assignments==functionview


@pytest.fixture
def studentSystem():
    with open('Data/users.json') as json_file:
        users=json.load(json_file)
    with open('Data/courses.json') as  json_file:
        courses=json.load(json_file)
    professorSystem = Student.Student('yted91',users,courses)
    return professorSystem