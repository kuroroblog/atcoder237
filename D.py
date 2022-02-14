# <方針>
# i − 1のすぐ左 or 右にiを挿入する。 ⏩ i − 1とiは隣り合っている。 ⏩ 両端キューを活用する。
# 両端キューとは? : https://www.weblio.jp/content/%E4%B8%A1%E7%AB%AF%E3%82%AD%E3%83%A5%E3%83%BC#:~:text=%E4%B8%A1%E7%AB%AF%E3%82%AD%E3%83%A5%E3%83%BC%EF%BC%88%E3%82%8A%E3%82%87%E3%81%86%E3%81%9F%E3%82%93%E3%82%AD%E3%83%A5%E3%83%BC,%E5%89%8A%E9%99%A4%E3%81%A7%E3%81%8D%E3%82%8B%E3%82%AD%E3%83%A5%E3%83%BC%E3%81%A7%E3%81%82%E3%82%8B%E3%80%82

from collections import deque

# 標準入力を受け付ける。
N = int(input())
S = input()

# deque参考 : https://note.nkmk.me/python-collections-deque/
d = deque([str(N)])

for i in range(N):
    num = N - i - 1
    if S[num] == 'L':
        d.append(str(num))
    else:
        d.appendleft(str(num))

print(' '.join(list(d)))
