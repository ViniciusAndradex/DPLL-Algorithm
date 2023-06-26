from utils.formula import Not


class LiteralConverter():
    def __init__(self, literals_map):
        self._literals_map = literals_map

    def to_interp(self, int_interp):
        converted_inter = set()
        for i in int_interp:
            for k, v in self._literals_map.items():
                if v == i:
                    converted_inter.add((k, True))
                elif v * -1 == i:
                    converted_inter.add((Not(k), False))
        return converted_inter

    def to_clauses_of_int(self, clauses):
        converted_clauses = set()
        for clause in clauses:
            converted_clause = []
            for literal in clause:
                if isinstance(literal, Not):
                    converted_clause.append(self._literals_map[literal.inner] * -1)
                else:
                    converted_clause.append(self._literals_map[literal])
            converted_clauses.add(frozenset(converted_clause))
        return converted_clauses