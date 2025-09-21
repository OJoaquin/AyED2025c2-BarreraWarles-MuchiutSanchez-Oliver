
def OrdenamientoBurbuja(Lista):
    for numero in range(len(Lista)-1,0,-1):
        for x in range(numero):
            if Lista[x]>Lista[x+1]:
                temporal = Lista[x]
                Lista[x] = Lista[x+1]
                Lista[x+1] = temporal
    return Lista

#Lista = [54,26,93,17,77,31,44,55,20]
#OrdenamientoBurbuja(Lista)
#print(Lista)