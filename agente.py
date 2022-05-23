# Instrucciones basicas
# El traje o malla tactica consta de tres areas
# A --> Area superiro
# B --> Area media
# C --> Area inferior
# Sus testado peuden ser 0 ó 1
# 1 --> Sin tratar
# 0 --> Ya masajeado

def logica_absoluta():
    # inicializando estados de nuestras areas
    estado_area = {'superior': '0', 'medio': '0', 'bajo':'0'}
    recordar_areas = ['superior', 'medio', 'bajo']
    recordar_estados = [0, 0, 0]
    ejecutado = 0
    
    accionar_area = input("Introduzca el área de inicio ") # El usuario puede ubicar el area por la cual desea empezar con los masajes
    accionar_area = accionar_area.lower() # Vuelve todo en minusculas
    estado_entrada = input(f"Ingrese el estado del area {accionar_area}: ") # El usuario puede ingresar ele stado del area por el cual desidio partir 
    # status_input_complement = input("Introducir el area del estado7: ")
    print(accionar_area)

    estado_area[accionar_area] = estado_entrada
    print(recordar_areas.index(accionar_area))
    print(estado_area)

    for area in recordar_areas:
        if area != accionar_area:
            complemento_estados = input(f"Ingrese el estado del area '{area}': ") # El usuario puede ingresar ele stado del area por el cual desidio partir 
            estado = recordar_areas.index(area)
            recordar_estados[estado] = complemento_estados
            # Interactuamos con el objeto principal ó importante
            estado_area[area] = complemento_estados
    
    print(estado_area)


logica_absoluta()