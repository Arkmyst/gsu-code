class DirectedGraph:
    def __init__(self):
        # A dictionary to store nodes by label
        self.nodes = {}

        # A dictionary to store adjacency list (node -> list of nodes)
        self.adjacency_list = {}

        self.time = 0

    class Node:
        def __init__(self, label):
            self.label = label

        def __str__(self):
            return self.label

    def add_node(self, label):
        node = self.Node(label)

        if label not in self.nodes:
            self.nodes[label] = node
            self.adjacency_list[node] = []

    def remove_node(self, label):
        node_to_remove = self.nodes.get(label)
        if node_to_remove is None:
            return
        for node in self.adjacency_list:
            if node_to_remove in self.adjacency_list[node]:
                self.adjacency_list[node].remove(node_to_remove)

        self.adjacency_list.pop(node_to_remove, None)
        self.nodes.pop(label, None)

    def add_edge(self, one, two):
        node_one = self.nodes.get(one)
        node_two = self.nodes.get(two)

        if node_one is None or node_two is None:
            raise ValueError("No such node exists!")

        self.adjacency_list[node_one].append(node_two)

    def remove_edge(self, one, two):
        node_one = self.nodes.get(one)
        node_two = self.nodes.get(two)

        if node_one is None or node_two is None:
            return

        self.adjacency_list[node_one].remove(node_two)

    def are_adjacent(self, one, two):
        node_one = self.nodes.get(one)
        node_two = self.nodes.get(two)

        if node_one is None or node_two is None:
            return False

        return node_two in self.adjacency_list[node_one]

    def dfs_rec(self, start_label, visited):
        # Get the starting node
        start_node = self.nodes.get(start_label)
        visited.add(start_node)
        self.time += 1

        # Recur for all adjacent nodes
        for neighbor in self.adjacency_list[start_node]:
            if neighbor not in visited:
                self.dfs_rec(neighbor.label, visited)
        self.time += 1
        finish_times[start_label] = self.time


# Driver code

# Construct the graph
graph = DirectedGraph()

for label in ["0", "1", "2", "3", "4"]:
    graph.add_node(label)

graph.add_edge("0", "2")
graph.add_edge("1", "2")
graph.add_edge("2", "3")
graph.add_edge("2", "4")

# Compute finish times
finish_times = {}
visited_global = set()
for node in graph.nodes.values():
    if node not in visited_global:
        graph.dfs_rec(node.label, visited_global)

print("Nodes and their finish times:")
print(finish_times)

# Topological sorting based on finished time
sorted_finish_times = dict(sorted(finish_times.items(), key=lambda item: item[1], reverse=True))
print("Nodes sorted by finish times\n", sorted_finish_times)
print("Topological order: ", list(sorted_finish_times.keys()))
