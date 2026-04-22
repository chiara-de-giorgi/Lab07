from collections import defaultdict

import flet as ft

from UI.view import View
from model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        # other attributes
        self._mese = 0

    def handle_umidita_media(self, e):
        self._view.lst_result.controls.clear()

        mese_selezionato=self._view.dd_mese.value

        situazioni=self._model.getAllSituazioni()

        if not mese_selezionato:
            self._view.create_alert("Selezionare un mese")
            self._view.update_page()
            return

        media=defaultdict(list)  #Un tipo di dizionario che non solleva mai errore KeyError (perchè la chiave viene sempre creata)
                                 #Dizionario chiave:località --> valore: lista dei valori delle umidità


        for s in situazioni:
            if int(mese_selezionato) == s.data.month:
                media[s.localita].append(s.umidita)
                # if s.localita not in media:
                #     somma[s.localita]=0
                # somma[s.localita]+=s.umidita



        self._view.lst_result.controls.append(ft.Text("L' umidità media nel mese selezionato è: "))

        for localita, valori in media.items():
            media=sum(valori)/len(valori)
            self._view.lst_result.controls.append(ft.Text(f"{localita}: {media:.4f}"))

        self._view.update_page()
        return






    def handle_sequenza(self, e):
        pass

    def read_mese(self, e):
        self._mese = int(e.control.value)

