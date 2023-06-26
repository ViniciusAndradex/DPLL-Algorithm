# restrição para um dado x horário

# semestre, professor
import os
import csv

csvPath = os.path.relpath("inputs/disciplinescsv")
# readerPath = os.path.relpath("../../inputs/disciplines/disciplines.txt")
# files = os.listdir(readerPath)

def model_to_cnf(disciplines_file):
    header = ["semestre", "disciplina", "professor"]

    with open(f'{disciplines_file}', "r") as arquivo:
        semester = []
        linesList = [""]

        for line in arquivo:
            if len(line.strip()) == 2:
                semester.append(line)
            lines = arquivo.readline()
            lineContent = lines.split(",")

            linesList.append(lineContent)

        print(linesList)

        semester = lineContent[0]
        disciplines = ["Programacao linear"]
        professors = ["Teste"]

        rows = [semester, disciplines, professors]

        print(rows)

        # with open(f"inputs/disciplinescsv2.csv", "w", newline="") as csv_file:
        #     write = csv.DictWriter(csv_file, fieldnames=header)
        #     write.writeheader()
        #     write.writerows(rows)
