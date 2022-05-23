# Instrucciones basicas
# El traje o malla tactica consta de tres areas
# A --> Area superiro
# B --> Area media
# C --> Area inferior
# Sus testado peuden ser 0 ó 1
# 1 --> Sin tratar
# 0 --> Ya masajeado

# inicializando estados de nuestras areas
estado_area = {'superior': '0', 'medio': '0', 'bajo':'0'}    
# Guardamos el objeto actualizado y configurado por el usuario, para compararlo al final
objeto_deseado = estado_area.copy()
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

    recordar_areas = ['superior', 'medio', 'bajo']
    recordar_estados = [0, 0, 0]
    ejecucion = 1
    
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
    ejecucion = 0

    # Copiar el objeto inicial
    objeto_inicial = estado_area.copy()
    
    for key in estado_area.keys():
        if accionar_area == key:
            # Location A is Dirty.
            print(f"La terapia de masajeo iniciara desde el area {key} ")

            if estado_area.get(key) == '1':
                print(f"La area {key} hace falta masajear")
                # masajear el area y declararla como ya tratada '0'
                estado_area[key] = '0'
                ejecucion += 1 # Incremento del costo de masaje por area en +1
                print(f"Masajeo en la area {key} del traje tactico")
                print(f"Costo actual de ejecución: {ejecucion}")
                ejecucion += verificar_estados(key, ejecucion)
            elif estado_area.get(key) == '0':
                print(f"La area {key} ya se enceuntra masajeado")
                ejecucion += verificar_estados(key, ejecucion)

    return {"ejecucion": ejecucion, "objeto_inicial":objeto_inicial}

def verificar_estados(anteriorArea, ejecucion):
    costo = ejecucion
    guardarArea = anteriorArea
    for area in estado_area:
        if(area != anteriorArea):
            if estado_area[area] == '1':
                print(f"La area {area} hace falta masajear")
                # masajear el area y declararla como ya tratada '0'
                estado_area[area] = '0'
                costo += 1 # Incremento del costo de masaje por area en +1
                print(f"Del area {guardarArea} los movimeintos se trasladan al area {area}")

                print(f"Costo actual de ejecución: {costo}")
            else:
                print(f'EL area {area} ya se enceuntra masajeada')
                print('No es necesario el conteo ejecución para el coste')
            guardarArea = area
    return costo

result = logica_absoluta()
costo_ejecucion = result.get("ejecucion")
objeto_inicial = result.get("objeto_inicial")

print(f'El costo de ejecución es de: {costo_ejecucion}')
print(f'El estado inicial es: {objeto_inicial}')
print(f'El estado esperado es: {objeto_deseado}')
print(f'El resultado final: {estado_area}')