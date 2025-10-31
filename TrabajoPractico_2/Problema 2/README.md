# Temperaturas

En este este script, disponemos de un archivo de temperaturas diarias, debemos implementar modulos para poder trabajar con el archivo mediante funciones.
---
## 🏗Arquitectura General

Disponemos de 2 modulos principales, AVL para poder crear el arbol, y el modulo de Temperaturas_DB, en la que implementaremos las siguientes funciones:
- guardar_temperatura(temperatura, fecha)
- devolver_temperatura(fecha)
- max_temp_rango(fecha1, fecha2)
- min_temp_rango(fecha1, fecha2)
- temp_extremos_rango(fecha1, fecha2)
- borrar_temperatura(fecha)
- devolver_temperaturas(fecha1, fecha2)
- cantidad_muestras()

Las gráficas de los resultados están disponible en la carpeta [data](./data) del proyecto.

El informe completo está disponible en la carpeta [docs](./docs) del proyecto.

---
## 📑Dependencias

1. **Python 3.x**
2. **matplotlib** (`pip install matplotlib`)
3. listar dependencias principales
4. Dependencias listadas en requierements.txt

---
## 🚀Cómo Ejecutar el Proyecto
1. **Clonar o descargar** el repositorio.

2. **Crear y activar** un entorno virtual.

3. **Instalar las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```
   El archivo `requirements.txt` se encuentran en la carpeta [deps](./deps) del proyecto.

---
## 🙎‍♀️🙎‍♂️Autores

- Muchiut Sanchez Martiniano
- Oliver Joaquin
- Barrera Warles Tobias

---

> **Consejo**: Mantén el README **actualizado** conforme evoluciona el proyecto, y elimina (o añade) secciones según necesites. Esta plantilla es sólo un punto de partida general.
