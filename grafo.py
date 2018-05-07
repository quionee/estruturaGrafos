
class Grafo:
	# construtor
	def __init__(self, tipo, valorado, nomeArq, qtdArestas, lista):
		self.tipo = tipo[0]
		self.valorado = valorado
		self.qtdVertices = int(nomeArq.split('_')[0][1:])
		self.qtdArestas = qtdArestas
		self.lista = lista
		
	# estrutura de dado: lista de adjacencia
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
					a = lista[j]
					b = lista[j + 1]
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
