#11729 하노이 탑 이동 순서
n = int(input())


cnt = 0
seq = []
def hanoi(n, start, by, to):
    global cnt, seq
    if n == 1:
        seq.append((start, to))
        cnt += 1
    else:
        hanoi(n-1, start, to, by)
        seq.append((start, to))
        cnt += 1
        hanoi(n-1, by, start, to)

hanoi(n, 1, 2, 3)
print(cnt)
for s in seq:
    print(s[0], s[1])

