""""
PROGRAMA 04
nombre: Jonathan Serrano Ortiz
matricula:1723110233
grupo:21
fecha:18-01-2024
descripcion: este programa imprime la matricula y el nombre de dos personas
"""
class Alumnos: #definimos la clace Alumnos
  matricula=None #atributos matricula
  nombre=None #atributos nombre
  def __init__ (self, matricula, nombre): #inicializamos los atributos de la clace Alimnos
    self.matricula=matricula # asignamos un valor a la matricula
    self.nombre=nombre # asignamos un valor al nombre
objetoAlumnos=Alumnos(1723110233, "Jonathan") #instanciar el objeto alumnos
objetoAlumnos2=Alumnos(nombre="Salvador",matricula=222) # instanciar el objeto alumnos2
print(objetoAlumnos.matricula, objetoAlumnos.nombre) #imprimir la matricula y nombre
print(objetoAlumnos2.matricula, objetoAlumnos2.nombre)# imprimir la matricula y nombre de objetoAlumnos2