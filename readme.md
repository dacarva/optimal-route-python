# Instrucciones para correr este repositorio

## Prerrequisitos:

Usar un compilador de Python versión 3.x. Se recomienda Python 3.7

## Instrucciones

### Archivos de descripción de redes

Las redes se describen a través de un objeto codificado en JSON cuyas llaves son las estaciones de la red y sus valores son listas que incluyen las estaciones que se conectan con éstas.

En este ejemplo, la estación **C** se conecta con las estaciones **B**, **D** y **G**.

```json:
{
    "A": ["B"],
    "B": ["A","C"],
    "C": ["B","D","G"],
    "D": ["C","E"],
    "E": ["D","F"],
    "F": ["E","I"],
    "G": ["C","H"],
    "H": ["G","I"],
    "I": ["H","F"]
}
```

### Archivos de descripción de estaciones exprés

Para describir las estaciones que tienen paradas de trenes exprés, se utiliza un objeto cuyas llaves son las estaciones y sus valores listas de los trenes exprés que no paran en dichas estaciones. En este ejemplo en la estación **H** no para el tren ***Red**

```json:
{
    "G": ["Green"],
    "H": ["Red"],
    "I": ["Green"]
}
```

### Ejecutando el programacion

Correr el archivo en la terminal mediante el comando:

```
python3 main.py
```

El programa lo ayudará a escoger los archivos JSON dentro de su computador, preguntará los nodos de salida y llegada y calculará la ruta óptima.

Para cualquier inquietud puede escribirme a davidfelipec88@gmail.com
