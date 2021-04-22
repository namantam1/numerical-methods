"""
dy/dx = F(x,y) y(x0) = y0

y1 = y(x0+h) = y0 + (k1 + 2k2 + 2k3 + k4)/6

k1 = h * f(x0, y0)
k2 = h * f(x0+0.5h, y0+0.5k1)
k3 = h * f(x0+0.5h, y0+0.5k2)
k4 = h * f(x0+h, y0+k3)
"""
from sympy.parsing.sympy_parser import parse_expr
from sympy import symbols

def get_eq(eq):
    return parse_expr(eq)

def evalute(eq, x=0, y=0):
    # print(eq)
    return eq.subs({"x": x, "y": y})
    # return eq.evalf(subs={'x': x, 'y': y})

def print_formula():
    console("FORMULA ->")
    console("k1 = h * f(x0, y0)")
    console("k2 = h * f(x0+0.5h, y0+0.5k1)")
    console("k3 = h * f(x0+0.5h, y0+0.5k2)")
    console("k4 = h * f(x0+h, y0+k3)")
    console("y1 = y(x0+h) = y0 + (k1 + 2k2 + 2k3 + k4)/6\n")

def get_k1(eq, x0, y0, h):
    res = h * evalute(eq, x0, y0)
    console(f"k1 = {h} * f({x0}, {y0}) = {res}")
    return res

def get_k2(eq, x0, y0, h, k1):
    res = h * evalute(eq, x0+0.5*h, y0+0.5*k1)
    console(f"k2 = {h} * f({x0} + 0.5 * {h}, {y0} + 0.5 * {k1}) = {res}")
    return res

def get_k3(eq, x0, y0, h, k2):
    res = h * evalute(eq, x0+0.5*h, y0+0.5*k2)
    console(f"k3 = {h} * f({x0} + 0.5 * {h}, {y0} + 0.5 * {k2} = {res}")
    return res

def get_k4(eq, x0, y0, h, k3):
    res = h * evalute(eq, x0+h, y0+k3)
    console(f"k4 = {h} * f({x0} + {h}, {y0} + {k3}) = {res}")
    return res

def console(*args, **kwargs):
    print(">> ", *args, **kwargs)

if __name__ == "__main__":
    fxy = input("Enter F(x,y) => ")
    x0 = float(input("Enter x0 => "))
    y0 = float(input("Enter y(0) => "))
    h = float(input("Enter step size h => "))
    to_find = float(input("Enter required x to find y => "))
    n = round(to_find/h)

    eq = get_eq(fxy)
    console("Equation = ", eq, "\n")
    print_formula()

    for i in range(n):
        console(F"STEP {i+1} -> ")

        k1 = get_k1(eq, x0, y0, h)
        k2 = get_k2(eq, x0, y0, h, k1)
        k3 = get_k3(eq, x0, y0, h, k2)
        k4 = get_k4(eq, x0, y0, h, k3)
        temp = y0

        y0 = y0 + (k1 + 2*k2 + 2*k3 + k4) / 6
        x0 = x0 + h

        console(f"y({x0}) = {temp} + (k1 + 2*k2 + 2*k3 + k4) / 6 = {y0}\n")
