# Python program to find strongly connected components in a given
# directed graph using Tarjan's algorithm (single DFS)
# Complexity : O(V+E)

from collections import defaultdict
import networkx as nx
import timeit
import matplotlib.pyplot as plt
import math
import random


# This class represents an directed graph
# using adjacency list representation
def show_figure(data):
    plt.figure(figsize=(9,9))
    plt.title('Dependence of the running time on the number of vertices')
    plt.xlabel('Number of vertices')
    plt.ylabel('Running time')
    plt.grid()

    x = []
    y = []
    for exp in data:
        x.append(exp['size'])
        y.append(exp['time'])

    plt.plot(x, y)
    plt.show()


# S = 512
class Graph:

    def __init__(self, vertices):
        # No. of vertices
        self.V = vertices
        self.Time = 0
        self.G = nx.gnp_random_graph(self.V, 1.5/self.V, seed = 15, directed=True)
        self.graph = nx.to_dict_of_lists(self.G)
        self.Nod = nx.number_of_nodes(self.G)
        self.Edg = nx.number_of_edges(self.G)
        self.Sum = self.Nod + self.Edg

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    '''A recursive function that find finds and prints strongly connected
    components using DFS traversal
    u --> The vertex to be visited next
    disc[] --> Stores discovery times of visited vertices
    low[] -- >> earliest visited vertex (the vertex with minimum
                discovery time) that can be reached from subtree
                rooted with current vertex
     st -- >> To store all the connected ancestors (could be part
           of SCC)
     stackMember[] --> bit/index array for faster check whether
                  a node is in stack
    '''

    def SCCUtil(self, u, low, disc, stackMember, st):

        # Initialize discovery time and low value
        disc[u] = self.Time
        low[u] = self.Time
        self.Time += 1
        stackMember[u] = True
        st.append(u)

        # Go through all vertices adjacent to this
        for v in self.graph[u]:

            # If v is not visited yet, then recur for it
            if disc[v] == -1:

                self.SCCUtil(v, low, disc, stackMember, st)

                # Check if the subtree rooted with v has a connection to
                # one of the ancestors of u
                # Case 1 (per above discussion on Disc and Low value)
                low[u] = min(low[u], low[v])

            elif stackMember[v] == True:

                '''Update low value of 'u' only if 'v' is still in stack
                (i.e. it's a back edge, not cross edge).
                Case 2 (per above discussion on Disc and Low value) '''
                low[u] = min(low[u], disc[v])

        # head node found, pop the stack and print an SCC
        w = -1  # To store stack extracted vertices
        if low[u] == disc[u]:
            while w != u:
                w = st.pop()
                # print(w, end=' ')
                stackMember[w] = False

            # print("")

    # The function to do DFS traversal.
    # It uses recursive SCCUtil()
    def SCC(self):

        # Mark all the vertices as not visited
        # and Initialize parent and visited,
        # and ap(articulation point) arrays
        disc = [-1] * (self.V)
        low = [-1] * (self.V)
        stackMember = [False] * (self.V)
        st = []

        # Call the recursive helper function
        # to find articulation points
        # in DFS tree rooted with vertex 'i'
        for i in range(self.V):
            if disc[i] == -1:
                self.SCCUtil(i, low, disc, stackMember, st)




def testtime(n):
    sizes = [100 * n + 100 * i * n for i in range(20)]
    i = 0
    tests = []


    for size in sizes:
         time = 0
         G = Graph(size)
         print("Nodes")
         print(G.Nod)
         print("Edges")
         print(G.Edg)
         print(G.Sum)
         tests.append({'size': sizes[i]})
         for j in range(10):
             start = timeit.default_timer()
             G.SCC()
             stop = timeit.default_timer()
             time += stop - start
         tests[i]['time'] = time / 10
         i += 1
    return tests

T = testtime(1)
show_figure(T)
T = testtime(2)


