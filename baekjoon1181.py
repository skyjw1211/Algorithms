# 단어정렬
n = int(input())

ls = []
for _ in range(n):
    word = input()
    if (len(word), word) not in ls:
        ls.append((len(word), word))

ls = sorted(ls) #(기준: l[0], l[1])

for l in ls:
    print(l[1]) #단어만 출력

"""
13
but
i
wont
hesitate
no
more
no
more
it
cannot
wait
im
yours
"""


