import os #operating system

#讀取檔案
product = []
if os.path.isfile('product.csv'): #檢查檔案是否存在
	print('找到此檔案!')
	with open('product.csv', 'r' , encoding = 'utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue
			name, price = line.strip().split(',') 
			product.append([name, price])
	print(product)
else:
	print('找不到此檔案喔...')

#讓使用者輸入購買紀錄
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
	    break 
	price = input('請輸入商品價格: ')
	price = int(price)
	#p = [name, price]
	product.append([name, price])
print(product)

#印出所有購買紀錄
for p in product:
	print(p[0], '的價格是', p[1])

#寫入檔案
with open('product.csv', 'w', encoding = 'utf-8') as f:
	f.write('商品,價格\n')
	for p in product:
		f.write(p[0] + ',' + str(p[1]) + '\n') #只能字串相加