string1 = input("Enter 1st string: ")
string2 = input("Enter 2nd string: ")

# Initialize an empty result string
result = ""

# Use a loop to iterate over the letters of the two strings
for i in range(max(len(string1), len(string2))):
  # Add the i-th letter from string1 to the result
  if i < len(string1):
    result += string1[i]
  # Add the i-th letter from string2 to the result
  if i < len(string2):
    result += string2[i]

print(result)  # Output: "HWeolrllod"
