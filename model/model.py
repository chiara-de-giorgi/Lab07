from database.meteo_dao import MeteoDao


class Model:
    def __init__(self):
        pass

    def getAllSituazioni(self):
        return MeteoDao.get_all_situazioni()



    # def getAllMesi(self, e):
    #     return MeteoDao.getAllMesi()
    #
    # def getAllLocalità(self, e):
    #     return MeteoDao.getAllLocalità()