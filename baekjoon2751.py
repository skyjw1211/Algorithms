#수 정렬하기2
n = int(input())
ls = []
for i in range(n):
    ls.append(int(input()))
    
ls.sort()
for l in ls:
    print(l)