from queue import PriorityQueue
from scipy import io
import numpy as np


class Node:
    def __init__(self, node_id, node_distance_from_source):
        self.node_id = node_id
        self.distance = node_distance_from_source

    def set_distance(self, distance):
        self.distance = distance

    def get_distance(self):
        return self.distance


class Graph:
    def __init__(self, mtx_file_path):
        self.graph_sparse = io.mmread(mtx_file_path).tocsr()  # scipy sparse csr matrix
        self.distance_map = {}

    def init_node_distance(self, source):
        # self.pq_nodes = PriorityQueue()
        self.distances = np.array([np.inf] * self.graph_sparse.shape[0])
        self.distances[source] = 0
        self.visited = [False] * self.graph_sparse.shape[0]
        # for id, dist in enumerate(self.distances):
        #     # inserting a tuple will sort the PriorityQueue 
        #     # based on first element of each tuple
        #     self.pq_nodes.put((dist, id))

    def calculate_distances(self, source):
        source = source - 1
        self.init_node_distance(source)
        while not all(self.visited):
            node_id = np.argmin(self.distances)  # self.pq_nodes.get()
            self.visited[node_id] = True
            neighbour_nodes = self.graph_sparse[node_id].nonzero()[1]  # returns indices on column axis for node_id row
            # neighbour_distances = self.graph_sparse[node_id, neighbour_nodes].toarray()[0]  # get the node_id's current distances to neighbours
            for neighbour in neighbour_nodes:
                if not self.visited[neighbour] and \
                    self.graph_sparse[node_id, neighbour] + self.distances[node_id] < self.distances[neighbour]:
                    self.distances[neighbour] = self.graph_sparse[node_id, neighbour] + self.distances[node_id] 
        self.distance_map[source] = self.distances
        print('Shortest path from node-{} to all nodes is {}'.format(source, self.distances))
