import random


def ordenamiento_por_mezcla(lista):
    if len(lista) > 1:
        medio = len(lista)//2
        izquerda = lista[:medio]
        derecha = lista[medio:]
        print(izquerda, '*' * 5, derecha)

        #llamada recursiva en cada mitad 
        ordenamiento_por_mezcla(izquerda)
        ordenamiento_por_mezcla(derecha)

        #iteradores para recorrer las dos sublistas 
        i = 0
        j = 0 
        # Iterador para la lista principal
        k = 0 

        while i < len(izquerda) and j < len(derecha):
            if izquerda[i] < derecha[j]:
                lista[k] = izquerda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1            
            
            k += 1

        while i < len(izquerda):
            lista[k] = izquerda[i]
            i += 1 
            k += 1 
        
        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1 
            k += 1

        print(f'izquierda {izquerda}, derecha {derecha}')
        print(lista)
        print('-' * 50)
    return lista 

if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamano sera la lista? '))

    lista =  [random.randint(0,100) for i in range(tamano_de_lista)]
    print(lista)
    print('-' * 20)

    lista_ordenada = ordenamiento_por_mezcla(lista)
    print(lista_ordenada)