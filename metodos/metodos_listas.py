### Métodos de listas

lista = ["Santiago","Cerutti",35]
# (Con la función LIST también es posible crear una lista, no es necesario pero puede ser útil cuanddo tenemos que crear una lista vacía)
# lista = list(["Santiago","Cerutti",35])


## Agregar elementos ---
# APPEND: Agrega un elemento al final de la lista
lista.append(1.75)

# INSERT: Agrega un elemento a la lista en la posición que le especifiquemos (recordadr que empieza en 0 el índice)
lista.insert(2,"Argentino")

# EXTEND: Agrega varios elementos
lista.extend(["La Plata","31/3/1989"])

## Eliminar elementos ---
# POP: Eliminando un elemento de la lista según su índice. Si usamos -1 se elimina el último, con -2 el ante último, etc.
lista.pop(6)
lista.pop(-1)

# REMOVE: Elimina un elemento de la lista según su valor (tiene que existir, de lo contrario salta error)
lista.remove("Argentino")

## ORDENAMIENTO -----
# REVERSE: Invierte los elementos de la lista pero no los ordena de ninguna manera
lista.reverse()

# SORT: Ordena los elementos de una forma ascendente, siempre y cuando NO haya cadenas (numéricos o boleanos). 
lista.remove("Santiago")
lista.remove("Cerutti")
lista.sort()

# Si usamos el PARÁMETRO reverse del método sort() ordenamos de forma descendiente
lista.sort(reverse=True)

# CLEAR: Elimina todos los elementos de la lista
lista.clear()
print(lista)


# LEN: Devuelve la cantidad de elementos a la lista
resultadof = len(lista)