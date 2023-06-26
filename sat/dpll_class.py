from typing import Union
import datetime


class Dpll:
    def dpll(self, clausulas, valoracao):
        return self.dpll_check(clausulas, valoracao)

    def dpll_check(self, clausulas, valoracao):
        clausulas, valoracao = self.unit_propagation(clausulas, valoracao)

        if len(clausulas) == 0:
            with open(f'cnf-formulas/satisfiable/satisfiable_{datetime.datetime.now()}.cnf', 'w') as archive:
                valoracao = list(valoracao)
                for x in valoracao:
                    archive.write(str(x) + ' ')
                archive.write('0')

            return
        if set() in clausulas:
            with open(f'cnf-formulas/unsatisfiable/unsatisfiable_{datetime.datetime.now()}.cnf', 'w') as archive:
                archive.write('UNSATISFIABLE')
            return

        atomic = self.get_atomic(clausulas)
        clausula1, clausula2 = clausulas.copy(), clausulas.copy()
        clausula1.append({atomic})
        clausula2.append({atomic * -1})

        result = self.dpll_check(clausula1, valoracao)

        if result is not False:
            return result
        return self.dpll_check(clausula2, valoracao)

    def unit_propagation(self, clausulas, valoracao):
        while self.has_unit_clause(clausulas):
            literal = self.literal_unit(clausulas)
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
        return None

    @staticmethod
    def get_atomic(clausulas):
        # Clausula -> 1 atomica da clausula
        for position, clausula in enumerate(clausulas):
            return list(clausula)[position]

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
                clausula = self.remove_clauses_with_literal(clausula, literal)
        return clausula

    @staticmethod
    def _remove_complement_literal(clauses, literal):
        # Procurar os literais de valor inverso ao literal e retiralos das clausulas
        # Clauses é none
        return list(map(lambda c: c.difference({literal * -1}), clauses))