#
# Copyright (c) 2020. Asutosh Nayak (nayak.asutosh@ymail.com)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#


from queue import PriorityQueue
from scipy import io
import numpy as np
import os
from tqdm.autonotebook import tqdm
from logger import Logger
import pickle
import time
import datetime


class Node:
    """
    not used
    """

    def __init__(self, node_id, node_distance_from_source):
        self.node_id = node_id
        self.distance = node_distance_from_source

    def set_distance(self, distance):
        self.distance = distance

    def get_distance(self):
        return self.distance


class Graph:
    def __init__(self, mtx_file_path, logger: Logger):
        self.graph_sparse = io.mmread(
            mtx_file_path).tocsr()  # scipy sparse csr matrix
        self.distance_map = {}
        self.logger = logger

    def init_node_distance(self, source):
        # self.pq_nodes = PriorityQueue()
        self.distances = np.array([np.inf] * self.graph_sparse.shape[0])
        self.distances[source] = 0
        self.visited = np.zeros((self.graph_sparse.shape[0],), dtype=bool)
        # [False] * self.graph_sparse.shape[0]
        # for id, dist in enumerate(self.distances):
        #     # inserting a tuple will sort the PriorityQueue
        #     # based on first element of each tuple
        #     self.pq_nodes.put((dist, id))

    def min_distance_node(self):
        min = np.inf
        node = -1
        for id, dist in enumerate(self.distances):
            if not self.visited[id] and dist < min:
                min = dist
                node = id
        return node

    def calculate_distances(self, source):
        source = source - 1
        self.init_node_distance(source)
        count = 0
        with tqdm(total=len(self.visited)) as pbar:
            while not self.visited.all():
                node_id = self.min_distance_node()  # self.pq_nodes.get()
                if node_id == -1:
                    self.logger.append_log(
                        'No connecte node found: unvisited count' + str(np.sum(self.visited == False)))
                    break
                self.visited[node_id] = True
                self.logger.append_log(
                    'current node:' + str(node_id) + 'dist=' + str(self.distances[node_id]))
                # returns indices on column axis for node_id row
                neighbour_nodes = self.graph_sparse[node_id].nonzero()[1]
                self.logger.append_log('neighbor nodes:' +
                                    str(list(neighbour_nodes)))
                for neighbour in neighbour_nodes:
                    if not self.visited[neighbour] and \
                            self.graph_sparse[node_id, neighbour] + self.distances[node_id] < self.distances[neighbour]:
                        self.distances[neighbour] = self.graph_sparse[node_id,
                                                                    neighbour] + self.distances[node_id]
                        self.logger.append_log(
                            'distance updated for node-{}'.format(str(neighbour)))
                pbar.update(1)
                count = count + 1
                self.logger.append_log(
                    'visited nodes:' + str(np.sum(self.visited)))
            self.distance_map[source + 1] = self.distances
            # print('Shortest path from node-{} to all nodes is {}'.format(source, self.distances))
            pickle.dump(self.distance_map, open(
                '../outputs/distance_map_' + str(time.time()) + '.pickle', 'wb'))
            self.logger.flush()
