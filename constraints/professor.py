from utils.formula import Atom, Not, And


class ProfessorConstraint():
    def __init__(self, disciplines, schedules_quantity):
        super().__init__(disciplines, schedules_quantity)

    def apply(self):
        and_list = []
        for h in range(self.schedules_quantity):
            for i1 in range(len(self.disciplines) - 1):
                for i2 in range(i1 + 1, len(self.disciplines)):
                    if self.disciplines[i1].professor == self.disciplines[i2].professor:
                        and_list.append(Not(And(Atom(f'{i1 + 1}_{h + 1}'),
                                                Atom(f'{i2 + 1}_{h + 1}'))))
        return self._big_formula.and_all(and_list)