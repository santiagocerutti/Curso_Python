## Variables

# Se definen y declaran al mismo tiempo
a = 2
b = 3
c = a + b
print(c)

nombre = "Facultad"
print(nombre)

# Es posible redefinirlas o modificarlas
nombre = "Facultad de Ciencias Económicas"
print(nombre)

# Otra forma de modificar una variable 
numero = 1
print(numero)

numero += 5
print(numero)

numero -=3
print(numero)

# Concatenar con +
nombre = "Santiago"
apellido = "Cerutti"
nombre_completo = nombre + apellido
print(nombre_completo)

nombre_completo = nombre + " " + apellido
print(nombre_completo)

# camelCase:  nombreCompleto
# snake_case: nombre_completo

# Concatenar con f strings (convierte a texto lo que está en llaves)
nombre = "Santiago"
saludo = "Hola, mi nombre es {nombre}"
print(saludo)

nombre = "Santiago"
saludo = f"Hola, mi nombre es {nombre}"
print(saludo)

# Operadores de pertenencia
print("Santiago" in saludo) 
print("santiago" in saludo) 
print("San"      in saludo) 

print("Santiago" not in saludo) 

# Borrar variable
del saludo
