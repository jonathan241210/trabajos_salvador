""""
PROGRAMA 03
nombre: Jonathan Serrano Ortiz
matricula:1723110233
grupo:21
fecha:18-01-2024
descripcion: este programa imprime la matricula, el nombre, y el mensaje
objetos alumnos
"""
class Alumnos: # definimos la clace Alumnos
  matricula=1723110233 # definimos la matricula
  nombre="Jonathan Serrano Ortiz" # definimos el nombre
  def __init__ (self, matricula, nombre): # inicializamos los atributos de la clace Alumnos
    self.matricula=matricula # asignamos un valor al atributo matricula
    self.nombre=nombre # asignamos un valor al atributo nombre
    print("Objetos Alumnos") # imprimimos el mensaje solicitado
objetoAlumnos=Alumnos(1723110233, "Jonathan")# instanciar el objeto Alumnos
print(objetoAlumnos.matricula, objetoAlumnos.nombre) # imprimimos el valor del atributo matricula y nombre