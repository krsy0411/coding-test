# 신장트리
하나의 그래프에서 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프
> 사이클이 발생하면 신장트리가 X

### 최소비용 신장트리(MST: minimum spanning tree) 알고리즘 제약조건
1. 그래프 내 존재하는 간선들만 사용
2. n-1개(정점 개수 - 1)의 간선만 사용
3. 사이클을 형성하는 간선은 사용불가

# 크루스칼 알고리즘
신장 트리 중 최소한의 비용으로 만들 수 있는 신장 트리를 찾는 알고리즘

## 크루스칼 알고리즘 동작과정
1. 간선 데이터를 비용에 따라 오름차순 정렬
2. 간선을 하나씩 확인(가장 최소 비용의 간선)하며 현재의 간선이 사이클을 발생시키는지 확인
    * 사이클이 발생하지 않는 경우 : 최소신장트리에 포함
    * "하는 경우 : 포함시키지 않음
3. 모든 간선에 대해 2번 과정 반복