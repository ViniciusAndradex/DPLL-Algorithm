from utils.formula import Formula, Atom, Implies, Or, Not, And


class CNFConverter:
    @classmethod
    def convert(cls, formula: Formula) -> Formula:
        formula = cls._implication_free(formula)
        formula = cls._negation_normal_form(formula)
        formula = cls._distributive(formula)
        return formula

    @classmethod
    def _distributive(cls, formula: Formula) -> Formula:
        if isinstance(formula, Atom) or isinstance(formula, Not) and isinstance(formula.inner, Atom):
            return formula
        if isinstance(formula, And):
            left = cls._distributive(formula.left)
            right = cls._distributive(formula.right)
            return And(left, right)
        if isinstance(formula, Or):
            left_formula = cls._distributive(formula.left)
            right_formula = cls._distributive(formula.right)
            if isinstance(left_formula, And):
                left = cls._distributive(Or(left_formula.left, right_formula))
                right = cls._distributive(Or(left_formula.right, right_formula))
                return And(left, right)
            if isinstance(right_formula, And):
                left = cls._distributive(Or(left_formula, right_formula.left))
                right = cls._distributive(Or(left_formula, right_formula.right))
                return And(left, right)
            return Or(left_formula, right_formula)

    @classmethod
    def _negation_normal_form(cls, formula: Formula) -> Formula:
        if isinstance(formula, Atom) or isinstance(formula, Not) and isinstance(formula.inner, Atom):
            return formula
        if isinstance(formula, Not) and isinstance(formula.inner, Not):
            return cls._negation_normal_form(formula.inner.inner)
        if type(formula) in [And, Or]:
            left = cls._negation_normal_form(formula.left)
            right = cls._negation_normal_form(formula.right)
            return type(formula)(left, right)
        if isinstance(formula, Not) and isinstance(formula.inner, And):
            left = cls._negation_normal_form(Not(formula.inner.left))
            right = cls._negation_normal_form(Not(formula.inner.right))
            return Or(left, right)
        if isinstance(formula, Not) and isinstance(formula.inner, Or):
            left = cls._negation_normal_form(Not(formula.inner.left))
            right = cls._negation_normal_form(Not(formula.inner.right))
            return And(left, right)

    @classmethod
    def _implication_free(cls, formula: Formula) -> Formula:
        if isinstance(formula, Atom):
            return formula
        if isinstance(formula, Implies):
            left = cls._implication_free(formula.left)
            right = cls._implication_free(formula.right)
            return Or(Not(left), right)
        if type(formula) in [And, Or]:
            left = cls._implication_free(formula.left)
            right = cls._implication_free(formula.right)
            return type(formula)(left, right)
        if isinstance(formula, Not):
            return Not(cls._implication_free(formula.inner))