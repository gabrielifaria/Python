import tkinter as tk  # Importa a biblioteca tkinter com alias 'tk'
from tkinter import messagebox  # Importa a classe 'messagebox' do tkinter
import random  # Importa a biblioteca random para gerar números aleatórios

# Definindo as configurações do jogo
NUM_LINHAS = 4  # Número de linhas na grade do jogo
NUM_COLUNAS = 4  # Número de colunas na grade do jogo
CARTAO_SIZE_W = 10  # Largura dos cartões
CARTAO_SIZE_H = 5  # Altura dos cartões
CORES_CARTAO = ['aliceblue', 'antiquewhite4', 'aquamarine3', 'blueviolet', 'cadetblue1', 'cadetblue1', 'coral2', 'coral2']  # Cores dos cartões
COR_FUNDO = "#343a40"  # Cor de fundo da janela
COR_LETRA = "white"  # Cor do texto
FONT_STYLE = ('Arial', 12, 'bold')  # Estilo da fonte
MAX_TENTATIVAS = 25  # Número máximo de tentativas permitidas

# Criando a interface principal
janela = tk.Tk()  # Cria uma janela principal
janela.title('Jogo da Memória')  # Define o título da janela
janela.configure(bg=COR_FUNDO)  # Configura a cor de fundo da janela

# Personalizando botão:
estilo_botao = {'activebackground': '#f8f9fa', 'font': FONT_STYLE, 'fg': COR_LETRA}
janela.option_add('*Button', estilo_botao)  # Define o estilo dos botões

# Label para número de tentativas
label_tentativas = tk.Label(janela, text='Tentativas: {}/{}'.format(9, MAX_TENTATIVAS), fg=COR_LETRA, bg=COR_FUNDO,
                            font=FONT_STYLE)  # Cria um rótulo para exibir o número de tentativas
# Criar grid para cartões
label_tentativas.grid(row=NUM_LINHAS, columnspan=NUM_COLUNAS, padx=10, pady=10)  # Coloca o rótulo na janela


# Cria uma grade aleatória de cores para os cartões
def create_card_grid():
    cores = CORES_CARTAO * 2  # Duplica as cores para que haja pares correspondentes
    random.shuffle(cores)  # Embaralha a ordem das cores
    grid = []
    for _ in range(NUM_LINHAS):
        linha = []
        for _ in range(NUM_COLUNAS):
            cor = cores.pop()  # Pega a próxima cor da lista
            linha.append(cor) #acrecenta a proxima cor ao vetor linha
        grid.append(linha) #acrescenta a linha a grade
    return grid #retorna a grade


# Resposta aos cliques do jogador nos cartões
def card_clicked(linha, coluna):
    cartao = cartoes[linha][coluna]
    cor = cartao['bg']
    if cor == 'black':
        cartao['bg'] = grid[linha][coluna]  # Altera a cor do cartão para revelar a cor escolhida
        cartao_revelado.append(cartao)  # Adiciona o cartão à lista de cartões revelados
        if len(cartao_revelado) == 2:
            check_match()  # Verifica se há uma correspondência


# Verificar se os dois cartões são iguais
def check_match():
    cartao1, cartao2 = cartao_revelado  # Obtém os dois cartões revelados
    if cartao1['bg'] == cartao2['bg']:  # Se as cores dos cartões forem iguais, os cartões correspondem
        cartao1.after(1000, cartao1.destroy)  # Destroi o primeiro cartão após 1 segundo
        cartao2.after(1000, cartao2.destroy)  # Destroi o segundo cartão após 1 segundo
        cartas_correspondentes.extend([cartao1, cartao2])  # Adiciona os cartões correspondentes à lista
        check_win()  # Verifica se o jogador ganhou
    else:
        cartao1.after(1000, lambda: cartao1.config(bg='black'))  # Volta a esconder o primeiro cartão após 1 segundo
        cartao2.after(1000, lambda: cartao2.config(bg='black'))  # Volta a esconder o segundo cartão após 1 segundo
    cartao_revelado.clear()  # Limpa a lista de cartões revelados
    update_score()  # Atualiza a pontuação


# Verificar se o jogador ganhou o jogo
def check_win():
    if len(cartas_correspondentes) == NUM_LINHAS * NUM_COLUNAS:
        messagebox.showinfo('Parabéns!', "Você ganhou o jogo!")  # Exibe uma mensagem de parabéns
        janela.quit()  # Fecha a janela do jogo


# Atualizar a pontuação e verificar derrota
def update_score():
    global numero_tentativas
    numero_tentativas += 1
    label_tentativas.config(text='Tentativas: {}/{}'.format(numero_tentativas, MAX_TENTATIVAS))  # Atualiza o texto do rótulo
    if numero_tentativas >= MAX_TENTATIVAS:
        messagebox.showinfo('FIM DE JOGO', "VOCÊ PERDEU!")  # Exibe uma mensagem de derrota


# Criar grade de cartões
grid = create_card_grid()  # Chama a função para criar a grade de cartões
cartoes = []  # Lista para armazenar os cartões
cartao_revelado = []  # Lista para armazenar os cartões revelados
cartas_correspondentes = []  # Lista para armazenar os pares de cartões correspondentes
numero_tentativas = 0  # Variável para contar o número de tentativas

for linha in range(NUM_LINHAS):
    linha_de_cartoes = []
    for col in range(NUM_COLUNAS):
        cartao = tk.Button(janela, command=lambda r=linha, c=col: card_clicked(r, c), width=CARTAO_SIZE_W,
                           height=CARTAO_SIZE_H, bg='black', relief=tk.RAISED, bd=3)
        cartao.grid(row=linha, column=col, padx=5, pady=5)  # Coloca os botões na janela
        linha_de_cartoes.append(cartao)
    cartoes.append(linha_de_cartoes)

janela.mainloop()  # Inicia o loop principal da interface gráfica
