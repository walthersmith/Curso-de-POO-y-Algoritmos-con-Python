import random

def ordenamiento_por_insercion(lista):        
    for i in range(1, len(lista)):        
        print(f'lista {i} valor {lista[i]}') 
        index = i-1
        valor_actual = lista[i]
        while index >= 0 and valor_actual < lista[index]:
            print(lista)
            lista[index+1] =  lista[index]
            print(lista)
            index-=1
        lista[index+1] = valor_actual
        print(lista)
    return lista
 

if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamano sera la lista? '))

    lista =  [random.randint(0,100) for i in range(tamano_de_lista)]
    print(lista)

    lista_ordenada = ordenamiento_por_insercion(lista)
    print('----*****-----')
    print(lista_ordenada)