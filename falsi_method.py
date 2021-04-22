"""
Method of falsi position,
Regula falsi method,
Method of interpolations
"""

from sympy import sqrt, symbols, log
from sympy.parsing.sympy_parser import parse_expr

class Falsi:
    upto = 5
    fx = "cos(x) - x*exp(x)"
    expr = parse_expr(fx)
    # fx =  input("Enter function - ")

    def set_vars(self, fx, upto):
        self.fx = fx
        self.expr = parse_expr(fx)
        self.upto = upto

    def evalute(self, val):
        return round(self.expr.subs("x", val), self.upto)

    def falsi(self, x0, x1):
        fx0 = self.evalute(x0)
        fx1 = self.evalute(x1)
        print(f"x0 = {x0} and fx0 = {fx0}")
        print(f"x1 = {x1} and fx1 = {fx1}")
        print(f"x => {x0} - (({x1}-{x0})*{fx0})/({fx1}-{fx0})")
        return round(x0 - ((x1-x0)*fx0)/(fx1-fx0), self.upto)

    def solve(self, x0, x1):
        flag = 2
        x = [None, x0, x1]
        k1 = x0
        k2 = x1
        while(True):
            k = self.falsi(x0,x1)
            y = self.evalute(k)
            fx0 = self.evalute(x0)
            fx1 = self.evalute(x1)
            print(f"x{flag} = {k} and y = {y}\n\n")
            if(k==x0 or k==x1):
                print("legal break")
                break
            if(y*fx1<1 and y>fx1):
                x1 = k
                x0 = x1
            elif(y*fx1<1 and y<fx1):
                x0 = k
            elif(y*fx0<1 and y>fx0):
                x1 = k
            elif(y*fx0<1 and y<fx0):
                x0 = k
                x1 = x0
            else:
                print("illegal break")
                break
            flag += 1


falsi = Falsi()


if __name__ == "__main__":
    upto = int(input("upto decimal - "))
    fx = input("function - ")
    x0 = float(input("x0 = "))
    x1 = float(input("x1 = "))
    falsi.set_vars(fx, upto)
    falsi.solve(float(x0), float(x1))
