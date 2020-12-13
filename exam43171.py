# https://level.goorm.io/exam/43171/%EC%96%B4%EB%8A%90-%EA%B0%9C%EB%B0%9C%EC%9E%90-%EC%9D%B4%EC%95%BC%EA%B8%B0/quiz/1

import sys

data = list(str(sys.stdin.readline()))
data.pop()
data = list(map(int, data))

M = max(data)+1

for i in range(M, 100):
    tot = 0
    for j in range(len(data)):
        tot += pow(i, j)*data[len(data)-1-j]
    if pow(tot, 0.5) - int(pow(tot, 0.5)) == 0:
        print(i)
        break
