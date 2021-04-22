"""
dy/dx = F(x,y) y(x0) = y0

y(x1) = y1 at x = x1 = x0 + h

y1_0 = y0 + h * F(x0, y0)
y1_1 = y0 + h/2 * [F(x0, y0) + F(x1, y1_0)]
y1_2 = y0 + h/2 * [F(x0, y0) + F(x1, y1_1)]
.
.
.
y1_nP1 = y0 + h/2 * [F(x0, y0) + F(x1, y1_n)]
"""
from sympy.parsing.sympy_parser import parse_expr
from sympy import symbols

def get_eq(eq):
    return parse_expr(eq)

def evalute(eq, x, y):
    return eq.subs({"x": x, "y": y})

if __name__ == "__main__":
    fxy = input("Enter F(x,y) => ")
    x0 = float(input("Enter x0 => "))
    y0 = float(input("Enter y(0) => "))
    h = float(input("Enter step size h => "))
    # to_find = float(input("Enter required yn => "))
    # n = round(to_find/h)
    n = int(input("Steps n => "))

    eq = get_eq(fxy)
    fx0y0 = evalute(eq, x0, y0)
    y1_n = y0 + h * fx0y0
    x1 = x0 + h
    print(">> y1_0 = y0 + h * F(x0, y0)")
    print(f">> y1_0 = {y0} + {h} * {fx0y0} = {y1_n}")
    print(f">> x1 = {x1}\n")

    for i in range(n):
        fxnyn = eq.subs({"x": x1, "y": y1_n})
        y1_n = y0 + h/2 * (fx0y0 + fxnyn)

        print(f">> y1_{i+1} = y0 + h * [F(x0, y0) + F(x1, y1_{i})]")
        print(f">> y1_{i+1} = {y0} + {h/2} * [{fx0y0} + {fxnyn}] = {y1_n}\n")
