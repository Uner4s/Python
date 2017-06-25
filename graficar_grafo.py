import matplotlib.pyplot as plt
import networkx as nx

def leer_grafo_2(G2, archivo):
    for linea in archivo:
        i, j, peso = linea.split()
        G2.add_edge(i, j, weight=int(peso))

def main():
    nombre_archivo = input('Ingrese nombre de archivo a leer: ')
    archivo = open(nombre_archivo)
    archivo.readline()

    # Inicializamos el grafo dirigido G2.
    G2 = nx.DiGraph()

    # Creamos los arcos del grafo G2 a partir del archivo.
    leer_grafo_2(G2, archivo)

    # Generamos la lista de arcos a partir del grafo.
    # Los arcos tendrán la forma (inicio, término)
    arcos = [(ini, ter) for (ini, ter, d) in G2.edges(data=True)]

    # Instrucción para asignar las posiciones
    pos = nx.spring_layout(G2) 

    # 'Dibujamos' los nodos del grafo G2, utilizando las posiciones
    # pos y con 700px de tamaño para cada uno.
    nx.draw_networkx_nodes(G2, pos, node_size = 700)

    # 'Dibujamos' los arcos del grafo G2, utilizando las posiciones
    # pos, sacando la lista de arcos de la variable arcos y con 3px
    # de grosor para cada arco.
    nx.draw_networkx_edges(G2, pos, edgelist = arcos, width=3)

    # 'Dibujamos' las etiquetas del grafo G2, utilizando las posiciones
    # pos, tamaño de fuente 20 y familia de fuente 'sans-serif'.
    nx.draw_networkx_labels(G2, pos, font_size=20, font_family='sans-serif')

    # Exportaremos el grafo al archivo 'grafo.png'.
    plt.savefig('grafo.png')

    # Ahora sí dibujamos el grafo, mostrando todo lo que configuramos
    # previamente y generando el archivo recién indicado.
    plt.show()

if __name__ == '__main__':
    main()
