from sympy.parsing.sympy_parser import parse_expr
from sympy import symbols

"""
yn+1 = yn + hF(xn, yn)
y0 = y(x0)
"""

# x = symbols("x")
# y = Function("y")(x)

def get_eq(eq):
    return parse_expr(eq)

if __name__ == "__main__":
    fxy = input("Enter F(x,y) => ")
    x0 = float(input("Enter x0 => "))
    y0 = float(input("Enter y(0) => "))
    h = float(input("Enter step size h => "))
    to_find = float(input("Enter required of x to find y => "))
    n = round(to_find/h)
    print(n)

    eq = get_eq(fxy)
    # yn = 0

    for i in range(n):
        fx0y0 = eq.subs({"x": x0, "y": y0})
        y0 = y0 + h * fx0y0
        x0 = x0 + h

        print(f">> y{i+1} = y({x0}) = y{i} + {h} * F({x0}, {y0})")
        print(f">> y{i+1} = y({x0}) = {y0} + {h} * {fx0y0}")
        print(f">> y{i+1} = ", y0)
        print(f">> x{i+1} = ", x0, "\n")

