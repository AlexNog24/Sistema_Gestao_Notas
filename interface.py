import logica


# ---- UTILITÁRIOS DE INPUT ----

def ler_inteiro(mensagem):
    """Lê um inteiro do utilizador, repetindo até ser válido."""
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("  Valor inválido. Introduza um número inteiro.")


def ler_real(mensagem):
    """Lê um float do utilizador, repetindo até ser válido."""
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("  Valor inválido. Introduza um número (ex: 14.5).")


def ler_texto(mensagem):
    """Lê uma string não vazia do utilizador."""
    while True:
        valor = input(mensagem).strip()
        if valor:
            return valor
        print("  O campo não pode estar vazio.")


def separador():
    print("-" * 40)


# ---- LISTAGENS AUXILIARES ----

def mostrar_lista_alunos(lista=None):
    if lista is None:
        lista = logica.alunos
    print("ID  | Nome do Aluno")
    separador()
    if not lista:
        print("  Nenhum aluno encontrado.")
    for a in lista:
        print(f"{a['id']:<4}| {a['nome']}")
    separador()


def mostrar_lista_disciplinas(lista=None):
    if lista is None:
        lista = logica.disciplinas
    print("ID  | Nome da Disciplina")
    separador()
    if not lista:
        print("  Nenhuma disciplina encontrada.")
    for d in lista:
        print(f"{d['id']:<4}| {d['nome']}")
    separador()


# ---- MENUS DE ALUNOS ----

def menu_gestao_alunos():
    while True:
        print("\n---- GESTÃO DE ALUNOS ----")
        print("1. Listar Alunos")
        print("2. Adicionar Aluno")
        print("3. Editar Aluno")
        print("4. Remover Aluno")
        print("5. Pesquisar Aluno por Nome")
        print("6. Listar por Ordem Alfabética")
        print("0. Voltar")
        opcao = ler_inteiro("Opção: ")

        if opcao == 1:
            print("\n---- LISTA DE ALUNOS ----")
            mostrar_lista_alunos()
        elif opcao == 2:
            print("\n---- ADICIONAR ALUNO ----")
            nome = ler_texto("Nome do novo aluno: ")
            print(logica.adicionar_aluno(nome))
        elif opcao == 3:
            print("\n---- EDITAR ALUNO ----")
            mostrar_lista_alunos()
            id_a = ler_inteiro("ID do aluno a editar: ")
            novo = ler_texto("Novo nome: ")
            print(logica.editar_aluno(id_a, novo))
        elif opcao == 4:
            print("\n---- REMOVER ALUNO ----")
            mostrar_lista_alunos()
            id_a = ler_inteiro("ID do aluno a remover: ")
            confirmacao = input("Tem a certeza? (s/n): ").strip().lower()
            if confirmacao == "s":
                print(logica.remover_aluno(id_a))
            else:
                print("Operação cancelada.")
        elif opcao == 5:
            print("\n---- PESQUISAR ALUNO ----")
            termo = ler_texto("Nome (ou parte do nome): ")
            resultado = logica.pesquisar_alunos_por_nome(termo)
            mostrar_lista_alunos(resultado)
        elif opcao == 6:
            print("\n---- ALUNOS POR ORDEM ALFABÉTICA ----")
            mostrar_lista_alunos(logica.listar_alunos_ordenados("nome"))
        elif opcao == 0:
            break
        else:
            print("Opção inválida!")


# ---- MENUS DE DISCIPLINAS ----

def menu_gestao_disciplinas():
    while True:
        print("\n---- GESTÃO DE DISCIPLINAS ----")
        print("1. Listar Disciplinas")
        print("2. Adicionar Disciplina")
        print("3. Editar Disciplina")
        print("4. Remover Disciplina")
        print("5. Pesquisar Disciplina por Nome")
        print("6. Listar por Ordem Alfabética")
        print("0. Voltar")
        opcao = ler_inteiro("Opção: ")

        if opcao == 1:
            print("\n---- LISTA DE DISCIPLINAS ----")
            mostrar_lista_disciplinas()
        elif opcao == 2:
            print("\n---- ADICIONAR DISCIPLINA ----")
            nome = ler_texto("Nome da nova disciplina: ")
            print(logica.adicionar_disciplina(nome))
        elif opcao == 3:
            print("\n---- EDITAR DISCIPLINA ----")
            mostrar_lista_disciplinas()
            id_d = ler_inteiro("ID da disciplina a editar: ")
            novo = ler_texto("Novo nome: ")
            print(logica.editar_disciplina(id_d, novo))
        elif opcao == 4:
            print("\n---- REMOVER DISCIPLINA ----")
            mostrar_lista_disciplinas()
            id_d = ler_inteiro("ID da disciplina a remover: ")
            confirmacao = input("Tem a certeza? (s/n): ").strip().lower()
            if confirmacao == "s":
                print(logica.remover_disciplina(id_d))
            else:
                print("Operação cancelada.")
        elif opcao == 5:
            print("\n---- PESQUISAR DISCIPLINA ----")
            termo = ler_texto("Nome (ou parte do nome): ")
            resultado = logica.pesquisar_disciplinas_por_nome(termo)
            mostrar_lista_disciplinas(resultado)
        elif opcao == 6:
            print("\n---- DISCIPLINAS POR ORDEM ALFABÉTICA ----")
            mostrar_lista_disciplinas(logica.listar_disciplinas_ordenadas("nome"))
        elif opcao == 0:
            break
        else:
            print("Opção inválida!")


# ---- MENUS DE NOTAS ----

def menu_gestao_notas():
    while True:
        print("\n---- GESTÃO DE NOTAS ----")
        print("1. Atribuir / Alterar Nota")
        print("2. Consultar Notas de um Aluno")
        print("3. Consultar Notas de uma Disciplina")
        print("0. Voltar")
        opcao = ler_inteiro("Opção: ")

        if opcao == 1:
            print("\n---- ATRIBUIR / ALTERAR NOTA ----")
            if not logica.alunos:
                print("ERRO: Não há alunos registados.")
            elif not logica.disciplinas:
                print("ERRO: Não há disciplinas registadas.")
            else:
                mostrar_lista_alunos()
                id_a = ler_inteiro("ID do aluno: ")
                mostrar_lista_disciplinas()
                id_d = ler_inteiro("ID da disciplina: ")
                valor = ler_real("Nota (0 a 20): ")
                print(logica.atribuir_nota(id_a, id_d, valor))

        elif opcao == 2:
            print("\n---- NOTAS DO ALUNO ----")
            if not logica.alunos:
                print("ERRO: Não há alunos registados.")
            else:
                mostrar_lista_alunos()
                id_a = ler_inteiro("ID do aluno: ")
                aluno = logica.obter_aluno_por_id(id_a)
                if not aluno:
                    print("ERRO: Aluno não encontrado.")
                else:
                    print(f"\nNotas de {aluno['nome']}:")
                    print(f"{'Disciplina':<20}| Nota")
                    separador()
                    for item in logica.notas_do_aluno(id_a):
                        nota_str = f"{item['nota']:.1f}" if item["nota"] is not None else "(sem nota)"
                        print(f"{item['disciplina']:<20}| {nota_str}")
                    separador()

        elif opcao == 3:
            print("\n---- NOTAS DA DISCIPLINA ----")
            if not logica.disciplinas:
                print("ERRO: Não há disciplinas registadas.")
            else:
                mostrar_lista_disciplinas()
                id_d = ler_inteiro("ID da disciplina: ")
                disc = logica.obter_disciplina_por_id(id_d)
                if not disc:
                    print("ERRO: Disciplina não encontrada.")
                else:
                    print(f"\nNotas em {disc['nome']}:")
                    print(f"{'Aluno':<20}| Nota")
                    separador()
                    for item in logica.notas_da_disciplina(id_d):
                        nota_str = f"{item['nota']:.1f}" if item["nota"] is not None else "(sem nota)"
                        print(f"{item['aluno']:<20}| {nota_str}")
                    separador()

        elif opcao == 0:
            break
        else:
            print("Opção inválida!")


# ---- MENUS DE RELATÓRIOS ----

def menu_relatorios():
    while True:
        print("\n---- RELATÓRIOS ----")
        print("1. Média de um Aluno")
        print("2. Média de uma Disciplina")
        print("3. Resumo Geral e Ranking")
        print("0. Voltar")
        opcao = ler_inteiro("Opção: ")

        if opcao == 1:
            print("\n---- MÉDIA DO ALUNO ----")
            if not logica.alunos:
                print("ERRO: Não há alunos registados.")
            else:
                mostrar_lista_alunos()
                id_a = ler_inteiro("ID do aluno: ")
                aluno = logica.obter_aluno_por_id(id_a)
                if not aluno:
                    print("ERRO: Aluno não encontrado.")
                else:
                    m = logica.media_aluno(id_a)
                    if m is None:
                        print(f"O aluno '{aluno['nome']}' não tem notas registadas.")
                    else:
                        print(f"Média de '{aluno['nome']}': {m:.2f} valores")

        elif opcao == 2:
            print("\n---- MÉDIA DA DISCIPLINA ----")
            if not logica.disciplinas:
                print("ERRO: Não há disciplinas registadas.")
            else:
                mostrar_lista_disciplinas()
                id_d = ler_inteiro("ID da disciplina: ")
                disc = logica.obter_disciplina_por_id(id_d)
                if not disc:
                    print("ERRO: Disciplina não encontrada.")
                else:
                    m = logica.media_disciplina(id_d)
                    if m is None:
                        print(f"Sem notas registadas em '{disc['nome']}'.")
                    else:
                        print(f"Média de '{disc['nome']}': {m:.2f} valores")

        elif opcao == 3:
            print("\n---- RESUMO GERAL ----")
            r = logica.resumo_geral()
            print(f"Total de alunos      : {r['total_alunos']}")
            print(f"Total de disciplinas : {r['total_disciplinas']}")
            print(f"Total de notas       : {r['total_notas']}")
            if r["ranking"]:
                print("\nRanking de alunos por média:")
                print(f"{'Pos':<5}{'Aluno':<20}| Média")
                separador()
                for pos, item in enumerate(r["ranking"], 1):
                    print(f"{pos:<5}{item['nome']:<20}| {item['media']:.2f}")
                separador()
            else:
                print("Sem notas registadas para gerar ranking.")

        elif opcao == 0:
            break
        else:
            print("Opção inválida!")


# ---- MENU PRINCIPAL ----

def menu_principal():
    logica.iniciar_dados()

    while True:
        print("\n==== SISTEMA DE GESTÃO DE NOTAS ====")
        print("1. Gestão de Alunos")
        print("2. Gestão de Disciplinas")
        print("3. Gestão de Notas")
        print("4. Relatórios")
        print("5. Reiniciar Dados")
        print("0. Sair")
        opcao = ler_inteiro("Opção: ")

        if opcao == 1:
            menu_gestao_alunos()
        elif opcao == 2:
            menu_gestao_disciplinas()
        elif opcao == 3:
            menu_gestao_notas()
        elif opcao == 4:
            menu_relatorios()
        elif opcao == 5:
            confirmacao = input("Tem a certeza que quer apagar todos os dados? (s/n): ").strip().lower()
            if confirmacao == "s":
                logica.reset()
                print("Sistema reiniciado.")
            else:
                print("Operação cancelada.")
        elif opcao == 0:
            print("A sair do sistema... Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")
