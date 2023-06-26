class Discipline:
    def __init__(self, semester, name, professor):
        self.semester = semester
        self.name = name
        self.professor = professor

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Discipline) and other.name == self.name and other.semester == self.semester and other.professor == self.professor

    def __repr__(self) -> str:
        return f'{self.name}'

    def __str__(self) -> str:
        return self.__repr__()