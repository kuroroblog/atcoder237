# <回文になるための条件>
# 文字列Sは、全て`a`である場合
# 文字列Sは元から回文である場合
# 文字列Sの左側と右側にある、連続するaの個数を等しくして、回文である場合

# 標準入力を受け付ける。
S = input()

# 文字列Sは、全て`a`である場合
if S.count('a') == len(S):
    print('Yes')
    exit()

# 文字列Sは元から回文である場合
# 回文の判定方法 : https://www.delftstack.com/ja/howto/python/python-palindrome/
if S == S[::-1]:
    print('Yes')
    exit()

SLen = len(S)

# 文字列Sの右側から、何個連続してaが続いているか数える。
right_a_count = 0
while S[SLen - 1] == 'a':
    SLen -= 1
    right_a_count += 1

# 文字列Sの左側から、何個連続してaが続いているか数える。
left_a_count = 0
while S[left_a_count] == 'a':
    left_a_count += 1

# 文字列Sの左側へ、連続するaを追加する。左側と右側にある、連続するaの個数を等しくする。
# 同じ文字列を複数回繰り返す方法 : https://it-engineer-info.com/language/python/repeat-string
S = ('a' * (right_a_count - left_a_count)) + S

# 文字列Sの左側と右側にある、連続するaの個数を等しくして、回文である場合
if S == S[::-1]:
    print('Yes')
else:
    print('No')
