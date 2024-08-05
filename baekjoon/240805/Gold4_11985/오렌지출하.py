'''
1 ~ n : 오렌지 번호, Ai : i번째 오렌지 크기
한 상자에 최대 M개
오렌지 넣는 비용  = K + s(a - b)
a : 상자에 넣은 오렌지 중 가장 큰 오렌지 크기
b : 상자에 넣은 오렌지 중 가장 작은 오렌지 크기
s : 상자에 넣은 오렌지 개수
K : 상자 포장 비용
'''

import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
orange = [0]+[int(input()) for _ in range(n)]
dp = [0] * (n + 1)
dp[1] = k

for i in range(2, n + 1):
    max_o = orange[i]
    min_o = orange[i]
    
    dp[i] = dp[i-1] + k

    for size in range(2, min(m, i)+1):

        j = i - size + 1 

        max_o = max(max_o, orange[j])
        min_o = min(min_o, orange[j])

        dp[i] = min(dp[i], dp[j-1] + k + size * (max_o - min_o))

print(dp[n])