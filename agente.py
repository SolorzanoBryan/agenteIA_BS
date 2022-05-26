# Instrucciones basicas
import time
# El traje o malla tactica consta de tres areas
# A --> Area superiro
# B --> Area media
# C --> Area inferior
# Sus testado peuden ser 0 ó 1
# 1 --> Sin tratar
# 0 --> Ya masajeado

# Inicializando estados de nuestras areas
estado_area = {'superior': '0', 'medio': '0', 'bajo':'0'}    
# Como el estado_area sera modificado, necesitaremos obtener una copia
# para saber si es que al final vuelve al estado esperado
objeto_deseado = estado_area.copy()
costo_ejecucion = 0 # El costo de ejecución tendra que ser monitorizado, para mas funcioanldiades en una posible mejora del agente
# --------------------------------------

# Funciones para obtener valores precisos y de forma automatica de una entidad (Meotods generales)
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
# ------------------------------------------------------------------------------------------------

# Nuestra función principal, la cual llevara las operaciones cabecillas
def logica_absoluta():

    # Codigo antoguo Vs codigo nuevo y mas seguro
    # recordar_areas = ['superior', 'medio', 'bajo']
    recordar_areas = obtenerKeys(estado_area)
    
    # Codigo antoguo Vs codigo nuevo y mas seguro
    # recordar_estados = obtenerValues(estado_area)
    recordar_estados = [0, 0, 0]
    ejecucion = 1
    
    accionar_area = input("Introduzca el área de inicio :") # El usuario puede ubicar el area por la cual desea empezar con los masajes
    accionar_area = accionar_area.strip() # Quita espacios , para no tener errores a la hora de comparar
    accionar_area = accionar_area.lower() # Vuelve todo en minusculas, para no tener errores a la hora de comparar
    estado_entrada = input(f"Ingrese el estado del area {accionar_area}: ") # El usuario puede ingresar el estado del area por el cual desidio partir 
    
    estado_area[accionar_area] = estado_entrada # Modificamos la infromación en nuestro diccionario de estados
    # print(recordar_areas.index(accionar_area)) # Para saber en que posición se encuentra dicha area en nuestro arreglo

    # Codigo que puede ser mejora con metodos, pero se dejo para usar mas logica interesante
    for area in recordar_areas: # Arreglo con los nombres de nustras areas (superior, medio bajo)
        if area != accionar_area: # Queremos entrar a procesar los estados de los demas estados, sin tomar en cuenta el que escogió el usuario
            complemento_estados = input(f"Ingrese el estado del area '{area}': ") # El usuario puede ingresar ele stado del area por el cual desidio partir 
            estado = recordar_areas.index(area) # Posición en nustro arreglo recordatorio, el caul esta relacionado con nuestra data original
            recordar_estados[estado] = complemento_estados # Con el dato del index, procedemos hacer el cambio en los estados recordatorios 
            
            # Interactuamos con el objeto principal ó importante
            estado_area[area] = complemento_estados
    ejecucion = 0

    # Copiar el objeto inicial ya definido por el usuario
    objeto_inicial = estado_area.copy()
    
    # Estructura ciclica para poder interactuar con el primer area que definio el usuario
    for key in estado_area.keys(): #
        if accionar_area == key: # Encontro esa area
            print(f"La terapia de masajeo iniciara desde el area {key} ") 
            if estado_area.get(key) == '1': # Vereficamos el valor de esa clave "propiedad"
                print(f"La area {key} hace falta masajear")
                estado_area[key] = '0' # masajear el area y declararla como ya tratada '0'
                ejecucion += 1 # Incremento del costo de masaje por area en +1
                print(f"Masajeo en la area {key} del traje táctico")
                print(f"Costo actual de ejecución: {ejecucion}")

                # Llamado importante a nuestra función verificar:Estados --> para manejar los demas areas
                ejecucion += verificar_estados(key, ejecucion)
            elif estado_area.get(key) == '0':
                print(f"La area {key} ya se enceuntra masajeado") # Mensaje informatorio
                # En cualquier caso es necesario interactuar con los demas estados
                ejecucion += verificar_estados(key, ejecucion)

    return {"ejecucion": ejecucion, "objeto_inicial":objeto_inicial} # Retornamos los valores por el tema de encapsulamiento de lo procesado

def verificar_estados(anteriorArea, ejecucion): # El parametro anteriorArea, es para mencionar desde que y hacia donde se va a mover los vibraciones en el traje tactico
    costo = ejecucion # El segundo parametro es para llevar el conteo de una posible ejecución anterior
    guardarArea = anteriorArea

    for area in estado_area: # Recorremos el objeto principal
        time.sleep(4)  # espera 4 segundos // Para permitir un tiempo de interpretación razonable 
        if(area != anteriorArea):
            if estado_area[area] == '1': # Si el estado de esa area esta en "1", se hace el procesonm  para proceder con las vibraciones
                print(f"La area {area} hace falta masajear")
                # masajear el area y declararla como ya tratada '0'
                estado_area[area] = '0'
                costo += 1 # Incremento del costo de masaje por area en +1
                print(f"Del area {guardarArea} los movimientos se trasladan al area {area}")
                print(f"Costo actual de ejecución: {costo}")
            else:
                # Estas líneas son en caso de uqe el area ya se enceuntre masajeada
                print(f'EL area {area} ya se enceuntra masajeada')
                print('No es necesario el conteo ejecución para el coste')
            guardarArea = area # IMportante guardar la ultima harea para poder utilizar nuevametne un mensaje de traslado correcto (visualizar linea 100)
    return costo

# Recordar que devolvemos como resultado algo parecido a un objeto, por ende toca hacer una desestructuración
result = logica_absoluta()
costo_ejecucion = result.get("ejecucion") # Desestructuración
objeto_inicial = result.get("objeto_inicial") # Desestructuración

print(f'El costo de ejecución es de: {costo_ejecucion-1}')
print(f'El estado inicial es: {objeto_inicial}')
print(f'El estado esperado es: {objeto_deseado}')
print(f'El resultado final: {estado_area}')