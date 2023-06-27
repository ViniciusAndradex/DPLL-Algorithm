import datetime


class Dpll:
    def dpll(self, clausulas, valoracao):
        return self.dpll_check(clausulas, valoracao)

    def dpll_check(self, clausulas, valoracao):
        clausulas, valoracao = self.unit_propagation(clausulas, valoracao.copy())

        if len(clausulas) == 0:
            with open(f'cnf-formulas/satisfiable/satisfiable_discipline_{datetime.datetime.now()}.cnf', 'w') as archive:
                valoracao = list(valoracao)
                for x in valoracao:
                    archive.write(str(x) + ' ')
                archive.write('0')

            return
        if set() in clausulas:
            with open(f'cnf-formulas/unsatisfiable/unsatisfiable_discipline_{datetime.datetime.now()}.cnf', 'w') as archive:
                archive.write('UNSATISFIABLE')
            return

        atomic = self.get_atomic(clausulas)

        clausula1 = {frozenset({atomic})}.union(clausulas.copy())
        clausula2 = {frozenset({atomic * -1})}.union(clausulas.copy())

        result = self.dpll_check(clausula1, valoracao)

        if result is not False:
            return result
        return self.dpll_check(clausula2, valoracao)

    def unit_propagation(self, clausulas, valoracao):
        while self.has_unit_clause(clausulas):
            literal = self.literal_unit(clausulas)
            # Remover todas as clausulas que tem o literal e remover o complemento desse literal (o valor inverso do
            # literal)
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

    @staticmethod
    def remove_clauses_with_literal(clausula, literal):
        return set(filter(lambda c: literal not in c, clausula))

    @staticmethod
    def _remove_complement_literal(clauses, literal):
        # Procurar os literais de valor inverso ao literal e retiralos das clausulas
        # Clauses é none
        return list(map(lambda c: c.difference({literal * -1}), clauses))
