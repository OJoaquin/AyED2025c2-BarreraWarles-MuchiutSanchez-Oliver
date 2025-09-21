def OrdenamientoRapido(unaLista):
   OrdenamientoRapidoAuxiliar(unaLista,0,len(unaLista)-1)
   return unaLista

def OrdenamientoRapidoAuxiliar(unaLista,primero,ultimo):
   if primero<ultimo:

       puntoDivision = Particion(unaLista,primero,ultimo)

       OrdenamientoRapidoAuxiliar(unaLista,primero,puntoDivision-1)
       OrdenamientoRapidoAuxiliar(unaLista,puntoDivision+1,ultimo)


def Particion(unaLista,primero,ultimo):
   valorPivote = unaLista[primero]

   marcaIzq = primero+1
   marcaDer = ultimo

   hecho = False
   while not hecho:

       while marcaIzq <= marcaDer and unaLista[marcaIzq] <= valorPivote:
           marcaIzq = marcaIzq + 1

       while unaLista[marcaDer] >= valorPivote and marcaDer >= marcaIzq:
           marcaDer = marcaDer -1

       if marcaDer < marcaIzq:
           hecho = True
       else:
           temp = unaLista[marcaIzq]
           unaLista[marcaIzq] = unaLista[marcaDer]
           unaLista[marcaDer] = temp

   temp = unaLista[primero]
   unaLista[primero] = unaLista[marcaDer]
   unaLista[marcaDer] = temp


   return marcaDer

unaLista = [54,26,93,17,77,31,44,55,20]
OrdenamientoRapido(unaLista)
print(unaLista)