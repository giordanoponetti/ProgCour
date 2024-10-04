#	to print 'data' where elements are to the power of 2
#	and just multiple of 3 are printed
#	done by defining the function is_divby3 and passing
#	the result to the condition in the for loop

data = [1,2,3,4,5,6,7,8,9]

def is_divby3(number):
	return number%3==0


print([x**2 for x in data if is_divby3(x)])
