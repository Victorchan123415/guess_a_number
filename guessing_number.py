import random


mini = input('please enter a lowerbound: ')
maxi = input('please enter a upperbound: ')
mini = int(mini)
maxi = int(maxi)
r = random.randint(mini, maxi)

count = 0
while True:
	count = count + 1
	
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
	print('this is your', count, 'guess')  