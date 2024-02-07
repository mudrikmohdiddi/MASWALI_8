"""4. Number Analysis Program
Design a program that asks the user to enter a series of 20 numbers.
The program should store the numbers in a list and then display the following data:
• The lowest number in the list
• The highest number in the list
• The total of the numbers in the list
• The average of the numbers in the list"""

number=[]
high_number=0
series=int(input("Please enter number of series:"))
for i in range(1,series+1):
    enter_number=float(input(f"Please enter number series.{i} on {series} series:"))
    number.append(enter_number)
    if(high_number<enter_number):
        high_number=enter_number
lower_number=high_number
total_number=0
for i in number:
    if(lower_number>i):
        lower_number=i
    total_number+=i
print(f"The lowest number in the list is {lower_number}")
print(f"The highest number in the list is {high_number}")
print(f"The total of the numbers in the list is {total_number}")
print(f"The average of the numbers in the list is {total_number/len(number)}")
    
    


