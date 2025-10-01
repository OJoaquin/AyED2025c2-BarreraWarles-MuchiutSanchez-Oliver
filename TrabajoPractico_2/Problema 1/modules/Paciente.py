# -*- coding: utf-8 -*-

from random import randint, choices

nombres = ['Leandro', 'Mariela', 'Gastón', 'Andrea', 'Antonio', 'Estela', 'Jorge', 'Agustina']
apellidos = ['Perez', 'Colman', 'Rodriguez', 'Juarez', 'García', 'Belgrano', 'Mendez', 'Lopez']

niveles_de_riesgo = [1, 2, 3]
descripciones_de_riesgo = ['crítico', 'moderado', 'bajo']
# probabilidades de aparición de cada tipo de paciente
probabilidades = [0.1, 0.3, 0.6] 

class Paciente:
    orden_de_llegada = 0
    def __init__(self):
        n = len(nombres)
        self.__nombre = nombres[randint(0, n-1)]
        self.__apellido = apellidos[randint(0, n-1)]
        self.__riesgo = choices(niveles_de_riesgo, probabilidades)[0]
        self.__descripcion = descripciones_de_riesgo[self.__riesgo-1]
        Paciente.orden_de_llegada +=1
        self.Numero_de_llegada = Paciente.orden_de_llegada

    def get_nombre(self):
        return self.__nombre
    
    def get_apellido(self):
        return self.__apellido
    
    def get_riesgo(self):
        return self.__riesgo
    
    def get_descripcion_riesgo(self):
        return self.__descripcion
    
    def __str__(self):
        cad = self.__nombre + ' '
        cad += self.__apellido + '\t -> '
        cad += str(self.__riesgo) + '-' + self.__descripcion
        cad += '\t (Nro. de llegada: ' + str(self.Numero_de_llegada) + ')'
        return cad
    def __lt__(self,other):
        if self.get_riesgo() < other.get_riesgo():
            return True
        
        elif self.get_riesgo() == other.get_riesgo():

            if self.Numero_de_llegada < other.Numero_de_llegada:
                return True
            else:
                return False
        else:
            return False
        
if __name__ == '__main__':
    paciente1 = Paciente()
    paciente2 = Paciente() 
    paciente3 = Paciente()
    
    print(paciente1)
    print(paciente2)
    print(paciente3)
    if paciente1 < paciente2:
        print("El paciente 1 tiene mayor prioridad")
    else:
        print("El paciente 2 tiene mayor prioridad")
        