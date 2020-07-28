### 수 정렬하기 1

n = int(input())

ls = []

for i in range(n):
    k = int(input())
    if not ls:
        ls.append(k)
    else:
        for j in range(len(ls)):
            if ls[j]>k:
                ls.insert(j, k)
                break
        if j == len(ls)-1:
            ls.append(k)
for num in ls:
    print(num)