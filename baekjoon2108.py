#통계학
import sys
from collections import Counter

n = int(sys.stdin.readline())

nums = []
for _ in range(n):
    nums.append(int(sys.stdin.readline()))

nums.sort()

arith_avg = round(sum(nums)/n) #평균값
centre = nums[n//2] #중앙값

nums_freq = Counter(nums).most_common()
if len(nums_freq) > 1 and nums_freq[0][1] == nums_freq[1][1]:
    freq = nums_freq[1][0]
else:
    freq = nums_freq[0][0]

range_value = max(nums)-min(nums) #범위

print(arith_avg)
print(centre)
print(freq)
print(range_value)