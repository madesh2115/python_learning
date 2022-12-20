#Python Learning
#-----------------

# 1. Sum of given Number?
#Given Number
number = [10, 20, 30, 40, 50]

# Method 1
# --------

print(number[0] + number[1] + number[2] + number[3] + number[4])

# Method 2 in while loop
# -----------------------

sum = 0
i = 0
while i<len(number):
	sum = sum + number[i]
	i+=1
print(sum)

# Method 2 in for loop
# ---------------------

sum = 0
for no in number:
	sum = sum + no
print(sum)

# -------------------