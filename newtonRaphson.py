
import math

def newtonRaphson(f, Df, x0, tol=5e-6 , niter = 10):
    fn = []
    E = []
    X = []
    N = []
    c = 0
    xn = x0
    fxn = f(xn)
    Dfxn = Df(xn)
    error = 100
    fn.append(fxn)
    X.append(xn)
    E.append(error)
    N.append(c)
    print("n   | nx        | fx        | e        ")
    print(f"{N[c]}   |{X[c]}        |{fn[c]}    |{E[c]}")
    while error > tol and fxn!= 0 and Dfxn!=0 and c<niter:
        xn = xn - fxn/Dfxn
        fxn = f(xn)
        Dfxn = Df(xn)
        fn.append(fxn)
        X.append(xn)
        c = c+1
        error = abs(X[c]-X[c-1])/xn
        N.append(c)
        E.append(error)
        print(f"{N[c]}   |{X[c]}        |{fn[c]}    |{E[c]}")

    print("-----------------------------------------")
    if f==0:
        s=xn
        print(s,"es raiz de f(x)")
    elif error<tol:
        s=xn
        print(s,"es una aproximacion de un raiz de f(x) con una tolerancia", tol)
        print("N",N)
        print("xn",xn)
        print("fn",fn)
        print("Error",E)
    else:
        s=xn
        print("Fracaso en ",niter, " iteraciones ") 
    return None

def main():
    p = lambda x: math.pi**-x * (-1 + x) + x**(2/3) - 41
    Dp = lambda x: (3*math.pi**-x * x + 3*math.pi**-x * x * math.log10(math.pi) - 3*math.pi**-x * x**2 * math.log10(math.pi) + 2 * x**(2/3))/(3*x)
    approx = newtonRaphson(p,Dp,41,0.5e-6,100)
    print(approx)

main()



    