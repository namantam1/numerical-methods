"""
Method of falsi position,
Regula falsi method,
Method of interpolations
"""

from sympy import sqrt, diff, Symbol
from sympy.parsing.sympy_parser import parse_expr

class Newton:

    def __init__(self, upto=0, fx="x**2"):
        self._upto = upto
        self.fx = fx

    @property
    def fx(self):
        return self._fx

    @property
    def fx1(self, val):
        return self._fx1
    
    def eval_fx(self, val):
        return round(self._fx.subs("x", val), self._upto)

    def eval_fx1(self, val):
        return round(self._fx1.subs("x", val), self._upto)

    @fx.setter
    def fx(self, val):
        if not isinstance(val, Symbol):
            val = parse_expr(val)

        self._fx = val
        self._fx1 = diff(val, "x")

    def set_vars(self, fx, upto):
        self.fx = fx
        self._upto = upto

    def newton(self, x):
        """
        x1 = x - f(x)/f1(x)
        """
        fx = self.eval_fx(x)
        fx1 = self.eval_fx1(x)
        print(f"\nx => {x} - {fx}/{fx1}")
        return round(x - (fx/fx1), self._upto)

    def solve(self, x0):
        flag = 1
        print(f"fx1 => {self._fx1}\n")
        print(f"x0 => ", x0)
        while True:
            x = self.newton(x0)
            print(f"x{flag} => {x}")
            if x == x0:
                break
            x0 = x
            flag += 1


# newton = Newton()


if __name__ == "__main__":
    upto = int(input("upto decimal - "))
    fx = input("function - ")
    x0 = float(input("x0 = "))
    n = Newton(upto, fx)
    n.solve(x0)

