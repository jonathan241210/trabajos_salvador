"""
Programa: eva02.py
Nombre_completo: Jonathan Serrano Ortiz
Matricula: 1723110233
Fecha: 1/29/2024
"""
class Libro: # definimos la clace Libro
  titulo = None # definimos la variable titulo
  autor = None # definimos la variable autor
  prestado = None # definimos la variable prestado
  anio_publicacion = None # definimos la variable anio_publicacion
  genero = None # definimos la variable genero
  def __init__(self, titulo, autor, anio_publicacion, genero, prestado=False):
    #definimos el constructor init
      self.titulo = titulo # accedemos a la variable titulo
      self.autor = autor # accedemos a la variable autor
      self.prestado = prestado # accedemos a la variable prestado
      self.anio_publicacion = anio_publicacion # accedemos a la variable anio_publicacion
      self.genero = genero # accedemos a la variable genero

  def prestar(self): # definimos el metodo prestar
      self.prestado = True # accedemos a la variable prestado

  def devolver(self): # definimos el metodo devolver
      self.prestado = False # accedemos a la variable prestado

  def mostrar_informacion(self): # definimos el metodo mostrar_informacion
      print(f"Título: {self.titulo}\n") #imprimimos el texto solicitado
      print(f"Autor: {self.autor}")#imprimimos el texto solicitado
      print(f"Año de publicación: {self.anio_publicacion}")#imprimimos el texto solicitado
      print(f"Género: {self.genero}")#imprimimos el texto solicitado
      print(f"Prestado: {'Sí' if self.prestado else 'No'}")#imprimimos el texto solicitado

libro1 = Libro("El Principito", "Antoine de Saint-Exupéry", 1943, "Ficción")
# creamos el objeto Libro
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", 1967, "Ficción", True)
# creamos el objeto Libro2
libro1.prestar()# invocamos el el metodo prestar
libro1.mostrar_informacion()# invocamos el el metodo mostrar_informacion
libro2.mostrar_informacion()# invocamos el el metodo mostrar_informacion2
libro1.devolver()# invocamos el el metodo devolver
libro1.mostrar_informacion()# invocamos el el metodo mostrar_informacion
libro2.mostrar_informacion()# invocamos el el metodo mostrar_informacion2

