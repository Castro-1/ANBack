def current_error(x2,x1,error):
		if error == 0:
			return abs(x2-x1)
		else:
			return abs(x2-x1)/x2