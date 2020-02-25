import pytest
import Staff
import json

#Tests if the program can handle a wrong username
def test_grade(staffSystem):
    name='akend3'
    course='comp_sci'
    assignment='assignment1'
    grade=50
    staffSystem.change_grade(name,course,assignment,grade)
    with open('../Data/users.json') as json_file:
        json_obj=json.load(json_file)
        assert json_obj[name][course][assignment][grade]==grade

@pytest.fixture
def staffSystem():
    staffSystem = Staff.Staff()
    return staffSystem