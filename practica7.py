#UNIDAD 2
a = 10
b = 9
c = 18
if a>b: # 3 diferentes bloques de codigo
    print(a)
if a>c:
    print(a)
if b>c:
    print(b)

print("------------")
if a>b:# un solo bloque de codigo 
    print(a)
elif a>c:# por si no se cumple la primer condicion
    print(a)
elif b>c:# por si no se cumple la segunda condicion
    print(b)


print("------------")
if a>b:# 2 bloques de codigo
    print(a)
elif a>c:
    print(a)
if b>c:
    print(b)

print("----------")
if a>b:# esto es un if anidado
    if a>c:
        print(a)
else:
    print(c)

print("------------")
if a>b and a>c:# se tienen que cumplir ambas condiciones
    print(a)
else:
    print(c)

print("--------------")
if a>b or a>c:# se debe cumplir por lo menos una condicion para que ejecute el codigo
    print(a)
else:
    print(c)
print("------------")

