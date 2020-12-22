"""
Simplifies gplean programs with sympy
"""

import sympy
from sympy.printing.repr import srepr
from sympy import sympify, simplify
from symbolicRegressor import getSymbolicRegressorModel


def simplifySymbolicRegressor(model):
    locals = {
        "sub": lambda x, y: x - y,
        "div": lambda x, y: x / y,
        "mul": lambda x, y: x * y,
        "add": lambda x, y: x + y,
        "neg": lambda x: -x,
        "pow": lambda x, y: x ** y,
        "cos": lambda x: sympy.cos(x),
    }

    return srepr(simplify(sympify(model, locals=locals)))


if __name__ == "__main__":
    """
    Before simplification: sub(add(-0.999, X1), mul(sub(X1, X0), add(X0, X1)))
    After simplification:
        Expected: mul(X0, X0) - mul(X1, X1) + X1 - 1
        Actual: Add(Symbol('X1'), Mul(Add(Symbol('X0'), Mul(Integer(-1), Symbol('X1'))), Add(Symbol('X0'), Symbol('X1'))), Float('-0.999', precision=53))

    Comments:
        symplified_model is the factorized form of expected simplification which is even better than expected
    """
    model = getSymbolicRegressorModel()
    symplified_model = simplifySymbolicRegressor(str(model))
    print(symplified_model)
