import pytest
import Staff
import json


def test_gradefloat(staffSystem):
    name='akend3'
    course='comp_sci'
    assignment='assignment1'
    #The grade should not have to be a whole number
    grade=20.5
    staffSystem.change_grade(name,course,assignment,grade)
    with open('../Data/users.json') as json_file:
        json_obj=json.load(json_file)
        assert json_obj[name][course][assignment][grade]==grade

@pytest.fixture
def staffSystem():
    staffSystem = Staff.Staff()
    return staffSystem