#Programa que identifica la validez del movimiento del caballo en ajedrez.
#Entradas y restricciones:
#- fila, columna: primera posición del caballo, deben ser enteros entre 1 y 8.
#- fila2, columna2: segunda posición del caballo, deben ser enteros entres 1 y 8
#Salida:
#-La validez del movimiento del caballo.
#Hecho por: Tamara Nicole Rodriguez Luna.
print("Escriba la posicion actual de la figura")
print("Fila (1-8):")
fila = int(input())
if fila >= 1 and fila <= 8:
    print("Columna (1-8):")
    columna = int(input())
    if columna >= 1 and columna <= 8:
        print("Escriba la posicion destino de la figura.")
        print("Fila (1-8):")
        fila2 = int(input())
        if fila2 >= 1 and fila2 <= 8:
            print("Columna (1-8):")
            columna2 = int(input())
            if columna >= 1 and columna <= 8:
                if fila > fila2:
                    caso1 = fila - fila2
                    if caso1 == 2:
                        if columna >= columna2:
                            caso7= columna - columna2
                            if caso7 == 1:
                                print("El movimiento es valido.")
                            else:
                                print("El movimiento no es valido.")
                        else:
                            if columna <= columna2:
                                caso8 = columna2 - columna
                                if caso8 == 1:
                                    print("El movimiento es valido")
                                else:
                                    print("El movimiento no es valido.")
                            else:
                                if columna == columna2:
                                    print("Movimiento no es valido.")
                                else:
                                    print("Movimiento no es valido.")
                    else:
                         if caso1 == 1:
                               if columna >= columna2:
                                     caso9 = columna - columna2
                                     if caso9 == 2:
                                         print("El movimiento es valido.")
                                     else:
                                         print("El movimiento no es valido.")
                               else:
                                  if columna <= columna2:
                                      caso10 = columna2 - columna
                                      if caso10 == 2:
                                         print("El movimiento es valido.")
                                      else:
                                         print("El movimiento no es valido")
                                  else:
                                     if columna == columna2:
                                        print("El movimiento no es valido.")
                                     else:
                                        print("El movimiento no es valido.")
                         else:
                           print("El movimiento no es valido.")
                           
                else:
                    caso2= fila2 - fila
                    if caso2 == 2:
                            if columna >= columna2:
                                caso3 = columna - columna2
                                if caso3 == 1:
                                    print("El movimiento es valido.")
                                else:
                                    print("El movimiento no es valido.")
                            else:
                                 if columna <= columna2:
                                    caso4 = columna2 - columna
                                    if caso4 == 1:
                                      print("El movimiento es valido")
                                    else:
                                      print("El movimiento no es valido")
                                 else:
                                    if columna == columna2:
                                      print("Movimiento no es valido.")
                                    else:
                                      print("Movimiento no es valido.")
                    else:
                          if caso2 == 1:
                                if columna >= columna2:
                                    caso5 = columna - columna2
                                    if caso5 == 2:
                                        print("El movimiento es valido.")
                                    else:
                                        print("El movimiento no es valido.")
                                else:
                                    if columna <= columna2:
                                        caso6 = columna2 - columna
                                        if caso6 == 2:
                                            print("El movimiento es valido.")
                                        else:
                                            print("El movimiento no es valido.")
                                    else:
                                        if columna == columna2:
                                            print("Movimiento no es valido.")
                                        else:
                                            print("Movimiento no es valido.")
                          else:
                              print("El movimiento no es valido.")
            else:
                print("columna no valida.")
        else:
            print("Fila no valida.")
    else:
         print("Columna no valida")
else:
    print("Fila no valida")
