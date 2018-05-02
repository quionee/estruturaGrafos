
arquivo = open("n5_dir_unwgt_comb0.txt")

oi = arquivo.readline()

print(oi)

aux = 0

while arquivo.readline():
	aux += 1

arquivo.seek(0)

for i in range(aux):
	arquivo.readline()

indice = arquivo.readline(1)

indice = int(indice) + 1

print(indice)

matriz = [0] * indice

for lin in range(indice):
	matriz[lin] = [0] * indice
	
print(matriz)

arquivo.seek(0)
oi = arquivo.readline()

for i in range(aux):
	a = arquivo.readline(1)
	arquivo.readline(1)
	b = arquivo.readline(1)
	arquivo.readline()
	matriz[int(a)][int(b)] = 1
	print(a)
	print(b)

for i in range(indice):
	print(matriz[i])
