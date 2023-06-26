from sat.dpll_class import Dpll
from sat.dpll import Dpll as dP
from utils.cnf_to_list_and_set import cnf_to_list
from utils.input_generator import get_disciplines, to_model, atoms_map
from utils.literal_converter import LiteralConverter
from utils.clausal_converter import ClausalFormConverter

dppl = Dpll()
dppl_teste = dP()

clauses = cnf_to_list("inputs/teste_4.cnf")

disciplines = get_disciplines()[0]

model = to_model(disciplines[:7], 3)
dict_map = atoms_map(len(disciplines), 10)
converter = LiteralConverter(dict_map)
cnf_model = converter.to_clauses_of_int(ClausalFormConverter.convert(to_model(disciplines, 10)))

dppl.dpll(clauses, set())
dppl_teste.dpll(cnf_model, set())
