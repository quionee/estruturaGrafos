
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
    nomeArq = raw_input("Nome do arquivo: ")
    arquivo = open(nomeArq)
    
    if nomeArq.split('_')[2][:1] == "u":
        valorado = False
    else:
        valorado = True
    
    tipo = arquivo.readline()
    
    print '''--> Escolha sua forma de armazenamento do grafo:
    -Digite A para Matriz de Adjacencia
    -Digite I para Matriz de Incidencia
    -Digite L para Lista de Adjacencia'''
    
    qtdArestas = 0
    while arquivo.readline():
        qtdArestas += 1
    
    lista = leArquivo(nomeArq, valorado)
    grafo = Grafo(tipo, valorado, nomeArq, qtdArestas, lista);
    
    tipoEstrutura = raw_input("Tipo de estrutura: ")
    
    if tipoEstrutura == "A":
        matrizAd = grafo.matrizAdjacencia()
        grafo.imprimeMatrizAdjacencia(matrizAd)
    elif tipoEstrutura == "I":
        matrizInc = grafo.matrizIncidencia()
        grafo.imprimeMatrizIncidencia(matrizInc)
    elif tipoEstrutura == "L":
        listaAd = grafo.listaAdjacencia()
        grafo.imprimeListaAdjacencia(listaAd)
    
    menu = True
    print '''--> Escolha uma acao, digite:
    -V para obter vizinhos de u
    -P para obter precessores de u
    -S para obter sucessores de u
    -SAIR para encerrar o programa'''

    while menu:
        opcao = str(raw_input("Sua escolha eh: "))
        if opcao == "V":
            #~ obtem vizinhos de u
            u = input("u: ")
            if u >= 0 and u < grafo.qtdVertices:
                if tipoEstrutura != "L":
                    if tipoEstrutura == "A":
                        grafo.convMatAdList(matrizAd)
                    elif tipoEstrutura == "I":
                        grafo.convMatIncList(matrizInc)
                    listaAd = grafo.listaAdjacencia()
                    grafo.imprimeListaAdjacencia(listaAd)
                    tipoEstrutura = "L"
                grafo.obtemVizinhos(listaAd, u)
            else:
                print("O vertice pedido nao existe no grafo")
        if opcao == "P":
            u = input("u: ")
            if u >= 0 and u < grafo.qtdVertices:
                if tipoEstrutura != "I":
                    if tipoEstrutura == "A":
                        grafo.convMatAdList(matrizAd)
                    elif tipoEstrutura == "L":
                        grafo.convListAdList(listaAd)
                    matrizInc = grafo.matrizIncidencia()
                    tipoEstrutura = "I"
                aux = []
                print(grafo.obtemPred(matrizInc, u, aux))
            else:
                print("O vertice pedido nao existe no grafo")
        if opcao == "S":
            u = input("u: ")
            if u >= 0 and u < grafo.qtdVertices:
                if tipoEstrutura != "I":
                    if tipoEstrutura == "A":
                        grafo.convMatAdList(matrizAd)
                    elif tipoEstrutura == "L":
                        grafo.convListAdList(listaAd)
                    matrizInc = grafo.matrizIncidencia()
                    tipoEstrutura = "I"
                aux = []
                print(grafo.obtemSuc(matrizInc, u, aux))
            else:
                print("O vertice pedido nao existe no grafo")
        if opcao == "SAIR":
            menu = False
    
    #~ grafo.convMatAdList(matrizAd)
    #~ grafo.convMatAdMatInc()
    #~ grafo.imprimeMatrizIncidencia(grafo.matrizIncidencia())
    #~ grafo.convMatAdListAd
    #~ grafo.imprimeListaAdjacencia(grafo.listaAdjacencia())
    

    #~ grafo.convMatIncList(matrizInc)
    #~ isso = grafo.convMatIncMatAd()
    #~ grafo.imprimeMatrizAdjacencia(isso)
    #~ isso = grafo.convMatIncListAd()
    #~ grafo.imprimeListaAdjacencia(isso)
    
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
    
    #~ u = int(input("u: "))
    #~ v = int(input("v: "))
    #~ print(grafo.obtemVizinhos(listaAd, u))
    #~ aux = []
    #~ grafo.obtemSuc(matrizInc, u, aux)
    #~ print(aux)
    
    #~ print(grafo.ehVizinho(matrizAd, u, v))
    
    #~ print(grafo.ehPredecessor(matrizInc, u, v))

    #~ print(grafo.ehSucessor(matrizInc, u, v))
    
    #~ lisAux = [[1, 2], [3, 0], [7, 5]]
    #~ matrizInc = grafo.geraSubgrafoIA(matrizInc, lisAux)
    #~ grafo.imprimeMatrizIncidencia(matrizInc)
    #~ print(grafo.qtdVertices)
if __name__ == "__main__":
    main()
