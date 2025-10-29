Muestras = []
from modules.Temperaturas_DB import Temperaturas_DB
Base_De_Datos_Temperaturas = Temperaturas_DB()


# with open (r"C:\Marti\facu\Algoritmo\AyED2025c2-BarreraWarles-MuchiutSanchez-Oliver\TrabajoPractico_2\Problema 2\data\muestras.txt", 'r') as file:
#     lineas = file.readlines()
#     for linea in lineas:
#         [fecha, temperatura] = linea.strip().split(';')
#         Base_De_Datos_Temperaturas.guardar_temperatura(float(temperatura), fecha)
        #Muestras.append([fecha, float(temperatura)])
        #print(Muestras)
ruta = "./data/muestras.txt"
Base_De_Datos_Temperaturas.cargar_datos(ruta)
if __name__ == "__main__":
        print(Base_De_Datos_Temperaturas.transformar_fecha("2023-10-05"))
        print(Base_De_Datos_Temperaturas.max_temp_rango("2025/1/01", "2025/10/31"))
        print(Base_De_Datos_Temperaturas.min_temp_rango("2025/1/01", "2025/10/31"))
        print(Base_De_Datos_Temperaturas.temp_extremos_rango("2025/1/01", "2025/10/31"))
        print(Base_De_Datos_Temperaturas.devolver_temperaturas("2025/1/01", "2025/10/31"))
        print(Base_De_Datos_Temperaturas.cantidad_muestras())