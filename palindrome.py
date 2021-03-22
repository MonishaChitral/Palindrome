userinp = input("Enter input:")

if type(userinp) == int:
	temp = userinp
	rev  = 0
	while(userinp>0):
		dig=userinp%10
		rev=(rev*10)+dig
		userinp=userinp/10
	if(temp == rev):
		print("The number is palindrome!")
	else:
		print("The number is not palindrome!!")
else:
	if userinp == userinp[::-1]:
		print("The string is palindrome!")
	else:
		print("The string is not a palindrome!")
		
print("Thank you:)")
