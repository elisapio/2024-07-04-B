import flet as ft
from UI.view import View
from model.modello import Model


class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillDD(self):
        year = self._model.get_anni()

        for y in year:
            self._view.ddyear.options.append(ft.dropdown.Option(y))
        self._view.update_page()

    def fillDD2(self,e):
        anno = int(self._view.ddyear.value)
        stato = self._model.get_stati(anno)
        for s in stato:
            self._view.ddstate.options.append(ft.dropdown.Option(key=s.id, text=s.name))
        self._view.update_page()

    def handle_graph(self, e):
        a = self._view.ddyear.value
        c = self._view.ddstate.value

        if a is None:
            self._view.create_alert("Inserire l'anno")
            return

        if c is None:
            self._view.create_alert("Inserire la nazione")
            return

        self._view.txt_result1.controls.clear()
        self._model.buildGraph(a, c)

        self._view.txt_result1.controls.append(ft.Text(
            f"Numero di nodi: {self._model.get_num_of_nodes()} Numero di archi: {self._model.get_num_of_edges()}"))

        self._view.txt_result1.controls.append(
             ft.Text(f"Il grafo ha: {self._model.get_num_connesse()} componenti connesse"))
        connessa = self._model.get_connessaMAX()
        self._view.txt_result1.controls.append(ft.Text(f"La componente connessa più grande "
                                                        f"è costituita da {len(connessa)} nodi:"))

        for c in connessa:
            self._view.txt_result1.controls.append(ft.Text(c))

        self._view.btn_path.disabled = False
        self._view.update_page()

    def handle_path(self, e):
        pass

