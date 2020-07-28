#좌표 정렬하기2
n = int(input())

ls = []
for _ in range(n):
    ls.append(tuple(map(int, input().split())))

ls = sorted(ls, key = lambda x: (x[1], x[0])) #(기준: l[1], l[0])

for l in ls:
    print(l[0], l[1])

