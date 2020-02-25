import Student
import pytest
import json 

def test_grades(studentSystem):
    name='yted91'
    course='software_engineering'

    functiongrades=studentSystem.check_grades(course)
    with open('Data/users.json') as json_file:
        jsob_obj=json.load(json_file)
        assignments = jsob_obj[name]['courses'][course]
        grades = []
        for key in assignments:
            grades.append([key, assignments[key]['grade']])
        assert grades==functiongrades
    

@pytest.fixture
def studentSystem():
    with open('Data/users.json') as json_file:
        users=json.load(json_file)
    with open('Data/courses.json') as  json_file:
        courses=json.load(json_file)
    professorSystem = Student.Student('yted91',users,courses)
    return professorSystem