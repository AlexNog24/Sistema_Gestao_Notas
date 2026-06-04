import tkinter as ttk
from logica import iniciar_dados
from interface import (
    menu_gestao_alunos, menu_gestao_disciplinas, menu_gestao_notas,
    menu_relatorios, reiniciar_dados
)


# open_sudoku_tab()
gui = ttk.Tk()
gui.title("Gestão de Notas")
gui.resizable(False, False)
gui.geometry("450x650")

iniciar_dados()

titulo = ttk.Label(
    gui, text="SISTEMA DE GESTÃO DE NOTAS", font=("Arial", 12, "bold"))
titulo.pack(pady=(25, 5))

subtitulo = ttk.Label(gui, text="Bem-vindo!", font=("Arial", 10))
subtitulo.pack(pady=(0, 20))

btn_alunos = ttk.Button(gui, text="1. Gestão de Alunos",
                        width=30, height=2, command=menu_gestao_alunos)
btn_alunos.pack(pady=10)

btn_disciplinas = ttk.Button(gui,
                             command=menu_gestao_disciplinas,
                             text="2. Gestão de Disciplinas",
                             width=30,
                             height=2)
btn_disciplinas.pack(pady=10)

btn_notas = ttk.Button(gui,
                       command=menu_gestao_notas,
                       text="3. Gestão de Notas",
                       width=30,
                       height=2)
btn_notas.pack(pady=10)

btn_relatorios = ttk.Button(gui, text="4. Relatórios",
                            width=30, height=2, command=menu_relatorios)
btn_relatorios.pack(pady=10)

btn_reiniciar = ttk.Button(gui, text="5. Reiniciar Dados",
                           width=30, height=2, command=reiniciar_dados)
btn_reiniciar.pack(pady=10)

btn_sair = ttk.Button(gui, text="0. Sair", width=30,
                      height=2, command=gui.destroy)
btn_sair.pack(pady=10)
