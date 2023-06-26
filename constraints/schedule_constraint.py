from utils.formula import Atom, Not, And
from .allocator import AllocatorConstraintBase

class ScheduleConstraint(AllocatorConstraintBase):
    def __init__(self, disciplines, schedules_quantity):
        super().__init__(disciplines, schedules_quantity)

    def apply(self):
        and_list = []
        for i in range(len(self.disciplines)):
            list_of_at_least_one_schedule = []
            list_of_at_most_one_schedule = []
            for h1 in range(self.schedules_quantity - 1):
                list_of_at_least_one_schedule.append(Atom(f'{i + 1}_{h1 + 1}'))
                if h1 == self.schedules_quantity - 2:
                    list_of_at_least_one_schedule.append(Atom(f'{i + 1}_{h1 + 2}'))
                for h2 in range(h1 + 1, self.schedules_quantity):
                    list_of_at_most_one_schedule.append(Not(And(Atom(f'{i + 1}_{h1 + 1}'),
                                                                Atom(f'{i + 1}_{h2 + 1}'))))
            and_list.append(And(self._big_formula.or_all(list_of_at_least_one_schedule),
                                self._big_formula.and_all(list_of_at_most_one_schedule)))
        return self._big_formula.and_all(and_list)