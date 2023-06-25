from typing import Union


class Dpll:
    def dpll(self, clausulas, valoracao):
        return self.dpll_check(clausulas, valoracao)

    def dpll_check(self, clausulas, valoracao):
        clausulas, valoracao = self.unit_propagation(clausulas, valoracao)

        if clausulas == []:
            return valoracao
        # if type(valoracao) == dict and len(valoracao) == 0:
        if {} in clausulas:
            return False

        atomic, position = self.get_atomic(clausulas)

        clausula1 = clausulas[position].union({atomic})
        print('clausula 1', clausula1)
        clausula2 = clausulas[position].union({atomic * -1})
        print('clausula 2', clausula2)
        result = self.dpll_check(clausula1, valoracao)

        if result:
            return result
        return self.dpll_check(clausula2, valoracao)

    def unit_propagation(self, clausulas, valoracao):
        while True:
            literal = self.literal_unit(clausulas)
            if not literal:
                break
            valoracao = literal.add(valoracao)
            # Remover todas as clausulas que tem o literal e remover o complemento desse literal (o valor inverso do literal)
            clausulas = self.remove_clauses_with_literal(clausulas, literal)
            if clausulas is not None:
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
            return list(clausula)[0], position

    @staticmethod
    def literal_unit(clausulas):
        if clausulas is not None:
            for clausula in clausulas:
                print(type(clausula))
                if len(clausula) == 1:
                    return list(clausula)[0]

    @staticmethod
    def remove_clauses_with_literal(clausula, literal):
        sette = set()
        return sette.add(filter(lambda c: literal not in c, clausula))

    @staticmethod
    def _remove_complement_literal(clauses, literal):
        # Procurar os literais de valor inverso ao literal e retiralos das clausulas
        sette = set();
        # Clauses é none
        return sette.add(map(lambda c: c.difference({literal * -1}), clauses))