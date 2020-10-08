import tkinter.ttk as ttk
from tkinter import *

from ttkthemes import ThemedStyle


def adivinhar():
    """
    -> Analisa cada Checkbutton selecionado e soma à própria variável "resul"
    Após fazer o cálculo, configura o texto do placar para o número obtido
    :return: não há
    """
    resul = 0
    if v_verde.get():
        resul += 1
    if v_vermelho.get():
        resul += 2
    if v_azul.get():
        resul += 4
    if v_amarelo.get():
        resul += 8
    if v_marrom.get():
        resul += 16
    if v_roxo.get():
        resul += 32
    placar.configure(text=resul)

# INICIALIZAÇÃO DA JANELA
root = Tk()
root.title('Quadros Mágicos')

# CONFIGURAÇÕES DO ESTILO DA JANELA
style = ThemedStyle(root)
style.set_theme('breeze')
# CONFIGURAÇÃO DO ESTILO PARA O BOTÃO
style.configure('my.TButton', font=('Arial', 12, 'bold'))

# IMAGEM
quadro_img = PhotoImage(file='img/quadrado_magico.png')

lb_quadro = ttk.Label(root, image=quadro_img)

lb_instrucao = ttk.Label(root,
                         text='Pense em um  número de 1~60 e selecione os quadros onde ele está (pode estar em mais de um):',
                         font="Arial 12 bold")

# COMBOBOXES VARIABLES
v_verde = IntVar()
v_vermelho = IntVar()
v_azul = IntVar()
v_amarelo = IntVar()
v_marrom = IntVar()
v_roxo = IntVar()

# COMBOBOXES
cb_verde = ttk.Checkbutton(root, text='VERDE', variable=v_verde)
cb_vermelho = ttk.Checkbutton(root, text='VERMELHO', variable=v_vermelho)
cb_azul = ttk.Checkbutton(root, text='AZUL', variable=v_azul)
cb_amarelo = ttk.Checkbutton(root, text='AMARELO', variable=v_amarelo)
cb_marrom = ttk.Checkbutton(root, text='MARROM', variable=v_marrom)
cb_roxo = ttk.Checkbutton(root, text='ROXO', variable=v_roxo)

botao = ttk.Button(root, text='Adivinhar', command=adivinhar, width=45, style='my.TButton')

# RESULTADO DA ADIVINHAÇÃO
placar = ttk.Label(root, font="Arial 50 bold", foreground='green')

# GRIDS
lb_quadro.grid(row=0, columnspan=6)
lb_instrucao.grid(row=1, columnspan=6)
cb_verde.grid(row=2, column=0, pady=10)
cb_vermelho.grid(row=2, column=1, pady=10)
cb_azul.grid(row=2, column=2, pady=10)
cb_amarelo.grid(row=2, column=3, pady=10)
cb_marrom.grid(row=2, column=4, pady=10)
cb_roxo.grid(row=2, column=5, pady=10)
botao.grid(row=3, columnspan=6, pady=10)
placar.grid(row=4, columnspan=6)

root.mainloop()
