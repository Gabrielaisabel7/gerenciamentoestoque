# Sistema de Gestão para Lojas Condimentos Bom Jesus
## Link para a Documentação

A documentação completa do projeto pode ser encontrada [aqui]((https://docs.google.com/document/d/1MaJqQFF0VUvH_ecQKQRh2ho6i8U8x-Ov/edit?usp=sharing&ouid=110255632272579881467&rtpof=true&sd=true))

## Objetivo do Projeto

Este projeto tem como objetivo desenvolver um **Sistema de Gerenciamento de Estoque e Funcionários** para as **Lojas Condimentos Bom Jesus**, localizadas na Central de Abastecimento de Caruaru (CEACA). O sistema foi criado para resolver o problema de **integração de estoques** entre as duas lojas e otimizar o tempo de atendimento, promovendo **maior agilidade no processo de venda**, centralizando a gestão dos produtos e funcionários.

## História e Contexto

As **Lojas Condimentos Bom Jesus**, administradas por **Gilda** e **Lenildo**, são focadas no comércio de **produtos alimentícios** e possuem mais de 30 anos de experiência com a primeira loja e 16 anos com a segunda.

Até o momento, o processo de gerenciamento de estoque e funcionários era realizado de maneira manual. Isso criava dificuldades, principalmente pela **falta de integração entre os estoques das lojas**, o que exigia que os **funcionários se deslocassem fisicamente entre as lojas** para verificar o estoque.

O objetivo deste sistema é **eliminar esse deslocamento**, oferecendo uma solução mais ágil e eficiente, permitindo acesso rápido às informações de estoque e funcionários de forma centralizada.

## Funcionalidades do Sistema

### Gerenciamento de Estoque:
- **Cadastro de produtos**: Permite adicionar novos produtos ao estoque.
- **Atualização de quantidades e preços**: Facilita a atualização dos produtos existentes.
- **Remoção de produtos**: Remove produtos do estoque quando necessário.
- **Exibição do estoque atual**: Mostra a quantidade de produtos disponíveis nas lojas.

### Gerenciamento de Funcionários:
- **Cadastro de funcionários**: Adiciona novos funcionários ao sistema.
- **Atualização de nome de usuário e senha**: Altera as credenciais dos funcionários.
- **Remoção de funcionários**: Permite excluir funcionários do sistema.
- **Exibição de funcionários cadastrados**: Lista todos os funcionários no sistema.

## Tecnologias Utilizadas

- **Python**: Linguagem principal utilizada no desenvolvimento do sistema.
- **Arquivos locais (TXT)**: Para o armazenamento dos dados de estoque e funcionários.

## Estrutura de Arquivos

- `armazenamentoEstoque.py`: Gerencia as funções de manipulação do estoque (adicionar, atualizar, listar e remover produtos).
- `armazenamentoFuncionario.py`: Gerencia as funções de manipulação de funcionários (adicionar, atualizar, listar e remover).
- `estoque.txt`: Armazena as informações dos produtos no estoque das lojas.
- `recursos_humanos.txt`: Armazena as informações dos funcionários.
