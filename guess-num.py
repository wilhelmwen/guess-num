import random
r = random.randint(1, 100)
print(r)
while True:
	num = input('請輸入數字: ')
	num = int(num)
	if num == r:
		print('終於猜對了')
		break

