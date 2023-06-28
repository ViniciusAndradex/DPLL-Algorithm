from sat.dpll import Dpll as dP
from utils.cnf_to_set_and_frozenset import cnf_to_list
from utils.input_generator import get_disciplines, to_model, atoms_map
from utils.literal_converter import LiteralConverter
from utils.clausal_converter import ClausalFormConverter

dppl_projeto = dP()

clauses = cnf_to_list("inputs/teste_1.cnf")

disciplines = get_disciplines()[0]

model = to_model(disciplines[:7], 3)
dict_map = atoms_map(len(disciplines), 10)
converter = LiteralConverter(dict_map)
cnf_model = converter.to_clauses_of_int(ClausalFormConverter.convert(to_model(disciplines, 10)))

dppl_projeto.dpll(clauses, set())
dppl_projeto.dpll(cnf_model, set())
