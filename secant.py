def secantmethod(func, x0, x1, niter, tol = 5E-3):
    e = fm = []
    i = 0
    def f(x):
        f = eval(func)
        return f
    fx0 = f(x0)
    fx1 = f(x1)
    xi  = x0 - (fx0/((fx0 - fx1)/(x0-x1)))
    e.append(100)
    fm.append(xi)
    while tol < e[i] and i <= niter:
        i+=1
        fx0 = f(x0)
        fx1 = f(x1)

        xi  = x0 - (fx0/((fx0 - fx1)/(x0-x1)))

        x0 = x1
        x1 = xi
        fm.append(xi)
        error = abs(fm[i]-fm[i-1])
        e.append(error)

    print(f"the root was found to be at {xi} after {i} iterations!")

secantmethod("x**2 - 3", 1, 3, 100)
