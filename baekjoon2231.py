#분해합

x = input()
num = int(x)

def check_constructor(n, x):
    sum = n
    while n != 0:
        sum += n%10
        n //= 10
    return sum == x

min_const = -1
num -= 1
while num>0:
    if check_constructor(num, int(x)):
        min_const = num
    num -=1


if min_const != -1:
    print(min_const)
else: 
    print(0)




