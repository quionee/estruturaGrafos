
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
    nomeArq = input("Nome do arquivo: ")
    arquivo = open(nomeArq)
    
    if nomeArq.split('_')[2][:1] == "u":
        valorado = False
    else:
        valorado = True
    
    tipo = arquivo.readline()
    
    print('''--> Escolha sua forma de armazenamento do grafo:
    -Digite A para Matriz de Adjacencia
    -Digite I para Matriz de Incidencia
    -Digite L para Lista de Adjacencia''')
    
    qtdArestas = 0
    while arquivo.readline():
        qtdArestas += 1
        
    tipoEstrutura = input("Tipo de estrutura: ")
    lista = leArquivo(nomeArq, valorado)
    grafo = Grafo(tipo, valorado, nomeArq, qtdArestas, lista, tipoEstrutura);
    
    if grafo.tipoEstrutura == "A":
        estrutura = grafo.matrizAdjacencia()
        grafo.imprimeMatrizAdjacencia(estrutura)
    elif grafo.tipoEstrutura == "I":
        estrutura = grafo.matrizIncidencia()
        grafo.imprimeMatrizIncidencia(estrutura)
    elif grafo.tipoEstrutura == "L":
        estrutura = grafo.listaAdjacencia()
        grafo.imprimeListaAdjacencia(estrutura)
    
    menu = True
    print('''--> Escolha uma acao, digite:
    -1 para obter vizinhos de u
    -2 para obter predecessores de u
    -3 para obter sucessores de u
    -4 para verificar se u e v sao vizinhos
    -5 para verificar se v eh predecessor de u
    -6 para verificar se v eh sucessor de u
    -7 para deletar um vertice u
    -8 para deletar uma aresta u v
    -9 para gerar um subgrafo induzido por vertices
    -10 para gerar um suggrafo induzido por arestas
    -11 para imprimir o grafo na estrutura atual
    -SAIR para encerrar o programa''')

    while menu:
        opcao = int(input("Sua escolha eh: "))
        #~ obtem vizinhos de u
        if opcao == 1:
            u = int(input("\tu: "))
            if u >= 0 and u < grafo.qtdVertices:
                estrutura = grafo.convParaListaAd(estrutura)
                grafo.obtemVizinhos(estrutura, u)
            else:
                print("Vertice invalido")
        #~ obtem predecessores
        if opcao == 2:
            u = int(input("u: "))
            if u >= 0 and u < grafo.qtdVertices:
                estrutura = grafo.convParaMatInc(estrutura)
                aux = []
                print(grafo.obtemPred(estrutura, u, aux))
            else:
                print("Vertice invalido")
        #~ obtem sucessores
        if opcao == 3:
            u = int(input("u: "))
            if u >= 0 and u < grafo.qtdVertices:
                estrutura = grafo.convParaMatInc(estrutura)
                aux = []
                print(grafo.obtemSuc(estrutura, u, aux))
            else:
                print("Vertice invalido")
        #~ verifica se u e v sao vizinhos
        if opcao == 4:
            u = int(input("u: "))
            v = int(input("v: "))
            if u >= 0 and u < grafo.qtdVertices and v >= 0 and v < grafo.qtdVertices:
                estrutura = grafo.convParaMatAd(estrutura)
                if grafo.ehVizinho(estrutura, u, v):
                    print("u e v sao vizinhos")
                else:
                    print("u e v nao sao vizinhos")
            else:
                print("Algum vertice invalido")
        #~ verifica se v eh predecessor de u
        if opcao == 5:
            u = int(input("u: "))
            v = int(input("v: "))
            if u >= 0 and u < grafo.qtdVertices and v >= 0 and v < grafo.qtdVertices:
                estrutura = grafo.convParaMatInc(estrutura)
                if grafo.ehPredecessor(estrutura, u, v):
                    print("v eh predecessor de u")
                else:
                    print("v nao eh predecessor de u")
            else:
                print("Algum vertice invalido")
        #~ verifica se v eh sucessor de u
        if opcao == 6:
            u = int(input("u: "))
            v = int(input("v: "))
            if u >= 0 and u < grafo.qtdVertices and v >= 0 and v < grafo.qtdVertices:
                estrutura = grafo.convParaMatInc(estrutura)
                if grafo.ehSucessor(estrutura, u, v):
                    print("v eh sucessor de u")
                else:
                    print("v nao eh sucessor de u")
            else:
                print("Algum vertice invalido")
        #~ deleta o vertice u
        if opcao == 7:
            u = int(input("u: "))
            if u >= 0 and u < grafo.qtdVertices:
                estrutura = grafo.convParaMatInc(estrutura)
                grafo.delVertice(estrutura, u)
            else:
                print("Vertice invalido")
        #~ deleta a aresta u v
        if opcao == 8:
            u = int(input("u: "))
            v = int(input("v: "))
            if u >= 0 and u < grafo.qtdVertices and v >= 0 and v < grafo.qtdVertices:
                estrutura = grafo.convParaMatInc(estrutura)
                grafo.delAresta(estrutura, u, v)
            else:
                print("Algum vertice invalido")
        #~ gera um subgrafo induzido por vertices
        if opcao == 9:
            tamLista = int(input("Quantidade de vertices a serem retirados: "))
            lista = [0] * tamLista
            invalido = False
            for i in range(tamLista):
                aux = int(input())
                lista.append(aux)
                if aux < 0 and aux >= qtdVertices:
                    invalido = True
            if invalido:
                print("Algum vertice invalido")
            else:
                estrutura = grafo.convParaMatInc(estrutura)
                grafo.geraSubgrafoIV(estrutura, lista)
        #~ gera um suggrafo induzido por arestas
        if opcao == 10:
            tamLista = int(input("Quantidade de arestas a serem retiradas: "))
            lista = []
            invalido = False
            for i in range(tamLista):
                u = int(input())
                v = int(input())
                lista.append([u, v])
                print(lista)
                if u < 0 and u >= grafo.qtdVertices and v < 0 and v >= grafo.qtdVertices:
                    invalido = True
            if invalido:
                print("Algum vertice invalido")
            else:
                estrutura = grafo.convParaMatInc(estrutura)
                grafo.geraSubgrafoIA(estrutura, lista)
        if opcao == 11:
            if grafo.tipoEstrutura == "A":
                grafo.imprimeMatrizAdjacencia(estrutura)
            elif grafo.tipoEstrutura == "I":
                grafo.imprimeMatrizIncidencia(estrutura)
            else:
                grafo.imprimeListaAdjacencia(estrutura)
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
