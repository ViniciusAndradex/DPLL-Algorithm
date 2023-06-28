def cnf_to_list(archive):
    with open(f'{archive}', "r") as arquivo:
        lines = arquivo.readlines()
        clauses = []
        for line in lines:
            if line[0] not in 'cp':
                line.replace('\n', '')
                line = line[:-2]
                clauses.append(line)

        for pos, clause in enumerate(clauses):
            clause = clause.split()
            clauses.pop(pos)
            clauses.insert(pos, set())
            for item in clause:
                clauses[pos].add(int(item))
        tupla = tuple(clauses)
        # print({frozenset(tupla)})
        frozen = set(map(frozenset, tupla))
        # clauses = frozenset(tuple(clauses))
    return frozen
