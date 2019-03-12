import random
r = random.randint(1, 100)
t = 0
print(r)
while True:
	num = input('請輸入數字: ')
	num = int(num)
	t = t + 1
	if num == r:
		print('終於猜對了')
		
		print('總共猜了', t, '次')
		break


