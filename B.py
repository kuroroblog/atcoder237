# 標準入力を受け付ける。
H, W = map(int, input().split())

A = []
for _ in range(H):
    A.append(list(map(int, input().split())))

# 転置行列なので、行と列の長さを反転させる。 = ループの順序を反転させる。
for i in range(W):
    tmp = []
    # 転置行列なので、行の探索ではなく列の探索を行う。
    for j in range(H):
        tmp.append(str(A[j][i]))

    print(' '.join(tmp))
