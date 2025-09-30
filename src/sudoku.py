lista = [
    " "," "," "," "," "," "," "," "," ",
    " "," "," "," "," "," "," "," "," ",
    " "," "," "," "," "," "," "," "," ",
    " "," "," "," "," "," "," "," "," ",
    " "," "," "," "," "," "," "," "," ",
    " "," "," "," "," "," "," "," "," ",
    " "," "," "," "," "," "," "," "," ",
    " "," "," "," "," "," "," "," "," ",
    " "," "," "," "," "," "," "," "," "
    ]
fila1 = lista[0:9]
fila2 = lista[9:18]
fila3 = lista[18:27]
fila4 = lista[27:36]
fila5 = lista[36:45]
fila6 = lista[45:54]
fila7 = lista[54:63]
fila8 = lista[63:72]
fila9 = lista[72:81]
col1 = lista[0:81:9]
col2 = lista[1:81:9]
col3 = lista[2:81:9]
col4 = lista[3:81:9]
col5 = lista[4:81:9]
col6 = lista[5:81:9]
col7 = lista[6:81:9]
col8 = lista[7:81:9]
col9 = lista[8:81:9]
bloque1 = lista[0:3] + lista[9:12] + lista[18:21]
bloque2 = lista[3:6] + lista[12:15] + lista[21:24]
bloque3 = lista[6:9] + lista[15:18] + lista[24:27]
bloque4 = lista[27:30] + lista[36:39] + lista[45:48]
bloque5 = lista[30:33] + lista[39:42] + lista[48:51]
bloque6 = lista[33:36] + lista[42:45] + lista[51:54]
bloque7 = lista[54:57] + lista[63:66] + lista[72:75]
bloque8 = lista[57:60] + lista[66:69] + lista[75:78]
bloque9 = lista[60:63] + lista[69:72] + lista[78:81]

filas = fila1, fila2, fila3, fila4, fila5, fila6, fila7, fila8, fila9
columnas = col1, col2, col3, col4, col5, col6, col7, col8, col9
bloques = bloque1, bloque2, bloque3, bloque4, bloque5, bloque6, bloque7, bloque8, bloque9

def es_correcta(lista):
    respuesta = "Sí"
    for casilla in lista:
        #Comprobamos que los valores estén en el rango 1 - 9 y únicamente se acepten números:
        if not isinstance(casilla, int) or casilla < 1 or casilla > 9:
            print("Datos incorrectos. Recuerda: rango 1-9 y únicamente números.")
            respuesta = "No"
            break
        else:
            #Comprobamos que los sub-bloques y columnas no contengan números repetidos:
            if bloque1.count(bloque1[0]) > 1:
                print("Error en bloque 1.")
                respuesta = "No"
                break
            if bloque2.count(bloque2[0]) > 1:
                print("Error en bloque 2.")
                respuesta = "No"
                break
            if bloque3.count(bloque3[0]) > 1:
                print("Error en bloque 3.")
                respuesta = "No"
                break
            if bloque4.count(bloque4[0]) > 1:
                print("Error en bloque 4.")
                respuesta = "No"
                break
            if bloque5.count(bloque5[0]) > 1:
                print("Error en bloque 5.")
                respuesta = "No"
                break
            if bloque6.count(bloque6[0]) > 1:
                print("Error en bloque 6.")
                respuesta = "No"
                break
            if bloque7.count(bloque7[0]) > 1:
                print("Error en bloque 7.")
                respuesta = "No"
                break
            if bloque8.count(bloque8[0]) > 1:
                print("Error en bloque 8.")
                respuesta = "No"
                break
            if bloque9.count(bloque9[0]) > 1:
                print("Error en bloque 9.")
                respuesta = "No"
                break
            if col1.count(col1[0]) > 1:
                print("Error en columna 1.")
                respuesta = "No"
                break
            if col2.count(col2[0]) > 1:
                print("Error en columna 2.")
                respuesta = "No"
                break
            if col3.count(col3[0]) > 1:
                print("Error en columna 3.")
                respuesta = "No"
                break
            if col4.count(col4[0]) > 1:
                print("Error en columna 4.")
                respuesta = "No"
                break
            if col5.count(col5[0]) > 1:
                print("Error en columna 5.")
                respuesta = "No"
                break
            if col6.count(col6[0]) > 1:
                print("Error en columna 6.")
                respuesta = "No"
                break
            if col7.count(col7[0]) > 1:
                print("Error en columna 7.")
                respuesta = "No"
                break
            if col8.count(col8[0]) > 1:
                print("Error en columna 8.")
                respuesta = "No"
                break
            if col9.count(col9[0]) > 1:
                print("Error en columna 9.")
                respuesta = "No"
                break
    return respuesta      
      
fila = 1 
celda = 0
while fila <= 9:
    valores_fila = input("Introduce 9 valores para la fila " + str(fila) + ": ")
    # Validamos que son exactamente 9 caracteres
    if len(valores_fila) != 9:
        print("Debes introducir exactamente 9 dígitos.")
        continue

    # Validamos que todos sean números
    if not valores_fila.isdigit():
        print("Solo se permiten números.")
        continue

    # Validamos que no haya repetidos
    if len(set(valores_fila)) != 9:
        print("No pueden haber números repetidos en la fila.")
        continue

    try:
        for valor in valores_fila:
            valor = int(valor)
            if not 1 <= valor <= 9:
                raise ValueError("Los números deben estar en el rango 1–9.")
            lista[celda] = valor
            celda += 1
        fila += 1
    except ValueError as e:
        print(f"Entrada inválida: {e}")

respuesta = es_correcta(lista)  

print("---- S U D O K U ----")
print()
print(lista[0:9])
print(lista[9:18])
print(lista[18:27])
print(lista[27:36])
print(lista[36:45])
print(lista[45:54])
print(lista[54:63])
print(lista[63:72])
print(lista[72:81])
print()
print(respuesta)