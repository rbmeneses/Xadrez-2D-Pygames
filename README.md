![Screenshot da Aplicação](https://github.com/rbmeneses/Xadrez-2D-Pygames/blob/main/xadrez.png)
Xadrez Humano vs Gemini (Pygame)
Um jogo de xadrez 2D completo desenvolvido em Python com a biblioteca Pygame. Desafie um amigo no modo multiplayer local ou teste suas habilidades contra uma inteligência artificial com múltiplos níveis de dificuldade.

(Imagem ilustrativa do gameplay)

📜 Descrição
Este projeto implementa um jogo de xadrez funcional com uma interface gráfica limpa e intuitiva. O objetivo foi criar uma experiência de xadrez clássica, respeitando todas as regras fundamentais do jogo, e oferecer um oponente de IA desafiador para jogadores individuais.

O nome "Gemini" é utilizado de forma temática na interface do jogo. A IA do oponente é implementada com o robusto algoritmo Minimax com poda alfa-beta, uma técnica clássica e eficiente para jogos de estratégia.

✨ Features
Gameplay
Modos de Jogo:

♟️ Multiplayer Local: Jogue contra outra pessoa no mesmo computador.

🤖 Singleplayer vs. IA: Desafie uma inteligência artificial.

IA com 4 Níveis de Dificuldade:

A dificuldade ajusta a profundidade de busca da IA: Fácil (1), Médio (2), Difícil (3) e Expert (4).

Regras Completas de Xadrez:

Implementação completa de Xeque, Xeque-mate e Empate por Afogamento (Stalemate).

Movimentos especiais: Roque (curto e longo), captura En Passant e Promoção de Peão (automaticamente para Rainha).

Interface e Experiência
Feedback Visual Claro:

Destaque para a peça selecionada e seus movimentos legais.

Marcação visual da última jogada realizada no tabuleiro.

Destaque em vermelho sobre o Rei quando ele está em xeque.

Interface Completa:

Menu inicial para seleção de modo de jogo e dificuldade.

Barra lateral com informações de turno e histórico de jogadas em notação.

Coordenadas (A-H, 1-8) exibidas ao redor do tabuleiro.

Tela de "Fim de Jogo" com opção para jogar novamente.

Fallback de Assets: Caso as imagens das peças na pasta /assets não sejam encontradas, o jogo renderiza as iniciais de cada peça para garantir a jogabilidade.

🛠️ Tecnologias Utilizadas
Python 3.x

Pygame: Biblioteca para desenvolvimento de jogos 2D.

🚀 Instalação e Execução
Para executar o projeto localmente, siga os passos abaixo.

Pré-requisitos
Python 3 instalado em seu sistema. Você pode baixá-lo em python.org.

Passos
Clone o repositório:

Bash

git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
Instale as dependências:
A única dependência externa é a pygame. Instale-a usando pip:

Bash

pip install pygame
Estrutura de Arquivos:
Certifique-se de que a pasta assets (contendo os arquivos .png das peças) esteja no mesmo diretório que o script Python.

/seu-repositorio
|-- Xadrez Humano vs Gemini1.1.py
|-- /assets
    |-- black_king.png
    |-- white_king.png
    |-- ... (todas as outras imagens)
Execute o Jogo:

Bash

python "Xadrez Humano vs Gemini1.1.py"
🧠 Sobre a Inteligência Artificial
A IA deste jogo, embora chamada de "Gemini" na interface, não utiliza um modelo de linguagem. Ela é movida pelo algoritmo Minimax com poda alfa-beta.

Minimax: É um algoritmo de busca recursiva usado para tomar decisões em jogos de dois jogadores. Ele explora uma árvore de possíveis jogadas futuras para encontrar o movimento ótimo.

Poda Alfa-Beta: Uma otimização do Minimax que "poda" (ignora) ramos da árvore de busca que não influenciarão na decisão final, tornando o cálculo da melhor jogada muito mais rápido.

Níveis de Dificuldade: A dificuldade selecionada no menu (Fácil, Médio, Difícil, Expert) define a profundidade da busca. Uma profundidade maior significa que a IA "pensa" mais movimentos à frente, resultando em um desafio maior, porém exigindo mais tempo de processamento para cada jogada.

📂 Estrutura do Código
O código-fonte é organizado de forma modular e orientada a objetos para facilitar a leitura e manutenção.

Piece (e subclasses): Define a estrutura base e o comportamento específico de cada tipo de peça de xadrez (Rei, Rainha, Peão, etc.).

Board: Classe central que gerencia o estado do tabuleiro, a posição das peças, a validação de movimentos e a aplicação de todas as regras do jogo.

AI: Contém a implementação do algoritmo Minimax com poda alfa-beta, responsável por calcular a melhor jogada para o computador.

Game: Orquestra todo o jogo. Gerencia o loop principal, os estados (menu, jogando, fim de jogo), os eventos do mouse e a renderização de todos os elementos na tela.

Estrutura e Prompt: cognosIA 

Data: 20/09/2025
