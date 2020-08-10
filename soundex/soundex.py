# !pip install jellyfish

import jellyfish
import re
import pandas as pd
import os
print(os.getcwd())
#soundex 알고리즘
def soundex(word):
    word = word.lower()
    n = len(word)
    vowel_like = ['a', 'e', 'i', 'o', 'u', 'y', 'h', 'w']#drop
    lips = ['b', 'f', 'v', 'p']#1
    others = ['c', 'g','j','k', 'q', 's', 'x', 'z']#2
    dt = ['d', 't']#3
    #l #4
    mn = ['m', 'n']#5
    #r 6
    code = word[0]
    redundant_pat = re.compile(r'([123456])(\1)+')
    
    for i in range(1, n):
        if word[i] in lips:
            code += '1'
        elif word[i] in others:
            code += '2'
        elif word[i] in dt:
            code += '3'
        elif word[i] in 'l':
            code += '4'
        elif word[i] in mn:
            code += '5'
        elif word[i] == 'r':
            code += '6'
        else:
            continue
    while True:
        code_save = code
        code = re.sub(redundant_pat, r'\1', code)
        
        if code_save == code:
            break
    if len(code) == 1:
        code += '000'
    elif len(code) == 2:
        code += '00'
    elif len(code) == 3:
        code += '0'
    
    return code


df = pd.read_csv("../Algorithms/soundex/미국영국아일랜드이름.csv", index_col = False, encoding = 'utf8')
df.head()
boy_names = df['boy'].to_list()
girl_names = df['girl'].to_list()


soundex_ls_b = list(map(lambda x: soundex(x), boy_names))
soundex_ls_g = list(map(lambda x: soundex(x), girl_names))


d_b = {'boy': boy_names, 'soundex': soundex_ls_b}
df_b = pd.DataFrame(data=d_b)


d_g = {'girl': girl_names, 'soundex': soundex_ls_g}
df_g = pd.DataFrame(data=d_g)


while 1:
    gender = input("성별을 입력하세요(g/b): ")
    name = input("이름을 영어로 입력하세요: ")
    if gender == 'g':
        print(df_g[df_g.soundex == soundex(name)])
    if gender == 'b':
        print(df_b[df_b.soundex == soundex(name)])
    exit = input("종료?(y/n):")
    if exit == 'y':
        break