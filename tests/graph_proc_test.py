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

class GraphTest(unittest.TestCase):
    def setUp(self) -> None:     
        mtx_path = './tests/graph1.mtx'
        self.graph_proc = graph_proc.Graph(mtx_path)

    def test_calculate_distances(self):
        self.graph_proc.calculate_distances(1)
        self.graph_proc.calculate_distances(6)
        self.assertEqual(list(self.graph_proc.distance_map[1]), [0, 1, 2, 1, 1, 2, 2, 2, 3, 2])
        self.assertEqual(list(self.graph_proc.distance_map[6]), [2, 1, 2, 3, 3, 0, 2, 3, 1, 2])