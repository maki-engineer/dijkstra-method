from typing import List


def dijkstra(graph: List[List[int]], start: int, end: int) -> List:
    """ダイクストラ法を行う。

    Args:
        graph (List[List[int]]): 頂点間の距離を格納した隣接行列(二次元配列)
        start (int): スタート地点
        end (int): ゴール地点

    Returns:
        List: 最短経路と最短距離を配列で返す。
    """

    nodes = len(graph)
    shortest_nodes = [float('inf')] * nodes
    shortest_nodes[start] = 0
    shortest_path = [[] for _ in range(nodes)]
    unvisited = set(range(nodes))

    while unvisited:
        current = min(unvisited, key=lambda node: shortest_nodes[node])
        unvisited.remove(current)

        for node in unvisited:
            if graph[current][node] > 0:
                new_distance = shortest_nodes[current] + graph[current][node]
                if new_distance < shortest_nodes[node]:
                    shortest_nodes[node] = new_distance
                    shortest_path[node] = shortest_path[current] + [node]

    return [shortest_path[end], shortest_nodes[end]]


graph = [
    [0, 2, 8, 4, 0, 0, 0],
    [2, 0, 0, 0, 3, 0, 0],
    [8, 0, 0, 0, 2, 3, 0],
    [4, 0, 0, 0, 0, 8, 0],
    [0, 3, 2, 0, 0, 0, 9],
    [0, 0, 3, 8, 0, 0, 3],
    [0, 0, 0, 0, 9, 3, 0]
]
start = 0
end = 6

shortest_path, shortest_distance = dijkstra(graph, start, end)
print(f"最短経路：{shortest_path}")      # >> 最短経路：[1, 4, 2, 5, 6]
print(f"最短距離：{shortest_distance}")  # >> 最短距離：13
