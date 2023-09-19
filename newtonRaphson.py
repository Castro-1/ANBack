
def newtonRaphson(func, dfunc, xi, niter, tol = 5E-3):
    fm = e = []
    i = 0
    def f(x):
        f = eval(func)
        return f
    
    def d(x):
        d = eval(dfunc)
        return d
    
    fxi = f(xi)
    dfxi = d(xi) 
    xr = xi - (fxi/dfxi)

    fm.append(xr)
    e.append(100)

    while tol < e[i] and i <= niter:
        i+=1
        fxi = f(xi)
        dfxi = d(xi) 

        xr = xi - (fxi/dfxi)
        fm.append(xr)
        error = abs(fm[i]-fm[i-1])
        e.append(error)

        xi = xr
    print(f"the root was found to be at {xi} after {i} iterations with an error of {e[i]}!")
        
newtonRaphson("2*x**3 + x**2 -1", "6*x**2 + 2*x", 1, 1000)


    