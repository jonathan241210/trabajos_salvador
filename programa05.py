""""
PROGRAMA 05
nombre: Jonathan Serrano Ortiz
matricula:1723110233
grupo:21
fecha:18-01-2024
descripcion: este programa imprime el mensaje objetos alumnos, el nombre más un texto y la suma de dos numeros  
"""

class alumnos:# se crea una clace denominada alumnos
  matricula=None# definimos la matricula
  nombre=None# definimos el nombre
  def __init__ (self, matricula, nombre):#definimos el constructor
    self.matricula=matricula#accediendo a la variable matricula 
    self.nombre=nombre#accediendo a la variable nombre
    print("objetos Alumnos")#imprimiendo un mensaje
  def estudiar(self):#definimos el metodo estudiar
    print(f"{self.nombre} estudia")# imprimimos el nombre y texto
  def sumar (self, numero1, numero2):#definimos el metodo sumar
    suma=numero1+numero2#definimos la variable suma más los dos numeros
    print(f"la suma de {numero1} y {numero2} es {suma}")#imprimimos el resultado de la suma
jonathan=alumnos(111,"jonathan")#creamos el objeto de la clace alumno
jonathan.estudiar()#invocamos el metodo estudiar
jonathan.sumar(10,5)#invocamos el metodo sumar
