from dpll_class import Dpll

clauses = [{1, 2}, {2, -1}, {2}, {2, 3}]

dppl = Dpll()

teste = dppl.dpll(clauses, set())
print(teste)
