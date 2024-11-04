#1 Implement the Graph Class
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)  

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    def add_edge(self, vertex1, vertex2, weight=1):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        self.graph[vertex1].append((vertex2, weight))
        self.graph[vertex2].append((vertex1, weight)) 
    
    def print_graph(self):
        for vertex, edges in self.graph.items():
            print(f"{vertex}: {', '.join(f'({neighbor}, {weight})' for neighbor, weight in edges)}")

g = Graph()
g.add_edge(0, 1, 1)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 2)
g.add_edge(1, 3, 5)
g.add_edge(2, 3, 1)
g.print_graph()

#2 Implement BFS to Find the Shortest Path
from collections import deque

class Graph:
    
    def __init__(self):
        self.graph = defaultdict(list)  

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    def add_edge(self, vertex1, vertex2, weight=1):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        self.graph[vertex1].append((vertex2, weight))
        self.graph[vertex2].append((vertex1, weight)) 
    
    def print_graph(self):
        for vertex, edges in self.graph.items():
            print(f"{vertex}: {', '.join(f'({neighbor}, {weight})' for neighbor, weight in edges)}")

    def bfs_shortest_path(self, start, goal):
        visited = set()
        queue = deque([(start, [start])]) 
        while queue:
            vertex, path = queue.popleft()
            if vertex == goal:
                return path
            if vertex not in visited:
                visited.add(vertex)
                for neighbor, _ in self.graph[vertex]:  
                    queue.append((neighbor, path + [neighbor]))
        return None  

g = Graph()
g.add_edge(0, 1, 1)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 2)
g.add_edge(1, 3, 5)
g.add_edge(2, 3, 1)
g.print_graph()
print("\nShortest path from 0 to 4:", g.bfs_shortest_path(0, 4))

#3Add Cycle Detection
class Graph:
    
    def __init__(self):
        self.graph = defaultdict(list)  

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    def add_edge(self, vertex1, vertex2, weight=1):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        self.graph[vertex1].append((vertex2, weight))
        self.graph[vertex2].append((vertex1, weight)) 
    
    def print_graph(self):
        for vertex, edges in self.graph.items():
            print(f"{vertex}: {', '.join(f'({neighbor}, {weight})' for neighbor, weight in edges)}")

    def bfs_shortest_path(self, start, goal):
        visited = set()
        queue = deque([(start, [start])]) 
        while queue:
            vertex, path = queue.popleft()
            if vertex == goal:
                return path
            if vertex not in visited:
                visited.add(vertex)
                for neighbor, _ in self.graph[vertex]:  
                    queue.append((neighbor, path + [neighbor]))
        return None  
    
    def has_cycle(self):
        visited = set()

        def dfs(vertex, parent):
            visited.add(vertex)
            for neighbor, _ in self.graph[vertex]:
                if neighbor not in visited:
                    if dfs(neighbor, vertex):
                        return True
                elif parent != neighbor:  # Found a back edge
                    return True
            return False

        for vertex in self.graph:
            if vertex not in visited:
                if dfs(vertex, None):
                    return True
        return False

g = Graph()
g.add_edge(0, 1, 1)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 2)
g.add_edge(1, 3, 5)
g.add_edge(2, 3, 1)
g.print_graph()
print("\nShortest path from 0 to 4:", g.bfs_shortest_path(0, 4))

#4 Implement Dijkstra's Algorithm
import heapq

class Graph:
    
    def __init__(self):
        self.graph = defaultdict(list)  

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    def add_edge(self, vertex1, vertex2, weight=1):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        self.graph[vertex1].append((vertex2, weight))
        self.graph[vertex2].append((vertex1, weight)) 
    
    def print_graph(self):
        for vertex, edges in self.graph.items():
            print(f"{vertex}: {', '.join(f'({neighbor}, {weight})' for neighbor, weight in edges)}")

    def bfs_shortest_path(self, start, goal):
        visited = set()
        queue = deque([(start, [start])]) 
        while queue:
            vertex, path = queue.popleft()
            if vertex == goal:
                return path
            if vertex not in visited:
                visited.add(vertex)
                for neighbor, _ in self.graph[vertex]:  
                    queue.append((neighbor, path + [neighbor]))
        return None  
    
    def has_cycle(self):
        visited = set()

        def dfs(vertex, parent):
            visited.add(vertex)
            for neighbor, _ in self.graph[vertex]:
                if neighbor not in visited:
                    if dfs(neighbor, vertex):
                        return True
                elif parent != neighbor:  # Found a back edge
                    return True
            return False

        for vertex in self.graph:
            if vertex not in visited:
                if dfs(vertex, None):
                    return True
        return False
    
    def dijkstra(self, start):
        distances = {vertex: float('infinity') for vertex in self.graph}
        distances[start] = 0
        priority_queue = [(0, start)]  # (distance, vertex)

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.graph[current_vertex]:
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances

g = Graph()
g.add_edge(0, 1, 1)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 2)
g.add_edge(1, 3, 5)
g.add_edge(2, 3, 1)
g.print_graph()
print("\nShortest path from 0 to 4:", g.bfs_shortest_path(0, 4))
print("Graph has cycle:", g.has_cycle())

#5 Check if the Graph is Bipartite

class Graph:
    
    def __init__(self):
        self.graph = defaultdict(list)  

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    def add_edge(self, vertex1, vertex2, weight=1):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        self.graph[vertex1].append((vertex2, weight))
        self.graph[vertex2].append((vertex1, weight)) 
    
    def print_graph(self):
        for vertex, edges in self.graph.items():
            print(f"{vertex}: {', '.join(f'({neighbor}, {weight})' for neighbor, weight in edges)}")

    def bfs_shortest_path(self, start, goal):
        visited = set()
        queue = deque([(start, [start])]) 
        while queue:
            vertex, path = queue.popleft()
            if vertex == goal:
                return path
            if vertex not in visited:
                visited.add(vertex)
                for neighbor, _ in self.graph[vertex]:  
                    queue.append((neighbor, path + [neighbor]))
        return None  
    
    def has_cycle(self):
        visited = set()

        def dfs(vertex, parent):
            visited.add(vertex)
            for neighbor, _ in self.graph[vertex]:
                if neighbor not in visited:
                    if dfs(neighbor, vertex):
                        return True
                elif parent != neighbor:  # Found a back edge
                    return True
            return False

        for vertex in self.graph:
            if vertex not in visited:
                if dfs(vertex, None):
                    return True
        return False
    
    def dijkstra(self, start):
        distances = {vertex: float('infinity') for vertex in self.graph}
        distances[start] = 0
        priority_queue = [(0, start)]  # (distance, vertex)

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.graph[current_vertex]:
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances
    
    def is_bipartite(self):
        color = {}

        def bfs(vertex):
            queue = deque([vertex])
            color[vertex] = 0  # Start coloring with 0

            while queue:
                current = queue.popleft()
                for neighbor in self.graph[current]:
                    if neighbor[0] not in color:
                        color[neighbor[0]] = 1 - color[current]
                        queue.append(neighbor[0])
                    elif color[neighbor[0]] == color[current]:  # Same color as current
                        return False
            return True

        for vertex in self.graph:
            if vertex not in color:
                if not bfs(vertex):
                    return False
        return True

g = Graph()
g.add_edge(0, 1, 1)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 2)
g.add_edge(1, 3, 5)
g.add_edge(2, 3, 1)
g.print_graph()
print("\nShortest path from 0 to 4:", g.bfs_shortest_path(0, 4))
print("Graph has cycle:", g.has_cycle())
print("Is the graph bipartite?", g.is_bipartite())