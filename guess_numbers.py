import itertools
import streamlit as st

def calc_step(x, y):
    if y==0:
        return [x+y, x-y, x*y, -100000]
    else:
        return [x+y, x-y, x*y, x/y]

def check(a):
    if a == 0:
        return '+'
    elif a == 1:
        return '-'
    elif a == 2:
        return '*'
    elif a == 3:
        return '/'
    # else:
    #     return a

def create_result(c, i, j, k):
    t = str(c[0]) + check(i) + str(c[1])
    if (j > 1) and (i < 2):
        t = '(' + t + ')'
    t += check(j) + str(c[2])
    if k > 1:
        t = '(' + t + ')'
    t += check(k) + str(c[3])
    t += "= 10"
    return t

def main(n):
    nums = [int(x) for x in str(n)]
    combs = list(itertools.permutations(nums, 4))
    answers = []
    for c in combs: #[:30]:
        ans2 = calc_step(c[0], c[1])
        for i, a2 in enumerate(ans2):
            ans3 = calc_step(a2, c[2])
            for j, a3 in enumerate(ans3):
                ans4 = calc_step(a3, c[3])
                for k, a4 in enumerate(ans4):
                    if a4 == 10:
                        answers.append(create_result(c, i, j, k))

    st.write('答えの数:', str(len(answers)), ' 以下に例を挙げます')
    for i, a in enumerate(answers):
        if i <3:
            st.write('・', a)
# 文字を入力

# 開始ボタン
while True:
    n = st.text_input('4桁の半角数字を入力して')
    if st.button('計算'):
        try:
            main(n)
        except:
            st.write('エラーが出たのでもう一度入力してください')
    break




# import itertools
# import sys

# # n = 5341
# # コマンドライン引数を取得
# n = sys.argv[1]



# def calc_step(x, y):
#     if y==0:
#         return [x+y, x-y, x*y, -100000]
#     else:
#         return [x+y, x-y, x*y, x/y]

# def check(a):
#     if a == 0:
#         return '+'
#     elif a == 1:
#         return '-'
#     elif a == 2:
#         return '*'
#     elif a == 3:
#         return '/'
#     else:
#         return a

# def create_result(c, i, j, k):
#     t = str(c[0]) + check(i) + str(c[1])
#     if (j > 1) and (i < 2):
#         t = '(' + t + ')'
#     t += check(j) + str(c[2])
#     if k > 1:
#         t = '(' + t + ')'
#     t += check(k) + str(c[3])
#     # t += check(j)
#     # t += str(c[2])
#     # t += check(k)
#     # t += str(c[3])
#     t += "= 10"
#     return t

# def main(n):
#     nums = [int(x) for x in str(n)]
#     # リスト内の４つの要素の並び替えを全て出力する
#     combs = list(itertools.permutations(nums, 4))
#     # print(combs)
#     answers = []
#     # 4つの順番の組み合わせ
#     for c in combs[:30]:
#         ans2 = calc_step(c[0], c[1])
#         for i, a2 in enumerate(ans2):
#             ans3 = calc_step(a2, c[2])
#             for j, a3 in enumerate(ans3):
#                 ans4 = calc_step(a3, c[3])
#                 for k, a4 in enumerate(ans4):
#                     if a4 == 10:
#                         answers.append(create_result(c, i, j, k))

#     print('答えの数:', len(answers))
#     # print('答えの例')
#     for i, a in enumerate(answers):
#         if i <3:
#             print('・', a)
#         else:
#             break
# main(n)