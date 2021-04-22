"""
integral(f(x)) = (h/2)[y0+yn+2(y1+y2+y3...y(n-1))]
integral(f(x)) => (h/2)[2(y0+yn+y1+y2+y3...y(n-1))-(y0+yn)]
"""
from sympy import parse_expr, Symbol

class Integrate:

    def __init__(self, h=1, fx="x", a=0, b=6):
        self._h = h
        self._n = int(((b-a)/h) + 1)
        self.fx = fx
        self._x = [a+self._h*(i) for i in range(self._n)]
        self._y = [self.eval_fx(i) for i in self._x]

    @property
    def fx(self):
        return self._fx

    @fx.setter
    def fx(self, val):
        if not isinstance(val, Symbol):
            val = parse_expr(val)

        self._fx = val

    def eval_fx(self, val):
        return self._fx.subs("x", val)

    def trapeziod(self):
        print("\nTrapezoid\n==========")
        sum_y = 0
        for i, y in enumerate(self._y):
            print(f"x{i} = {self._x[i]}, y{i} = {y}")
            sum_y += y
        sol = (self._h/2)*(2*sum_y - (self._y[0]+self._y[-1]))
        print(f"Solution => {sol}")

    def simpson13(self):
        print("\nSimpson13\n==========")
        sum_y0 = self._y[0] + self._y[-1]
        sum_y4 = 0
        sum_y2 = 0
        for i, y in enumerate(self._y):
            print(f"x{i} = {self._x[i]}, y{i} = {y}")
            if not (y==self._y[0] or y==self._y[-1]):
                if i%2==0:
                    sum_y2 += y
                else:
                    sum_y4 += y
        sol = (self._h/3)*(sum_y0 + 4*sum_y4 + 2*sum_y2)
        print(f"Solution => {sol}")

    def simpson38(self):
        print("\nSimpson38\n==========")
        sum_y0 = self._y[0] + self._y[-1]
        sum_y3 = 0
        sum_y2 = 0
        for i, y in enumerate(self._y):
            print(f"x{i} = {self._x[i]}, y{i} = {y}")
            if not (y==self._y[0] or y==self._y[-1]):
                if i%3==0:
                    sum_y2 += y
                else:
                    sum_y3 += y
        sol = (3*self._h/8)*(sum_y0 + 3*sum_y3 + 2*sum_y2)
        print(f"Solution => {sol}")

if __name__ == "__main__":
    fx = input("Enter funxtion => ")
    h = float(input("Enter h => "))
    a = float(input("Enter a => "))
    b = float(input("Enter b => "))
    tp = Integrate(h, fx, a, b)
    tp.trapeziod()
    tp.simpson13()
    tp.simpson38()
