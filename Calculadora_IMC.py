# #Damos la bienvenida al usuario con una pequeña descripción de lo que es el IMC
print("Hola, es un gusto conocerte. A continuación te pediremos información para poder conocer tu Indice de Masa Corporal (IMC)")
print("El índice de masa corporal (IMC) sirve para medir la relación entre el peso y la talla, lo que  permite identificar el sobrepeso y la obesidad en adultos.")
#Pedimpos que el usuario llene los datos
nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))
peso = int(input("Introduce tu peso en kilogramos: "))
altura = float(input("Introduce tu estatura en metros: "))
print("Muchas gracias" , nombre, " vamos  a revisar tu IMC, ten paciencia. :D")
#Ya que tenemos la información del usuario, procedemos a hacer el calculo del IMC
print("Veamos...")
print(".")
print(".")
print(".")
if edad <= 17:
    print("Eres menor de edad")
elif edad >= 18:
    print("Eres mayor de edad")
IMC = peso / altura**2
print("IMC: " + str(IMC))
#Definimos las variables de los distintos tipos de resultados del IMC
if IMC >= 0 and IMC <= 18.9:
    print("Peso bajo")
elif IMC >= 18.50 and IMC <= 24.99:
    print("Peso normal")
elif IMC >= 25.00 and IMC <= 29.99:
    print("Sobrepeso")
elif IMC >= 30.00 and IMC <= 34.99:
    print("Obesidad leve")
elif IMC >= 35.00 and IMC <= 39.99:
    print("Obesidad media")
elif IMC <= 40.00:
    print("Obesidad morbida")
#Agradecemos su participación
print("Agradecemos tu tiempo para responder", nombre, "ten un bonito día")
