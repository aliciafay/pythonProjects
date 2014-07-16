#alicia leslie
#Palindrome
#example-noon,dad,racecar

#enter your string
#compare index of string with while loop, 1)need length of string
#1st element=0 
#last=len(s)-1

def main():
	s=input("Enter a string:")
	if isPalindrome(s):
		print(s,"is a palindrome")
	else:
		print(s,"is not a palindrome")

def isPalindrome(s):
	#index of the first character
	low=0
	#index of last character
	high=len(s)-1
	while low<high:
		if s[low]!=s[high]:
			return False
		low+=1
		high-=1
	return True
main()
