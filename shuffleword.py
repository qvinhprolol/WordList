import random
word = input("Nhập từ muốn trộn chữ cái vào: ")
charlist = list(word)
n = len(word)
i = 0
while i < n:
    z = random.randint(0,n)
    if z < len(charlist):
        print(charlist[z])
        charlist.remove(charlist[z])
        i = i + 1
    else:
        continue


    