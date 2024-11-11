from database.DAO import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._nodes = []
        self._grafo = nx.Graph()
        pass

    def get_anni(self):
        return DAO.ge_all_years()

    def get_stati(self, y):
        return DAO.ge_all_states(y)





    def buildGraph(self, a,c ):
        self._grafo.clear()
        self._nodes = DAO.get_all_nodes(a, c)
        self._grafo.add_nodes_from(DAO.get_all_nodes(a,c))

        for i in range(0, len(self._nodes) - 1):
            for j in range(i + 1, len(self._nodes)):
                if self._nodes[i].shape == self._nodes[j].shape and self._nodes[i].distance_HV(self._nodes[j]) < 100:
                    self._grafo.add_edge(self._nodes[i], self._nodes[j])

    def get_num_connesse(self):
        return nx.number_connected_components(self._grafo)

    def get_connessaMAX(self):
        conn = list(nx.connected_components(self._grafo))
        conn.sort(key=lambda x: len(x), reverse=True)
        return conn[0]

    # def getGraphDetails(self):
    #     return len(self.graph.nodes), len(self.graph.edges)

    def get_num_of_nodes(self):
        return self._grafo.number_of_nodes()

    def get_num_of_edges(self):
        return self._grafo.number_of_edges()



