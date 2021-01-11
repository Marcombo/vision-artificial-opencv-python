from tabulate import tabulate

cabecera = ["NOMBRE", "DIRECCIÓN", "TELÉFONO"]
datos_persona1 = ["Tomás", "Gran Vía, 10, 1ºA", "9112345"]
datos_persona2 = ["Juan", "Alcalá, 11, 2ºB", "9167890"]

tabla =[datos_persona1, datos_persona2]
tabla_con_formato = tabulate(tabla, cabecera)
print(tabla_con_formato)
