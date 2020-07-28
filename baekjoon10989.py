# 수 정렬하기 3
import sys
n = int(sys.stdin.readline())


countings = [0]*10001 #0~10000
for num in range(n):
    countings[int(sys.stdin.readline())] += 1
   

for i in range(10001):
    while countings[i] > 0:
        print(i)
        countings[i] -= 1
