from typing import Union


class Dpll:
    def dpll(self, clausulas, valoracao):
        return self.dpll_check(clausulas, valoracao)

    def dpll_check(self, clausulas, valoracao):
        clausulas, valoracao = self.unit_propagation(clausulas, valoracao)

        if clausulas == []:
            return valoracao

        if clausulas is not None and set in clausulas:
            return False

        clausula1, clausula2, result = None, None, None


        if self.get_atomic(clausulas):
            atomic, position = self.get_atomic(clausulas)

            clausula1 = clausulas[position].union({atomic})
            clausula2 = clausulas[position].union({atomic * -1})

            result = self.dpll_check(clausula1, valoracao)

        if result:
            return result
        return self.dpll_check(clausula2, valoracao)

    def unit_propagation(self, clausulas, valoracao):
        literal = 0
        while literal is not None:
            print(clausulas, "abacaxi")
            literal = self.literal_unit(clausulas)
            print(clausulas, "amendoin")
            if literal == None:
                break
                print('break')
            print(clausulas, "abobora")
            # Remover todas as clausulas que tem o literal e remover o complemento desse literal (o valor inverso do literal)
            valoracao = valoracao.union({literal})
            clausulas = self.remove_clauses_with_literal(clausulas, literal)
            clausulas = self._remove_complement_literal(clausulas, literal)
            print(clausulas, "abacate")
        return clausulas, valoracao

    @staticmethod
    def has_unit_clause(clausula):
        for unit_clause in clausula:
            if len(unit_clause) == 1:
                return unit_clause

    @staticmethod
    def get_atomic(clausulas):
        # Clausula -> 1 atomica da clausula
        if clausulas is set:
            for position, clausula in enumerate(clausulas):
                return list(clausula)[0], position
        # return clausulas, 1

    @staticmethod
    def literal_unit(clausulas):
        for clausula in clausulas:
            if len(clausula) == 1:
                return list(clausula)[0]
        return None

    @staticmethod
    def remove_clauses_with_literal(clausula, literal):
        for position, clause in enumerate(clausula):
            if literal in clause:
                clausula.pop(position)
        return clausula

    @staticmethod
    def _remove_complement_literal(clauses, literal):
        # Procurar os literais de valor inverso ao literal e retiralos das clausulas
        # Clauses é none
        return list(map(lambda c: c.difference({literal * -1}), clauses))