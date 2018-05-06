
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

def getTipo(nomeArq):
	arquivo = open(nomeArq)
	return arquivo.readline() 
	
def getQtdVertices(lista):
	return max(lista) + 1

def getQtdArestas(lista):
	return len(lista) / 2

# estrutura de dado: lista de adjacencia
def matrizAdjacencia(lista, tipo, valorado):
	qtdVertices = getQtdVertices(lista)
	qtdArestas = getQtdArestas(lista)

	print "TO NA MATRIZ ADJACENCIA"

	j = 0
	if valorado:
		listaAux = []
		aux = 0
		while aux < len(lista):
			listaAux.append(lista[aux])
			listaAux.append(lista[aux + 1])
			aux += 3
		
		qtdVertices = max(listaAux) + 1
		qtdArestas = getQtdArestas(listaAux)
		
		print qtdVertices
		print qtdArestas
		
		matriz = [0] * qtdVertices
		
		for lin in range(qtdVertices):
			matriz[lin] = [0] * qtdVertices
		
		#~ # direcionado
		if tipo[0] == "D":
			for i in range(qtdArestas):
				a = lista[j]
				b = lista[j + 1]
				matriz[a][b] = lista[j + 2]
				j += 3

		#~ # nao-direcionado
		else:
			for i in range(qtdArestas):
				a = lista[j]
				b = lista[j + 1]
				matriz[a][b] = lista[j + 2]
				matriz[b][a] = lista[j + 2]
				j += 3
		
	else:
		matriz = [0] * qtdVertices

		for lin in range(qtdVertices):
			matriz[lin] = [0] * qtdVertices
		#~ # direcionado
		if tipo[0] == "D":
			for i in range(qtdArestas):
				a = lista[j]
				b = lista[j + 1]
				matriz[a][b] = 1
				j += 2

		#~ # nao-direcionado
		else:
			for i in range(qtdArestas):
				a = lista[j]
				b = lista[j + 1]
				matriz[a][b] = 1
				matriz[b][a] = 1
				j += 2
		
	return matriz

# estrutura de dado: matriz de incidencia
def matrizIncidencia(lista, tipo):
	qtdVertices = getQtdVertices(lista)
	qtdArestas = getQtdArestas(lista)
	
	matriz = [0] * qtdArestas

	for lin in range(qtdArestas):
		matriz[lin] = [0] * qtdVertices

	j = 0
	#~ # direcionado
	if tipo[0] == "D":
		for i in range(qtdArestas):
			a = lista[j]
			b = lista[j + 1]
			matriz[i][a] = 1
			matriz[i][b] = -1
			j += 2

	#~ # nao-direcionado
	else:
		for i in range(qtdArestas):
			a = lista[j]
			b = lista[j + 1]
			matriz[i][a] = 1
			matriz[i][b] = 1
			j += 2

	return matriz

# estrutura de dados: lista de adjacencia
def listaAdjacencia(lista, tipo):
	qtdVertices = getQtdVertices(lista)
	qtdArestas = getQtdArestas(lista)
	
	listaAdjacencia = [0] * qtdVertices

	for lin in range(qtdVertices):
		listaAdjacencia[lin] = []

	j = 0
	# direcionado
	if tipo[0] == "D":
		for i in range(qtdArestas):
			a = lista[j]
			b = lista[j + 1]
			listaAdjacencia[a].append(b)
			j += 2
	
	# nao-direcionado
	else:
		for i in range(qtdArestas):
			a = lista[j]
			b = lista[j + 1]
			listaAdjacencia[a].append(b)
			listaAdjacencia[b].append(a)
			j += 2
	
	return listaAdjacencia

def imprimeMatrizAdjacencia(matriz):
	print "\nMatriz de Adjacencia: \n"
	for i in range(len(matriz)):
		print(matriz[i])

def imprimeMatrizIncidencia(matriz):
	print "\nMatriz de Incidencia: \n"
	for lin in range(len(matriz)):
		print(matriz[lin])
		
def imprimeListaAdjacencia(lista):
	print "\nLista de Adjacencias: \n"	
	for i in range(len(lista)):
		print [i], '->', lista[i]

# converte matriz adjacencia para lista auxiliar
def convMatAdList(matriz):
	listaAux = []
	if tipo[0] == "D":
		for lin in range(qtdVertices):
			for col in range(qtdVertices):
				if (matriz[lin][col] == 1):
					listaAux.append(lin)
					listaAux.append(col)
	else:
		for lin in range(qtdVertices):
			for col in range(qtdVertices):
				if (matriz[lin][col] == 1):
					listaAux.append(lin)
					listaAux.append(col)
					matriz[col][lin] = 0
	
	return listaAux

# converte matriz de adjancencia para matriz de incidencia
def convMatAdMatInc(matrizAd):
	return matrizIncidencia(convMatAdList(matrizAd))
	
# converte matriz de adjacencia para lista de adjacencia
def convMatAdListAd(matrizAd):
	return ListaAdjacencia(convMatAdList(matrizAd))


def main():
	nomeArq = raw_input()
	arquivo = open(nomeArq)
	tipo = arquivo.readline()
	valorado = False
	aux = arquivo.readline()
	valor = aux.split(" ")
	if valor[2] != "\n":
		valorado = True
	
	#~ listaAdj = listaAdjacencia(leArquivo(nomeArq), tipo)
	#~ imprimeListaAdjacencia(listaAdj)
	#~ matrizInc = matrizIncidencia(leArquivo(nomeArq), tipo)
	#~ imprimeMatrizIncidencia(matrizInc)
	matrizAd = matrizAdjacencia(leArquivo(nomeArq, valorado), tipo, valorado)
	imprimeMatrizAdjacencia(matrizAd)
	
	
	
	print tipo
	#~ listaAdj = convMatAdListAd(matrizAd)
	#~ imprimeListaAdjacencia(listaAdj)
	

if __name__ == "__main__":
	main()
