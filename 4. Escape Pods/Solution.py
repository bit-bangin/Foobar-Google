from collections import deque
CORRIDOR_CAPACITY = 2000001

class EscapePods:
    """
    Represents directed graph using adjacency matrix representation.
    """
    def __init__(self, entrances, exits, path):
        n = len(path)
        m = n + 2

        # Graph[0] - now source "s"
        # Graph[-1] - now egress "t"
        self.graph = []
        self.size = m
        for i in range(m):
            self.graph.append([0] * m)

        for i in range(n):
            for j in range(n):
                self.graph[i+1][j+1] = path[i][j]

        for num in entrances:
            self.graph[0][num + 1] = CORRIDOR_CAPACITY

        for num in exits:
            self.graph[num + 1][m - 1] = CORRIDOR_CAPACITY

    def bfs(self):
        parents = [-1] * self.size
        queue = deque()
        queue.append(0)
        while queue and parents[-1] == -1:
            u = queue.popleft()
            for v in range(self.size):
                if self.graph[u][v] > 0 and parents[v] == -1:
                    queue.append(v)
                    parents[v] = u
        path = []
        u = parents[-1]
        while u != 0:
            if u == -1:
                return None
            path.append(u)
            u = parents[u]
        path.reverse()
        return path

    def solve(self):
        max_flow = 0
        path = self.bfs()

        while path:
            """
            Augment flow, while path exists from soure to egress. Find minimum
            residual capacity of edges along the path located.
            """
            cap = CORRIDOR_CAPACITY
            u = 0
            for v in path:
                cap = min(cap, self.graph[u][v])
                u = v
            max_flow += cap
            u = 0
            for v in path:
                self.graph[u][v] -= cap
                self.graph[v][u] += cap
                u = v
            path = self.bfs()
        return max_flow

def solution(entrances, exits, path):
    """
    Using Ford-Fulkerson algorithm, returns maximum flow from
    source (entrance) to egress (exits) in given graph.
    """
    escape_pods = EscapePods(entrances, exits, path)
    res = escape_pods.solve()
    return res
================================================================================
================================================================================
def solution(entrances, exits, path):
    """
    """
    # entrances = [0, 1]
    # exits = [4, 5]
    # path = [
      # [0, 0, 4, 6, 0, 0],  # Room 0: Bunnies
      # [0, 0, 5, 2, 0, 0],  # Room 1: Bunnies
      # [0, 0, 0, 0, 4, 4],  # Room 2: Intermediate room
      # [0, 0, 0, 0, 6, 6],  # Room 3: Intermediate room
      # [0, 0, 0, 0, 0, 0],  # Room 4: Escape pods
      # [0, 0, 0, 0, 0, 0],  # Room 5: Escape pods
    # ]

    # Then in each time step, the following might happen:
    # 0 sends 4/4 bunnies to 2 and 6/6 bunnies to 3
    # 1 sends 4/5 bunnies to 2 and 2/2 bunnies to 3
    # 2 sends 4/4 bunnies to 4 and 4/4 bunnies to 5
    # 3 sends 4/6 bunnies to 4 and 4/6 bunnies to 5
================================================================================
================================================================================

Max Flow (Ford-Fulkerson)
Ford-Fulkerson Algorithm
The following is simple idea of Ford-Fulkerson algorithm:
1) Start with initial flow as 0.
2) While there is a augmenting path from source to sink.
           Add this path-flow to flow.
3) Return flow.

[ Residual Graph ]
Residual Graph of a flow network is:
    ----- A GRAPH indicating additional possible flow.
- If there is a path from source to sink in residual graph:
        - then it is possible to add flow.
- Every edge of a residual graph has a value (residual capacity)
        - Equal to (original capacity of the edge) minus (current flow).
        - Residual Capacity is essentially:
            - Current capacity of the edge.
[ Implementation details ]
- Residual capacity is 0 if there is no edge b/t 2 vertices of residual graph.
- We can initialize the residual graph as original graph.
        - There is no initial flow
        - Initially residual capacity is equal to original capacity.
- To find an augmenting path we can implement (of the residual graph)
        - BFS
        - DFS
- Using BFS, we can find out if there is a path from source to sink.
        - BFS also builds parent[] array.
- Using the parent[] array, we traverse through the found path
        - Locate possible flow via specified path
            - Find minimum residual capacity along the path.
        - We later add the found path flow to overall flow.
- We need to update residual capacities in the residual graph.
        - Subtract path flow from all edges along the path
        - Add path flow along the reverse edges
            - Significant, because later need to send flow in reverse direction
================================================================================
================================================================================
