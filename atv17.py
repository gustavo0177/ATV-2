def intercala_lista_ordenadas(lista1, lista2):
    i, j = 0, 0
    resultado = []

    while i < len(lista1) and j < len(lista2):
        if lista1[i] < lista2[j]:
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1
        
    
    while i < len(lista1):
        resultado.append(lista1[i])
        i +=1

    
    while j < len(lista2):
        resultado.append(lista2[j])
        j += 1

    return resultado     