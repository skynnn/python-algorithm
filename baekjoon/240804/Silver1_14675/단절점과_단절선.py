'''
단절점 : 해당 정점을 제거했을 때, 그 정점이 포함된 그래프가 2개 이상으로 나뉘는 경우
단절선 : 해당 간선을 제거했을 때, 그 간선이 포함된 그래프가 2개 이상으로 나뉘는 경우
트리 : 사이클 X, 모든 정점 연결
트리에서 단절점과 단절선 찾기
'''
import sys
input = sys.stdin.readline

n = int(input()) # 트리의 정점 개수
tree = [[] for i in range(n + 1)]
for i in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

q = int(input()) # 질의의 개수
for _ in range(q):
    # t = 1 -> k 단절점?
    # t = 2 -> k 간선 단절선?
    t, k = map(int, input().split())
    if t == 1:
        # 자식이 하나 밖에 없는 루트 or 리프 노드인 경우 -> 단절점 X
        if len(tree[k]) <= 1:
            print('no')
        else :
            print('yes')
    else: # t == 2 -> 모든 간선은 노드 2개를 연결하고 있음 -> 모두 단절선
        print('yes')