## Operadores Lógicos ( & , | , not)

# AND (ambas tienen que ser verdaderas)
t_and_t = True & True #Devuelve True
t_and_f = True & False #Devuelve False
f_and_t = False & True #Devuelve False
f_and_f = False & False #Devuelve False

# OR (una de las dos tiene que ser verdadera)
t_or_t = True | False #Devuelve True
t_or_f = True | False #Devuelve True
f_or_t = False | True #Devuelve True
f_or_f = False | False #Devuelve False

# NOT
not_t = not True #Devuelve False
not_f = not False #Devuelve True
