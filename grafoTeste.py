
class Grafo:
	# construtor
	def __init__(self, tipo, valorado, nomeArq, qtdArestas, lista, tipoEstrutura):
		self.tipo = tipo[0]
		self.valorado = valorado
		self.qtdVertices = int(nomeArq.split('_')[0][1:])
		self.qtdArestas = qtdArestas
		self.lista = lista
		self.tipoEstrutura = tipoEstrutura
		self.listaDeVertices = [0] * self.qtdVertices
		for i in range(self.qtdVertices):
			self.listaDeVertices[i] = i
		
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
			print(lin, matriz[lin])
			
	def imprimeListaAdjacencia(self, lista):
		print("\nLista de Adjacencias: \n")
		for i in range(len(lista)):
			print(self.listaDeVertices[i], "->", lista[i])
			
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
					valor = self.listaDeVertices[i]
					conjuntoVizinhos.append(valor)
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
							valor = self.listaDeVertices[j]
							if any(k == valor for k in aux):
								jaExiste = True
							if not(jaExiste):
								aux.append(valor)
								self.obtemPred(estrutura, j, aux)
		elif self.tipoEstrutura == "A":
			for i in range(self.qtdVertices):
				if estrutura[i][u] != 0:
					jaExiste = False
					valor = self.listaDeVertices[i]
					if any(k == valor for k in aux):
						jaExiste = True
					if not(jaExiste):
						aux.append(valor)
						self.obtemPred(estrutura, i, aux)
		else:
			if self.valorado:
				for i in range(self.qtdVertices):
					for j in range(len(estrutura[i])):
						if estrutura[i][j][0] == u:
							valor = self.listaDeVertices[i]
							jaExiste = False
							if any(k == valor for k in aux):
								jaExiste = True
							if not(jaExiste):
								aux.append(valor)
								self.obtemPred(estrutura, i, aux)
			else:
				for i in range(self.qtdVertices):
					for j in range(len(estrutura[i])):
						if estrutura[i][j] == u:
							valor = self.listaDeVertices[i]
							jaExiste = False
							if any(k == valor for k in aux):
								jaExiste = True
							if not(jaExiste):
								aux.append(valor)
								self.obtemPred(estrutura, i, aux)
		return aux

	# obtem sucessores utilizando matriz de incidencia
	def obtemSuc(self, estrutura, u, aux):
		if self.tipoEstrutura == "I":
			for i in range(self.qtdArestas):
				if estrutura[i][u] > 0:
					for j in range(self.qtdVertices):
						if estrutura[i][j] < 0:
							jaExiste = False
							valor = self.listaDeVertices[j]
							if any(k == valor for k in aux):
								jaExiste = True
							if not(jaExiste):
								aux.append(valor)
								self.obtemSuc(estrutura, j, aux)
		elif self.tipoEstrutura == "A":
			for i in range(self.qtdVertices):
				if estrutura[u][i] != 0:
					jaExiste = False
					valor = self.listaDeVertices[i]
					if any(k == valor for k in aux):
						jaExiste = True
					if not(jaExiste):
						aux.append(valor)
						self.obtemSuc(estrutura, i, aux)
		else:
			if self.valorado:
				x = u
				for i in range(len(estrutura[u])):
					u = self.verificaU(estrutura[x][i][0])
					jaExiste = False
					if any(k == estrutura[x][i][0] for k in aux):
						jaExiste = True
					if not(jaExiste):
						aux.append(estrutura[x][i][0])
						self.obtemSuc(estrutura, u, aux)
			else:
				x = u
				for i in range(len(estrutura[u])):
					u = self.verificaU(estrutura[x][i])
					jaExiste = False
					if any(k == estrutura[x][i] for k in aux):
						jaExiste = True
					if not(jaExiste):
						aux.append(estrutura[x][i])
						self.obtemSuc(estrutura, u, aux)
		return aux

	# verifica se u e v sao vizinhos
	def ehVizinho(self, estrutura, u, v):
		ehViz = False
		if self.tipoEstrutura == "A":
			v = verificaU(v)
			if self.tipo == "D":
				if estrutura[u][v] != 0:
					ehViz = True
			else:
				if estrutura[u][v] != 0 or estrutura[v][u] != 0:
					ehViz = True
		elif self.tipoEstrutura == "I":
			listaAux = self.obtemVizinhos(estrutura,u)
			for i in range(len(listaAux)):
				if listaAux[i] == v:
					ehviz = True
		return ehViz
	
	# verifica se v eh predecessor de u utilizando obtemPred
	def ehPredecessor(self, estrutura, u, v):
		lisAux = []
		lisAux = self.obtemPred(estrutura, u, lisAux)
		ehPred = False
		if any(i == v for i in lisAux):
			ehPred = True
		return ehPred

	# verifica se v eh sucessor de u utilizando obtemSuc
	def ehSucessor(self, estrutura, u, v):
		lisAux = []
		lisAux = self.obtemSuc(estrutura, u, lisAux)
		ehSuc = False
		if any(i == v for i in lisAux):
			ehSuc = True
		return ehSuc

	# deleta vertices e as arestas adjacentes a ele utilizando matriz de incidencia
	def delVertice(self, estrutura, u):
		print("u: ", u)
		if self.tipoEstrutura == "I":
			i = 0
			while i < self.qtdArestas:
				if estrutura[i][u] != 0:
					del estrutura[i]
					self.qtdArestas = self.qtdArestas - 1
				else:
					del estrutura[i][u]
					i += 1
			self.qtdVertices = self.qtdVertices - 1
		elif self.tipoEstrutura == "A":
			cont = 0
			for i in range(self.qtdVertices):
				if estrutura[i][u] != 0:
					cont += 1
				del estrutura[i][u]
			del estrutura[u]
			self.qtdVertices -= 1
			self.qtdArestas -= cont
		else:
			del estrutura[u]
			self.qtdVertices -= 1
			if self.valorado:
				for i in range(self.qtdVertices):
					j = 0
					while j < len(estrutura[i]):
						if estrutura[i][j][0] == self.listaDeVertices[u]:
							del estrutura[i][j]
							self.qtdArestas -= 1
						j += 1
			else:
				for i in range(self.qtdVertices):
					j = 0
					while j < len(estrutura[i]):
						if estrutura[i][j] == self.listaDeVertices[u]:
							del estrutura[i][j]
						j += 1
		del self.listaDeVertices[u]
		return estrutura

	# deleta aresta e todos vertices adjacentes a ele
	def delAresta(self, estrutura, u, v):
		encontrou = False
		if self.tipoEstrutura == "I":
			i = 0
			if self.tipo == "D":
				while i < self.qtdArestas and not(encontrou):
					if estrutura[i][u] > 0 and estrutura[i][v] < 0:
						del estrutura[i]
						self.qtdArestas = self.qtdArestas - 1
						encontrou = True
					i += 1
				if not(encontrou):
					print("\nAresta invalida\n'''''")
			else:
				while i < self.qtdArestas and not(encontrou):
					if estrutura[i][u] != 0 and estrutura[i][v] != 0:
						del estrutura[i]
						self.qtdArestas = self.qtdArestas - 1
						encontrou = True
					i += 1
		elif self.tipoEstrutura == "A":
			if self.tipo == "D":
				if estrutura[u][v] == 0:
					print("\nAresta invalida\n")
				else:
					estrutura[u][v] = 0
			else:
				estrutura[u][v] = 0
				estrutura[v][u] = 0
			self.qtdArestas -= 1
		else:
			j = 0
			if self.tipo == "D":
				if self.valorado:
					while j < len(estrutura[u]) and not(encontrou):
						if estrutura[u][j][0] == v:
							del estrutura[u][j]
							encontrou = True
						j += 1
				else:
					while j < len(estrutura[u]) and not(encontrou):
						if estrutura[u][j] == v:
							del estrutura[u][j]
							encontrou = True
						j += 1
			else:
				if self.valorado:
					while j < len(estrutura[u]) and not(encontrou):
						if estrutura[u][j][0] == v:
							del estrutura[u][j]
							encontrou = True
						j += 1
					j = 0
					while j < len(estrutura[v]) and not(encontrou):
						if estrutura[v][j][0] == u:
							del estrutura[v][j]
							encontrou = True
						j += 1
				else:
					while j < len(estrutura[u]) and not(encontrou):
						if estrutura[u][j] == v:
							del estrutura[u][j]
							encontrou = True
						j += 1
					j = 0
					while j < len(estrutura[v]) and not(encontrou):
						if estrutura[v][j] == v:
							del estrutura[v][j]
							encontrou = True
						j += 1
		self.qtdArestas -= 1
		return estrutura

	# gera subgrafo induzido por vertices
	def geraSubgrafoIV(self, estrutura, lista):
		for i in range(len(lista)):
			u = self.verificaU(lista[i])
			self.delVertice(estrutura, u)
		return estrutura

	# gera subgrafo induzido por arestas
	def geraSubgrafoIA(self, estrutura, lista):
		tamLista = len(lista)
		for h in range(tamLista):
			u = self.verificaU(lista[h][0])
			v = self.verificaU(lista[h][1])
			print(u, v)
			self.delAresta(estrutura, u, v)
			if self.tipoEstrutura == "A":
				i = 0
				while i < self.qtdVertices:
					print("CHEGUEI")
					if estrutura[i].count(0) == self.qtdVertices:
						print("VAMO VER")
						cont = 0
						for j in range(self.qtdVertices):
							if estrutura[j][i] != 0:
								cont += 1
						if cont == 0:
							self.delVertice(estrutura, i)
					i += 1
		#~ elif self.tipoEstrutura == "L":
		
		#~ else:
			#~ i = 0
			#~ while i < self.qtdVertices:
				#~ cont = 0
				#~ for j in range(self.qtdArestas):
					#~ if estrutura[j][i] == 0:
						#~ cont += 1
				#~ if cont == self.qtdArestas:
					#~ for k in range(self.qtdArestas):
						#~ del estrutura[k][i]
					#~ self.qtdVertices -= 1
				#~ i += 1
		return estrutura

	# verifica se u pertence a lista de vertices
	def verificaU(self, u):
		existe = False
		for i in range(len(self.listaDeVertices)):
			if self.listaDeVertices[i] == u:
				u = i
				existe = True
		if existe:
			return u
		else:
			return u * 10000
