
arquivo = open("n10_dir_unwgt_comb0.txt")
tipo = arquivo.readline()

qtdArestas = 0
while arquivo.readline():
	qtdArestas += 1

arquivo.seek(0)

for i in range(qtdArestas):
	arquivo.readline()

qtdVertices = int(arquivo.readline(1)) + 1

# matriz de incidencia

matrizIncidencia = [0] * qtdArestas

for lin in range(qtdArestas):
	matrizIncidencia[lin] = [0] * qtdVertices
	
arquivo.seek(0)
arquivo.readline()

# direcionado
if tipo[0] == "D":
	print("grafo direcionado")
	for i in range(qtdArestas):
		a = int(arquivo.readline(1))
		arquivo.readline(1)
		b = int(arquivo.readline(1))
		arquivo.readline()
		matrizIncidencia[i][a] = 1
		matrizIncidencia[i][b] = -1
	
# nao-direcionado
else:
	print("grafo nao-direcionado")
	for i in range(qtdArestas):
		a = int(arquivo.readline(1))
		arquivo.readline(1)
		b = int(arquivo.readline(1))
		arquivo.readline()
		matrizIncidencia[i][a] = 1
		matrizIncidencia[i][b] = 1

print("\nMatriz de Incidencia: \n")
for lin in range(qtdArestas):
	print(matrizIncidencia[lin])

# matriz de adjacencia

matrizAdjacencia = [0] * qtdVertices

for lin in range(qtdVertices):
	matrizAdjacencia[lin] = [0] * qtdVertices

arquivo.seek(0)
arquivo.readline()

# direcionado
if tipo[0] == "D":
	for i in range(qtdArestas):
		a = int(arquivo.readline(1))
		arquivo.readline(1)
		b = int(arquivo.readline(1))
		arquivo.readline()
		matrizAdjacencia[a][b] = 1

# nao-direcionado
else:
	for i in range(qtdArestas):
		a = int(arquivo.readline(1))
		arquivo.readline(1)
		b = int(arquivo.readline(1))
		arquivo.readline()
		matrizAdjacencia[a][b] = 1
		matrizAdjacencia[b][a] = 1

print("\n\nMatriz de Adjacencia: \n")
for i in range(qtdVertices):
	print(matrizAdjacencia[i])

