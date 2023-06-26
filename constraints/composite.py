from utils.big_formula import BigFormula

class ConstraintComposite():
    _big_formula = BigFormula

    def __init__(self):
        self._constraints = []

    def add(self, constraint) :
        self._constraints.append(constraint)

    def add_all(self, constraints):
        self._constraints.extend(constraints)

    def apply(self):
        formulas = []
        for constraint in self._constraints:
            formulas.append(constraint.apply())
        formulas = list(filter(lambda formula: formula is not False, formulas))
        if not formulas:
            return False
        return self._big_formula.and_all(formulas)