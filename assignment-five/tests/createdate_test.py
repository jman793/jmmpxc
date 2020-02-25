import pytest
import Staff
import json


def test_create(staffSystem):
    course='comp_sci'
    duedate="2/2/2020"
    randassign={
        'due_date':duedate
    }

#The system shuold not require assignemtns to all be called 'assignmentx' where x is in sequential order
    staffSystem.create_assignment('assignment-1',duedate,course)
    with open('../Data/courses.json') as json_file:
        json_obj=json.load(json_file)
        assert json_obj[course]['assignments']['random assign']==randassign

@pytest.fixture
def staffSystem():
    staffSystem = Staff.Staff()
    return staffSystem