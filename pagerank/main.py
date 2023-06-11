from .models.pagerank import Pagerank
from .dataset import nodes

def main():
    pagerank = Pagerank(nodes)
    print("Pagerank created")
    final_pagerank = pagerank.calculate()

    for i in range(len(nodes)):
        print(f"{nodes[i]['name']}: {final_pagerank[i]}")
