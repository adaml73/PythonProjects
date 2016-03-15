i = int(input('enter i value '))
n = int(input('enter n value '))
ans = 0
selectType = input('selectType, 1, 2, or 3 ')

def powerOne(i, n, ans):
		ans = (n * ( n + 1)) / 2 
		return ans


def powerTwo(i, n, ans):
		ans = (n * (n + 1) * (2 * n + 1)) / 6
		return ans 

def powerThree(i, n, ans): 
		ans = ( n ** 2 ) * (( n + 1 ) ** 2)
		ans = ans / 4
		return ans  




if selectType == 1: 
	ans = powerOne(i, n, ans)
	 

elif selectType == 2: 
	ans = powerTwo(i, n, ans)
	 
elif selectType == 3:
	  ans = powerThree(i, n, ans)
else: 
	print("invalid input type")


print("Calculated answer")
print ans







	









