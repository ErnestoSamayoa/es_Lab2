#Metodo capitalize
texto = "hola mundo"
resultado = texto.capitalize()
print(resultado)

##Metodo find
texto = "Hola Mundo"
resultado = texto.find("undo")
print(resultado)


#Metodo center (centra el texto en un conjunto de caracteres)
texto = "Hola"
resultado = texto.center(20,'*')
print(resultado)


##Metodo isalnum() Devuelve True si todos los caracteres de la cadeba son alfanúmericos
texto = "Python1234567"
resultado = texto.isalnum()
print(resultado)

##Metodo isdigit() 
texto = "234234"
resultado = texto.isdigit()
print(resultado)

##Metodo islower Devuelve True si todos los caracteres de la cadena estan en minuscula 
texto = "asdfasdfasdf"
resultado = texto.islower()
print(texto)

##Metodo isspace(): Devuelve si todos los caracteres de la cadena son espacios en blanco
texto = "        "
resultado = texto.isspace()
print(resultado)

##Probar los siguientes metodos:

#lstrip(): devuelve una copia de la cadena con los blancos iniciales emitidos
texto = "\tHola Ernesto\n"
print(texto)

texto = texto.lstrip("s tHo\t\n")
print(texto)

#replace(): Una cadena puede reemplazar una subcadena en otra cadena.
texto = 'Hello World!'
print(texto.replace("Hello", "Goodbye"))

#rstrip(): Este método se utiliza para eliminar todos los caracteres finales mencionados en su argumento. 
texto = "\tHola Ernesto\n"
print(texto)

texto = texto.rstrip("s tHo\t\n")
print(texto)

#split(): devuelve una lista que contiene las palabras de la cadena. Si incluye la cadena s, se utliza como separador
texto = " Hola amigos soy Ernesto"

text = texto.split()
print(text)