### If y Else

a = 2

if a > 1 :
    # Si a > 1 es True -> se ejecuta lo que se escribe aquí.
    print("Se cumple la condición")
else:
    # Si a > 1 es False -> se ejecuta lo que se escribe aquí.
    print("NO se cumple la condición")
    
# Pueden anidarse varias condiciones
if a == 0 :
    print("a vale 0")
if a == 1 :
    print("a vale 1")
if a == 2 :
    print("a vale 2")
else:
    print("a no vale ni 0 ni 1 ni 2")

# Pero en estos casos es recomendable usar elif ( combinación de else if) ya que dependiendo de la condición pueden que se cumplan más de 1. Ejemplo:
b = 3
if b > 3:
    print("b es mayor a 3")
if b > 2:
    print("b es mayor a 2")
if b > 1:
    print("b es mayor a 1") 

# Cómo la segunda condición ya implica la tercera, queremos que sólo se muestre la segunda. Para eso usamos:
if b > 3:
    print("b es mayor a 3")
elif b > 2:
    print("b es mayor a 2")
elif b > 1:
    print("b es mayor a 1") 

# También es posible incluir condiciones dentro de las condiciones
c = 5

if c > 0:
    print("c es positivo")
    if c < 5:
        print("c es menor a 5")
    elif c < 10:
        print("c es menor a 10")
    else:
        print("c es mayor a 10")

