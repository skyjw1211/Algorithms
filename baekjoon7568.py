#덩치

n = int(input())


ls = []
for _ in range(n):
    ls.append(tuple(map(int, input().split())))


def compare(a, b):
    if a[0]>b[0] and a[1]>b[1]:
        return 1 #a>b
    elif a[0]<b[0] and a[1]<b[1]:
        return -1 #a<b
    else:
        return 0 #cannot compare

for i in range(n):
    upper = 0
    for j in range(n):
        if compare(ls[j], ls[i])==1: #나보다 큰 사람 있으면 +1
            upper += 1
    print(upper+1, end = ' ')    #등수

