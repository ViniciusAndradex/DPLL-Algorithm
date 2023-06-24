from typing import Union
from collections import Counter


class Dpll:
    def dpll(self, clausulas, valoracao):
        return self.dpll_check(clausulas, valoracao)

    def dpll_check(self, clausulas, valoracao):
        clausulas, valoracao = self.unit_propagation(clausulas, valoracao)

        if clausulas == {}:
            return valoracao
        if {} in valoracao:
            return False

        atomic = self.get_atomic(clausulas)
        clausula1 = Union[clausulas, {{atomic}}]
        clausula2 = Union[clausulas, {{not atomic}}]

        result = self.dpll_check(clausula1, valoracao)

        if result:
            return result
        return self.dpll_check(clausula2, valoracao)

    def unit_propagation(self, clausulas, valoracao):
        while self.has_unit_clause(clausulas):
            literal = self.literal_unit(clausulas)
            valoracao = Union[valoracao, literal]
            clausulas = self.remove_clauses_with_literal(clausulas, literal)
            clausulas = self.remove_complement_with_literal(clausulas, literal)
        return clausulas, valoracao

    @staticmethod
    def has_unit_clause(clausula):
        for unit_clause in clausula:
            if len(unit_clause) == 1:
                return unit_clause

    @staticmethod
    def literal_unit(clausula):
        return clausula[0]

    @staticmethod
    def remove_clauses_with_literal(clausula, literal):
        return set(filter(lambda c: literal not in c, clausula))

    @staticmethod
    def _remove_complement_literal(clauses, literal):
        return set(map(lambda c: c.difference({literal * -1}), clauses))