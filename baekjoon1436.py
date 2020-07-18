#영화감독 숌

n = int(input())

ls = []

cnt = 665
while True:
    cnt+=1
    if '666' in str(cnt):
        ls.append(cnt)
    if len(ls) == n:
        print(cnt)
        break
