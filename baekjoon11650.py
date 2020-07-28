#좌표 정렬하기
n = int(input())

ls = []
for _ in range(n):
    ls.append(tuple(map(int, input().split())))

ls = sorted(ls) #자동으로 정렬(기준: l[0], l[1])

for l in ls:
    print(l[0], l[1])


