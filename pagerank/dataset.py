import pandas as pd
import numpy as np
from .models.pagerank import Node
import os

path = os.path.dirname(os.path.abspath(__file__))

df = pd.read_csv(path + '/data/data.csv')
df = df.dropna()
df = df.reset_index(drop=True)

df = df[['initial_url', 'final_url']]

urls = list(set(df['initial_url'].tolist() + df['final_url'].tolist()))

## Build a dictionary of nodes

nodes = []

for i, url in enumerate(urls):
    node: Node = {
        'id': i,
        'name': url,
        'links': [],
        'pagerank': 0
    }

    nodes.append(node)

for node in nodes:
    for node_n in nodes:
        if node_n['name'] in df[df['initial_url'] == node['name']]['final_url'].tolist():
            node['links'].append(node_n['id'])