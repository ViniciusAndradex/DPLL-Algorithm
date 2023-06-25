from typing import Union


class Dpll:
    def dpll(self, clausulas, valoracao):
        return self.dpll_check(clausulas, valoracao)

    def dpll_check(self, clausulas, valoracao):
        clausulas, valoracao = self.unit_propagation(clausulas, valoracao)

        if clausulas == []:
            return valoracao

        if clausulas is not None and set() in clausulas:
            return 'Unsatisfatible'

        atomic, position = self.get_atomic(clausulas)
        clausula1 = clausulas[position].union({atomic})
        clausula2 = clausulas[position].union({atomic * -1})

        result = self.dpll_check(clausula1, valoracao)

        if result:
            return result
        return self.dpll_check(clausula2, valoracao)

    def unit_propagation(self, clausulas, valoracao):
        while True:
            literal = self.literal_unit(clausulas)
            if literal is None:
                break
            # Remover todas as clausulas que tem o literal e remover o complemento desse literal (o valor inverso do literal)
            valoracao = valoracao.union({literal})
            clausulas = self.remove_clauses_with_literal(clausulas, literal)
            clausulas = self._remove_complement_literal(clausulas, literal)
        return clausulas, valoracao

    @staticmethod
    def has_unit_clause(clausula):
        for unit_clause in clausula:
            if len(unit_clause) == 1:
                return unit_clause

    @staticmethod
    def get_atomic(clausulas):
        # Clausula -> 1 atomica da clausula
        for position, clausula in enumerate(clausulas):
            return list(clausula)[position], position

    @staticmethod
    def literal_unit(clausulas):
        for clausula in clausulas:
            if len(clausula) == 1:
                return list(clausula)[0]
        return None

    def remove_clauses_with_literal(self, clausula, literal):
        for position, clause in enumerate(clausula):
            if literal in clause:
                clausula.pop(position)
                self.remove_clauses_with_literal(clausula, literal)
        return clausula

    @staticmethod
    def _remove_complement_literal(clauses, literal):
        # Procurar os literais de valor inverso ao literal e retiralos das clausulas
        # Clauses é none
        return list(map(lambda c: c.difference({literal * -1}), clauses))