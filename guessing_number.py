import random

r = random.randint(1, 100)
mini = 0
maxi = 100

while True:
	num = input('please guess the number: ')
	num = int(num)
	if num == r:
		print('congratulation! you got it right!')
		break
	elif num > r :
		maxi = num
		print('the number is between', mini, 'and', num)
	elif num < r:
		mini = num
		print('the number is between', num, 'and', maxi)



