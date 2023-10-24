def newtonRaphsonModified(f, Df, Ddf, x0, tol=0.5e-3 , niter = 10):
    xn = x0
    for n in range(0,niter):
        fxn = f(xn)
        if abs(fxn) < tol:
            print('Found solution after',n,'iterations.')
            return xn
        Dfxn = Df(xn)
        Ddfxn = Ddf(xn)
        xn = xn - (fxn*Dfxn)/((Dfxn**2) - (fxn*Ddfxn))
    print('Exceeded maximum iterations. No solution found.')
    return None

def main():
    p = lambda x: x**4 - 8*x**3 + 21*x**2 - 18*x
    Dp = lambda x: 4*x**3 - 24*x**2 + 42*x - 18
    Ddp = lambda x: 12*x**2 - 48*x + 42
    approx = newtonRaphsonModified(p,Dp,Ddp,-1,0.5e-10,100)
    print(approx)

main()



    
    