

def validar_input(min: int, max: int) -> int:
    opcion = input(f'Seleccione una opción entre [{min} - {max}]: ')
    while not (opcion.isdigit() and min <= int(opcion) <= max):
        print('Error: elija una opción válida.')
        opcion = input(f'Seleccione una opción entre [{min} - {max}]: ')
    opcion = int(opcion)
    print(f'Usted eligió la opción: {opcion}')
    return opcion