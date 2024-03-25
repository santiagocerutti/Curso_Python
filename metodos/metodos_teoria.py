### Métodos

# Los métodos son funciones específicas de los objetos ya que están relacionadas a los atributos que el mismo posee.
# Todos los métodos son funciones pero no todas las funciones son métodos. 

# Por ejemplo print() es una función (que nos permite ver en la consola lo que depositemos dentro del paréntesis) pero no es un método, ya que no forma parte de los atributos de un objeto en particular.

# dir() es un ejemplo de otra funcion, esta nos devuelve una lista con todos los atributos del objeto que mencionamos dentro del paréntesis. 

# Obviamente los mismos atributos de un objeto van a variar dependiendo si se trata de una cadena, una lista, etc. En base a esos atributos es que podemos usar o no ciertos métodos.
cadena = "Esta es una cadena"
lista = [1,2,3]

#print(dir(cadena))
#print(dir(lista))

#Los métodos, aunque van seguidos de paréntesis, se escriben a continuación del objeto luego de un punto. Es decir NO debemos escribir el objeto dentro del método.

# funcion(objeto)   Correcto
# metodo(objeto)    Incorrecto
# objeto.metodo()   Correcto

# Ejemplo:
print(cadena.upper())


