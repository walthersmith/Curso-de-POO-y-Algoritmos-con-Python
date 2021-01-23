import random


def busqueda_binaria(lista, comienzo, final, objetivo, itera_bin =0):
    #print(f'buscando {objetivo} entre {lista[comienzo]} {[comienzo]} y {lista[final - 1]} {[final - 1]} ')
    itera_bin += 1
    #caso base: si el elmento  inicial es mas grande que el final enconces no se concontro
    if comienzo > final:
        return (False,itera_bin)

    medio = (comienzo + final) // 2 
    # el // es para division de enteros sin la parte decimal

    if lista[medio] == objetivo:
        return (True, itera_bin) 

    elif lista[medio] < objetivo:
        #print(f'#1 {objetivo} entre {medio +1} y {final}  ')
        return busqueda_binaria(lista,medio +1, final, objetivo,itera_bin = itera_bin)
    else: 
        #print(f'#2 {objetivo} entre {comienzo} y {final -1}  ')
        return busqueda_binaria(lista, comienzo, medio -1, objetivo,itera_bin = itera_bin)



def busqueda_lineal(lista,objetivo,iter_lin=0):
    match = False 

    for elemento in lista: #O(n)
        iter_lin += 1
        if elemento == objetivo:
            match = True 
            break
    return (match,iter_lin)


if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamaño sera la lista? '))
    objetivo = int(input('Que numero quieres encontrar? '))

    lista = sorted([random.randint(0,100) for i in range(tamano_de_lista)])

    print("----------Busqueda binaria---------------")
    #print(lista) 
    (encontrado,itera_bin) = busqueda_binaria(lista,0,len(lista),objetivo)
    #print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista ') 
    print(f'Se realizaron {itera_bin} interaciones')

    print("----------Busqueda lineal---------------")

    (encontrado,iter_lin) = busqueda_lineal(lista,objetivo)
    #print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista ') 
    print(f'Se realizaron {iter_lin} interaciones')


    #https://miro.medium.com/max/1200/1*4poxx4vMDQfGEq3HeswJoA.gif
    #https://riptutorial.com/es/algorithm/example/26648/o--log-n--tipos-de-algoritmos