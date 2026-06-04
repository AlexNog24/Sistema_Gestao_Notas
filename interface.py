import tkinter as tk
from tkinter import ttk, messagebox
import logica

# ---- FUNÇÕES DE INTERFACE GRÁFICA ----


def atualizar_treeview_alunos(tree, lista=None):
    if lista is None:
        lista = logica.alunos
    for item in tree.get_children():
        tree.delete(item)
    for a in lista:
        tree.insert("", "end", values=(a["id"], a["nome"]))


def menu_gestao_alunos():
    janela = tk.Toplevel()
    janela.title("Gestão de Alunos")
    janela.geometry("700x450")
    janela.grab_set()

    frame_inputs = tk.Frame(janela)
    frame_inputs.pack(pady=10)

    tk.Label(frame_inputs, text="ID:").grid(row=0, column=0, padx=5, pady=5)
    entry_id = tk.Entry(frame_inputs, width=10)
    entry_id.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(frame_inputs, text="Nome:").grid(row=0, column=2, padx=5, pady=5)
    entry_nome = tk.Entry(frame_inputs, width=30)
    entry_nome.grid(row=0, column=3, padx=5, pady=5)

    frame_botoes = tk.Frame(janela)
    frame_botoes.pack(pady=10)

    tree = ttk.Treeview(janela, columns=("ID", "Nome"), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Nome", text="Nome")
    tree.column("ID", width=50, anchor=tk.CENTER)
    tree.column("Nome", width=400, anchor=tk.W)
    tree.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

    def on_add():
        nome = entry_nome.get()
        msg = logica.adicionar_aluno(nome)
        if "ERRO" in msg:
            messagebox.showerror("Erro", msg)
        else:
            messagebox.showinfo("Sucesso", msg)
        atualizar_treeview_alunos(tree)

    def on_edit():
        try:
            id_a = int(entry_id.get())
            novo = entry_nome.get()
            msg = logica.editar_aluno(id_a, novo)
            if "ERRO" in msg:
                messagebox.showerror("Erro", msg)
            else:
                messagebox.showinfo("Sucesso", msg)
            atualizar_treeview_alunos(tree)
        except ValueError:
            messagebox.showerror("Erro", "O ID deve ser um número inteiro.")

    def on_remove():
        try:
            id_a = int(entry_id.get())
            if messagebox.askyesno("Confirmar", f"Tem a certeza que deseja remover o aluno com ID {id_a}?"):
                msg = logica.remover_aluno(id_a)
                if "ERRO" in msg:
                    messagebox.showerror("Erro", msg)
                else:
                    messagebox.showinfo("Sucesso", msg)
                atualizar_treeview_alunos(tree)
        except ValueError:
            messagebox.showerror("Erro", "O ID deve ser um número inteiro.")

    def on_search():
        termo = entry_nome.get()
        res = logica.pesquisar_alunos_por_nome(termo)
        atualizar_treeview_alunos(tree, res)

    def on_list_alpha():
        res = logica.listar_alunos_ordenados("nome")
        atualizar_treeview_alunos(tree, res)

    tk.Button(frame_botoes, text="Adicionar", width=10,
              command=on_add).grid(row=0, column=0, padx=5)
    tk.Button(frame_botoes, text="Editar", width=10,
              command=on_edit).grid(row=0, column=1, padx=5)
    tk.Button(frame_botoes, text="Remover", width=10,
              command=on_remove).grid(row=0, column=2, padx=5)
    tk.Button(frame_botoes, text="Pesquisar", width=10,
              command=on_search).grid(row=0, column=3, padx=5)
    tk.Button(frame_botoes, text="Ordem Alfabética", width=15,
              command=on_list_alpha).grid(row=0, column=4, padx=5)

    atualizar_treeview_alunos(tree)


def atualizar_treeview_disciplinas(tree, lista=None):
    if lista is None:
        lista = logica.disciplinas
    for item in tree.get_children():
        tree.delete(item)
    for d in lista:
        tree.insert("", "end", values=(d["id"], d["nome"]))


def menu_gestao_disciplinas():
    janela = tk.Toplevel()
    janela.title("Gestão de Disciplinas")
    janela.geometry("700x450")
    janela.grab_set()

    frame_inputs = tk.Frame(janela)
    frame_inputs.pack(pady=10)

    tk.Label(frame_inputs, text="ID:").grid(row=0, column=0, padx=5, pady=5)
    entry_id = tk.Entry(frame_inputs, width=10)
    entry_id.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(frame_inputs, text="Nome:").grid(row=0, column=2, padx=5, pady=5)
    entry_nome = tk.Entry(frame_inputs, width=30)
    entry_nome.grid(row=0, column=3, padx=5, pady=5)

    frame_botoes = tk.Frame(janela)
    frame_botoes.pack(pady=10)

    tree = ttk.Treeview(janela, columns=("ID", "Nome"), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Nome", text="Nome")
    tree.column("ID", width=50, anchor=tk.CENTER)
    tree.column("Nome", width=400, anchor=tk.W)
    tree.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

    def on_add():
        nome = entry_nome.get()
        msg = logica.adicionar_disciplina(nome)
        if "ERRO" in msg:
            messagebox.showerror("Erro", msg)
        else:
            messagebox.showinfo("Sucesso", msg)
        atualizar_treeview_disciplinas(tree)

    def on_edit():
        try:
            id_d = int(entry_id.get())
            novo = entry_nome.get()
            msg = logica.editar_disciplina(id_d, novo)
            if "ERRO" in msg:
                messagebox.showerror("Erro", msg)
            else:
                messagebox.showinfo("Sucesso", msg)
            atualizar_treeview_disciplinas(tree)
        except ValueError:
            messagebox.showerror("Erro", "O ID deve ser um número inteiro.")

    def on_remove():
        try:
            id_d = int(entry_id.get())
            if messagebox.askyesno("Confirmar", f"Tem a certeza que deseja remover a disciplina com ID {id_d}?"):
                msg = logica.remover_disciplina(id_d)
                if "ERRO" in msg:
                    messagebox.showerror("Erro", msg)
                else:
                    messagebox.showinfo("Sucesso", msg)
                atualizar_treeview_disciplinas(tree)
        except ValueError:
            messagebox.showerror("Erro", "O ID deve ser um número inteiro.")

    def on_search():
        termo = entry_nome.get()
        res = logica.pesquisar_disciplinas_por_nome(termo)
        atualizar_treeview_disciplinas(tree, res)

    def on_list_alpha():
        res = logica.listar_disciplinas_ordenadas("nome")
        atualizar_treeview_disciplinas(tree, res)

    tk.Button(frame_botoes, text="Adicionar", width=10,
              command=on_add).grid(row=0, column=0, padx=5)
    tk.Button(frame_botoes, text="Editar", width=10,
              command=on_edit).grid(row=0, column=1, padx=5)
    tk.Button(frame_botoes, text="Remover", width=10,
              command=on_remove).grid(row=0, column=2, padx=5)
    tk.Button(frame_botoes, text="Pesquisar", width=10,
              command=on_search).grid(row=0, column=3, padx=5)
    tk.Button(frame_botoes, text="Ordem Alfabética", width=15,
              command=on_list_alpha).grid(row=0, column=4, padx=5)

    atualizar_treeview_disciplinas(tree)


def menu_gestao_notas():
    janela = tk.Toplevel()
    janela.title("Gestão de Notas")
    janela.geometry("700x450")
    janela.grab_set()

    frame_inputs = tk.Frame(janela)
    frame_inputs.pack(pady=10)

    tk.Label(frame_inputs, text="ID Aluno:").grid(
        row=0, column=0, padx=5, pady=5)
    entry_id_aluno = tk.Entry(frame_inputs, width=10)
    entry_id_aluno.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(frame_inputs, text="ID Disciplina:").grid(
        row=0, column=2, padx=5, pady=5)
    entry_id_disc = tk.Entry(frame_inputs, width=10)
    entry_id_disc.grid(row=0, column=3, padx=5, pady=5)

    tk.Label(frame_inputs, text="Nota:").grid(row=0, column=4, padx=5, pady=5)
    entry_nota = tk.Entry(frame_inputs, width=10)
    entry_nota.grid(row=0, column=5, padx=5, pady=5)

    frame_botoes = tk.Frame(janela)
    frame_botoes.pack(pady=10)

    tree = ttk.Treeview(janela, columns=("Ref", "Nota"), show="headings")
    tree.heading("Ref", text="Aluno / Disciplina")
    tree.heading("Nota", text="Nota")
    tree.column("Ref", width=300, anchor=tk.W)
    tree.column("Nota", width=100, anchor=tk.CENTER)
    tree.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

    def on_atribuir():
        try:
            id_a = int(entry_id_aluno.get())
            id_d = int(entry_id_disc.get())
            nota = float(entry_nota.get())
            msg = logica.atribuir_nota(id_a, id_d, nota)
            if "ERRO" in msg:
                messagebox.showerror("Erro", msg)
            else:
                messagebox.showinfo("Sucesso", msg)
        except ValueError:
            messagebox.showerror(
                "Erro", "Verifique se os IDs são inteiros e a nota é numérica.")

    def on_consultar_aluno():
        try:
            id_a = int(entry_id_aluno.get())
            aluno = logica.obter_aluno_por_id(id_a)
            if not aluno:
                messagebox.showerror("Erro", "Aluno não encontrado.")
                return
            for item in tree.get_children():
                tree.delete(item)
            for res in logica.notas_do_aluno(id_a):
                nota = f"{res['nota']:.1f}" if res['nota'] is not None else "(sem nota)"
                tree.insert("", "end", values=(res["disciplina"], nota))
        except ValueError:
            messagebox.showerror("Erro", "ID do aluno inválido.")

    def on_consultar_disc():
        try:
            id_d = int(entry_id_disc.get())
            disc = logica.obter_disciplina_por_id(id_d)
            if not disc:
                messagebox.showerror("Erro", "Disciplina não encontrada.")
                return
            for item in tree.get_children():
                tree.delete(item)
            for res in logica.notas_da_disciplina(id_d):
                nota = f"{res['nota']:.1f}" if res['nota'] is not None else "(sem nota)"
                tree.insert("", "end", values=(res["aluno"], nota))
        except ValueError:
            messagebox.showerror("Erro", "ID da disciplina inválido.")

    tk.Button(frame_botoes, text="Atribuir Nota",
              command=on_atribuir).grid(row=0, column=0, padx=5)
    tk.Button(frame_botoes, text="Consultar por Aluno (usa ID)",
              command=on_consultar_aluno).grid(row=0, column=1, padx=5)
    tk.Button(frame_botoes, text="Consultar por Disc. (usa ID)",
              command=on_consultar_disc).grid(row=0, column=2, padx=5)


def menu_relatorios():
    janela = tk.Toplevel()
    janela.title("Relatórios")
    janela.geometry("700x450")
    janela.grab_set()

    frame_inputs = tk.Frame(janela)
    frame_inputs.pack(pady=10)

    tk.Label(frame_inputs, text="ID Aluno:").grid(
        row=0, column=0, padx=5, pady=5)
    entry_id_aluno = tk.Entry(frame_inputs, width=10)
    entry_id_aluno.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(frame_inputs, text="ID Disciplina:").grid(
        row=0, column=2, padx=5, pady=5)
    entry_id_disc = tk.Entry(frame_inputs, width=10)
    entry_id_disc.grid(row=0, column=3, padx=5, pady=5)

    frame_botoes = tk.Frame(janela)
    frame_botoes.pack(pady=10)

    text_area = tk.Text(janela, state=tk.DISABLED, width=70, height=15)
    text_area.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

    def escrever_texto(texto):
        text_area.config(state=tk.NORMAL)
        text_area.delete("1.0", tk.END)
        text_area.insert(tk.END, texto)
        text_area.config(state=tk.DISABLED)

    def on_media_aluno():
        try:
            id_a = int(entry_id_aluno.get())
            aluno = logica.obter_aluno_por_id(id_a)
            if not aluno:
                messagebox.showerror("Erro", "Aluno não encontrado.")
                return
            m = logica.media_aluno(id_a)
            if m is None:
                escrever_texto(
                    f"O aluno '{aluno['nome']}' não tem notas registadas.\n")
            else:
                escrever_texto(
                    f"Média de '{aluno['nome']}': {m:.2f} valores\n")
        except ValueError:
            messagebox.showerror("Erro", "ID do aluno inválido.")

    def on_media_disc():
        try:
            id_d = int(entry_id_disc.get())
            disc = logica.obter_disciplina_por_id(id_d)
            if not disc:
                messagebox.showerror("Erro", "Disciplina não encontrada.")
                return
            m = logica.media_disciplina(id_d)
            if m is None:
                escrever_texto(f"Sem notas registadas em '{disc['nome']}'.\n")
            else:
                escrever_texto(f"Média de '{disc['nome']}': {m:.2f} valores\n")
        except ValueError:
            messagebox.showerror("Erro", "ID da disciplina inválido.")

    def on_resumo():
        r = logica.resumo_geral()
        linhas = [
            f"Total de alunos      : {r['total_alunos']}",
            f"Total de disciplinas : {r['total_disciplinas']}",
            f"Total de notas       : {r['total_notas']}\n"
        ]

        if r["ranking"]:
            linhas.append("Ranking de alunos por média:")
            linhas.append(f"{'Pos':<5}{'Aluno':<20}| Média")
            linhas.append("-" * 40)
            for pos, item in enumerate(r["ranking"], 1):
                linhas.append(
                    f"{pos:<5}{item['nome']:<20}| {item['media']:.2f}")
        else:
            linhas.append("Sem notas registadas para gerar ranking.")

        escrever_texto("\n".join(linhas) + "\n")

    tk.Button(frame_botoes, text="Média Aluno",
              command=on_media_aluno).grid(row=0, column=0, padx=5)
    tk.Button(frame_botoes, text="Média Disciplina",
              command=on_media_disc).grid(row=0, column=1, padx=5)
    tk.Button(frame_botoes, text="Resumo Geral e Ranking",
              command=on_resumo).grid(row=0, column=2, padx=5)


def reiniciar_dados():
    if messagebox.askyesno("Confirmar", "Tem a certeza que quer apagar todos os dados?"):
        logica.reset()
        messagebox.showinfo("Sucesso", "Sistema reiniciado com sucesso.")


def menu_principal():
    """
    Função mantida para compatibilidade. Se executar o main.py, 
    ele fará o redirecionamento automático para a interface Tkinter.
    """
    import tkinterEXP
