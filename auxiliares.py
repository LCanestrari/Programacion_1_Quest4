from variables import lista_heroes

def mostrar_menu ():
    texto =\
        """
        1 - Recorrer la lista imprimiendo por consola nombre de cada personaje masculino
        2 - Recorrer la lista imprimiendo por consola nombre de cada personaje femenino
        3 - Recorrer la lista imprimiendo por consola nombre de cada personaje masculino
        4 - Recorrer la lista imprimiendo por consola nombre de cada personaje masculino
        9 - Salir.
        """
    
def es_dato(heroe:dict, key: str, valor) -> bool:
    return heroe[key] == valor

def utn_imprimir_heroe_genero(lista_personajes : list[dict], genero : str):
    for heroe in lista_personajes:
        if es_dato(heroe, 'genero', genero):
            print(heroe.get('nombre'))


def calcular_min_raza(lista_personajes: list[dict], key:str, raza:str):
    minimo = {}
    for heroe in lista_personajes:
        if es_dato(heroe, key , raza) and (not minimo or minimo.get(key) > heroe.get(key)):
            minimo = heroe
    return minimo

def calcular_max_raza(lista_personajes: list[dict], key:str, raza:str):
    maximo = {}
    for heroe in lista_personajes:
        if es_dato(heroe, key , raza) and (not maximo or maximo.get(key) < heroe.get(key)):
            maximo = heroe
    return maximo

def calcular_max_min_dato(lista_personajes: list[dict], calculo:str,key:str, raza:str):
    heroe_elegido = {}
    if calculo.lower() == 'maximo':
        heroe_elegido = calcular_max_raza(lista_personajes, key, raza)
    elif calculo.lower() == 'minimo':
        heroe_elegido = calcular_min_raza(lista_personajes, key, raza)
    return heroe_elegido

def calcular_imprimir_heroe_raza(lista_personajes: list[dict], calculo:str, key:str, raza:str):
    heroe_elegido = calcular_max_min_dato(lista_personajes, calculo, key, raza)
    nombre = heroe_elegido.get('nombre')
    texto =\
        f"""
        El heroe que tiene el {calculo} de {key} es: {nombre} con valor: {heroe_elegido.get(key)}        
        """
    
def sumar_dato_personaje_empresa(lista_personajes: list[dict], key:str, empresa:str):
    suma = 0
    for heroe in lista_personajes:
        if type(heroe) == dict and heroe and es_dato(heroe, 'empresa', empresa):
            suma += heroe.get(key)
    return suma

def cantidad_de_personajes_empresa(lista_personajes: list[dict], empresa:str):
    cantidad = 0
    for heroe in lista_personajes:
        if es_dato(heroe, 'empresa', empresa):
            cantidad += 1
    return cantidad

def calcular_promedio_empresa(lista_personajes: list[dict], key:str, empresa:str):
    suma = sumar_dato_personaje_empresa(lista_personajes, key, empresa)
    cantidad = cantidad_de_personajes_empresa(lista_personajes, empresa)
    promedio = 0
    if cantidad > 0:
        promedio = suma / cantidad
    return promedio

def calcular_imprimir_promedio_altura_empresa(lista_personajes: list[dict], key:str, empresa:str):
    if lista_personajes:
        promedio = calcular_promedio_empresa(lista_personajes, key, empresa)
        texto =\
            f"""
            {key.title()} promedio empresa {empresa} es: {promedio:.2f} mts
            """
        print(texto)
    else:
        print("No hay personajes para calcular el promedio de altura.")

# if __name__ == '__main__':
#     from variables import lista_heroes

#     tipos_distintos = set()

#     for heroe in lista_heroes:
#         tipos_distintos.add(heroe.get('genero'))
    
#     print(tipos_distintos)

def calcular_cantidad_tipo(lista_personajes: list[dict], key:str):
    cantidad_de_tipo = dict()

    if lista_personajes:

        for heroe in lista_personajes:
            valor = heroe.get(key)
            if valor in cantidad_de_tipo.keys():
                cantidad_de_tipo[valor] += 1
            else:
                cantidad_de_tipo[valor] = 1

    return cantidad_de_tipo

# if __name__ == '__main__':
#     from variables import lista_heroes

#     tipos_distintos = calcular_cantidad_tipo(lista_heroes, 'color_ojos')
#     print(tipos_distintos)

def imprimir_cantidad_tipo(variedades_tipo:dict, key:str):
    for clave, valor in variedades_tipo.items():
        texto =\
            f""" Caracteristica: {key} {clave} - Cantidad de personajes :{valor} """
        print(texto)

# if __name__ == '__main__':
#     from variables import lista_heroes

#     tipos_distintos = calcular_cantidad_tipo(lista_heroes, 'color_ojos')
#     imprimir_cantidad_tipo(tipos_distintos, 'color de ojos')

def obtener_lista_de_tipos(lista_personajes: list[dict], key:str):
    set_elementos = set()

    for heroe in lista_personajes:
        set_elementos.add(heroe.get(key))

        return set_elementos
    
def normalizar_dato(dato, valor_default):
    if dato == '' or dato == "-":
        dato = valor_default
    return dato

def obtener_personajes_por_tipo(lista_personajes: list[dict], set_tipos:str, key):

    variedades_distintas = {}

    for variedad in set_tipos:
        if not variedad in variedades_distintas.keys():
            variedades_distintas[variedad] = []
        for heroe in lista_personajes:
            dato_raw = heroe.get(key)
            dato = normalizar_dato(dato_raw, 'N/A')

            if dato == variedad:
                variedades_distintas[variedad].append(heroe.get('nombre'))
    return variedades_distintas

def imprimir_personajes_por_tipo(tipos_distintos:dict, key:str):
    for clave, valor in tipos_distintos.items():
        texto =\
            f""" Caracteristica: {key} {clave}: {' | '.join(valor)} """
        print(texto)

def ordenar_personajes_por_dato(tipos_distintos:dict, orden:str = 'ASC'):
    for clave, valor in tipos_distintos.items():
        if orden == 'ASC':
            tipos_distintos[clave].sort()
        elif orden == 'DESC':
            tipos_distintos[clave].sort(reverse=True)
    return tipos_distintos