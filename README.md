# Sistema de Controle de Voos em Aeroporto

Este repositório contém um sistema de controle para gerenciamento de companhias aéreas e seus respectivos voos, utilizando estruturas de dados avançadas. O sistema é baseado em duas estruturas principais: **Fila** e **Pilha**, com a fila gerenciando as companhias aéreas e a pilha organizando os voos de cada companhia.

## Estruturas de Dados

- **Fila**: Utilizada para gerenciar as companhias aéreas no sistema, com a primeira companhia da fila sendo atendida primeiro (FIFO - First In, First Out).
- **Pilha**: Cada companhia aérea tem uma pilha associada para gerenciar os voos, com o voo mais recente sendo atendido primeiro (LIFO - Last In, First Out).

## Funcionalidades

O sistema oferece um conjunto de funcionalidades para gerenciar e organizar voos e companhias aéreas. As principais funcionalidades incluem:

- **Adicionar Companhia**: Registra uma nova companhia aérea no sistema.
- **Adicionar Voo**: Registra um voo para uma companhia aérea específica.
- **Atender Voo**: Remove e atende o voo do topo da pilha da primeira companhia da fila.
- **Remover Companhia**: Remove uma companhia aérea específica da fila.
- **Cancelar Voo**: Cancela um voo de uma companhia aérea específica.
- **Suspender Voo**: Suspende um voo de uma companhia aérea (adiamento).
- **Trocar Voos**: Permite a troca de posição entre dois voos de uma mesma companhia.
- **Mostrar Companhia e Voos**: Exibe as companhias aéreas e seus voos, do topo para a base.
- **Buscar Voos por Destino**: Permite buscar todos os voos para um destino específico.
- **Mostrar Estatísticas**: Exibe dados gerais do sistema, como a quantidade de companhias, voos e a companhia com maior número de voos registrados.

## Funções Implementadas

### Funções para Pilha

- `push(p, v)`: Adiciona um item à pilha `p`.
- `pop(p)`: Remove e retorna o item do topo da pilha `p`.
- `vazia(p)`: Verifica se a pilha `p` está vazia.

### Funções para Fila

- `inserir(f, v)`: Adiciona um item à fila `f`.
- `retirar(f)`: Remove e retorna o item do início da fila `f`.
- `vazia_fila(f)`: Verifica se a fila `f` está vazia.

### Funções do Sistema

- `inserirCompanhia(fila, nomeCompanhia)`: Adiciona uma nova companhia aérea à fila.
- `adicionarVoo(fila, nomeCompanhia, codigo, destino, horario)`: Adiciona um voo à pilha de uma companhia específica.
- `atenderVoo(fila)`: Atende o voo do topo da pilha da primeira companhia da fila.
- `removerCompanhia(fila, nomeCompanhia)`: Remove uma companhia aérea específica da fila.
- `cancelarVoo(fila, nomeCompanhia, codigoVoo)`: Cancela um voo de uma companhia aérea.
- `suspenderVoo(fila, nomeCompanhia, codigoVoo)`: Suspende (adiamento) um voo de uma companhia aérea.
- `trocarVoos(fila, nomeCompanhia, codigoVoo1, codigoVoo2)`: Troca a posição de dois voos de uma mesma companhia aérea.
- `mostrarCompanhiaVoo(fila)`: Exibe todas as companhias e seus voos, do topo para a base da pilha.
- `buscarVoosDestino(fila, destino)`: Exibe todos os voos com o destino especificado.
- `mostrarEstatisticas(fila)`: Exibe informações estatísticas do sistema, como número de companhias, voos e a companhia com mais voos registrados.