### Métodos de cadenas

cadena1 = "Bienvenidos"
cadena2 = "Hola, Cómo están?"

## Métodos que convierten valores
# UPPER
#print(lower(cadena1)) # No va a funcionar
metodo1 = cadena1.upper()

# LOWER
metodo2 = cadena1.lower()

## Métodos que buscan valores
# FIND: Devuelve la posición de una cadena dentro de otra (-1 si no hay coincidencia)
metodo3 = cadena1.find("B")
metodo4 = cadena1.find("i")
metodo5 = cadena2.find("están")
metodo6 = cadena2.find("estan")

# INDEX: También devuelve la posición de una cadena dentro de otra pero si no hay coincidencia lanza un error (una excepción)
#metodo7 = cadena2.index("estan")

## Métodos que consultan algo a los datos
# ISNUMERIC
metodo8 = cadena1.isnumeric()

# ISALPH (ojo con los caracteres especiales y los espacios)
metodo9 = cadena1.isalpha()
metodo10 = cadena2.isalpha()

# COUNT: Devuelve la cantidad de coincidencias de una subcadena en otra cadena
metodo11 = cadena1.count("e")
metodo12 = cadena2.count("e")


# STARTSWITH y ENDSWITH
metodo13 = cadena1.startswith("B")
metodo14 = cadena1.endswith("B")

# REPLACE: Reemplaza una parte de la cadena por otra cadena (sin modificar el objeto !!)
metodo15 = cadena1.replace("Bien","BIEN")
metodo16 = cadena2.replace(" ","_")

# SPLIT: Separa las cadenas a partir del caracter que le indiquemos. Nos devuelve una lista con elementos
metodo17 = cadena2.split(",")
print(metodo17)

# LEN es una función
funcion1 = len(cadena1)
print(funcion1)


#Contrast and combination of ITU databases and expenditure surveys

#[Error- 001] Dates before or beyond the PO Line! 12/01/2023 and/or 12/31/2023 date is outside the PO line duration. To proceed, please correct the dates.



