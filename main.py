from dpll_class import Dpll

clauses = [{1, 2, 3}, {-1, 2, 3}, {3, 1, 2}]

dppl = Dpll()

teste = dppl.dpll(clauses, [])
