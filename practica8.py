#UNIDAD 2
cadena = "hola mundo python" # variable "cadena" con un valor texto 
def contar_vocales(cadena): # definimos el metodo contar_vocales con la variable "cadena"
    contador_a = 0 # variable 'a'
    contador_e = 0 # variable 'e'
    contador_i = 0 # variable 'i'
    contador_o = 0 # variable 'o'
    contador_u = 0 # variable 'u'

    for letra in cadena.lower(): #varible 'letra' en 'cadena' LOWER(convierte en minusculas)
        if letra == 'a': # si esta condicion se cumple ejecuta el codigo de abajo
            contador_a += 1 # aumenta en 1 si se encuentra la letra 'a' dentro de "cadena"
        elif letra == 'e': # si esta condicion se cumple ejecuta el codigo de abajo
            contador_e += 1 # aumenta en 1 si se encuentra la letra 'e' dentro de "cadena"
        elif letra == 'i': # si esta condicion se cumple ejecuta el codigo de abajo
            contador_i += 1 # aumenta en 1 si se encuentra 'i' dentro de "cadena"
        elif letra == 'o': # si esta condicion se cumple ejecuta el codigo de abajo
            contador_o += 1 # aumenta en 1 si 'o' se encuentra en cadena
        elif letra == 'u': # si esta condicion se cumple ejecuta el codigo de abajo
            contador_u += 1 # aumenta en 1 si 'u' se encuentra en cadena

    print(f"En la cadena '{cadena}' hay:") #imprimir cadena de texto con una variable
    print(f"vocales 'a': {contador_a}") #imprimir cadena de texto con una variable
    print(f"vocales 'e': {contador_e}") #imprimir cadena de texto con una variable
    print(f"vocales 'i': {contador_i}") #imprimir cadena de texto con una variable
    print(f"vocales 'o': {contador_o}") #imprimir cadena de texto con una variable
    print(f"vocales 'u': {contador_u}") #imprimir cadena de texto con una variable

contar_vocales(cadena) #llamamos contar_vocales con la variable "cadena"
