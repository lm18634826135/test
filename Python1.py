temp = input("请输入你所猜的数字：")
guess = int(temp)
if guess == 8:
    print("对了")
else:
    if guess > 8:
        print("大了")
    else:
        print("小了")
print("over")
