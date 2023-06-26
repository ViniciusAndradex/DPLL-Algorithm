from utils.cnf_converter import CNFConverter
from utils.formula import Atom, Not, Or

class ClausalFormConverter:
    _cnf_converter = CNFConverter

    @classmethod
    def convert(cls, formula):
        formula = cls._cnf_converter.convert(formula)
        premises = cls._get_premises(formula)
        return set(map(cls._to_clause_nf, premises))

    @classmethod
    def _to_clause_nf(cls, formula):
        if isinstance(formula, Atom) or isinstance(formula, Not) and isinstance(formula.inner, Atom):
            return frozenset([formula])
        if isinstance(formula, Or):
            left = cls._to_clause_nf(formula.left)
            right = cls._to_clause_nf(formula.right)
            return left.union(right)

    @classmethod
    def _get_premises(cls, formula):
        if type(formula) in [Atom, Or, Not]:
            return {formula}
        left = cls._get_premises(formula.left)
        right = cls._get_premises(formula.right)
        return left.union(right)