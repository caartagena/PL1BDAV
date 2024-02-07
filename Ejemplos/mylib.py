# Bases de datos avanzadas Curso 2023-24 
# Ejemplo de módulo de biblioteca



def contar_líneas(fichero):
    """
        contar_líneas :: File -> Integer
        cuenta cuantas líneas tienen el argumento
        PRE: fichero debe estar abierto para lectura
    """
    contador = 0                                                                # inicializamos un contador de lineas a cero
    for _línea in fichero:                                                      # por cada línea del fichero (línea se ignora)
        contador = contador + 1                                                 # sumamos 1 al contador
    return contador                                                             # finalmente devolvemos la cuenta

def contar_carácteres(cadena):
    """
        cuenta los char en una cadena. 
        Versión recursiva con esquema worker/wrapper
        >>> contar_carácteres("Ángel")
        5
    """
    def _contar(s, n):                                                          # mapeamos "" -> 0
        """ worker recursivo """                                                # ó 
        return n if not s else _contar(s[1:], n + 1)                            # 1 + resto de la cadena recursivamente

    return _contar(cadena, 0)                                                   # el wrapper inicializa


if __name__ == "__main__":                                                      # si ejecutamos este modulo
    import doctest
    doctest.testmod(verbose = True)                                             # lanzar la suite de tests