'''
길이 N인 수열 A -> 여러 개의 짝수 팰린드롬으로 분할
짝수 팰린드롬 : 수열의 길이 짝수, 뒤집은 수열 = 기존 수열
짝수 팰린드롬 최대 몇개?
'''

def is_peliondrome(word):
    for left in range(len(word) // 2):
        right = len(word) - left - 1
        if word[left] != word[right]:
            return False
    return True

n = int(input())
numbers = list(map(int, input().split()))
start, end = 0, 2
cnt = 0

while end <= n:
    word = numbers[start : end]
    if is_peliondrome(word):
        cnt += 1
        start = end
        end += 2
    else:
        if end == n: # 마지막까지 왔는데 팰린드롬이 아니라면 짝수 팰린드롬 만족 X
            cnt = -1
            break
        end += 2

print(cnt)