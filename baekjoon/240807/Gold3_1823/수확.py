'''
양 끝에 있는 벼만 수확 가능
벼의 가치 v(i), 벼를 k번째로 수확 -> v(i)*k 이익
최대 이익?
'''
import sys
sys.setrecursionlimit(2000)
input = sys.stdin.readline

n = int(input())
rice_value = [int(input()) for _ in range(n)]
dp = [[0] * n for _ in range(n)]

def best(left, right, d):
    if left > right:
        return 0
    
    if dp[left][right] == 0:
        dp[left][right] = max(best(left + 1, right, d + 1) + rice_value[left] * d,
                              best(left, right - 1, d + 1) + rice_value[right] * d)
        
    return dp[left][right]

print(best(0, n - 1, 1))