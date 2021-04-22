from sympy import Symbol, simplify

X = Symbol("x")

if __name__ == "__main__":
    # xi = "5 7 11 13 17"
    # yi = "150 392 1452 2366 5202"
    # val = 9
    xi = input("Enter x => ")
    yi = input("Enter y => ")
    val = input("Enter value => ")
    xi = [float(i) for i in xi.split(" ")]
    yi = [float(i) for i in yi.split(" ")]
    n = len(xi)
    d = [yi]
    Y = yi[0]

    for i in range(n-1):
        k = []
        mul = 1
        for j in range(n-i-1):
            num = d[i][j+1] - d[i][j]
            den = xi[j+i+1] - xi[j]
            k.append(num/den)
            
        for  l in range(i+1):
            mul *= X - xi[l]

        d.append(k)
        print(f"d{i+1} => ", k)

        Y += mul*k[0]

    print(Y)
    print(simplify(Y))
    print(Y.subs("x", val))
