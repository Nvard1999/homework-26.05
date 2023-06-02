 Write a program that asks the user for weight in kilograms and converts it to pounds. There are 2.2 pounds in a kilogram
 kg = input("enter the weight in Kg")
 pounds = float(kg) * 2.2
 print(pounds)


Write a program that generates and prints 50 random integers, each between 3 and 6.
 import random
 for i in range(50):
 	a = random.randint(3,6)
 	print (a)



Write a program that asks the user to enter two numbers, x, and y, and computes | x − y | /  x+y.
 x = int(input())
 y = int(input())
 if (x + y == 0):
 	print("division by zero error. |x-y|/(x+y) can not be evaluated.")
 else:
 	print("|x-y|/(x+y) = ",abs (x-y)/(x+y))


A year is a leap year if it is divisible by 4, except that years divisible by 100 are not leap years unless they are also divisible by 400. Ask the user to enter a year, and, using the // operator, determine how many leap years there have been between 1600 and that year.
 year = int(input("Year = "))
 count = ((year - 1600) // 4 - (year - 1600) // 100 + (year - 1600) // 400)
 print(count)


A number is called a perfect number if it is equal to the sum of all of its divisors, not including the number itself. For instance, 6 is a perfect number because the divisors of 6 are 1, 2, 3, 6, and 6 = 1 + 2 + 3. As another example, 28 is a perfect number because its divisors are 1, 2, 4, 7,14, 28, and 28=1+2+4+7+14. However,15 is not a perfect number because its divisors are 1, 3, 5, 15, and 15 != 1 + 3 + 5. Write a program that finds all four of the perfect numbers that are less than 10000.
count = 0
for i in range(1,10000):
	s = 0
	for j in range(1,i):
		if i % j == 0:
			s += j
	if s == i:
		count += 1
print(count)
