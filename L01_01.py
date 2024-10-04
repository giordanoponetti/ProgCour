# to print 'data' where elements are to the power of 2
# and just multiple of 3 are printed

data = [1,2,3,4,5,6,7,8,9]
print([x**2 for x in data if x%3==0])
