#나이순 정렬
#stable sort
import sys
n = int(input())
ls = []

for i in range(n):
    temp = sys.stdin.readline().split()
    age = int(temp[0])
    name = temp[1]
    order = i
    
    ls.append((age, name, order))

ls = sorted(ls, key = lambda x: (x[0], x[2]))

for i in range(n):
    print(ls[i][0], ls[i][1])


"""
3
21 Junkyu
21 Dohyun
20 Sunyoung
"""