from modules.AVL import AVL
class Temperaturas_DB:
    def __init__(self):
        self.Base_De_Datos_Temperaturas = AVL()
        pass
    def guardar_temperatura(self, temperatura, fecha):
        self.Base_De_Datos_Temperaturas.agregar(temperatura, fecha)
        pass
    def devolver_temperatura(self, fecha):
        self.Base_De_Datos_Temperaturas.obtener(fecha)
        pass
    def max_temp_rango(self, fecha_inicio, fecha_fin):
        pass