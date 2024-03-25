### Datos Compuestos

## Listas
lista = ["Santiago","Cerutti",35]
print(lista)

print(lista[0])
print(lista[1])
print(lista[2])
# Es decir, se cuenta desde el 0. El índice es la posición, la primera es cero y es ahí donde se aloja el elemento 1.

# También es posible extraer los sub-elementos de un elemento
print(lista[0][0])
print(lista[1][0])

# También podemos modificar un solo elemento de la lista
lista[0] = "San"
print(lista[0])

## Tuplas
tupla = ("Santiago","Cerutti",35)

# Es igual a una lista, pero NO SE PUEDE MODIFICAR

## Set o conjunto. Son elementos que no permiten modificar los elementos pero sí redefinir el conjunto por completo. Además, no podemos acceder a un elemento mediante el índice (se puede con un bucle). Y tampoco me permite almacenar valores duplicados.
conjunto =  {"Santiago","Cerutti",35}

## Diccionario (dict) (idéntico a JSON en JV)
diccionario = {
    'nombre' : "Santiago",
    'apellido' : "Cerutti",
    'edad' : 35
}

# En lugar de usar un índice para referirnos a un elemento, definimo el nombre (clave o key) para referirnos a cada elemento.
# La estructura es key : values y separamos con comas excepto el último
print(diccionario)
print(diccionario["apellido"])