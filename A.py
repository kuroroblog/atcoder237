# 標準入力を受け付ける。
N = int(input())

# -2の31乗, 2の31乗をpow関数を用いて表現する。
# pow関数とは? : https://himibrog.com/python-pow/
# if文を用いて`Yes`, `No`の判定を行う。
# 未満 = 自身の数を含まない。
# 以上 = 自身の数を含む。
if pow(-2, 31) <= N and N < pow(2, 31):
    print('Yes')
else:
    print('No')
