# certo
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

def getQtdArestasValorado(lista):
	listaAux = []
	aux = 0
	while aux < len(lista):
		listaAux.append(lista[aux])
		listaAux.append(lista[aux + 1])
		aux += 3

	return getQtdArestas(listaAux)

def getQtdVerticesValorado(lista):
	listaAux = []
	aux = 0
	while aux < len(lista):
		listaAux.append(lista[aux])
		listaAux.append(lista[aux + 1])
		aux += 3
	
	return max(listaAux) + 1

# estrutura de dado: lista de adjacencia
def matrizAdjacencia(lista, tipo, valorado):
	j = 0
	if valorado:
		qtdVertices = getQtdVerticesValorado(lista)
		qtdArestas = getQtdArestasValorado(lista)
		
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
		qtdVertices = getQtdVertices(lista)
		qtdArestas = getQtdArestas(lista)
		
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
def matrizIncidencia(lista, tipo, valorado):
	qtdVertices = getQtdVertices(lista)
	qtdArestas = getQtdArestas(lista)
	
	j = 0
	if valorado:
		qtdVertices = getQtdVerticesValorado(lista)
		qtdArestas = getQtdArestasValorado(lista)
		
		matriz = [0] * qtdArestas

		for lin in range(qtdArestas):
			matriz[lin] = [0] * qtdVertices
			
		#~ # direcionado
		if tipo[0] == "D":
			for i in range(qtdArestas):
				a = lista[j]
				b = lista[j + 1]
				matriz[i][a] = lista[j + 2]
				matriz[i][b] = -lista[j + 2]
				j += 3

		#~ # nao-direcionado
		else:
			for i in range(qtdArestas):
				a = lista[j]
				b = lista[j + 1]
				matriz[i][a] = lista[j + 2]
				matriz[i][b] = lista[j + 2]
				j += 3
	else:
		matriz = [0] * qtdArestas

		for lin in range(qtdArestas):
			matriz[lin] = [0] * qtdVertices

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
def listaAdjacencia(lista, tipo, valorado):
	qtdVertices = getQtdVertices(lista)
	qtdArestas = getQtdArestas(lista)
	
	if valorado:
		qtdVertices = getQtdVerticesValorado(lista)
		qtdArestas = getQtdArestasValorado(lista)
		
		listaAdjacencia = [0] * qtdVertices

		for lin in range(qtdVertices):
			listaAdjacencia[lin] = []
				
		j = 0
		# direcionado
		if tipo[0] == "D":
			for i in range(qtdArestas):
				a = lista[j]
				b = lista[j + 1]
				listaAdjacencia[a].append([b, lista[j + 2]])
				#~ listaAdjacencia[a][1].append(lista[j + 2])
				j += 3
		
		# nao-direcionado
		else:
			for i in range(qtdArestas):
				a = lista[j]
				b = lista[j + 1]
				listaAdjacencia[a].append([b, lista[j + 2]])
				listaAdjacencia[b].append([a, lista[j + 2]])
				j += 3

	else:
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
def convMatAdList(matriz, tipo, valorado):
	qtdVertices = len(matriz)
	qtdArestas = len(matriz)
	listaAux = []
	if valorado:
		if tipo[0] == "D":
			for lin in range(qtdVertices):
				for col in range(qtdVertices):
					if (matriz[lin][col] != 0):
						listaAux.append(lin)
						listaAux.append(col)
						listaAux.append(matriz[lin][col])
		else:
			for lin in range(qtdVertices):
				for col in range(qtdVertices):
					if (matriz[lin][col] != 0):
						listaAux.append(lin)
						listaAux.append(col)
						listaAux.append(matriz[lin][col])
						matriz[col][lin] = 0
	else:
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
def convMatAdMatInc(matrizAd, tipo, valorado):
	return matrizIncidencia(convMatAdList(matrizAd, tipo, valorado), tipo, valorado)
	
# converte matriz de adjacencia para lista de adjacencia
def convMatAdListAd(matrizAd, tipo, valorado):
	return listaAdjacencia(convMatAdList(matrizAd, tipo, valorado), tipo, valorado)

# converte matriz de incidencia para lista auxiliar
def convMatIncList(matriz, tipo, valorado):
	qtdVertices = len(matriz[0])
	qtdArestas = len(matriz)
	listaAux = []
	if valorado:
		if tipo[0] == "D":
			for lin in range(qtdArestas):
				for col in range(qtdVertices):
					if (matriz[lin][col] > 0):
						a = col
					elif (matriz[lin][col] < 0):
						b = col
				listaAux.append(a)
				listaAux.append(b)
				listaAux.append(matriz[lin][a])
		else:
			for lin in range(qtdArestas):
				for col in range(qtdVertices):
					if (matriz[lin][col] > 0):
						listaAux.append(col)
						valor = matriz[lin][col]
				listaAux.append(valor)
	else:
		if tipo[0] == "D":
			for lin in range(qtdArestas):
				for col in range(qtdVertices):
					if (matriz[lin][col] == 1):
						a = col
					elif (matriz[lin][col] == -1):
						b = col
				listaAux.append(a)
				listaAux.append(b)
		else:
			for lin in range(qtdArestas):
				for col in range(qtdVertices):
					if (matriz[lin][col] == 1):
						listaAux.append(col)
	
	return listaAux

# converte matriz de incidencia para matriz de adjancencia
def convMatIncMatAd(matrizAd, tipo, valorado):
	return matrizAdjacencia(convMatIncList(matrizAd, tipo, valorado), tipo, valorado)
	
# converte matriz de incidencia para lista de adjancencia
def convMatIncListAd(matrizAd, tipo, valorado):
	return listaAdjacencia(convMatIncList(matrizAd, tipo, valorado), tipo, valorado)

# converte lista de adjacencia para lista auxiliar
def convListAdList(lista, tipo, valorado):
	qtdVertices = len(lista)
	listaAux = []
	if valorado:
		if tipo[0] == "D":
			for i in range(qtdVertices):
				qtdArestas = len(lista[i])
				for j in range(qtdArestas):
					listaAux.append(i)
					listaAux.append(lista[i][j][0])
					listaAux.append(lista[i][j][1])

		else:
			for i in range(qtdVertices):
				qtdArestas = len(lista[i])
				for j in range(qtdArestas):
					if lista[i][j] != -1:
						listaAux.append(i)
						listaAux.append(lista[i][j][0])
						listaAux.append(lista[i][j][1])
						del lista[lista[i][j][0]][0]
						
	else:
		if tipo[0] == "D":
			for i in range(qtdVertices):
				qtdArestas = len(lista[i])
				for j in range(qtdArestas):
					listaAux.append(i)
					listaAux.append(lista[i][j])
		else:
			for i in range(qtdVertices):
				qtdArestas = len(lista[i])
				if qtdArestas > 0:
					for j in range(qtdArestas):
						listaAux.append(i)
						listaAux.append(lista[i][j])
						del lista[lista[i][j]][0]	
	return listaAux

# converte lista de adjacencia para matriz de adjancencia
def convListAdMatAd(lista, tipo, valorado):
	return matrizAdjacencia(convListAdList(lista, tipo, valorado), tipo, valorado)
	
# converte lista de adjancencia para matriz de incidencia
def convListAdMatInc(lista, tipo, valorado):
	return matrizIncidencia(convListAdList(lista, tipo, valorado), tipo, valorado)



# obtem vizinho
def obtemVizinhos(estrutura, vertice, valorado):
	conjuntoVizinhos = []
	if valorado:
		for i in range(len(estrutura[vertice])):
			conjuntoVizinhos.append(estrutura[vertice][i][0])
		return conjuntoVizinhos
	return estrutura[vertice]

# obtem pred
def obtemPred(estrutura, vertice, aux):
	qtdVertices = len(estrutura[0])
	qtdArestas = len(estrutura)
	for i in range(qtdArestas):
		if estrutura[i][vertice] < 0:
			for j in range(qtdVertices):
				if estrutura[i][j] > 0:
					jaExiste = False
					if any(k == j for k in aux):
						jaExiste = True
					if not(jaExiste):
						aux.append(j)
						obtemPred(estrutura, j, aux)
	return aux
					
		
		

def main():
	nomeArq = raw_input()
	arquivo = open(nomeArq)
	tipo = arquivo.readline()
	valorado = False
	aux = arquivo.readline()
	valor = aux.split(" ")
	if valor[2] != "\n":
		valorado = True
	
	
	# matriz adjancencia = A
	# matriz incidencia = I
	# lista adjacencia = L
	tipoEstrutura = raw_input("Tipo de estrutura: ")
	
	if tipoEstrutura == "A":
		estrutura = matrizAdjacencia(leArquivo(nomeArq, valorado), tipo, valorado)
		imprimeMatrizAdjacencia(estrutura)
	elif tipoEstrutura == "I":
		estrutura = matrizIncidencia(leArquivo(nomeArq, valorado), tipo, valorado)
		imprimeMatrizIncidencia(estrutura)
	elif tipoEstrutura == "L":
		estrutura = listaAdjacencia(leArquivo(nomeArq, valorado), tipo, valorado)
		imprimeListaAdjacencia(estrutura)
	
	# obtem vertice
	#~ if tipoEstrutura != "L":
		#~ if tipoEstrutura == "A":
			#~ estrutura = convMatAdListAd(estrutura, tipo, valorado)
		#~ elif tipoEstrutura == "I":
			#~ estrutura = convMatIncListAd(estrutura, tipo, valorado)
		#~ tipoEstrutura = "L"
	
	#~ vertice = input("Vertice: ")
	#~ print obtemVizinhos(estrutura, vertice, valorado)
	
	# obtem predecessor
	if tipoEstrutura != "I":
		if tipoEstrutura == "A":
			estrutura = convMatAdMatInc(estrutura, tipo, valorado)
		elif tipoEstrutura == "I":
			estrutura = convListAdMatInc(estrutura, tipo, valorado)
		tipoEstrutura = "I"
	
	vertice = input("Vertice: ")
	aux = []
	print obtemPred(estrutura, vertice, aux)
	
	
	#~ convListAdMatAd(listaAdj, tipo, valorado)
	#~ imprimeMatrizAdjacencia(convListAdMatAd(listaAdj, tipo, valorado))
	#~ matAd = convListAdMatAd(listaAdj, tipo, valorado)
	#~ print matAd
	#~ imprimeMatrizAdjacencia(matAd)
	#~ lis = convMatAdListAd(matAd, tipo, valorado)
	#~ imprimeListaAdjacencia(lis)
	#~ matInc = convMatAdMatInc(matAd, tipo, valorado)
	#~ imprimeMatrizIncidencia(matInc)
	
	#~ print "lista"
	#~ imprimeListaAdjacencia(convMatIncListAd(matrizInc, tipo, valorado))
	#~ print "matriz"
	#~ imprimeMatrizAdjacencia(convMatIncMatAd(matrizInc, tipo, valorado))
	

if __name__ == "__main__":
	main()
