def sigma1(n):
	def loop(n,sum):
		if n > 0:
		  return loop(n-1,n+sum)
		else:
		  return sum 
	return loop(n,0)	
def sigma2(n)
	sum = 0 
	while n > 0:
		sum = n + sum
		n = n - 1
	return sum 