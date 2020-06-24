#
# Copyright (c) 2020. Asutosh Nayak (nayak.asutosh@ymail.com)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#

import sys
from scipy import io
sys.path.append('../src')
import unittest
import src.graph_proc as graph_proc
from src.logger import Logger
import networkx as nx

class GraphTest(unittest.TestCase):

    def setUp(self) -> None:     
        logger = Logger('../outputs/logs', 'test_log')
        self.test_graph = nx.read_edgelist('./tests/graph1.edgelist')
        self.graph_proc = graph_proc.Graph(None, logger, self.test_graph)

    def test_calculate_distances(self):
        sources = [1, 56, 23]
        for source in sources:
            self.graph_proc.calculate_distances_naive(source)
            distances = self.graph_proc.distance_map[source]
            nx_distances = list(nx.shortest_path_length(self.test_graph, source).values())
            print(distances[0:10], nx_distances[0:10])
            self.assertListEqual(distances.tolist(), nx_distances)