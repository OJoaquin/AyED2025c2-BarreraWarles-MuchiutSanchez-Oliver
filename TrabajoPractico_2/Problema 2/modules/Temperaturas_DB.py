from modules.AVL import AVL
from datetime import datetime, date, timedelta
#from Main import Base_De_Datos_Temperaturas
class Temperaturas_DB:
    def __init__(self):
        self.__arbol = AVL()
    def transformar_fecha(self, fecha):
                  # Acepta datetime, date o string en varios formatos, incluido año de 2 dígitos 'aa/mm/dd'
        if fecha is None:
            return None
        if isinstance(fecha, datetime):
            return fecha
        if isinstance(fecha, date):
            return datetime(fecha.year, fecha.month, fecha.day)
        if isinstance(fecha, str):
            s = fecha.strip()
            # intentar formatos seguros y comunes (añadir los que necesites)
            if not s:
                raise ValueError("Fecha vacía")
            # intento ISO primero
            try:
                return datetime.fromisoformat(s)
            except Exception:
                pass
            formatos = (
                "%Y-%m-%d", "%Y/%m/%d",    # año 4 dígitos
                "%y/%m/%d",               # año 2 dígitos (aa/mm/dd)
                "%d/%m/%Y", "%d/%m/%y",   # día/mes/año con 4 o 2 dígitos
            )
            for fmt in formatos:
                try:
                    return datetime.strptime(s, fmt)
                except Exception:
                    continue
            raise ValueError(f"Formato de fecha no soportado: '{fecha}'")
        raise ValueError("Tipo de fecha no soportado")
    def guardar_temperatura(self, temperatura, fecha):
        clave = self.transformar_fecha(fecha)
        self.__arbol.agregar(clave, float(temperatura))
        pass
    
    def devolver_temperatura(self, fecha):
        clave = self.transformar_fecha(fecha)
        return self.__arbol.obtener(clave)
    
    def max_temp_rango(self, fecha_inicio, fecha_fin):
        max_temp = -1000.0
        fecha = self.transformar_fecha(fecha_inicio)
        while fecha <= self.transformar_fecha(fecha_fin):
            temperatura = self.devolver_temperatura(fecha)
            if temperatura is None:
                fecha += timedelta(days=1)
                continue
            if temperatura > max_temp:
                max_temp = self.devolver_temperatura(fecha)
            fecha += timedelta(days=1)
        return max_temp

    def min_temp_rango(self, fecha_inicio, fecha_fin):
        min_temp = 1000.0
        fecha = self.transformar_fecha(fecha_inicio)
        while fecha <= self.transformar_fecha(fecha_fin):
            temperatura = self.devolver_temperatura(fecha)
            if temperatura is None:
                fecha += timedelta(days=1)
                continue
            if temperatura < min_temp:
                min_temp = self.devolver_temperatura(fecha)
            fecha += timedelta(days=1)
        return min_temp
    def temp_extremos_rango(self, fecha_inicio, fecha_fin):
        minimo = self.max_temp_rango(fecha_inicio, fecha_fin)
        maximo = self.min_temp_rango(fecha_inicio, fecha_fin)
        return (minimo, maximo)
    
    def borrar_temperatura(self, fecha):
        self.__arbol.eliminar(fecha)
        pass
    
    def devolver_temperaturas(self, fecha_inicio, fecha_fin):
        fecha = self.transformar_fecha(fecha_inicio)
        temperaturas = []
        while fecha <= self.transformar_fecha(fecha_fin):
            temperatura = self.devolver_temperatura(fecha)
            if temperatura is not None:
                dd , mm, yyyy = fecha.day, fecha.month, fecha.year
                temperaturas.append(f"{dd}/{mm}/{yyyy}: {temperatura}ºC")
            fecha += timedelta(days=1)
        #temperaturas.sorted(reverse=False, key=lambda x: x[0])
        return temperaturas
    def cantidad_muestras(self):
        return self.__arbol.__len__()
    
    def cargar_datos(self, nombre_archivo):
        with open (nombre_archivo, 'r') as file:
            lineas = file.readlines()
            for linea in lineas:
                fecha,temperatura = linea.strip().split(';')
                self.guardar_temperatura(temperatura, fecha)
        pass

