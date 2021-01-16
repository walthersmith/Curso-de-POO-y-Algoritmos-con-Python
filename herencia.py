"""
Ejemplo de Herencia 
la cuales muy importante en la POO ya que nos permire reutilizar codigo 
de manera que evitemos reinventar la rueda 
ya que si tenemos un comportamient o  comin entre una serie de objetos  de la mis ma categoria 
esto puede heredarse entre las subclases  lo cal  facilita la mantenibilidad  del codigo.

"""

class Rectangulo:
    def __init__(self,base,altura):
        self.base = base 
        self.altura = altura 

    def area(self):
        return self.base * self.altura


class Cuadrado(Rectangulo):
    def __init__(self,lado):
        super().__init__(lado,lado)



if __name__ == "__main__":
    rectangulo = Rectangulo(base=3,altura=4)
    print(rectangulo.area())

    cuadrado = Cuadrado(lado=5)
    print(cuadrado.area())


#reto 

"""
se cren clases para modelar diferentes tipos de empleado  en una universidad 
"""

class Empleado:
    def __init__(self, nombre,dni,direccion,telefono,email):
        self._nombre = nombre 
        self._dni = dni
        self._direccion = direccion
        self._telefono = telefono
        self._email = email

    def datos_empleado(self):
        return f"nombre: {self._nombre} - dni {self._dni} - direccion: {self._direccion} - telefono {self._telefono} - email {self._email}"


class ProfesorCatedra(Empleado):
    def __init__(self,nombre,dni,direccion,telefono,email, asignaturas):
        super().__init__(nombre,dni,direccion,telefono,email) 
        self._asignaturas = asignaturas 

    def mostrar_asignaturas(self): 
        print("Asignaturas del profesor:")
        for asignatura in self._asignaturas: 
            print(asignatura.obtener_asignatura())



class Asignatura:
    def __init__(self,codigo,grupo,nombre_asignatura,fecha_desde, fecha_hasta, horas_total = 0):
        self._codigo = codigo
        self._grupo  = grupo 
        self._nombre_asignatura = nombre_asignatura
        self._fecha_desde = fecha_desde
        self._fecha_hasta = fecha_hasta
        self._horas_total = horas_total

    def obtener_asignatura(self):
        return f'codigo: {self._codigo} - grupo: {self._grupo} - nombre_asignatura: {self._nombre_asignatura} - fecha_desde: {self._fecha_desde} - fecha_hasta: {self._fecha_hasta} - horas_total: {self._horas_total}'    


if __name__ == "__main__":
    asignaturas = [ Asignatura(12334,"BD12","Matematicas discretas", "2020/10/30","2020/12/31",145),
                    Asignatura(14536,"BVC3","Calculo Vectorial", "2020/10/30","2020/11/30",114),
                    Asignatura(18987,"THB5","Ingles", "2020/10/30","2020/12/05",56)]
    profesor = ProfesorCatedra("Pepito perez",124431212,"car 22# 76 - 44b ", 5453123,'pepito@universidad.edu.co',asignaturas)

    print(profesor.datos_empleado())
    profesor.mostrar_asignaturas() 