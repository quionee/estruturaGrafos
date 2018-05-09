
class Grafo:
	# construtor
	def __init__(self, tipo, valorado, nomeArq, qtdArestas, lista, tipoEstrutura):
		self.tipo = tipo[0]
		self.valorado = valorado
		self.qtdVertices = int(nomeArq.split('_')[0][1:])
		self.qtdArestas = qtdArestas
		self.lista = lista
		self.tipoEstrutura = tipoEstrutura
		
	# estrutura de dado: matriz de adjacencia
	def matrizAdjacencia(self):
		j = 0
		if self.valorado:
			matriz = [0] * self.qtdVertices
			
			for lin in range(self.qtdVertices):
				matriz[lin] = [0] * self.qtdVertices
			
			#~ # direcionado
			if self.tipo == "D":
				for i in range(self.qtdArestas):
					a = self.lista[j]
					b = self.lista[j + 1]
					matriz[a][b] = self.lista[j + 2]
					j += 3

			#~ # nao-direcionado
			else:
				for i in range(self.qtdArestas):
					a = self.lista[j]
					b = self.lista[j + 1]
					matriz[a][b] = self.lista[j + 2]
					matriz[b][a] = self.lista[j + 2]
					j += 3
			
		else:
			matriz = [0] * self.qtdVertices

			for lin in range(self.qtdVertices):
				matriz[lin] = [0] * self.qtdVertices
			#~ # direcionado
			if self.tipo == "D":
				for i in range(self.qtdArestas):
					a = self.lista[j]
					b = self.lista[j + 1]
					matriz[a][b] = 1
					j += 2

			#~ # nao-direcionado
			else:
				for i in range(self.qtdArestas):
					a = self.lista[j]
					b = self.lista[j + 1]
					matriz[a][b] = 1
					matriz[b][a] = 1
					j += 2
			
		return matriz
		
	# estrutura de dado: matriz de incidencia
	def matrizIncidencia(self):
		j = 0
		if self.valorado:
			matriz = [0] * self.qtdArestas

			for lin in range(self.qtdArestas):
				matriz[lin] = [0] * self.qtdVertices
				
			#~ # direcionado
			if self.tipo == "D":
				for i in range(self.qtdArestas):
					a = self.lista[j]
					b = self.lista[j + 1]
					if a == b:
						matriz[i][a] = self.lista[j + 2] * 2
					else:
						matriz[i][a] = self.lista[j + 2]
						matriz[i][b] = -self.lista[j + 2]
					j += 3

			#~ # nao-direcionado
			else:
				for i in range(self.qtdArestas):
					a = self.lista[j]
					b = self.lista[j + 1]
					if a == b:
						matriz[i][a] = self.lista[j + 2] * 2
					else:
						matriz[i][a] = self.lista[j + 2]
						matriz[i][b] = self.lista[j + 2]
					j += 3
		else:
			matriz = [0] * self.qtdArestas

			for lin in range(self.qtdArestas):
				matriz[lin] = [0] * self.qtdVertices

			#~ # direcionado
			if self.tipo == "D":
				for i in range(self.qtdArestas):
					a = self.lista[j]
					b = self.lista[j + 1]
					if a == b:
						matriz[i][a] = 2
					else:
						matriz[i][a] = 1
						matriz[i][b] = -1
					j += 2

			#~ # nao-direcionado
			else:
				for i in range(self.qtdArestas):
					a = self.lista[j]
					b = self.lista[j + 1]
					if a == b:
						matriz[i][a] = 2
					else:
						matriz[i][a] = 1
						matriz[i][b] = 1
					j += 2

		return matriz
		
	# estrutura de dados: lista de adjacencia
	def listaAdjacencia(self):
		if self.valorado:
			listaAdjacencia = [0] * self.qtdVertices

			for lin in range(self.qtdVertices):
				listaAdjacencia[lin] = []
					
			j = 0
			# direcionado
			if self.tipo == "D":
				for i in range(self.qtdArestas):
					a = self.lista[j]
					b = self.lista[j + 1]
					listaAdjacencia[a].append([b, self.lista[j + 2]])
					j += 3
			
			# nao-direcionado
			else:
				for i in range(self.qtdArestas):
					a = self.lista[j]
					b = self.lista[j + 1]
					listaAdjacencia[a].append([b, self.lista[j + 2]])
					listaAdjacencia[b].append([a, self.lista[j + 2]])
					j += 3

		else:
			listaAdjacencia = [0] * self.qtdVertices

			for lin in range(self.qtdVertices):
				listaAdjacencia[lin] = []

			j = 0
			# direcionado
			if self.tipo == "D":
				for i in range(self.qtdArestas):
					a = self.lista[j]
					b = self.lista[j + 1]
					listaAdjacencia[a].append(b)
					j += 2
			
			# nao-direcionado
			else:
				for i in range(self.qtdArestas):
					a = self.lista[j]
					b = self.lista[j + 1]
					listaAdjacencia[a].append(b)
					listaAdjacencia[b].append(a)
					j += 2
		
		return listaAdjacencia
		
	def imprimeMatrizAdjacencia(self, matriz):
		print("\nMatriz de Adjacencia: \n")
		for i in range(len(matriz)):
			print(matriz[i])

	def imprimeMatrizIncidencia(self, matriz):
		print("\nMatriz de Incidencia: \n")
		for lin in range(self.qtdArestas):
			print(matriz[lin])
			
	def imprimeListaAdjacencia(self, lista):
		print("\nLista de Adjacencias: \n")
		for i in range(len(lista)):
			print([i], "->", lista[i])

	# converte matriz adjacencia para lista auxiliar
	def convMatAdList(self, matriz):
		listaAux = []
		if self.valorado:
			if self.tipo == "D":
				for lin in range(self.qtdVertices):
					for col in range(self.qtdVertices):
						if (matriz[lin][col] != 0):
							listaAux.append(lin)
							listaAux.append(col)
							listaAux.append(matriz[lin][col])
			else:
				for lin in range(self.qtdVertices):
					for col in range(self.qtdVertices):
						if (matriz[lin][col] != 0):
							listaAux.append(lin)
							listaAux.append(col)
							listaAux.append(matriz[lin][col])
							matriz[col][lin] = 0
		else:
			if self.tipo == "D":
				for lin in range(self.qtdVertices):
					for col in range(self.qtdVertices):
						if (matriz[lin][col] == 1):
							listaAux.append(lin)
							listaAux.append(col)
			else:
				for lin in range(self.qtdVertices):
					for col in range(self.qtdVertices):
						if (matriz[lin][col] == 1):
							listaAux.append(lin)
							listaAux.append(col)
							matriz[col][lin] = 0
		self.lista = listaAux
		
	# converte matriz de incidencia para lista auxiliar
	def convMatIncList(self, matriz):
		listaAux = []
		if self.valorado:
			if self.tipo == "D":
				for lin in range(self.qtdArestas):
					for col in range(self.qtdVertices):
						if (matriz[lin][col] > 0):
							a = col
						elif (matriz[lin][col] < 0):
							b = col
					listaAux.append(a)
					listaAux.append(b)
					listaAux.append(matriz[lin][a])
			else:
				for lin in range(self.qtdArestas):
					for col in range(self.qtdVertices):
						if (matriz[lin][col] > 0):
							listaAux.append(col)
							valor = matriz[lin][col]
					listaAux.append(valor)
		else:
			if self.tipo == "D":
				for lin in range(self.qtdArestas):
					for col in range(self.qtdVertices):
						if (matriz[lin][col] == 1):
							a = col
						elif (matriz[lin][col] == -1):
							b = col
					listaAux.append(a)
					listaAux.append(b)
			else:
				for lin in range(self.qtdArestas):
					for col in range(self.qtdVertices):
						if (matriz[lin][col] == 1):
							listaAux.append(col)
		
		self.lista = listaAux
		
	# converte lista de adjacencia para lista auxiliar
	def convListAdList(self, lista):
		listaAux = []
		if self.valorado:
			if self.tipo == "D":
				for i in range(self.qtdVertices):
					qtdArestasAtual = len(lista[i])
					for j in range(qtdArestasAtual):
						listaAux.append(i)
						listaAux.append(lista[i][j][0])
						listaAux.append(lista[i][j][1])

			else:
				for i in range(self.qtdVertices):
					qtdArestasAtual = len(lista[i])
					for j in range(qtdArestasAtual):
						if lista[i][j] != -1:
							listaAux.append(i)
							listaAux.append(lista[i][j][0])
							listaAux.append(lista[i][j][1])
							del lista[lista[i][j][0]][0]
							
		else:
			if self.tipo == "D":
				for i in range(self.qtdVertices):
					qtdArestasAtual = len(lista[i])
					for j in range(qtdArestasAtual):
						listaAux.append(i)
						listaAux.append(lista[i][j])
			else:
				for i in range(qtdVertices):
					qtdArestasAtual = len(lista[i])
					if qtdArestas > 0:
						for j in range(qtdArestasAtual):
							listaAux.append(i)
							listaAux.append(lista[i][j])
							del lista[lista[i][j]][0]   
		self.lista = listaAux

	def convParaListaAd(self, estrutura):
		if self.tipoEstrutura != "L":
			if self.tipoEstrutura == "A":
				self.convMatAdList(estrutura)
			elif self.tipoEstrutura == "I":
				self.convMatIncList(estrutura)
			estrutura = self.listaAdjacencia()
			self.tipoEstrutura = "L"
		return estrutura
		
	def convParaMatInc(self, estrutura):
		if self.tipoEstrutura != "I":
			if self.tipoEstrutura == "A":
				self.convMatAdList(estrutura)
			elif self.tipoEstrutura == "L":
				self.convListAdList(estrutura)
			estrutura = self.matrizIncidencia()
			self.tipoEstrutura = "I"
		return estrutura
	
	def convParaMatAd(self, estrutura):
		if self.tipoEstrutura != "A":
			if self.tipoEstrutura == "I":
				self.convMatIncList(estrutura)
			elif self.tipoEstrutura == "L":
				self.convListAdList(estrutura)
			estrutura = self.matrizAdjacencia()
			self.tipoEstrutura = "A"
		return estrutura
		
	# obtem vizinhos
	def obtemVizinhos(self, estrutura, u):
		conjuntoVizinhos = []
		if self.tipoEstrutura == "L":
			if self.valorado:
				for i in range(len(estrutura[u])):
					conjuntoVizinhos.append(estrutura[u][i][0])
				print(conjuntoVizinhos)
			else:
				print(estrutura[u])
		elif self.tipoEstrutura == "A":
			for i in range(self.qtdVertices):
				if estrutura[u][i] != 0:
					conjuntoVizinhos.append(i)
			print(conjuntoVizinhos)
		else:
			for i in range(self.qtdArestas):
				if estrutura[i][u] > 0:
					for j in range(self.qtdVertices):
						if estrutura[i][j] < 0:
							conjuntoVizinhos.append(j)
			print(conjuntoVizinhos)

	# obtem predecessores
	def obtemPred(self, estrutura, u, aux):
		if self.tipoEstrutura == "I":
			for i in range(self.qtdArestas):
				if estrutura[i][u] < 0 or estrutura[i].count(0) == self.qtdVertices - 1:
					for j in range(self.qtdVertices):
						if estrutura[i][j] > 0:
							jaExiste = False
							if any(k == j for k in aux):
								jaExiste = True
							if not(jaExiste):
								aux.append(j)
								self.obtemPred(estrutura, j, aux)
		elif self.tipoEstrutura == "A":
			for i in range(self.qtdVertices):
				if estrutura[i][u] != 0:
					jaExiste = False
					if any(k == i for k in aux):
						jaExiste = True
					if not(jaExiste):
						aux.append(i)
						self.obtemPred(estrutura, i, aux)
		else:
			if self.valorado:
				for i in range(self.qtdVertices):
					for j in range(len(estrutura[i])):
						if estrutura[i][j][0] == u:
							jaExiste = False
							if any(k == i for k in aux):
								jaExiste = True
							if not(jaExiste):
								aux.append(i)
								self.obtemPred(estrutura, i, aux)
			else:
				for i in range(self.qtdVertices):
					for j in range(len(estrutura[i])):
						if estrutura[i][j] == u:
							jaExiste = False
							if any(k == i for k in aux):
								jaExiste = True
							if not(jaExiste):
								aux.append(i)
								self.obtemPred(estrutura, i, aux)
		return aux

	# obtem sucessores utilizando matriz de incidencia
	def obtemSuc(self, estrutura, u, aux):
		if self.tipoEstrutura == "I":
			for i in range(self.qtdArestas):
				if estrutura[i][u] > 0:
					if estrutura[i].count(0) == self.qtdVertices - 1:
						jaExiste = False
						if any(k == u for k in aux):
							jaExiste = True
						if not(jaExiste):
							aux.append(u)
					else:
						for j in range(self.qtdVertices):
							if estrutura[i][j] < 0:
								jaExiste = False
								if any(k == j for k in aux):
									jaExiste = True
								if not(jaExiste):
									aux.append(j)
									self.obtemSuc(estrutura, j, aux)
		if self.tipoEstrutura == "A":
			if estrutura[u].count(0) == self.qtdVertices - 1:
				jaExiste = False
				if any(k == u for k in aux):
					jaExiste = True
				if not(jaExiste):
					aux.append(u)
			else:
				for i in range(self.qtdVertices):
					if estrutura[u][i] != 0:
						jaExiste = False
						if any(k == i for k in aux):
							jaExiste = True
						if not(jaExiste):
							aux.append(i)
							self.obtemSuc(estrutura, i, aux)
		else:
			if self.valorado:
				for i in range(len(estrutura[u])):
					jaExiste = False
					if any(k == estrutura[u][i][0] for k in aux):
						jaExiste = True
					if not(jaExiste):
						aux.append(estrutura[u][i][0])
						self.obtemSuc(estrutura, estrutura[u][i][0], aux)
			else:
				for i in range(len(estrutura[u])):
					jaExiste = False
					if any(k == estrutura[u][i] for k in aux):
						jaExiste = True
					if not(jaExiste):
						aux.append(estrutura[u][i])
						self.obtemSuc(estrutura, estrutura[u][i], aux)
		return aux

	# verifica se u e v sao vizinhos
	def ehVizinho(self, matriz, u, v):
		ehViz = False
		if matriz[u][v] != 0 or matriz[v][u] != 0:
			ehViz = True
		return ehViz
	
	# verifica se v eh predecessor de u utilizando obtemPred
	def ehPredecessor(self, matriz, u, v):
		lisAux = []
		lisAux = self.obtemPred(matriz, u, lisAux)
		ehPred = False
		if any(i == v for i in lisAux):
			ehPred = True
		return ehPred

	# verifica se v eh sucessor de u utilizando obtemSuc
	def ehSucessor(self, matriz, u, v):
		lisAux = []
		lisAux = self.obtemSuc(matriz, u, lisAux)
		ehSuc = False
		if any(i == v for i in lisAux):
			ehSuc = True
		return ehSuc

	# deleta vertices e as arestas adjacentes a ele utilizando matriz de incidencia
	def delVertice(self, matriz, u):
		i = 0
		while i < self.qtdArestas:
			if matriz[i][u] != 0:
				del matriz[i]
				self.qtdArestas = self.qtdArestas - 1
			else:
				del matriz[i][u]
				i += 1
		self.qtdVertices = self.qtdVertices - 1
		return matriz

	# deleta aresta e todos vertices adjacentes a ele
	def delAresta(self, matriz, u, v):
		i = 0
		encontrou = False
		if self.tipo == "D":
			while i < self.qtdArestas and not(encontrou):
				if matriz[i][u] > 0 and matriz[i][v] < 0:
					del matriz[i]
					self.qtdArestas = self.qtdArestas - 1
					encontrou = True
				i += 1
		else:
			while i < self.qtdArestas and not(encontrou):
				if matriz[i][u] != 0 and matriz[i][v] != 0:
					del matriz[i]
					self.qtdArestas = self.qtdArestas - 1
					encontrou = True
				i += 1
		return matriz

	# gera subgrafo induzido por vertices
	def geraSubgrafoIV(self, matriz, lista):
		tamLista = len(lista)
		for i in range(tamLista):
			self.delVertice(matriz, lista[i])
		
		return matriz
		
	# gera subgrafo induzido por arestas
	def geraSubgrafoIA(self, matriz, lista):
		tamLista = len(lista)
		for i in range(tamLista):
			self.delAresta(matriz, lista[i][0], lista[i][1])
		i = 0
		while i < self.qtdVertices:
			cont = 0
			for j in range(self.qtdArestas):
				if matriz[j][i] == 0:
					cont += 1
			if cont == self.qtdArestas:
				for k in range(self.qtdArestas):
					del matriz[k][i]
				self.qtdVertices -= 1
			i += 1
		return matriz
