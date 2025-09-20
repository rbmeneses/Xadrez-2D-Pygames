# -*- coding: utf-8 -*-

"""
Xadrez Humano vs Gemini (Pygame)
================================
## Prompt para Geração de Código - Xadrez Humano vs Gemini (Pygame)
**Objetivo:** Gerar código Python funcional para um jogo de xadrez 2D utilizando a biblioteca Pygame, permitindo partidas entre dois jogadores humanos localmente ou contra uma IA baseada no modelo Gemini (ou similar).
**Público-alvo:** Gamers
**Tom:** Instrutivo e direto, com foco na clareza e na funcionalidade.
**Formato:** Código Python comentado, estruturado e organizado.
**Requisitos:**
Gere o código-fonte completo em Python para o jogo "Xadrez Humano vs Gemini", conforme as seguintes especificações:
**1. Visão Geral:**
Um jogo de xadrez 2D em Pygame, com opção de jogo contra outro jogador local ou contra uma IA (Gemini ou similar).  A mecânica do xadrez deve ser respeitada integralmente.  Interface visual atraente e intuitiva, com foco na clareza e legibilidade.
**2. Mecânicas Principais (Core Loop):**
* **Seleção de Modo:** Menu inicial para escolha entre "Multiplayer Local" (dois jogadores humanos) e "Singleplayer" (contra a IA).
* **Seleção de Dificuldade (Singleplayer):**  No modo Singleplayer, permitir a seleção da dificuldade da IA: Fácil, Médio, Difícil e Expert.  Implemente diferentes níveis de profundidade de busca na IA para cada dificuldade.
* **Jogo:**  Implemente o fluxo de jogo padrão do xadrez, permitindo a seleção e movimentação das peças de acordo com as regras.  A IA deve realizar sua jogada após o jogador humano.
* **Verificação de Xeque-Mate/Empate:** Implemente a lógica para detectar e anunciar xeque-mate, empate por afogamento, empate por repetição de lances (regra dos três movimentos repetidos, por exemplo) e outros tipos de empate relevantes.
* **Repetição:** Após o fim da partida, oferecer a opção de jogar novamente, retornando ao menu inicial.
**3.  Peças e Movimentação:**
* Utilize as peças de xadrez padrão (Rei, Rainha, Torre, Bispo, Cavalo, Peão) com suas respectivas regras de movimento.
* Não há habilidades especiais ou progressão individual das peças.
**4. Sistema de Progressão:**
* Não há sistema de progressão por níveis ou experiência. A progressão se dá pela melhoria da habilidade do jogador.
**5. Direção de Arte (Visual):**
* **Estilo:** Clean e minimalista, com foco na clareza e legibilidade.
* **Cores:** Paleta de cores sóbrias e contrastantes para boa visualização (sugestão: tons de cinza, marrom e bege para o tabuleiro, e cores distintas para as peças brancas e pretas).
* **Tabuleiro:** Padrão clássico de xadrez 8x8, com cores alternadas.
* **Peças:**  Design estilizado, mas facilmente reconhecível.  Representar visualmente cada tipo de peça (Rei, Rainha, etc.).
* **Efeitos Visuais:**  Mínimos, utilizados para destacar jogadas especiais (xeque e xeque-mate - sugestão: destaque visual na casa do Rei em xeque).
**6.  IA (Gemini ou Similar):**
* Implementar a IA utilizando o modelo Gemini (ou similar, se a integração direta não for possível, utilize um algoritmo de xadrez como Minimax com poda alfa-beta).
* A dificuldade da IA deve ser ajustável através da profundidade da árvore de busca do algoritmo.
**7.  Código:**
* O código deve ser bem comentado, explicando a lógica por trás das diferentes seções.
* Utilize nomes de variáveis e funções descritivos.
* Organize o código em módulos ou classes para facilitar a leitura e manutenção.
**Considerações Adicionais:**
* Priorize a clareza e a funcionalidade do código.
*  Se a integração com Gemini for complexa, foque em uma IA funcional com diferentes níveis de dificuldade.
* Comente no código eventuais limitações ou decisões de design tomadas durante a implementação.
**Exemplo de estrutura de código (simplificada):**
# Importações (pygame, etc.)
# Classe Tabuleiro
# Classe Peça
# Classe IA (Gemini ou algoritmo Minimax)
# Funções auxiliares (verificar xeque-mate, empate, etc.)
# Inicialização do Pygame
# Criação do tabuleiro e das peças
# Loop principal do jogo
# Eventos (cliques do mouse, etc.)
# Atualização do estado do jogo
# Renderização (desenho do tabuleiro e das peças)
Explicação e Complementos:
Integração com Gemini (ou similar): A integração direta com um modelo de linguagem grande como Gemini em um jogo de xadrez em tempo real pode ser complexa e exigir recursos de computação significativos. A implementação fornecida utiliza um algoritmo Minimax com poda alfa-beta como exemplo simplificado de IA. Adaptar para Gemini exigiria uma interface e estrutura mais elaborada.
Classes Board e Piece: Essas classes conteriam a lógica de representação do tabuleiro, peças, movimentos, verificação de ataques, etc. A implementação completa dessas classes demandaria mais código, mas a estrutura básica foi fornecida.
IA (Minimax): A classe AI fornecida é uma representação simplificada. Uma implementação robusta de Minimax com poda alfa-beta e diferentes níveis de dificuldade requer mais código e otimizações.
Funções Auxiliares: Funções como is_checkmate, is_stalemate, etc., são essenciais para a lógica do jogo e precisam ser implementadas de acordo com as regras do xadrez.
Menu e Seleção de Modo/Dificuldade: A implementação do menu inicial e a seleção de modo/dificuldade podem ser feitas utilizando elementos da interface do Pygame (botões, caixas de texto, etc.).
Tratamento de Eventos: O loop principal deve tratar eventos de mouse e teclado para permitir a interação do jogador com o jogo.
Renderização: A função board.draw(screen) é responsável por desenhar o tabuleiro e as peças na tela. A implementação completa dessa função deve considerar as cores, o design das peças, e os efeitos visuais (destaque do rei em xeque, por exemplo).
Este código expandido e comentado fornece uma estrutura mais completa e funcional para o jogo de xadrez, abordando os pontos principais do prompt. A implementação completa de todos os recursos requer mais código e refinamento, mas esta base serve como um bom ponto de partida. Lembre-se de comentar o código detalhadamente e organizar as diferentes partes em funções e classes para facilitar a leitura e manutenção.
# Finalização do Pygame

Autor: Ricardo (adaptado e estruturado para este prompt criado por cognosIA)
Data: 20/09/2025
"""
# -*- coding: utf-8 -*-

"""
Xadrez Humano vs Gemini (Pygame)
================================

Um jogo de xadrez 2D completo implementado em Python com a biblioteca Pygame.
"""
# -*- coding: utf-8 -*-

"""
Xadrez Humano vs Gemini (Pygame)
================================

Um jogo de xadrez 2D completo implementado em Python com a biblioteca Pygame.
"""

import pygame
import sys
import copy
import math
import random

# --- 1. CONFIGURAÇÕES E CONSTANTES ---

# Dimensões da tela e do tabuleiro
BOARD_SIZE = 640  # Múltiplo de 8 para casas perfeitas
SQUARE_SIZE = BOARD_SIZE // 8
BOARD_OFFSET = 30 # Espaço para as coordenadas
SIDEBAR_WIDTH = 280
WIDTH = BOARD_SIZE + SIDEBAR_WIDTH + (BOARD_OFFSET * 2)
HEIGHT = BOARD_SIZE + (BOARD_OFFSET * 2)

# Cores (RGB)
WHITE = (255, 255, 255); BLACK = (0, 0, 0); BOARD_LIGHT = (238, 238, 210); BOARD_DARK = (118, 150, 86)
HIGHLIGHT_COLOR = (255, 255, 0, 100); CHECK_COLOR = (255, 0, 0, 150); MENU_BG_COLOR = (40, 40, 40)
TEXT_COLOR = (240, 240, 240); BUTTON_COLOR = (80, 80, 80); BUTTON_HOVER_COLOR = (120, 120, 120)
LAST_MOVE_COLOR = (173, 216, 230, 150) # Azul claro semitransparente

# Dificuldades da IA
DIFFICULTY_LEVELS = {'Fácil': 1, 'Médio': 2, 'Difícil': 3, 'Expert': 4}

# --- 2. CLASSES DAS PEÇAS E DO TABULEIRO ---
class Piece:
    def __init__(self, row, col, color, piece_type):
        self.row, self.col, self.color, self.piece_type = row, col, color, piece_type
        self.image_path = f'assets/{self.color}_{self.piece_type}.png'
        self.has_moved = False
    def move(self, row, col):
        self.row, self.col, self.has_moved = row, col, True
    def draw(self, screen):
        try:
            piece_image = pygame.image.load(self.image_path)
            piece_image = pygame.transform.scale(piece_image, (SQUARE_SIZE, SQUARE_SIZE))
            screen.blit(piece_image, (self.col * SQUARE_SIZE, self.row * SQUARE_SIZE))
        except (pygame.error, FileNotFoundError):
            font = pygame.font.SysFont('arial', int(SQUARE_SIZE * 0.7), bold=True)
            initial = 'N' if self.piece_type == 'knight' else self.piece_type[0].upper()
            piece_bg_color = BLACK if self.color == 'black' else WHITE
            piece_text_color = WHITE if self.color == 'black' else BLACK
            pygame.draw.circle(screen, piece_bg_color, (self.col * SQUARE_SIZE + SQUARE_SIZE // 2, self.row * SQUARE_SIZE + SQUARE_SIZE // 2), SQUARE_SIZE // 2 - 5)
            text_surf = font.render(initial, True, piece_text_color)
            text_rect = text_surf.get_rect(center=(self.col * SQUARE_SIZE + SQUARE_SIZE // 2, self.row * SQUARE_SIZE + SQUARE_SIZE // 2))
            screen.blit(text_surf, text_rect)
class King(Piece):
    def __init__(self, row, col, color): super().__init__(row, col, color, 'king')
class Queen(Piece):
    def __init__(self, row, col, color): super().__init__(row, col, color, 'queen')
class Rook(Piece):
    def __init__(self, row, col, color): super().__init__(row, col, color, 'rook')
class Bishop(Piece):
    def __init__(self, row, col, color): super().__init__(row, col, color, 'bishop')
class Knight(Piece):
    def __init__(self, row, col, color): super().__init__(row, col, color, 'knight')
class Pawn(Piece):
    def __init__(self, row, col, color): super().__init__(row, col, color, 'pawn')

class Board:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.turn = 'white'; self.selected_piece = None; self.valid_moves = []
        self.last_move = None; self.white_king_pos = (7, 4); self.black_king_pos = (0, 4)
        self._setup_pieces()
    def _setup_pieces(self):
        self.board[0][0]=Rook(0,0,'black');self.board[0][1]=Knight(0,1,'black');self.board[0][2]=Bishop(0,2,'black');self.board[0][3]=Queen(0,3,'black');self.board[0][4]=King(0,4,'black');self.board[0][5]=Bishop(0,5,'black');self.board[0][6]=Knight(0,6,'black');self.board[0][7]=Rook(0,7,'black')
        for i in range(8): self.board[1][i] = Pawn(1,i,'black')
        self.board[7][0]=Rook(7,0,'white');self.board[7][1]=Knight(7,1,'white');self.board[7][2]=Bishop(7,2,'white');self.board[7][3]=Queen(7,3,'white');self.board[7][4]=King(7,4,'white');self.board[7][5]=Bishop(7,5,'white');self.board[7][6]=Knight(7,6,'white');self.board[7][7]=Rook(7,7,'white')
        for i in range(8): self.board[6][i] = Pawn(6,i,'white')
    def draw(self, screen):
        for r in range(8):
            for c in range(8): pygame.draw.rect(screen, BOARD_LIGHT if (r + c) % 2 == 0 else BOARD_DARK, (c*SQUARE_SIZE, r*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
        if self.last_move:
            _, start_pos, end_pos = self.last_move
            for r, c in [start_pos, end_pos]:
                s = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE), pygame.SRCALPHA); s.fill(LAST_MOVE_COLOR); screen.blit(s, (c*SQUARE_SIZE, r*SQUARE_SIZE))
        if self.selected_piece:
            r,c=self.selected_piece.row,self.selected_piece.col;s=pygame.Surface((SQUARE_SIZE,SQUARE_SIZE),pygame.SRCALPHA);s.fill(HIGHLIGHT_COLOR);screen.blit(s,(c*SQUARE_SIZE,r*SQUARE_SIZE))
            for move in self.valid_moves: r,c=move;s=pygame.Surface((SQUARE_SIZE,SQUARE_SIZE),pygame.SRCALPHA);pygame.draw.circle(s,HIGHLIGHT_COLOR,(SQUARE_SIZE//2,SQUARE_SIZE//2),15);screen.blit(s,(c*SQUARE_SIZE,r*SQUARE_SIZE))
        if self.is_in_check(self.turn):
            r,c=self.white_king_pos if self.turn=='white' else self.black_king_pos;s=pygame.Surface((SQUARE_SIZE,SQUARE_SIZE),pygame.SRCALPHA);s.fill(CHECK_COLOR);screen.blit(s,(c*SQUARE_SIZE,r*SQUARE_SIZE))
        for r in range(8):
            for c in range(8):
                if self.board[r][c]: self.board[r][c].draw(screen)
    def select_piece(self, row, col):
        if self.selected_piece and (row,col) in self.valid_moves: self.make_move(self.selected_piece,row,col); self._change_turn(); return True
        else:
            self.selected_piece,self.valid_moves=None,[]
            piece=self.board[row][col]
            if piece and piece.color==self.turn: self.selected_piece,self.valid_moves=piece,self.get_legal_moves(piece)
            return False
    def make_move(self, piece, row, col):
        sr,sc=piece.row,piece.col;captured=self.board[row][col];move_info={'piece':piece,'start_pos':(sr,sc),'end_pos':(row,col),'captured_piece':captured,'original_has_moved':piece.has_moved,'previous_last_move':self.last_move,'promoted':False,'castling_rook_move':None,'en_passant_capture':None}
        self.board[sr][sc]=None;self.board[row][col]=piece;piece.move(row,col)
        if piece.piece_type=='king':
            if piece.color=='white':self.white_king_pos=(row,col)
            else:self.black_king_pos=(row,col)
            if abs(col-sc)==2:
                rs,rd=(0,3) if col<sc else (7,5);rook=self.board[row][rs];self.board[row][rs]=None;self.board[row][rd]=rook;rook.move(row,rd);move_info['castling_rook_move']=(rook,(row,rs),rook.has_moved)
        if piece.piece_type=='pawn':
            if row==0 or row==7:self.board[row][col]=Queen(row,col,piece.color);move_info['promoted']=True
            if not captured and abs(sc-col)==1:cp=(sr,col);target=self.board[cp[0]][cp[1]];self.board[cp[0]][cp[1]]=None;move_info['en_passant_capture']=(target,cp)
        self.last_move=(piece,(sr,sc),(row,col));return move_info
    def undo_move(self, move_info):
        p,sr,sc=move_info['piece'],move_info['start_pos'][0],move_info['start_pos'][1];er,ec=move_info['end_pos'][0],move_info['end_pos'][1]
        self.board[sr][sc]=p;p.row,p.col=sr,sc;p.has_moved=move_info['original_has_moved'];self.board[er][ec]=move_info['captured_piece']
        if p.piece_type=='king':
            if p.color=='white':self.white_king_pos=(sr,sc)
            else:self.black_king_pos=(sr,sc)
            if move_info['castling_rook_move']:r,rsp,rhm=move_info['castling_rook_move'];self.board[rsp[0]][rsp[1]]=r;self.board[r.row][r.col]=None;r.row,r.col=rsp;r.has_moved=rhm
        if move_info['promoted']:self.board[sr][sc]=p
        if move_info['en_passant_capture']:cp,pos=move_info['en_passant_capture'];self.board[pos[0]][pos[1]]=cp
        self.last_move=move_info['previous_last_move']
    def _change_turn(self): self.selected_piece,self.valid_moves,self.turn=None,[],'black' if self.turn=='white' else 'white'
    def get_legal_moves(self, piece):
        possible,legal=[],[]
        possible=self._get_possible_moves(piece)
        for move in possible:
            info=self.make_move(piece,move[0],move[1])
            if not self.is_in_check(piece.color):legal.append(move)
            self.undo_move(info)
        return legal
    def _get_possible_moves(self, piece):
        moves,r,c=[],piece.row,piece.col
        if piece.piece_type=='pawn':
            d=-1 if piece.color=='white' else 1
            if self._is_valid_square(r+d,c) and not self.board[r+d][c]:
                moves.append((r+d,c))
                if not piece.has_moved and self._is_valid_square(r+2*d,c) and not self.board[r+2*d][c]:moves.append((r+2*d,c))
            for dc in [-1,1]:
                if self._is_valid_square(r+d,c+dc) and self.board[r+d][c+dc] and self.board[r+d][c+dc].color!=piece.color:moves.append((r+d,c+dc))
            if self.last_move:
                lp,_,(er,ec)=self.last_move
                if lp.piece_type=='pawn' and abs(self.last_move[1][0]-er)==2 and r==er and abs(c-ec)==1:moves.append((r+d,ec))
        elif piece.piece_type=='knight':
            km=[(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)];[moves.extend(self._get_moves_in_direction(r,c,dr,dc,piece.color,True)) for dr,dc in km]
        elif piece.piece_type=='king':
            km=[(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)];[moves.extend(self._get_moves_in_direction(r,c,dr,dc,piece.color,True)) for dr,dc in km]
            if not piece.has_moved and not self.is_in_check(piece.color):
                if self.board[r][0] and not self.board[r][0].has_moved and not self.board[r][1] and not self.board[r][2] and not self.board[r][3]:
                    if not self._is_square_attacked(r,c-1,piece.color) and not self._is_square_attacked(r,c-2,piece.color):moves.append((r,c-2))
                if self.board[r][7] and not self.board[r][7].has_moved and not self.board[r][5] and not self.board[r][6]:
                    if not self._is_square_attacked(r,c+1,piece.color) and not self._is_square_attacked(r,c+2,piece.color):moves.append((r,c+2))
        else:
            dirs=[]
            if piece.piece_type in ['rook','queen']:dirs.extend([(1,0),(-1,0),(0,1),(0,-1)])
            if piece.piece_type in ['bishop','queen']:dirs.extend([(1,1),(1,-1),(-1,1),(-1,-1)])
            for dr,dc in dirs:moves.extend(self._get_moves_in_direction(r,c,dr,dc,piece.color))
        return moves
    def _get_moves_in_direction(self, r, c, dr, dc, color, single_step=False):
        moves,nr,nc=[],r+dr,c+dc
        while self._is_valid_square(nr,nc):
            target=self.board[nr][nc]
            if not target:moves.append((nr,nc))
            elif target.color!=color:moves.append((nr,nc));break
            else:break
            if single_step:break
            nr,nc=nr+dr,nc+dc
        return moves
    def _is_valid_square(self, r, c): return 0<=r<8 and 0<=c<8
    def _is_square_attacked(self, r, c, by_color):
        for row in range(8):
            for col in range(8):
                piece=self.board[row][col]
                if piece and piece.color!=by_color:
                    if self._can_piece_attack(piece,r,c):return True
        return False
    def _can_piece_attack(self, piece, target_r, target_c):
        r,c=piece.row,piece.col
        if piece.piece_type=='pawn':
            d=-1 if piece.color=='white' else 1
            if self._is_valid_square(r+d,c-1) and (r+d,c-1)==(target_r,target_c):return True
            if self._is_valid_square(r+d,c+1) and (r+d,c+1)==(target_r,target_c):return True
        elif piece.piece_type in ['king','knight']:
            moves=[]
            if piece.piece_type=='king':moves=[(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
            else:moves=[(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
            for dr,dc in moves:
                if self._is_valid_square(r+dr,c+dc) and (r+dr,c+dc)==(target_r,target_c):return True
        else:
            dirs=[]
            if piece.piece_type in ['rook','queen']:dirs.extend([(1,0),(-1,0),(0,1),(0,-1)])
            if piece.piece_type in ['bishop','queen']:dirs.extend([(1,1),(1,-1),(-1,1),(-1,-1)])
            for dr,dc in dirs:
                nr,nc=r+dr,c+dc
                while self._is_valid_square(nr,nc):
                    if (nr,nc)==(target_r,target_c):return True
                    if self.board[nr][nc] is not None:break
                    nr,nc=nr+dr,nc+dc
        return False
    def is_in_check(self, color):
        king_pos=self.white_king_pos if color=='white' else self.black_king_pos
        return self._is_square_attacked(king_pos[0],king_pos[1],color)
    def get_all_legal_moves(self, color):
        all_moves=[]
        for r in range(8):
            for c in range(8):
                piece=self.board[r][c]
                if piece and piece.color==color:
                    for move in self.get_legal_moves(piece):all_moves.append((piece,move[0],move[1]))
        return all_moves
    def check_game_over(self):
        if not self.get_all_legal_moves(self.turn):
            if self.is_in_check(self.turn):
                winner='Pretas' if self.turn=='white' else 'Brancas'
                return "checkmate",f"Xeque-mate! {winner} vencem."
            else:return "stalemate","Empate por Afogamento!"
        return None,None
    def evaluate(self):
        score,vals=0,{'pawn':1,'knight':3,'bishop':3,'rook':5,'queen':9,'king':0}
        for r in range(8):
            for c in range(8):
                piece=self.board[r][c]
                if piece:score+=vals[piece.piece_type] if piece.color=='white' else -vals[piece.piece_type]
        return score

# --- 3. INTELIGÊNCIA ARTIFICIAL (MINIMAX) ---
class AI:
    def __init__(self, difficulty):
        self.depth = difficulty
    def minimax(self, board, depth, alpha, beta, maximizing_player):
        game_status, _ = board.check_game_over()
        if depth == 0 or game_status is not None:
            return board.evaluate(), None
        if maximizing_player:
            max_eval, best_moves = -math.inf, []
            for piece, r, c in board.get_all_legal_moves('white'):
                move_info = board.make_move(piece, r, c); board._change_turn()
                evaluation, _ = self.minimax(board, depth - 1, alpha, beta, False)
                board._change_turn(); board.undo_move(move_info)
                if evaluation > max_eval: max_eval, best_moves = evaluation, [(piece, r, c)]
                elif evaluation == max_eval: best_moves.append((piece, r, c))
                alpha = max(alpha, evaluation)
                if beta <= alpha: break
            return max_eval, random.choice(best_moves) if best_moves else None
        else:
            min_eval, best_moves = math.inf, []
            for piece, r, c in board.get_all_legal_moves('black'):
                move_info = board.make_move(piece, r, c); board._change_turn()
                evaluation, _ = self.minimax(board, depth - 1, alpha, beta, True)
                board._change_turn(); board.undo_move(move_info)
                if evaluation < min_eval: min_eval, best_moves = evaluation, [(piece, r, c)]
                elif evaluation == min_eval: best_moves.append((piece, r, c))
                beta = min(beta, evaluation)
                if beta <= alpha: break
            return min_eval, random.choice(best_moves) if best_moves else None

# --- 4. CLASSE PRINCIPAL DO JOGO ---
class Game:
    def __init__(self, screen):
        self.screen=screen
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('arial', 20)
        self.coords_font = pygame.font.SysFont('arial', 16)
        self.title_font = pygame.font.SysFont('arial', 48, bold=True)
        self.history_font = pygame.font.SysFont('arial', 18)
        self.reset_game()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: self.running = False
                if self.game_state == 'menu': self._handle_menu_events(event)
                elif self.game_state == 'playing': self._handle_playing_events(event)
                elif self.game_state == 'game_over': self._handle_game_over_events(event)
            self.update_screen()
            self.clock.tick(60)
        pygame.quit(); sys.exit()

    def reset_game(self):
        self.board = Board(); self.game_state = 'menu'; self.game_over_message = ""
        self.ai = None; self.game_mode = None; self.buttons = {}; self.running = True
        self.move_history = []

    def _handle_menu_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for name, rect in self.buttons.items():
                if rect.collidepoint(event.pos): self._handle_button_click(name); break

    def _handle_playing_events(self, event):
        if self.game_mode == 'singleplayer' and self.board.turn == 'black': return
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            if BOARD_OFFSET <= pos[0] < BOARD_SIZE + BOARD_OFFSET and BOARD_OFFSET <= pos[1] < BOARD_SIZE + BOARD_OFFSET:
                col = (pos[0] - BOARD_OFFSET) // SQUARE_SIZE
                row = (pos[1] - BOARD_OFFSET) // SQUARE_SIZE
                if self.board.select_piece(row, col):
                    self._add_move_to_history()
                    status, msg = self.board.check_game_over()
                    if status: self.game_state, self.game_over_message = 'game_over', msg

    def _handle_game_over_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.buttons['play_again'].collidepoint(event.pos): self.reset_game()

    def _handle_button_click(self, name):
        if name == 'multiplayer': self.game_mode, self.game_state = 'multiplayer', 'playing'
        elif name.startswith('ai_'):
            diff = name.split('_')[1]
            self.ai = AI(DIFFICULTY_LEVELS[diff.capitalize()]); self.game_mode, self.game_state = 'singleplayer', 'playing'
    
    def _add_move_to_history(self):
        if not self.board.last_move: return
        piece, _, end_pos = self.board.last_move
        piece_name = self._translate_piece(piece)
        notation = self._get_algebraic_notation(end_pos[0], end_pos[1])
        self.move_history.append(f"{piece_name} para {notation}")

    def _get_algebraic_notation(self, r, c):
        return "ABCDEFGH"[c] + "87654321"[r]

    def _translate_piece(self, piece):
        pt_names = {'pawn': 'Peão', 'rook': 'Torre', 'knight': 'Cavalo', 'bishop': 'Bispo', 'queen': 'Rainha', 'king': 'Rei'}
        pt_colors = {'white': 'Branco', 'black': 'Preto'}
        return f"{pt_names[piece.piece_type]} {pt_colors[piece.color]}"

    def update_screen(self):
        self.screen.fill(MENU_BG_COLOR)
        if self.game_state == 'menu': self._draw_menu()
        elif self.game_state in ['playing', 'game_over']:
            self._draw_game_area()
            self._draw_sidebar()
            if self.game_state == 'playing' and self.game_mode == 'singleplayer' and self.board.turn == 'black': self._ai_move()
            if self.game_state == 'game_over': self._draw_game_over()
        pygame.display.flip()

    def _draw_menu(self):
        title = self.title_font.render("Xadrez Humano vs Gemini",True,WHITE); self.screen.blit(title,title.get_rect(center=(WIDTH/2,100)))
        self.buttons={}; y,w,h=200,300,50
        mp_rect=pygame.Rect((WIDTH-w)/2,y,w,h); self.buttons['multiplayer']=mp_rect; self._draw_button("Multiplayer Local",mp_rect); y+=70
        for name in DIFFICULTY_LEVELS.keys():
            sp_rect=pygame.Rect((WIDTH-w)/2,y,w,h); self.buttons[f'ai_{name.lower()}']=sp_rect; self._draw_button(f"vs Gemini ({name})",sp_rect); y+=60

    def _draw_button(self, text, rect):
        color=BUTTON_HOVER_COLOR if rect.collidepoint(pygame.mouse.get_pos()) else BUTTON_COLOR
        pygame.draw.rect(self.screen,color,rect,border_radius=10)
        surf=self.font.render(text,True,TEXT_COLOR); self.screen.blit(surf,surf.get_rect(center=rect.center))

    def _draw_game_area(self):
        board_rect = pygame.Rect(BOARD_OFFSET, BOARD_OFFSET, BOARD_SIZE, BOARD_SIZE)
        self.board.draw(self.screen.subsurface(board_rect))
        
        # Desenha coordenadas
        for i in range(8):
            # Letras (A-H)
            letter = self.coords_font.render("ABCDEFGH"[i], True, TEXT_COLOR)
            self.screen.blit(letter, (BOARD_OFFSET + i * SQUARE_SIZE + SQUARE_SIZE//2 - letter.get_width()//2, BOARD_OFFSET - 20))
            self.screen.blit(letter, (BOARD_OFFSET + i * SQUARE_SIZE + SQUARE_SIZE//2 - letter.get_width()//2, BOARD_OFFSET + BOARD_SIZE + 5))
            # Números (1-8)
            number = self.coords_font.render("87654321"[i], True, TEXT_COLOR)
            self.screen.blit(number, (BOARD_OFFSET - 20, BOARD_OFFSET + i * SQUARE_SIZE + SQUARE_SIZE//2 - letter.get_height()//2))
            self.screen.blit(number, (BOARD_OFFSET + BOARD_SIZE + 5, BOARD_OFFSET + i * SQUARE_SIZE + SQUARE_SIZE//2 - letter.get_height()//2))

    def _draw_sidebar(self):
        x = BOARD_OFFSET * 2 + BOARD_SIZE; y = BOARD_OFFSET
        
        turn = f"Turno: {'Brancas' if self.board.turn=='white' else 'Pretas'}"
        self.screen.blit(self.font.render(turn,True,TEXT_COLOR),(x,y)); y += 40
        
        if self.board.is_in_check(self.board.turn): self.screen.blit(self.font.render("XEQUE!",True,(255,100,100)),(x,y)); y += 40
        
        # Histórico de jogadas
        history_title = self.font.render("Histórico de Jogadas:", True, WHITE)
        self.screen.blit(history_title, (x, y)); y += 30
        
        # Mostra apenas os últimos movimentos que cabem na tela
        max_history_items = 22
        start_index = max(0, len(self.move_history) - max_history_items)
        display_history = self.move_history[start_index:]
        
        for move_text in display_history:
            self.screen.blit(self.history_font.render(move_text, True, TEXT_COLOR), (x, y))
            y += 22

    def _draw_game_over(self):
        s=pygame.Surface((WIDTH,HEIGHT),pygame.SRCALPHA);s.fill((0,0,0,180));self.screen.blit(s,(0,0))
        msg=self.title_font.render(self.game_over_message,True,WHITE);self.screen.blit(msg,msg.get_rect(center=(WIDTH/2,HEIGHT/2-50)))
        rect=pygame.Rect(WIDTH/2-150,HEIGHT/2+20,300,50);self.buttons['play_again']=rect;self._draw_button("Jogar Novamente",rect)
    
    def _ai_move(self):
        pygame.time.wait(100)
        _,best_move=self.ai.minimax(self.board,self.ai.depth,-math.inf,math.inf,False)
        if best_move:
            piece,r,c=best_move
            original_piece=self.board.board[piece.row][piece.col]
            if original_piece:
                self.board.make_move(original_piece,r,c);self.board._change_turn()
                self._add_move_to_history()
                status,msg=self.board.check_game_over()
                if status:self.game_state,self.game_over_message='game_over',msg
        else:
            status,msg=self.board.check_game_over()
            if status:self.game_state,self.game_over_message='game_over',msg

# --- 5. PONTO DE ENTRADA DO PROGRAMA ---
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Xadrez Humano vs Gemini")
    game = Game(screen)
    game.run()

if __name__ == "__main__":
    main()