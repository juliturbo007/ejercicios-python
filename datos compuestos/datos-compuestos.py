
# Creando una lista (se puede modificar)
lista = ["Julio Cesar", "Soy Julio", True,1.75]

print(lista)

# creando una tupla (no se puede modificar)
tupla = ["Julio Cesar", "Soy Julio", True,1.75]

print(tupla)

# esto es valido
# lista[3] = "chino"

# esto no es valido
# tupla[3] = "chinito"

# creando un conjunto (set) sirven para eliminar Duplicados, no se accede a elementos por indice,
conjunto = {"Julio Cesar", "Soy Julio", True,1.75}
# print(conjunto[4])  no se puede acceder al elemento

#creando un diccionario (dict) ( la estructura es key : value y separamos con comas)

Diccionario = {
    'nombre' : "Julio Cesar",
    'apellido' : "Briones Huerta",
    'Dinero' : 1700,
    'altura' : 1.75,
    'dato_duplicado' : "Julio Cesar"
     }

print(Diccionario['altura'])

print(lista[3])









