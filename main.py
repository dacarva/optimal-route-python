import json
from tkinter import filedialog
from tkinter import *
from collections import deque


root = Tk()


def get_express_trains(express_stations):
    trains = []
    for k, v in express_stations.items():
        for line in v:
            if line not in trains:
                trains.append(line)
    return trains


def bfs(adj, express_stations, s, express_train=None):
    if express_train:
        print('Express train', express_train)

    # Inicializando objetos y cola
    parent = {s: None}
    distances = {s: 0}

    queue = deque()
    queue.append(s)

    while queue:
        # Tomando como referencia la estación de la cola,
        # se verifica si sus hijos ya tienen distancias calculadas
        ref_station = queue.popleft()
        # print('Ref.', ref_station)

        for station in adj[ref_station]:
            # print('Current station =>', station)

            # Check of a neighbor station is express to recalculate

            # Si el nodo ya se analizó continuar
            # De lo contrario calcular el incremento en su distancia
            if station not in distances:
                parent[station] = ref_station
                # Si es un tren expreso no sumar distancia + 1
                distances[station] = distances[ref_station] + 1

                if express_train == None or station not in express_stations:
                    distances[station] = distances[ref_station] + 1

                elif express_train not in express_stations[station]:
                    distances[station] = distances[ref_station] + 1
                else:
                    distances[station] = distances[ref_station]

                queue.append(station)

            # Si el nodo ya se analizó pero sus nodos conexos optimizan las distancias, actualizar su padre
            elif distances[station] > distances[ref_station]:
                distances[station] = distances[ref_station] + 1
                parent[station] = ref_station
            # print('Parent', parent)
            # print('Distance', distances)

    return parent, distances


def get_path(node_a, node_b, adj, express_stations, express_train=None):
    parent, distance = bfs(adj, express_stations, node_a, express_train)
    print('parent', parent)
    print('distance', distance)

    node = node_b
    path = [node]
    # Viajar por los nodos encontrando la distancia más corta según sus padres
    while distance[node] > 0:
        node = parent[node]
        if node not in express_stations or express_train not in express_stations[node]:
            path.append(node)

    return path


if __name__ == '__main__':
    print('¡Hola! Bienvenido al programa de cálculo de rutas óptimas para metro')
    print('Iniciemos.\n Por favor selecciona el archivo JSON que contiene las listas de los vértices y conexiones de las estaciones')

    fileToOpen = filedialog.askopenfilename(
        initialdir="./", title="Selecciona listas de estaciones", filetypes=(("json files", "*.json"), ("all files", "*.*")))

    with open(fileToOpen, 'r') as read_file:
        train_adj = json.load(read_file)

    print('Ahora selecciona el archivo JSON que contiene las listas rutas expresas')

    fileToOpen = filedialog.askopenfilename(
        initialdir="./", title="Selecciona estaciones express", filetypes=(("json files", "*.json"), ("all files", "*.*")))

    with open(fileToOpen, 'r') as read_file:
        express_stations = json.load(read_file)

    node_a = input('Selecciona el punto de partida: ')
    node_b = input('Selecciona el punto de llegada: ')

    wantExpress = None
    express_train = None

    while wantExpress == None:
        wantExpress = input('¿Desea calcular una ruta express (S/N)? ')
        if wantExpress == 'S' or wantExpress == 's':
            selectedTrain = False
            while not selectedTrain:
                express_trains = get_express_trains(express_stations)
                separator = ', '
                express_train = input(
                    '¿Qué ruta expresa desea calcular? Las opciones son: ' + separator.join(express_trains) + ' - ')
                if express_train not in express_trains:
                    print('Corregir su respuesta')
                else:
                    selectedTrain = True
        elif wantExpress == 'N' or wantExpress == 'n':
            express_train = None
        else:
            print('Corregir su respuesta. Parámetros aceptados S y N')
            wantExpress = None

    print('El camino óptimo es: ', get_path(
        node_a, node_b, train_adj, express_stations, express_train))
