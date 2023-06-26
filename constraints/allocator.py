from typing import NoReturn

from utils.big_formula import BigFormula

class AllocatorConstraintBase:
    _big_formula = BigFormula

    def __init__(self, disciplines, schedules_quantity):
        self.disciplines = disciplines
        self.schedules_quantity = schedules_quantity

    @property
    def disciplines(self):
        return self._disciplines

    @disciplines.setter
    def disciplines(self, disciplines):
        if not disciplines:
            raise ValueError('Disciplines quantity cannot be less than one.')
        self._disciplines = disciplines

    def apply(self):
        raise NotImplemented

    @property
    def schedules_quantity(self) -> int:
        return self._schedules_quantity

    @schedules_quantity.setter
    def schedules_quantity(self, value: int) -> NoReturn:
        if value < 1:
            raise ValueError('Schedules quantity cannot be less than one.')
        self._schedules_quantity = value