
arquivo = open("n10_undir_unwgt_comb3.txt")
tipo = arquivo.readline()

qtdArestas = 0
while arquivo.readline():
	qtdArestas += 1

arquivo.seek(0)
arquivo.readline()

oi = []
lista = []
for i in range(qtdArestas):
	oi = arquivo.readline()
	valores = oi.split(" ")
	lista.append(int(valores[0]))
	lista.append(int(valores[1]))

qtdVertices = max(lista) + 1

def MatrizIncidencia(lista):
	matrizIncidencia = [0] * qtdArestas

	for lin in range(qtdArestas):
		matrizIncidencia[lin] = [0] * qtdVertices
		
	for i in range(qtdArestas):
		print(matrizIncidencia[i])

	j = 0
	#~ # direcionado
	if tipo[0] == "D":
		print("grafo direcionado")
		for i in range(qtdArestas):
			a = lista[j]
			b = lista[j + 1]
			matrizIncidencia[i][a] = 1
			matrizIncidencia[i][b] = -1
			j += 2

	#~ # nao-direcionado
	else:
		print("grafo nao-direcionado")
		for i in range(qtdArestas):
			a = lista[j]
			b = lista[j + 1]
			matrizIncidencia[i][a] = 1
			matrizIncidencia[i][b] = 1
			j += 2

	print("\nMatriz de Incidencia: \n")
	for lin in range(qtdArestas):
		print(matrizIncidencia[lin])

def MatrizAdjacencia(lista):
	matrizAdjacencia = [0] * qtdVertices

	for lin in range(qtdVertices):
		matrizAdjacencia[lin] = [0] * qtdVertices

	j = 0
	#~ # direcionado
	if tipo[0] == "D":
		for i in range(qtdArestas):
			a = lista[j]
			b = lista[j + 1]
			matrizAdjacencia[a][b] = 1
			j += 2

	#~ # nao-direcionado
	else:
		for i in range(qtdArestas):
			a = lista[j]
			b = lista[j + 1]
			matrizAdjacencia[a][b] = 1
			matrizAdjacencia[b][a] = 1
			j += 2

	print("\n\nMatriz de Adjacencia: \n")
	for i in range(qtdVertices):
		print(matrizAdjacencia[i])

	print(matrizAdjacencia)

def ListaAdjacencia(lista):
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

	for i in range(qtdVertices):
		print [i], '->' , listaAdjacencia[i]

ListaAdjacencia(lista)
