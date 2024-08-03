'''
길이가 10인 롤케이크 최대한 많이 만들기

1. 자를 롤케이크를 하나 고른다. 길이가 1보다 큰 롤케이크만 자르기 가능.
   이때, 고른 롤케이크 길이를 x
2. 0보다 크고, x보다 작은 자연수 y
3. 롤케이크를 잘라 길이가 y, x-y인 롤케이크 두개로 만든다

재현이는 롤케이크를 최대 M번 자를 수 있다.
길이 10인 롤케이크 개수 최대값은?
'''

n, m = map(int, input().split())
cake = list(map(int, input().split()))
cake.sort(key = lambda x :(x % 10, x)) # 나머지가 없는 경우, 더 적게 자르고 케이크 획득 가능
cnt = 0

for i in range(n):
    if m == 0:
        break

    while cake[i] > 10 and m > 0:
        cake[i] -= 10
        cnt += 1
        m -= 1
    
    if cake[i] == 10: # 케이크가 10이면 안 자르고 하나 더 획득 가능
        cnt += 1

print(cnt)