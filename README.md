### Estrutura de dados para grafos

O trabalho foi implementado para, a partir de uma estrutura de dados para armazenamento de um grafo (matriz de adjacência, matriz de incidência e lista de adjacência), ser possível realizar as seguintes funções, onde *u* e *v* são vértices pertencentes ao grafo:

	* obter vizinhos de u
	* obter predecessores de u
	* obter sucessores de u
	* verificar se u e v são vizinhos
	* verificar se v é predecessor de u
	* verificar se v é sucessor de u
	* deletar um vertice u
	* deletar uma aresta u v
	* gerar um subgrafo induzido por vertices
	* gerar um suggrafo induzido por arestas
	* imprimir o grafo na estrutura atual
	* converter estrutura atual para matriz de adjacência
	* converter estrutura atual para matriz de incidência
	* converter estrutura atual para lista de adjacência

#### Entrada e Execução

O programa recebe como entrada um arquivo texto. Os arquivos disponíveis para teste estão na pasta *arquivos_teste*.

Foi utilizado o python 3 para a implementação.

Para executar, basta rodar o comando `python3 main.py` no terminal e entrar com o nome do arquivo de teste. Após o nome do arquivo, as opções serão disponibilizadas no terminal, basta seguir as instruções.

#### Resultados

Os resultados podem ser verificados durante a execução, a opção *11* de execução imprime o grafo na estrutura de dados que estiver sendo usada para armazenamento no momento.

Copyright (c) 2018 Felipe Ferreira Carvalho Silva, Lorena Kerollen Botelho Tavares, Rodrigo Pinto Herculano