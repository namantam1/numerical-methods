"""
x0
y0 = y(x0)
h = x - x0

y(x) = y0 + (y0' * h / fact(1)) + (y0'' * h^2 / fact(2)) + (y0''' * h^3 / fact(3)) ...
"""
from sympy.parsing.sympy_parser import parse_expr
from sympy import diff, Function, symbols

x = symbols("x")
y = Function('y')('x')
k = input("enter function - ")
eq = parse_expr(k, {'x': x, 'y': y})

while True:
    order = input("Enter order or q to exit order - ")
    if order == "q":
        break
    order = int(order)
    d = diff(eq, "x", order)
    print(d)


