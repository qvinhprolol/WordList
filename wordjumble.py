import random
print("Đây là chương trình đoán từ hehehe")
word = 'complicated'
charlist = list(word)
n = len(word)
i = 0
print("Đây là từ mà đã xáo chữ cái")
while i < n:
    z = random.randint(0,n)
    if z < len(charlist):
        print(charlist[z])
        charlist.remove(charlist[z])
        i = i + 1
    else:
        continue

while True:
    guess = input('Nhập từ trước khi tráo đê: ')
    if guess == word:
        print('Chúc mừng con gà!!')
        break
    else:
        continue
        

