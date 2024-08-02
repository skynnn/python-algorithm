'''
a -> b 의존
 - b 감염 -> a 감염
 - a 감염 -> b 감염 X

해킹한 컴퓨터 번호, 의존성 -> 몇대의 컴퓨터 감염? 시간?
'''

import sys, heapq
input = sys.stdin.readline
inf = int(1e9)

def dijkstra(graph, start):
    # 컴퓨터 감염 최단 시간 기록
    time = [inf] * (n+1)
    time[start] = 0

    # 감염되는 컴퓨터, 마지막 컴퓨터 감염 시간
    cnt, end = 0, 0

    heap = []
    heapq.heappush(heap, (0, start))
    while heap:
        curr_time, curr_computer = heapq.heappop(heap)
        if curr_time < time[curr_computer]:
            continue
    
        for next in graph[curr_computer]:
            next_time, next_computer = next[0], next[1]
            # 최단 시간 갱신
            if curr_time + next_time < time[next_computer]:
                time[next_computer] = curr_time + next_time
                heapq.heappush(heap, (curr_time + next_time, next_computer))
    
    for t in time:
        if t < inf:
            cnt +=1
            # 마지막 컴퓨터 감염 시간
            if t > end:
                end = t

    return cnt, end

test = int(input())

for _ in range(test):
    n, d, c = map(int, input().split()) # 컴퓨터, 의존성, 해킹 컴퓨터 번호
    graph = [[] for _ in range(n + 1)]
    for _ in range(d):
        a, b, s = map(int, input().split()) # a가 b 의존, b 감염 s초 후 -> a 감염
        graph[b].append([s, a])
    cnt, end = dijkstra(graph, c)
    print(cnt, end)