print("question 1")
m=float(input("Enter marks"))
if (m<25):
    print("Grade F")
elif (m>=25 and m<45):
    print("Grade E")
elif (m>=45 and m<50):
    print("Grade D")
elif (m>=50 and m<60):
    print ("Grade C")
elif (m>=60 and m<80):
    print("Grade B")
elif (m>=80):
    print ("Grade A")

print("Question 2")
year = int(input("Year = "))
if((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
	print(year, " is a leap year")
else:
	print(year, " is not a leap year")

print("Question 3")
from random import randint
play=1
while play==1:
    x=randint(0,9)
    y=randint(0,9)
    print("The multiplication problem is",x,"*",y)
    a=int(input("what is your guess?"))
    if a==x*y:
        print("That is correct.")
    else:
        print("That is not correct. The correct answer is ",x*y)
    play=int(input("Enter 1 to play again or 0 to exit."))
else:
    print("Thanks for playing.")

print("Question 4")
for candies in range(200):
    if (candies % 5 != 2):
        continue
    if (candies % 6 != 3):
        continue
    if (candies % 7 != 2):
        continue
    print(str(candies) + " is the answer!")
    break


