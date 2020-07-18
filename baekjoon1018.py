#a<b#체스판 다시 칠하기

a = "BWBWBWBW"
b = "WBWBWBWB"

def dif_chr_cnt(s1, s2): #두 문자열 비교해서 다른 글자의 수를 리턴 여기서는 두 문자열의 길이가 항상 같도록 인자를 준다.
    cnt = 0
    for i in range(len(s1)):
        if s1[i]!=s2[i]:
            cnt += 1
    return cnt


y, x = map(int, input().split())

ls = [None]*y

for i in range(y):
    ls[i] = input()
min_cnt = 64 #8*8이기에 최대 64번 바꿀 수 있다. min_cnt는 cnt의 값이 감소하면 갱신된다.
#총 (y-7) * (x-7)개의 8*8 체스판을 만들 수 있다. 
#첫번 째줄이 어떤 값이냐에 따라 다르다. a, b중, 마지막 줄도 고려해야 함. version을 2개다 고려해야 한다. 

ab_ls = [a, b]
for i in range(y-7): #i는 가로 시작점
    for j in range(x-7): #j는 세로 시작점
        cnt1 = 0
        cnt2 = 0
        for k in range(8):
            cnt1 += dif_chr_cnt(ls[i+k][j:j+8], ab_ls[k%2]) #0이 a로 썼으면, 1은 b, 2는 a ...
            cnt2 += dif_chr_cnt(ls[i+k][j:j+8], ab_ls[(k+1)%2])
        if min_cnt > min(cnt1, cnt2):
            min_cnt = min(cnt1, cnt2)
print(min_cnt)