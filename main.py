from tkinter import *
from datetime import datetime
import time


root = Tk()
root.title("Análise Fundamentalista")

# ------------------------------------- VISUAL ------------------------------------ #
#cores pré definidas
COR_BASE = "#3788ab"

#define largura x altura
root.geometry("800x600")
#define se a janela pode ser redimensionada
root.resizable(True, True)
#background color
root.config(bg=COR_BASE)
#define icone da janela
root.iconphoto(False, PhotoImage(file=r'C:\Users\altie\OneDrive\Altieri\Softwares\Dev\Projetos Pessoais\Projeto_Exe_Anali_Acoes\assets\images\financial-profit.png'))
# ------------------------------------- X ------------------------------------ #

# ---------------------------------- FUNÇÕES --------------------------------- #
def obter_hora():
    hora = datetime.now().hour
    if 6 <= hora < 12:
        return "Bom dia"
    elif 12 <= hora < 18:
        return "Boa tarde"
    else:
        return "Boa noite"


# ----------------------------------- LABEL ---------------------------------- #
#SAUDAÇÃO
saudacao = obter_hora()
label_ola = Label(root, text=saudacao, anchor=W, padx=10, width=10, height=2, bg='#3788ab', font=("Courier", 20), fg="white")
label_ola.grid(row=0, column=0)

#USUÁRIO
label_user = Label(root, text="Usuário:", anchor=W, padx=10, width=15, height=2,  bg='#4788ab', font=("Courier", 15))
label_user.grid(row=1, column=1)

label_password = Label(root, text="Senha:", anchor=W, padx=10, width=15, height=2,  bg='#4788ab', font=("Courier", 15))
label_password.grid(row=2, column=1)


# faz a execução da interface gráfica
root.mainloop()
