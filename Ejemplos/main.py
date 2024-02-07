# Bases de Datos avanzadas 2023-24. 
# Esqueleto de trabajo en Python.


import sys                                                                      # importamos el módulo sys para usarlo 
                                                                                # en nuestro módulo
import mylib                                                                    # import módulo de biblioteca


def main(argumentos):
    """
        main :: [String] -> None
        programa principal argv debe contener al menos un elemento a procesar
        consultar https://docs.python.org/3/library/sys.html#sys.argv
    """
    print("Programa de lectura de ficheros")                                
    if len(sys.argv) > 1:                                                       # si tenemos un nombre de fichero 
        ruta_fichero = sys.argv[1]                                              # copiamos el nombre del segundo elemento
        with open(ruta_fichero, 'r') as fichero:                                # abrimos dicho nombre como un fichero de lectura
            líneas = mylib.contar_líneas(fichero)                               # llamamos a contar y obtenermos la cuenta
            print(f"El fichero {ruta_fichero} tiene {líneas} líneas")           # se lo mostramos al usuario
    else:                                                                       # si no hay argumentos que procesar
        print("No hay fichero que procesar..")                                  # notificamos al usuario
    return None                                                                 # y terminamos

if __name__ == "__main__":                                                      # Si este modulo es el principal 
    if '--test' in sys.argv:                                                    # Entonces si existe "--test" en la linea de argumentos
        import doctest                                                          # entonces importamos el módulo DoctTest
        doctest.testmod()                                                       # y lanzamos los test que hubiera definidos
    else:                                                                       # si no
        main(sys.argv)                                                          # llamamos a main y le pasamos argumentos