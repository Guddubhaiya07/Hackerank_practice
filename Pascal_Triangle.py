from math import comb
class Solution:

	def nthRowOfPascalTriangle(self, n):
	    return [comb(n-1,i) for i in range(n)]
	
