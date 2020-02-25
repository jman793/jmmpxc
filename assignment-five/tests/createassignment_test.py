import pytest
import Staff
import json


def test_create(staffSystem):
    course='comp_sci'
    duedate="2/2/20"
    assignement15={
        'due_date':duedate
    }

    staffSystem.create_assignment('assignment15',duedate,course)
    with open('../Data/courses.json') as json_file:
        json_obj=json.load(json_file)
        assert json_obj[course]['assignments']['assignment15']==assignment15

@pytest.fixture
def staffSystem():
    staffSystem = Staff.Staff()
    return staffSystem