"""
[
    [R0_0, R1_0],
    [R0_1, R1_1],
]

Rk_i = (4_i * Rk_(i-1) - R(k-1)_(i-1)) / (4_i - 1)
"""
from sympy.parsing.sympy_parser import parse_expr
from sympy import symbols

def console(val, *args, **kwargs):
    print(">> ", val, *args, **kwargs)

def romb(k, i, Rk_im1, Rkm1_im1):
    r = (4**i * Rk_im1 - Rkm1_im1) / (4**i - 1)
    console(f"R{k}{i} = ({4**i} * R{k}{i-1} - R{k-1}{i-1}) / ({4**i} - 1) = {r}")
    return r

def trape(h, y=[]):
    y0 = y.pop(0)
    yn = y.pop(-1)
    s = 0
    for i in y:
        s += i
    return h/2 * (y0 + yn + 2 * s)

def get_eq(eq):
    return parse_expr(eq)

def evalute(eq, val):
    return eq.subs({"x": val})

if __name__ == "__main__":
    y = input("Function => ")
    ul = float(input("UL => "))
    ll = float(input("LL => "))
    cyles = int(input("Cycles => "))
    # R = [[] for _ in range(cyles)]
    R = [None, ]
    eq = get_eq(y)

    console("Step 1 -> Trapezoid formula")
    for i in range(cyles):
        n = 2**i
        h = (ul-ll)/n
        x = [ll + j * h for j in range(n+1)]
        y = [evalute(eq, j) for j in x]
        console(f"n = {n} h = {h}")
        console("x => ", x)
        console("y => ", y)

        r = trape(h, y)
        console(f"R0{i+1} = ", r)
        R.append([r])
        print("\n")

    console("Step 2 -> Romberg formula ")
    n = cyles
    for i in range(1, n):
        for j in range(1, n-i+1):
            k = i+j
            # print(k, i)
            r = romb(k, i, R[k][i-1], R[k-1][i-1])
            # console(f"R{k}{i} = {r}")
            R[j+i].append(r)
        print("\n")

    for r in R:
        r and console(r)
