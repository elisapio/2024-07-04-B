from database.DAO import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._nodes = []
        self._grafo = nx.Graph()

        pass

    def get_anni(self):
        return DAO.get_all_years()

    def get_shape(self, year):
        return DAO.get_shapes_year(year)


    def buildGraph(self, a,s ):
        self._grafo.clear()
        self._nodes = DAO.get_all_nodes(a, s)
        self._grafo.add_nodes_from(DAO.get_all_nodes(a,s))

        for i in range(0, len(self._nodes) - 1):
            for j in range(i + 1, len(self._nodes)):
                if self._nodes[i].state == self._nodes[j].state and self._nodes[i].datetime < self._nodes[j].datetime:
                    weight = self._nodes[j].datetime - self._nodes[i].datetime
                    self._grafo.add_edge(self._nodes[i], self._nodes[j])
                elif self._nodes[i].state == self._nodes[j].state and self._nodes[i].datetime > self._nodes[j].datetime:
                    weight = self._nodes[i].datetime - self._nodes[j].datetime
                    self._grafo.add_edge(self._nodes[j], self._nodes[i])

    def get_num_connesse(self):
        return nx.number_connected_components(self._grafo)

    def get_connessaMAX(self):
        conn = list(nx.connected_components(self._grafo))
        conn.sort(key=lambda x: len(x), reverse=True)
        return conn[0]





    def get_num_of_nodes(self):
        return self._grafo.number_of_nodes()

    def get_num_of_edges(self):
        return self._grafo.number_of_edges()


