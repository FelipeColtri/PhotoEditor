#!/usr/bin/env python

import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageFilter

# Variáveis globais
imagem_carregada = None

# Função para abrir um arquivo de imagem
def abrir_arquivo():
    global imagem_carregada
    
    filetypes = (
        ('Imagens', '*.png *.jpg *.jpeg *.gif'),
        ('Todos os arquivos', '*.*')
    )
    
    arquivo = filedialog.askopenfile(filetypes=filetypes)
    
    if arquivo:
        imagem = Image.open(arquivo.name)
        imagem_carregada = imagem.copy()  # Armazenar a imagem original para a rotação
        imagem_exibir(imagem)

# Função para salvar um arquivo
def salvar_arquivo():
    if imagem_carregada:
        caminho_arquivo = filedialog.asksaveasfilename(defaultextension=".png")

        if caminho_arquivo:
            imagem_carregada.save(caminho_arquivo)

# Função para redimensionar a imagem e exibir inteira no painel
def imagem_exibir(imagem):
    largura_max = painel.winfo_width()
    altura_max = painel.winfo_height()
    largura, altura = imagem.size
    
    fator_redimensionamento = min(largura_max / largura, altura_max / altura)
    nova_largura = int(largura * fator_redimensionamento)
    nova_altura = int(altura * fator_redimensionamento)
    
    imagem_redimensionada = imagem.resize((nova_largura, nova_altura))
    imagem_tk = ImageTk.PhotoImage(imagem_redimensionada)
    painel.config(image=imagem_tk)
    painel.image = imagem_tk

# Função para rotacionar a imagem
def imagem_rotacionar(angulo):
    global imagem_carregada

    if imagem_carregada:
        imagem_carregada = imagem_carregada.rotate(angulo, expand=True)
        imagem_exibir(imagem_carregada)

# Função para espelhar horizontalmente e verticalmente a imagem
def imagem_flip(orientation):
    global imagem_carregada

    if imagem_carregada:
        if orientation == 'h':
            imagem_carregada = imagem_carregada.transpose(Image.FLIP_LEFT_RIGHT)
        elif orientation == 'v':
            imagem_carregada = imagem_carregada.transpose(Image.FLIP_TOP_BOTTOM)
        
        imagem_exibir(imagem_carregada)

# Função para tratar as cores da imagem
def imagem_cor(operation):
    global imagem_carregada

    if imagem_carregada:
        if operation == 'i':
            imagem_carregada = Image.eval(imagem_carregada, lambda x: 255 - x)
        elif operation == 'pb':
            imagem_carregada = imagem_carregada.convert('L')
        elif operation == 'b':
            imagem_carregada = imagem_carregada.filter(ImageFilter.BLUR)
        elif operation == 'c':
            imagem_carregada = imagem_carregada.filter(ImageFilter.CONTOUR)
        elif operation == 'e':
            imagem_carregada = imagem_carregada.filter(ImageFilter.EMBOSS)

        imagem_exibir(imagem_carregada)

# Criação da janela principal
janela = tk.Tk()

# Configuração da janela principal
janela.title("Photo Editor V0.1")

# Definir as dimensões da janela para o tamanho da tela
janela.geometry(f"{janela.winfo_screenwidth()}x{janela.winfo_screenheight()}")

# Menu lateral esquerdo
menu_lateral = tk.Frame(janela, width=100, bg="gray")
menu_lateral.pack(side=tk.LEFT, fill=tk.Y)

# Componentes do menu lateral
label_rotacionar_angulo = tk.Label(menu_lateral, text="Rotacionar:", bg="darkgray")
label_rotacionar_angulo.pack(fill=tk.X)

botao_rotacionar_esquerda = tk.Button(menu_lateral, text="Rotacionar Esquerda (-90°)", command=lambda: imagem_rotacionar(-90))
botao_rotacionar_esquerda.pack(fill=tk.X)

botao_rotacionar_direita = tk.Button(menu_lateral, text="Rotacionar Direita (+90°)", command=lambda: imagem_rotacionar(90))
botao_rotacionar_direita.pack(fill=tk.X)

input_rotacionar_angulo = tk.Entry(menu_lateral)
input_rotacionar_angulo.pack(fill=tk.X)

botao_rotacionar_angulo = tk.Button(menu_lateral, text="Rotacionar por Ângulo", command=lambda: imagem_rotacionar(int(input_rotacionar_angulo.get())))
botao_rotacionar_angulo.pack(fill=tk.X)

label_flips = tk.Label(menu_lateral, text="Espelhamentos:", bg="darkgray")
label_flips.pack(fill=tk.X)

botao_flip_horizontal = tk.Button(menu_lateral, text="Flip Horizontal", command=lambda: imagem_flip('h'))
botao_flip_horizontal.pack(fill=tk.X)

botao_flip_vertical = tk.Button(menu_lateral, text="Flip Vertical", command=lambda: imagem_flip('v'))
botao_flip_vertical.pack(fill=tk.X)

label_cores = tk.Label(menu_lateral, text="Opções de Cores:", bg="darkgray")
label_cores.pack(fill=tk.X)

botao_cor_inverter = tk.Button(menu_lateral, text="Inverter Cor", command=lambda: imagem_cor('i'))
botao_cor_inverter.pack(fill=tk.X)

botao_cor_preto_branco = tk.Button(menu_lateral, text="Preto e Branco", command=lambda: imagem_cor('pb'))
botao_cor_preto_branco.pack(fill=tk.X)

botao_cor_blur = tk.Button(menu_lateral, text="Filtro Borrar", command=lambda: imagem_cor('b'))
botao_cor_blur.pack(fill=tk.X)

botao_cor_contour = tk.Button(menu_lateral, text="Filtro Contorno", command=lambda: imagem_cor('c'))
botao_cor_contour.pack(fill=tk.X)

botao_cor_emboss = tk.Button(menu_lateral, text="Filtro Relevo", command=lambda: imagem_cor('e'))
botao_cor_emboss.pack(fill=tk.X)

# Painel para exibir a imagem
painel = tk.Label(janela)
painel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Menu superior
menu_superior = tk.Menu(janela)
menu_arquivo = tk.Menu(menu_superior, tearoff=0)
menu_arquivo.add_command(label="Abrir", command=abrir_arquivo)
menu_arquivo.add_command(label="Salvar", command=salvar_arquivo)
menu_superior.add_cascade(label="Arquivo", menu=menu_arquivo)
janela.config(menu=menu_superior)

# Iniciar o loop principal da janela
janela.mainloop()

