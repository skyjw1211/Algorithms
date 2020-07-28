#소트인사이드

number = input()

ls = []
for i in range(len(number)):
    ls.append(int(number[i]))


ls.sort(reverse=True)
for l in ls:
    print(l, end='')