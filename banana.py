
from grafo import Grafo
			
def leArquivo(nomeArq, valorado):
	arquivo = open(nomeArq)
	tipo = arquivo.readline()

	qtdArestas = 0
	while arquivo.readline():
		qtdArestas += 1

	arquivo.seek(0)
	arquivo.readline()

	aux = []
	lista = []
	if valorado:
		for i in range(qtdArestas):
			aux = arquivo.readline()
			valores = aux.split(" ")
			lista.append(int(valores[0]))
			lista.append(int(valores[1]))
			lista.append(int(valores[2]))
	else:
		for i in range(qtdArestas):
			aux = arquivo.readline()
			valores = aux.split(" ")
			lista.append(int(valores[0]))
			lista.append(int(valores[1]))

	return lista

def imprimeMatrizAdjacencia(matriz):
    print("\nMatriz de Adjacencia: \n")
    for i in range(len(matriz)):
        print(matriz[i])

def imprimeMatrizIncidencia(matriz):
    print("\nMatriz de Incidencia: \n")
    for lin in range(len(matriz)):
        print(matriz[lin])
        
def imprimeListaAdjacencia(lista):
    print("\nLista de Adjacencias: \n")
    for i in range(len(lista)):
        print([i], '->', lista[i])

def main():
	nomeArq = input()
	arquivo = open(nomeArq)
	
	if nomeArq.split('_')[2][:1] == "u":
		valorado = False
	else:
		valorado = True
	
	tipo = arquivo.readline()
	
	qtdArestas = 0
	while arquivo.readline():
		qtdArestas += 1
	
	lista = leArquivo(nomeArq, valorado)
	grafo = Grafo(tipo, valorado, nomeArq, qtdArestas, lista);
	print(grafo.tipo)
	print(grafo.qtdVertices)
	print(grafo.qtdArestas)
	print(grafo.valorado)
	print(grafo.lista)
	#~ imprimeMatrizAdjacencia(grafo.matrizAdjacencia())
	#~ imprimeMatrizIncidencia(grafo.matrizIncidencia())
	imprimeListaAdjacencia(grafo.listaAdjacencia())
	
if __name__ == "__main__":
	main()
