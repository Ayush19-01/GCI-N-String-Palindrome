# Made for the sole purpose of GCI 2019 
def replace(a,b):
	global count
	global y
	x=""
	for i in y:
		if i==a:
			x+=b
		if i!=a:
			x+=i
	print("String after applying replace function  {} time(s) = {}".format(count,x))
	print()
	return x
def palindrome1(low,high):
	global count
	global y
	global yorg
	if low>high or low==high:
		if count==0:
			print("The given string is already a palindrome so number of minimum steps to convert is 0")
			print()
		if count>0:
			print("String after applying replace function {} time(s) is succesfully converted  into a palindrome = {}".format(count,y))
			print()
			print('Minimum number to apply replace function to convert {} into palindrome : {} time(s)'.format('"'+yorg+'"',count))
			print()
		return None
	if low<high:
		if y[low]==y[high]:
			return(palindrome1(low+1,high-1))
		if y[low]!=y[high]:
			count+=1
			y=replace(y[high],y[low])
			return(palindrome1(low+1,high-1))
while True:
	count = 0
	print()
	y=input("Enter a string : ")
	yorg=y
	print()
	low=0
	high=len(y)-1
	palindrome1(low,high)
	ask=input("Do you wish to test for another string?[y/N] : ")
	if ask=="y":
		continue
	else:
		print()
		print("Closing...")
		break
