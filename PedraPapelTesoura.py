import tkinter as tk
from tkinter import *
import random
from PIL import Image, ImageTk
import os

# cores
co0 = "#FFFFFF"  # white / branca
co1 = "#333333"  # black / preta
co2 = "#fcc058"  # orange / laranja
co3 = "#fff873"  # yellow / amarela
co4 = "#34eb3d"   # green / verde
co5 = "#e85151"   # red / vermelha
co6 = "#fcc058"    #orange
co7 = "e85151"    #vermelha
co8 = "#34eb3d"    #verde

fundo = "#3b3b3b"

# configurando a janela
janela = Tk()
janela.title('')
janela.geometry('520x560')
janela.configure(bg=fundo)

# Dividindo a janela
Frame_cima = Frame(janela, width=520, height=200, bg=co1, relief='raised')
Frame_cima.grid(row=0, column=0, sticky=NW)

Frame_baixo = Frame(janela, width=520, height=400, bg=co0, relief='flat')
Frame_baixo.grid(row=1, column=0, sticky=NW)

# configurando o frame cima
app_1 = Label(Frame_cima, text="Você", height=1, anchor='center', font=('Ivy 20 bold'), bg=co1, fg=co0)
app_1.place(x=70, y=140)

app_1_linha = Label(Frame_cima, text="", height=10, anchor='center', font=('Ivy 20 bold'), bg=co0, fg=co0)
app_1_linha.place(x=0, y=0)

app_1_pontos = Label(Frame_cima, text="0", height=1, anchor='center', font=('Ivy 40 bold'), bg=co1, fg=co0)
app_1_pontos.place(x=80, y=60)

app_ = Label(Frame_cima, text=":", height=1, anchor='center', font=('Ivy 40 bold'), bg=co1, fg=co0)
app_.place(x=255, y=60)

# configurando o frame cima_parte2
app_2 = Label(Frame_cima, text="PC", height=1, anchor='center', font=('Ivy 20 bold'), bg=co1, fg=co0)
app_2.place(x=400, y=140)

app_2_linha = Label(Frame_cima, text="", height=10, anchor='center', font=('Ivy 20 bold'), bg=co0, fg=co0)
app_2_linha.place(x=515, y=0)

app_2_pontos = Label(Frame_cima, text="0", height=1, anchor='center', font=('Ivy 40 bold'), bg=co1, fg=co0)
app_2_pontos.place(x=410, y=60)

app_linha = Label(Frame_cima, text="", width=520, anchor='center', font=('Ivy 1 bold'), bg=co3, fg=co0)
app_linha.place(x=0, y=195)

# variáveis globais
voce = ""
pontos_voce = 0
pontos_pc = 0
rondas = 5

# Função lógica do jogo
def jogar(escolha):
    global rondas, pontos_voce, pontos_pc, voce

    if rondas > 0:
        opcoes = ['Pedra', 'Papel', 'Tesoura']
        pc = random.choice(opcoes)
        voce = escolha

        # caso for igual
        if voce == pc:
            print('Empate')
            app_1_linha['bg'] = co0
            app_2_linha['bg'] = co0
            app_linha['bg'] = co3
        # para frente
        elif (voce == 'Pedra' and pc == 'Tesoura') or (voce == 'Papel' and pc == 'Pedra') or (voce == 'Tesoura' and pc == 'Papel'):
            print('Você ganhou!')
            pontos_voce += 1
            app_1_linha['bg'] = co4
            app_2_linha['bg'] = co0
            app_linha['bg'] = co0
        else:
            print('PC ganhou!')
            pontos_pc += 1
            app_1_linha['bg'] = co0
            app_2_linha['bg'] = co4
            app_linha['bg'] = co0

        rondas -= 1
        app_1_pontos.config(text=str(pontos_voce))
        app_2_pontos.config(text=str(pontos_pc))
    else:
        fim_do_jogo()

# Função para iniciar o jogo
def iniciar_jogo():
    global rondas, pontos_voce, pontos_pc
    rondas = 5
    pontos_voce = 0
    pontos_pc = 0
    app_1_pontos.config(text=str(pontos_voce))
    app_2_pontos.config(text=str(pontos_pc))
    app_1_linha['bg'] = co0
    app_2_linha['bg'] = co0
    app_linha['bg'] = co3

# Função para encerrar o jogo
def fim_do_jogo():
    global pontos_voce, pontos_pc
    if pontos_voce > pontos_pc:
        print("Você ganhou!")
    elif pontos_voce < pontos_pc:
        print("PC ganhou!")
    else:
        print("Empate!")

# Configurando Frame baixo
caminho_imagem_pedra = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'Imagens', 'pedra.png')
icon_pedra = Image.open(caminho_imagem_pedra)
icon_pedra.thumbnail((100, 100))
icon_pedra = ImageTk.PhotoImage(icon_pedra)

b_pedra = tk.Button(Frame_baixo, command=lambda: jogar('Pedra'), width=100, image=icon_pedra, compound=tk.CENTER, bg=co0, fg=co0, font=('Ivy 10 bold'), anchor=tk.CENTER, relief=tk.FLAT)
b_pedra.place(x=30, y=120)

caminho_imagem_papel = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'Imagens', 'papel.png')
icon_papel = Image.open(caminho_imagem_papel)
icon_papel.thumbnail((100, 100))
icon_papel = ImageTk.PhotoImage(icon_papel)

b_papel = tk.Button(Frame_baixo, command=lambda: jogar('Papel'), width=100, image=icon_papel, compound=tk.CENTER, bg=co0, fg=co0, font=('Ivy 10 bold'), anchor=tk.CENTER, relief=tk.FLAT)
b_papel.place(x=190, y=120)

caminho_imagem_tesoura = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'Imagens', 'tesoura.png')
icon_tesoura = Image.open(caminho_imagem_tesoura)
icon_tesoura.thumbnail((100, 100))
icon_tesoura = ImageTk.PhotoImage(icon_tesoura)

b_tesoura = tk.Button(Frame_baixo, command=lambda: jogar('Tesoura'), width=100, image=icon_tesoura, compound=tk.CENTER, bg=co0, fg=co0, font=('Ivy 10 bold'), anchor=tk.CENTER, relief=tk.FLAT)
b_tesoura.place(x=360, y=120)

# Configurando botão para iniciar o jogo
b_jogar = tk.Button(Frame_baixo, command=iniciar_jogo, width=29, text="Jogar", bg=fundo, fg=co0, font=('Ivy 20 bold'), anchor=tk.CENTER, relief=tk.RAISED, overrelief=RIDGE)
b_jogar.place(x=8, y=300)

janela.mainloop()
