from grafo import Grafo

def lerArquivo(nomeArq, valorado):
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
    nomeArq = input("\nNome do arquivo: ")
    arquivo = open("arquivos_teste/" + nomeArq)

    if nomeArq.split('_')[2][:1] == "u":
        valorado = False
    else:
        valorado = True

    tipo = arquivo.readline()

    print('''\n--> Escolha sua forma de armazenamento do grafo:
    -Digite A para Matriz de Adjacencia
    -Digite I para Matriz de Incidencia
    -Digite L para Lista de Adjacencia''')

    qtdArestas = 0
    while arquivo.readline():
        qtdArestas += 1
    
    opcaoEscolhida = False
    while not(opcaoEscolhida):
        tipoEstrutura = input("\nTipo de estrutura: ")
        if tipoEstrutura == "A" or tipoEstrutura == "L" or tipoEstrutura == "I":
            opcaoEscolhida = True
        else:
            print("\nTipo de estrutura invalida\n")
    
    lista = lerArquivo("arquivos_teste/" + nomeArq, valorado)
    grafo = Grafo(tipo, valorado, nomeArq, qtdArestas, lista, tipoEstrutura);
    
    if grafo.tipoEstrutura == "A":
        estrutura = grafo.matrizAdjacencia()
        grafo.imprimeMatrizAdjacencia(estrutura)
    elif grafo.tipoEstrutura == "I":
        estrutura = grafo.matrizIncidencia()
        grafo.imprimeMatrizIncidencia(estrutura)
    else:
        estrutura = grafo.listaAdjacencia()
        grafo.imprimeListaAdjacencia(estrutura)

    menu = True
    print('''\n--> Escolha uma acao, digite:
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
    -12 para converter estrutura atual para matriz de adjacencia
    -13 para converter estrutura atual para matriz de incidencia
    -14 para converter estrutura atual para lista de adjacencia
    -SAIR para encerrar o programa''')

    while menu:
        opcao = input("\nSua escolha eh: ")
        #~ obtem vizinhos de u
        if opcao == "1":
            u = int(input("u: "))
            u = grafo.verificaU(u)
            if u >= 0 and u < grafo.qtdVertices:
                print(grafo.obtemVizinhos(estrutura, u))
            else:
                print("Vertice invalido")
        #~ obtem predecessores
        elif opcao == "2":
            u = int(input("u: "))
            u = grafo.verificaU(u)
            if u >= 0 and u < grafo.qtdVertices:
                print(grafo.obtemPred(estrutura, u))
            else:
                print("Vertice invalido")
        #~ obtem sucessores
        elif opcao == "3":
            u = int(input("u: "))
            u = grafo.verificaU(u)
            if u >= 0 and u < grafo.qtdVertices:
                print(grafo.obtemSuc(estrutura, u))
            else:
                print("Vertice invalido")
        #~ verifica se u e v sao vizinhos
        elif opcao == "4":
            u = int(input("u: "))
            v = int(input("v: "))
            u = grafo.verificaU(u)
            v = grafo.verificaU(v)
            if u >= 0 and u < grafo.qtdVertices and v >= 0 and v < grafo.qtdVertices:
                if grafo.ehVizinho(estrutura, u, v):
                    print("u e v sao vizinhos")
                else:
                    print("u e v nao sao vizinhos")
            else:
                print("Algum vertice invalido")
        #~ verifica se v eh predecessor de u
        elif opcao == "5":
            u = int(input("u: "))
            v = int(input("v: "))
            u = grafo.verificaU(u)
            if u >= 0 and u < grafo.qtdVertices and v >= 0 and v < grafo.qtdVertices:
                if grafo.ehPredecessor(estrutura, u, v):
                    print("v eh predecessor de u")
                else:
                    print("v nao eh predecessor de u")
            else:
                print("Algum vertice invalido")
        #~ verifica se v eh sucessor de u
        elif opcao == "6":
            u = int(input("u: "))
            v = int(input("v: "))
            if u >= 0 and u < grafo.qtdVertices and v >= 0 and v < grafo.qtdVertices:
                if grafo.ehSucessor(estrutura, u, v):
                    print("v eh sucessor de u")
                else:
                    print("v nao eh sucessor de u")
            else:
                print("Algum vertice invalido")
        #~ deleta o vertice u
        elif opcao == "7":
            u = int(input("u: "))
            u = grafo.verificaU(u)
            if u >= 0 and u < grafo.qtdVertices:
                grafo.delVertice(estrutura, u)
            else:
                print("Vertice invalido")
        #~ deleta a aresta u v
        elif opcao == "8":
            u = int(input("u: "))
            v = int(input("v: "))
            u = grafo.verificaU(u)
            v = grafo.verificaU(v)
            if u >= 0 and u < grafo.qtdVertices and v >= 0 and v < grafo.qtdVertices:
                grafo.delAresta(estrutura, u, v)
            else:
                print("Algum vertice invalido")
        #~ gera um subgrafo induzido por vertices
        elif opcao == "9":
            tamLista = int(input("Quantidade de vertices a serem retirados: "))
            lista = []
            invalido = False
            for i in range(tamLista):
                aux = int(input("vertice: "))
                lista.append(aux)
                if aux < 0 and aux >= grafo.qtdVertices:
                    invalido = True
            if invalido:
                print("Algum vertice invalido")
            else:
                grafo.geraSubgrafoIV(estrutura, lista)
        #~ gera um suggrafo induzido por arestas
        elif opcao == "10":
            tamLista = int(input("Quantidade de arestas a serem retiradas: "))
            lista = []
            invalido = False
            for i in range(tamLista):
                u = int(input("u: "))
                v = int(input("v: "))
                lista.append([u, v])
                if u < 0 and u >= grafo.qtdVertices and v < 0 and v >= grafo.qtdVertices:
                    invalido = True
            if invalido:
                print("Algum vertice invalido")
            else:
                grafo.geraSubgrafoIA(estrutura, lista)
        #~ imprime o grafo atual
        elif opcao == "11":
            if grafo.tipoEstrutura == "A":
                grafo.imprimeMatrizAdjacencia(estrutura)
            elif grafo.tipoEstrutura == "I":
                grafo.imprimeMatrizIncidencia(estrutura)
            else:
                grafo.imprimeListaAdjacencia(estrutura)
            print("\n")
        #~ converte para Matriz de Adjacência
        elif opcao == "12":
            if grafo.tipoEstrutura == "I":
                grafo.convMatIncList(estrutura)
                estrutura = grafo.matrizAdjacencia()
                grafo.tipoEstrutura = "A"
            elif grafo.tipoEstrutura == "L":
                grafo.convListAdList(estrutura)
                estrutura = grafo.matrizAdjacencia()
                grafo.tipoEstrutura = "A"
            else:
                print("\nSua estrutura atual ja eh matriz de adjacencia\n")
        #~ converte para Matriz de Incidência
        elif opcao == "13":
            if grafo.tipoEstrutura == "A":
                grafo.convMatAdList(estrutura)
                estrutura = grafo.matrizIncidencia()
                grafo.tipoEstrutura = "I"
            elif grafo.tipoEstrutura == "L":
                grafo.convListAdList(estrutura)
                estrutura = grafo.matrizIncidencia()
                grafo.tipoEstrutura = "I"
            else:
                print("\nSua estrutura atual ja eh matriz de incidencia\n")
        #~ converte para Lista de Adjacência
        elif opcao == "14":
            if grafo.tipoEstrutura == "A":
                grafo.convMatAdList(estrutura)
                estrutura = grafo.listaAdjacencia()
                grafo.tipoEstrutura = "L"
            elif grafo.tipoEstrutura == "I":
                grafo.convMatIncList(estrutura)
                estrutura = grafo.listaAdjacencia()
                grafo.tipoEstrutura = "L"
            else:
                print("\nSua estrutura atual ja eh lista de adjacencia\n")
        #~ imprime o menu novamente
        elif opcao == "15":
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
            -12 para converter estrutura atual para matriz de adjacencia
            -13 para converter estrutura atual para matriz de incidencia
            -14 para converter estrutura atual para lista de adjacencia
            -15 para imprimir o menu de opcoes
            -SAIR para encerrar o programa''')
        elif opcao == "SAIR":
            menu = False
        else:
            print("\n->Opcao invalida, tente novamente\n")
        

if __name__ == "__main__":
    main()
