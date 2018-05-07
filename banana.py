
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
	#~ matrizAd = grafo.matrizAdjacencia()
	#~ grafo.imprimeMatrizAdjacencia(matrizAd)
	#~ grafo.convMatAdList(matrizAd)
	#~ grafo.convMatAdMatInc()
	#~ grafo.imprimeMatrizIncidencia(grafo.matrizIncidencia())
	#~ grafo.convMatAdListAd
	#~ grafo.imprimeListaAdjacencia(grafo.listaAdjacencia())
	
	matrizInc = grafo.matrizIncidencia()
	grafo.imprimeMatrizIncidencia(matrizInc)
	# converte matriz de incidencia para lista aux
	#~ grafo.convMatIncList(matrizInc)
	#~ isso = grafo.convMatIncMatAd()
	#~ grafo.imprimeMatrizAdjacencia(isso)
	#~ isso = grafo.convMatIncListAd()
	#~ grafo.imprimeListaAdjacencia(isso)
	
	#~ listaAd = grafo.listaAdjacencia()
	#~ grafo.imprimeListaAdjacencia(listaAd)
	# converte matriz de incidencia para lista aux
	#~ grafo.convListAdList(listaAd)
	#~ isso = grafo.convListAdMatAd()
	#~ grafo.imprimeMatrizAdjacencia(isso)
	#~ isso = grafo.convListAdMatInc()
	#~ grafo.imprimeMatrizIncidencia(isso)
	
	#~ # obtem vertice
	#~ if tipoEstrutura != "L":
		#~ if tipoEstrutura == "A":
			#~ estrutura = convMatAdListAd(estrutura, tipo, valorado)
		#~ elif tipoEstrutura == "I":
			#~ estrutura = convMatIncListAd(estrutura, tipo, valorado)
		#~ tipoEstrutura = "L"
	
	u = int(input("u: "))
	#~ v = int(input("v: "))
	#~ print(grafo.obtemVizinhos(listaAd, u))
	#~ aux = []
	#~ grafo.obtemSuc(matrizInc, u, aux)
	#~ print(aux)
	
	#~ print(grafo.ehVizinho(matrizAd, u, v))
	
	#~ print(grafo.ehPredecessor(matrizInc, u, v))

	#~ print(grafo.ehSucessor(matrizInc, u, v))
	
	matrizInc = grafo.delVertice(matrizInc, u)
	grafo.imprimeMatrizIncidencia(matrizInc)
	
if __name__ == "__main__":
	main()
