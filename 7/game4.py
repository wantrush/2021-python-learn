print ("第一个游戏")
counts =3 
while counts > 0:
    #temp = input ("猜猜我想的是哪个数字？",counts,"次机会哦~：")
    temp = input ("猜猜我想的是哪个数字？三次机会哦~：")
    guess = int (temp)
    if guess ==8:
        print('准！')
        print('猜中也没有奖励！哈哈哈')
        break
    else:
        if guess > 8:
            print('大了大了！')
        else:
            print('小了小了！！')
        counts = counts -1
print('游戏结束：）')