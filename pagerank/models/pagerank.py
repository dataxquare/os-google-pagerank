import numpy as np
import math
from pydantic import BaseModel
from typing import List

class Node(BaseModel):
    id: int
    name: str
    links: List[int]  # list of ids of nodes who link to this node
    pagerank: float

class Pagerank:
    def __init__(self, graph: List[Node], alpha: int = 0.85, epsilon: int = 1.0e-8):
        self.graph = graph
        self.graph_len = len(self.graph)
        self.matrix = [[0]*self.graph_len]*self.graph_len
        self.alpha = alpha
        self.epsilon = epsilon
        self.google_matrix = None

    def build_matrix(self):
        n = len(self.graph)
        self.matrix = [[0]*n]*n

        for node in self.graph:
            for link in node['links']:
                self.matrix[link][node['id']] = 1

        return self.matrix

    def normalize_matrix(self):
        for i in range(self.graph_len):
            for j in range(self.graph_len):
                self.matrix[i][j] = self.matrix[i][j] / sum(self.matrix[i])

        return self.matrix

    def damping_matrix(self):
        normalized_matrix = self.normalize_matrix()

        q = [[1/self.graph_len]*self.graph_len]*self.graph_len
        a = np.array(self.matrix)
        q = np.array(q)
        self.google_matrix = np.add(
            (self.alpha)*a, (1-self.alpha) * q)  # create damping matrix

        return self.google_matrix

    def calculate(self, max_iterations: int = 100):
        self.build_matrix()
        self.damping_matrix()
        i = 0

        while i < max_iterations:
            pagerank = np.array([1/self.graph_len]*self.graph_len)
            new_pagerank = np.dot(pagerank, self.google_matrix)

            if np.sum(np.abs(new_pagerank - pagerank)) < self.epsilon:
                break

            i += 1
            pagerank = new_pagerank

        return new_pagerank
