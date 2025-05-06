#ejer tenemos que ingresar por pantalla un string con la fecha en formato ISO, por ej 
# 202505605 indenticar el mes en el que se encuentra en este caso mes de mayo 


# Solicitar la fecha por pantalla
fecha = input("Ingrese la fecha en formato ISO (ej: 20250505): ")

# Extraer el mes (posición 4 a 6)
mes_str = fecha[4:6]

# Diccionario para traducir número de mes a nombre
meses = {
    "01": "enero",
    "02": "febrero",
    "03": "marzo",
    "04": "abril",
    "05": "mayo",
    "06": "junio",
    "07": "julio",
    "08": "agosto",
    "09": "septiembre",
    "10": "octubre",
    "11": "noviembre",
    "12": "diciembre"
}

# Verificar que el mes sea válido y mostrar
if mes_str in meses:
    print(f"El mes es: {meses[mes_str]}")
else:
    print("Formato de mes no válido.")
