# Instrucciones basicas
# El traje o malla tactica consta de tres areas
# A --> Area superiro
# B --> Area media
# C --> Area inferior
# Sus testado peuden ser 0 ó 1
# 1 --> Sin tratar
# 0 --> Ya masajeado

estado_area = {'superior': '0', 'medio': '0', 'bajo':'0'}
costo_ejecucion = 0
def obtenerKeys(estado_area):
    list = []
    for area in estado_area.keys():
        list.append(area)
    return list

def obtenerValues():
    list = []
    for estado in estado_area.values():
        list.append(estado)
    return list

def logica_absoluta():
    # inicializando estados de nuestras areas
    objeto_deseado = estado_area.copy()
    recordar_areas = ['superior', 'medio', 'bajo']
    recordar_estados = [0, 0, 0]
    
    accionar_area = input("Introduzca el área de inicio ") # El usuario puede ubicar el area por la cual desea empezar con los masajes
    accionar_area = accionar_area.lower() # Vuelve todo en minusculas
    estado_entrada = input(f"Ingrese el estado del area {accionar_area}: ") # El usuario puede ingresar ele stado del area por el cual desidio partir 
    # status_input_complement = input("Introducir el area del estado7: ")
    # print(accionar_area)

    estado_area[accionar_area] = estado_entrada
    # print(recordar_areas.index(accionar_area))
    # print(estado_area)

    for area in recordar_areas:
        if area != accionar_area:
            complemento_estados = input(f"Ingrese el estado del area '{area}': ") # El usuario puede ingresar ele stado del area por el cual desidio partir 
            estado = recordar_areas.index(area)
            recordar_estados[estado] = complemento_estados
            # Interactuamos con el objeto principal ó importante
            estado_area[area] = complemento_estados

    for key in estado_area.keys():
        if accionar_area == key:
            # Location A is Dirty.
            print(f"La terapia de masajeo iniciara desde el area {key} ")

            if estado_area.get(key) == '1':
                print(f"La area {key} hace falta masajear")
                # masajear el area y declararla como ya tratada '0'
                estado_area[key] = '0'
                costo_ejecucion += 1 # Incremento del costo de masaje por area en +1
                print(f"Masajeo en la area {key} del traje tactico")
                print("Costo actual de ejecución: " + str(costo_ejecucion))
                verificar_estados(key)
            elif estado_area.get(key) == '0':
                print(f"La area {key} ya se enceuntra masajeado")
                verificar_estados(key)

def verificar_estados(anteriorArea):
    for area in estado_area:
        if estado_area[area] == '1':
            print(f"La area {area} hace falta masajear")
            # masajear el area y declararla como ya tratada '0'
            estado_area[area] = '0'
            costo_ejecucion = costo_ejecucion + 1 # Incremento del costo de masaje por area en +1
            print(f"Del area {anteriorArea} los movimeintos se trasladan al area {area}")

            print("Costo actual de ejecución: " + str(costo_ejecucion))
        else:
            print(f'EL area {area} ya se enceuntra masajeada')
            print('No es necesario el conteo ejecución para el coste')
    costo += 1
    estado_area['nuevo'] = 'nuevo'
    return {'costo': costo}


result = verificar_estados(estado_area, 'superior', costo_ejecucion)
costo_ejecucion += result['costo']
print(costo_ejecucion)
print(estado_area)
            
           
   





# logica_absoluta()