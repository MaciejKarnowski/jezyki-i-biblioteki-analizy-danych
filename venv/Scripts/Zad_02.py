class Graph:
    visited = set()

    def __init__(self, children=None):
        self.children = children
        self.graf = {}

    def add_vertex(self, vertex):
        self.graf[vertex] = []

    def remove_vertex(self, vertex):
        if vertex in self.graf:
            self.graf.pop(vertex)
            for vertex1 in self.graf:
                for edge in self.graf[vertex1]:
                    if vertex in edge:
                        self.graf[vertex1].remove(edge)

    def add_edge(self, vertex, vertex1):
        if vertex in self.graf and vertex1 in self.graf and vertex1 not in self.graf[vertex]:
            self.graf[vertex].append(vertex1)

    def remove_edge(self, vertex, vertex1):
        if vertex in self.graf and vertex1 in self.graf and vertex1 in self.graf[vertex]:
            self.graf[vertex].remove(vertex1)

    def pick_edges(self, vertex):
        output = []
        for vertex_1 in self.graf:
            if vertex in self.graf[vertex_1]:
                output.append(vertex_1)
        return set(output)

    def bfs(self, root):
        visited = {}
        for i in self.graf:
            visited[i] = False
        queue = []
        queue.append(root)
        visited[root] = True

        while queue:
            s = queue.pop(0)
            print(s)

            for i in self.graf[s]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True

    def dfs(self, root):
        visited = {}
        for i in self.graf:
            visited[i] = False

        stack = []

        stack.append(root)

        while len(stack):
            root = stack[-1]
            stack.pop()

            if not visited[root]:
                print(root)
                visited[root] = True

            for node in self.graf[root]:
                if not visited[node]:
                    stack.append(node)


x = Graph()
x.add_vertex(1)
x.add_vertex(2)
x.add_vertex(3)
x.add_edge(1, 2)
x.add_edge(1, 3)
x.add_edge(3, 1)
x.add_edge(3, 2)
x.add_edge(2, 1)
y = x.pick_edges(1)
x.bfs(1)
x.dfs(1)
