import os
import csv
import random
from utils.formula import Atom

path = os.path.abspath('../../inputs/disciplinecsv/text.csv')

def generate_disciplines():
    main_file = f'{path}/1.txt'
    disciplines_qnt = [3, 4, 4, 5, 5, 5, 6, 6, 7, 7]
    with open(main_file, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        fieldnames = list(reader.fieldnames)
        disciplines = list(reader)
        for i, v in enumerate(disciplines_qnt):
            partial_disciplines = random.sample(disciplines, v)
            with open(f'{path}/{i + 2}.csv', 'w', newline='') as partial_csvfile:
                whiter = csv.DictWriter(partial_csvfile, fieldnames=fieldnames)
                whiter.writeheader()
                whiter.writerows(partial_disciplines)


def atoms_map(n_disciplines, n_schedules):
    dict_map = {}
    count = 0
    for i in range(n_disciplines):
        for j in range(n_schedules):
            count += 1
            dict_map[Atom(f'{i + 1}_{j + 1}')] = count
    return dict_map
