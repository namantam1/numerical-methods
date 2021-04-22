from sympy import Symbol, simplify, expand

X = Symbol("x")
S1 = []
S2 = []

if __name__ == "__main__":
    x = input("x => ")
    y = input("y => ")
    x = [float(i) for i in x.split(" ")]
    y = [float(i) for i in y.split(" ")]
    assert len(x) == len(y), (
        "length not same"
    )
    print("\n")
    eq = 0
    for i in range(len(x)):
        num = 1
        den = 1
        sx = x[i]
        sy = y[i]
        st = ""
        for j in x:
            if j != sx:
                num *= X-j

                den *= sx-j
                st += f"({sx}-{j})"
        print(sy, " * ",simplify(num), " / ", st)
        print("=> " ,sy, " * ",simplify(num), " / ", simplify(den))
        S1.append((num/den)*sy)
        # eq += num/den

    print("\n")

    for s in S1:
        k = expand(s)
        print(k, " + ")
        S2.append(k)
        eq += k
    
    print("\n")


    print(simplify(eq))
