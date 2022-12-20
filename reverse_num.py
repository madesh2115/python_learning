# Program to reverse the digits of a number literally and addition

# Input  = 1234
# Output = 4321

# rem = num % 10                  	# extract the last digit
# reverse = reverse * 10 + rem    	# append rem to the end of the reversed number
# num = num//10                     # drop the last digit
# ----------------------------------------------------------------


num = int(input("Enter a number(Ex.1234): "))

reverse = 0
sum=0
while num > 0:
	rem = num % 10
	reverse = reverse*10+rem
	num = num//10
	sum = rem + sum
print("Reversed number: ", reverse)
print("Total of givein nember: ", sum)

# ------------------------