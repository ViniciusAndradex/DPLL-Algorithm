from functools import reduce

from utils.formula import And, Or

class BigFormula:
    @staticmethod
    def and_all(formulas):
        if not formulas:
            return False
        if len(formulas) == 1:
            return formulas[0]
        return reduce(lambda x, y: And(x, y), formulas)

    @staticmethod
    def or_all(formulas):
        if not formulas:
            return False
        if len(formulas) == 1:
            return formulas[0]
        return reduce(lambda x, y: Or(x, y), formulas)