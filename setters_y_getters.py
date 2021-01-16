"""
¿Qué son getters y setters? y uso de property
el objetivo de los getters  y setters es  asegurarnos el encapsulamiento de
la informacion 
en Python  se usa la convencion de "_" para definir que un metodo variable sea  privada 

pero esto no quiere decir que  lo sean  ya que en Python en si no existen variables privadas 
como podemos tener acceso a estas variables desde la programacion  puede ser peligroso  y
puede afectar la logica de nuestra aplicacion 

https://www.programiz.com/python-programming/property

"""

#ejemplo de clses  sin getters y setters

class Millas:
    def __init__(self, distancia = 0):
        self.distancia = distancia  
    
    def convertir_a_kilometros(self):
        return (self.distancia * 1.609344)

#se crea el objeto 
avion = Millas()
# se asigna la distancia 
avion.distancia = 200
#se obtiene el atributo de distancia 
print(avion.distancia)
#se obtiene el metodo para convertir a kilometros 
print(avion.convertir_a_kilometros())

"""
Ahora veamos como queda la clase usando los getters an setters 
tambien se añade  metodo para que no acepte valores negativos 
"""
class Millas2:
    def __init__(self,distancia = 0):
        self.distancia = distancia

    def convertir_a_kilometros(self):
        return (self.distancia * 1.609344)

    #metodo getter 
    def obtener_distancia(self):
        return self._distancia

    #metodo setter
    def definir_distancia(self,valor):
        if valor < 0:
            raise ValueError("No es posible convetir distancias menores a 0.")
        self._distancia = valor

#se crea el objeto 
avion2 = Millas2()
# se asigna la distancia 
avion2.definir_distancia(200)
#se obtiene el atributo de distancia 
print(avion2.obtener_distancia())
#se obtiene el metodo para convertir a kilometros 
print(avion.convertir_a_kilometros())


"""
Funcion Property
esta funcion es propia de python y nos retorn ala propiedad de un objero  que posee getters, setters y del 

property(fget=None, fset=None, fdel=None, doc=None)
where,

fget is function to get value of the attribute
fset is function to set value of the attribute
fdel is function to delete the attribute
doc is a string (like a comment)

"""

#ejemplo de clase usando la funcion property

class Millas3:
    def __init__(self):
        self.distancia = 0 

    #funcion para obtener el valor de _distancia
    def obtener_distancia(self):
        print("Llamada al metoro getter3")
        return self._distancia

    #funcion para definir el valor de _distancia
    def definir_distancia(self,recorrido):
        print("Llamada al metoro Setter3",recorrido)
        self._distancia = recorrido

    #funcion para eliminar el atributo _distancia
    def eliminar_distancia(self):
        del self._distancia

    distancia = property(obtener_distancia,definir_distancia,eliminar_distancia)

#creamos un nuevo objeto 

avion = Millas3()

#indidamos la distancia 
avion.distancia = 200
#indicamos su atributo distancia
print(avion.distancia)

"""
Ahora vamos a ver el ejemplo usando property como decorador
"""
class Millas4:
    def __init__(self):
        self._distancia = 0

    #funcion que obtiene el vaor de _distancia 
    #usando el decorador  property

    @property
    def obtener_distancia(self):
        print("Llamada al metoro getter")
        return self._distancia

    #funcion para definir el valor de _distancia 
    @obtener_distancia.setter
    def definir_distancia(self,valor):
        if valor < 0:
            raise ValueError("No es posible convertir distancias menores a 0.")
        print("Llamada al metoro setter")
        self._distancia = valor

#creamos un objero nuevo
avion = Millas4()
#indicamos la distancia 
avion._distancia = 200
#obtenemos su atributo  y distancia 
print(avion._distancia)


