from tkinter import *


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


# faz a execução da interface gráfica
root.mainloop()
