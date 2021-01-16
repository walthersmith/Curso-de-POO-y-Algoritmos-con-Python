
"""
CONCEPTO DE DECORADOR 
se conoce como  metaprogramacion (metaprograming) 
esto nos ayuda a tomar una funcion y le añade  alguna funcionalidad 
y la retorna 

AQUI UN EJEMPLO:
"""
def funcion_decoradora(funcion):
    def wrapper():
        print('Este es el ultimo mensaje...')
        funcion()
        print("este es el primer mensaje")
    return wrapper

def zumbido():
    print("BuzzZzzZz")


zumbido = funcion_decoradora(zumbido)

zumbido()


"""
Lo de arriba es algo complejo  pero python nos provee del uso del arroba @ para 
referenciar un decorador  y con esto obtenemos el mismo resultado de arriba 
"""
@funcion_decoradora
def zumbido2():
    print("BuzzZzzZz")

zumbido2()
