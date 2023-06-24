from typing import Union


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
            literal = self.literal_unit(valoracao)
            valoracao = Union[valoracao, literal]
            clausulas = self.remove_clauses_with_literal(clausulas, literal)
            clausulas = self.remove_complement_with_literal(clausulas, literal)
        return clausulas, valoracao

    @staticmethod
    def has_unit_clause(clausulas):
        for unit in clausulas:
            if len(unit) == 1:
                return unit

    @staticmethod
    def literal_unit(valoracao):
