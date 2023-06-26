from .schedule_constraint import ScheduleConstraint
from .semester import SemesterConstraint
from .professor import ProfessorConstraint


constraints = [
    ScheduleConstraint,
    SemesterConstraint,
    ProfessorConstraint
]