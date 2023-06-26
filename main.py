from sat.dpll_class import Dpll
from utils.cnf_to_list_and_set import cnf_to_list

dppl = Dpll()

clauses = cnf_to_list("inputs/teste_4.cnf")

teste = dppl.dpll(clauses, set())
