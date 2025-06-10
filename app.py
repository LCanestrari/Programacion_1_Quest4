import auxiliares
import os
from validaciones import validar_input
from variables import *


def aplicacion(lista_heroes):

    corriendo = True

    while corriendo:
        auxiliares.mostrar_menu()
        opcion = validar_input(0, 9)

        match opcion:
            case 1:
                print("Ejecutando opción 1")
                auxiliares.utn_imprimir_heroe_genero(lista_heroes, 'masculino')
            case 2:
                print("Ejecutando opción 2")
                auxiliares.utn_imprimir_heroe_genero(lista_heroes, 'femenino')
            case 3:
                auxiliares.calcular_imprimir_heroe_raza(lista_heroes, 'maximo', 'altura_mts', 'Human')
            case 4:
                auxiliares.calcular_imprimir_heroe_raza(lista_heroes, 'minimo', 'altura_mts', 'Desconocido')
            case 5:
                auxiliares.calcular_imprimir_heroe_raza(lista_heroes, 'minimo', 'altura_mts', 'Symbiote')
            case 6:
                auxiliares.calcular_imprimir_heroe_raza(lista_heroes, 'maximo', 'altura_mts', 'Mutant')
            case 7:
                pass
            case 8:
                pass
            case 9:
                pass
            case 0:
                corriendo = False

        
    os.system('pause')
    # os.system('cls')

