#Calcualting student Total and Average
# --------------------------------

name	=(input("\n Enter Your Name: "))
Tamil 	= int(input("\n Enter Tamil mark: "))
English = int(input("\n Enter English mark: "))
Science = int(input("\n Enter Science mark: "))
Maths 	= int(input("\n Enter Maths mark: "))
Social 	= int(input("\n Enter Social mark: "))

total = Tamil + English + Science + Maths + Social
average = total/5

print('\n Hey',name, ',Your total mark is: ',total, 'and your average is: ',average)