



# obtem predecessores utilizando matriz de incidencia
def obtemPred(estrutura, u, aux, uAux):
    qtdVertices = len(estrutura[0])
    qtdArestas = len(estrutura)
    
    #~ temLoop = False
    for i in range(qtdArestas):
        if estrutura[i][u] < 0:
            for j in range(qtdVertices):
                if j != uAux and estrutura[i][j] > 0:
                    jaExiste = False
                    if any(k == j for k in aux):
                        jaExiste = True
                    if not(jaExiste):
                        aux.append(j)
                        obtemPred(estrutura, j, aux, uAux)
                #~ elif estrutura[i].count(0) == qtdVertices - 1 and not temLoop:
                    #~ temLoop = True
                    #~ print estrutura[i]
                    #~ bosta = 0
                    #~ if any(t != 0 for t in  estrutura[i]):
                        #~ bosta += 1
                    #~ print "bosta: ", bosta
    return aux
                    
# obtem sucessores utilizando matriz de incidencia
def obtemSuc(estrutura, u, aux):
    qtdVertices = len(estrutura[0])
    qtdArestas = len(estrutura)
    for i in range(qtdArestas):
        if estrutura[i][u] > 0:
            for j in range(qtdVertices):
                if estrutura[i][j] < 0:
                    jaExiste = False
                    if any(k == j for k in aux):
                        jaExiste = True
                    if not(jaExiste):
                        aux.append(j)
                        obtemSuc(estrutura, j, aux)
    return aux      

# verifica se v eh predecessor de u utilizando obtemPred
def ehPredecessor(estrutura, u, v):
    lisAux = []
    lisAux = obtemPred(estrutura, u, lisAux)
    ehPred = False
    if any(i == v for i in lisAux):
        ehPred = True
    return ehPred

# verifica se v eh sucessor de u utilizando obtemSuc
def ehSucessor(estrutura, u, v):
    lisAux = []
    lisAux = obtemSuc(estrutura, u, lisAux)
    ehSuc = False
    if any(i == v for i in lisAux):
        ehSuc = True
    return ehSuc

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
    
    #~ u = input("u: ")
    #~ print obtemVizinhos(estrutura, u, valorado)
    
    # obtem predecessores
    if tipoEstrutura != "I":
        if tipoEstrutura == "A":
            estrutura = convMatAdMatInc(estrutura, tipo, valorado)
        elif tipoEstrutura == "L":
            estrutura = convListAdMatInc(estrutura, tipo, valorado)
        tipoEstrutura = "I"
    
    u = input("u: ")
    aux = []
    #~ qtdVertices = 5
    #~ if estrutura[u].count(0) == qtdVertices - 1:
        #~ for i in range(qtdVertices):
            #~ if (estrutura[u][i] != 0):
                #~ aux.append(i)
    #~ print obtemPred(estrutura, u, aux, u)
    
    # obtem sucessores
    #~ if tipoEstrutura != "I":
        #~ if tipoEstrutura == "A":
            #~ estrutura = convMatAdMatInc(estrutura, tipo, valorado)
        #~ elif tipoEstrutura == "L":
            #~ estrutura = convListAdMatInc(estrutura, tipo, valorado)
        #~ tipoEstrutura = "I"
        #~ imprimeMatrizIncidencia(estrutura)
    
    #~ u = input("u: ")
    #~ aux = []
    #~ print obtemSuc(estrutura, u, aux)
    
    
    # verifica se v eh predecessor de u
    #~ if tipoEstrutura != "I":
        #~ if tipoEstrutura == "A":
            #~ estrutura = convMatAdMatInc(estrutura, tipo, valorado)
        #~ elif tipoEstrutura == "L":
            #~ estrutura = convListAdMatInc(estrutura, tipo, valorado)
        #~ tipoEstrutura = "I"
    
    #~ u = input("u: ")
    #~ v = input("v: ")
    #~ print ehPredecessor(estrutura, u, v)
    
    
    
    # verifica se v eh sucessor de u
    #~ if tipoEstrutura != "I":
        #~ if tipoEstrutura == "A":
            #~ estrutura = convMatAdMatInc(estrutura, tipo, valorado)
        #~ elif tipoEstrutura == "L":
            #~ estrutura = convListAdMatInc(estrutura, tipo, valorado)
        #~ tipoEstrutura = "I"
    
    #~ u = input("u: ")
    #~ v = input("v: ")
    #~ print ehSucessor(estrutura, u, v)
    
    
    
    
    
    
    
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
