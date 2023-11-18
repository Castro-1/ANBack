from methods.part1.features import current_error
import math

def biseccion(fun,a,b,tol,niter,error):
	
	fm=[]
	E=[]
	X=[]
	x=a
	fi=eval(fun)
	x=b
	fs=eval(fun)

	if fi==0:
		s=a
		E=0
		X.append(a)
		fm.append(fi)
		# print(a, "es raiz de f(x)")
		return {"found":1,"x":X,"f":fm,"e":E}
	elif fs==0:
		s=b
		E=0
		X.append(b)
		fm.append(fs)
		# print(b, "es raiz de f(x)")
		return {"found":1,"x":X,"f":fm,"e":E}
	elif fs*fi<0:
		c=0
		Xm=(a+b)/2
		x=Xm                 
		fe=eval(fun)
		X.append(x)
		fm.append(fe)
		E.append(100)
		while E[c]>tol and fe!=0 and c<niter:
			if fi*fe<0:
					b=Xm
					x=b                 
					fs=eval(fun)
			else:
				a=Xm
				x=a
				fs=eval(fun)
			Xa=Xm
			Xm=(a+b)/2
			x=Xm 
			fe=eval(fun)
			X.append(x)
			fm.append(fe)
			Error=current_error(Xm,Xa,error)
			E.append(Error)
			c=c+1
		if fe==0:
				s=x
				# print(s,"es raiz de f(x)")
				return {"found":1,"x":X,"f":fm,"e":E}
		elif Error<tol:
				s=x
				# print(s,"es una aproamacion de un raiz de f(x) con una tolerancia", tol)
				# print("Fm",fm)
				# print("E",fm)
				return {"found":1,"x":X,"f":fm,"e":E}
		else:
				s=x
				# print("Fracaso en ",niter, " iteraciones ") 
				return {"found":0,"x":X,"f":fm,"e":E}

	else:
		# print("El intervalo es inadecuado")
		return {"error": "intervalo inadecuado"}

# print(biseccion("math.log10(x)-2",1,10,1e-3,100,0))
