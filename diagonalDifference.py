def diagonalDifference(arr):
	d1 = sum([arr[x][x] for x in range(len(arr))]) 
	d2 = sum([arr[x][len(arr)-1-x] for x in range (len(arr))])
	return abs(d1-d2)


a=[	[2,3,4],
	[3,4,5],
	[5,6,8]]
b=[[65,56,78,56],[-2,-45,56,67],[45,76,87,34],[4,56,78,45]]
c=[[34,56,78,97,56],[-23,-2,-6,6,8],[-12,-10,-6,-7,-8],[7,4,7,8,9],[4,5,7,8,9]]

print(diagonalDifference(a))
print(diagonalDifference(b))
print(diagonalDifference(c))