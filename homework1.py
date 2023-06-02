# kg = input("enter the weight in Kg")
# pounds = float(kg) * 2.2
# print(pounds)



# import random
# for i in range(50):
# 	a = random.randint(3,6)
# 	print (a)




# x = int(input())
# y = int(input())
# if (x + y == 0):
# 	print("division by zero error. |x-y|/(x+y) can not be evaluated.")
# else:
# 	print("|x-y|/(x+y) = ",abs (x-y)/(x+y))



# year = int(input("Year = "))
# count = ((year - 1600) // 4 - (year - 1600) // 100 + (year - 1600) // 400)
# print(count)



count = 0
for i in range(1,10000):
	s = 0
	for j in range(1,i):
		if i % j == 0:
			s += j
	if s == i:
		count += 1
print(count)