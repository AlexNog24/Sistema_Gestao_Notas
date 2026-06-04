import ficheiros

# ---- ESTADO GLOBAL (listas de dicionários) ----
alunos = []
disciplinas = []
notas = {}  # chave: (id_aluno, id_disciplina) -> float
_proximo_id_aluno = 1
_proximo_id_disciplina = 1


# ---- INICIALIZAÇÃO ----

def iniciar_dados():
    # Carrega dados dos ficheiros CSV ou cria dados iniciais se não existirem.
    global alunos, disciplinas, notas, _proximo_id_aluno, _proximo_id_disciplina

    alunos[:] = ficheiros.carregar_alunos()
    disciplinas[:] = ficheiros.carregar_disciplinas()

    notas.clear()
    notas.update(ficheiros.carregar_notas())

    if not alunos:
        nomes_iniciais = ["To", "Ze", "Bery", "Manel", "Leo"]
        for nome in nomes_iniciais:
            adicionar_aluno(nome)

    if not disciplinas:
        discs_iniciais = ["Mat", "Pt", "Prog", "Ing", "Fcsi"]
        for nome in discs_iniciais:
            adicionar_disciplina(nome)

    if alunos:
        _proximo_id_aluno = max(a["id"] for a in alunos) + 1
    if disciplinas:
        _proximo_id_disciplina = max(d["id"] for d in disciplinas) + 1


def reset():
    """Reinicia todos os dados e apaga os ficheiros."""
    global alunos, disciplinas, notas, _proximo_id_aluno, _proximo_id_disciplina
    alunos.clear()
    disciplinas.clear()
    notas.clear()
    _proximo_id_aluno = 1
    _proximo_id_disciplina = 1
    ficheiros.guardar_alunos(alunos)
    ficheiros.guardar_disciplinas(disciplinas)
    ficheiros.guardar_notas(notas)


# ---- ALUNOS ----

def adicionar_aluno(nome):
    """Adiciona um aluno. Retorna mensagem de sucesso ou erro."""
    global _proximo_id_aluno
    nome = nome.strip()
    if not nome:
        return "ERRO: O nome não pode estar vazio."
    for a in alunos:
        if a["nome"].lower() == nome.lower():
            return f"ERRO: Já existe um aluno com o nome '{nome}'."
    aluno = {"id": _proximo_id_aluno, "nome": nome}
    alunos.append(aluno)
    _proximo_id_aluno += 1
    ficheiros.guardar_alunos(alunos)
    return f"SUCESSO: Aluno '{nome}' adicionado com ID {aluno['id']}."


def remover_aluno(id_aluno):
    """Remove um aluno e todas as suas notas. Retorna mensagem."""
    global alunos, notas
    aluno = obter_aluno_por_id(id_aluno)
    if not aluno:
        return "ERRO: Aluno não encontrado."

    alunos[:] = [a for a in alunos if a["id"] != id_aluno]

    notas_novas = {k: v for k, v in notas.items() if k[0] != id_aluno}
    notas.clear()
    notas.update(notas_novas)

    ficheiros.guardar_alunos(alunos)
    ficheiros.guardar_notas(notas)
    return f"SUCESSO: Aluno '{aluno['nome']}' removido."


def editar_aluno(id_aluno, novo_nome):
    """Edita o nome de um aluno. Retorna mensagem."""
    novo_nome = novo_nome.strip()
    if not novo_nome:
        return "ERRO: O nome não pode estar vazio."
    aluno = obter_aluno_por_id(id_aluno)
    if not aluno:
        return "ERRO: Aluno não encontrado."
    for a in alunos:
        if a["nome"].lower() == novo_nome.lower() and a["id"] != id_aluno:
            return f"ERRO: Já existe um aluno com o nome '{novo_nome}'."
    aluno["nome"] = novo_nome
    ficheiros.guardar_alunos(alunos)
    return f"SUCESSO: Nome atualizado para '{novo_nome}'."


def obter_aluno_por_id(id_aluno):
    """Pesquisa sequencial de aluno por ID."""
    for a in alunos:
        if a["id"] == id_aluno:
            return a
    return None


def pesquisar_alunos_por_nome(termo):
    """Pesquisa sequencial de alunos cujo nome contenha o termo."""
    termo = termo.strip().lower()
    return [a for a in alunos if termo in a["nome"].lower()]


def listar_alunos_ordenados(criterio="nome"):
    """Retorna alunos ordenados por 'nome' ou 'id'."""
    if criterio == "nome":
        return sorted(alunos, key=lambda a: a["nome"].lower())
    return sorted(alunos, key=lambda a: a["id"])


# ---- DISCIPLINAS ----

def adicionar_disciplina(nome):
    """Adiciona uma disciplina. Retorna mensagem de sucesso ou erro."""
    global _proximo_id_disciplina
    nome = nome.strip()
    if not nome:
        return "ERRO: O nome não pode estar vazio."
    for d in disciplinas:
        if d["nome"].lower() == nome.lower():
            return f"ERRO: Já existe uma disciplina com o nome '{nome}'."
    disc = {"id": _proximo_id_disciplina, "nome": nome}
    disciplinas.append(disc)
    _proximo_id_disciplina += 1
    ficheiros.guardar_disciplinas(disciplinas)
    return f"SUCESSO: Disciplina '{nome}' adicionada com ID {disc['id']}."


def remover_disciplina(id_disc):
    """Remove uma disciplina e todas as notas associadas. Retorna mensagem."""
    global disciplinas, notas
    disc = obter_disciplina_por_id(id_disc)
    if not disc:
        return "ERRO: Disciplina não encontrada."

    disciplinas[:] = [d for d in disciplinas if d["id"] != id_disc]

    notas_novas = {k: v for k, v in notas.items() if k[1] != id_disc}
    notas.clear()
    notas.update(notas_novas)

    ficheiros.guardar_disciplinas(disciplinas)
    ficheiros.guardar_notas(notas)
    return f"SUCESSO: Disciplina '{disc['nome']}' removida."


def editar_disciplina(id_disc, novo_nome):
    """Edita o nome de uma disciplina. Retorna mensagem."""
    novo_nome = novo_nome.strip()
    if not novo_nome:
        return "ERRO: O nome não pode estar vazio."
    disc = obter_disciplina_por_id(id_disc)
    if not disc:
        return "ERRO: Disciplina não encontrada."
    for d in disciplinas:
        if d["nome"].lower() == novo_nome.lower() and d["id"] != id_disc:
            return f"ERRO: Já existe uma disciplina com o nome '{novo_nome}'."
    disc["nome"] = novo_nome
    ficheiros.guardar_disciplinas(disciplinas)
    return f"SUCESSO: Nome atualizado para '{novo_nome}'."


def obter_disciplina_por_id(id_disc):
    """Pesquisa sequencial de disciplina por ID."""
    for d in disciplinas:
        if d["id"] == id_disc:
            return d
    return None


def pesquisar_disciplinas_por_nome(termo):
    """Pesquisa sequencial de disciplinas cujo nome contenha o termo."""
    termo = termo.strip().lower()
    return [d for d in disciplinas if termo in d["nome"].lower()]


def listar_disciplinas_ordenadas(criterio="nome"):
    """Retorna disciplinas ordenadas por 'nome' ou 'id'."""
    if criterio == "nome":
        return sorted(disciplinas, key=lambda d: d["nome"].lower())
    return sorted(disciplinas, key=lambda d: d["id"])


# ---- NOTAS ----

def atribuir_nota(id_aluno, id_disc, valor):
    """
    Atribui ou altera uma nota. Retorna mensagem de sucesso ou erro.
    valor deve ser float entre 0 e 20.
    """
    if not obter_aluno_por_id(id_aluno):
        return "ERRO: Aluno não encontrado."
    if not obter_disciplina_por_id(id_disc):
        return "ERRO: Disciplina não encontrada."
    if valor < 0 or valor > 20:
        return "ERRO: Nota inválida. Deve estar entre 0 e 20."
    notas[(id_aluno, id_disc)] = valor
    ficheiros.guardar_notas(notas)
    aluno = obter_aluno_por_id(id_aluno)
    disc = obter_disciplina_por_id(id_disc)
    return f"SUCESSO: Nota {valor:.1f} registada para '{aluno['nome']}' em '{disc['nome']}'."


def obter_nota(id_aluno, id_disc):
    """Retorna a nota ou None se não existir."""
    return notas.get((id_aluno, id_disc), None)


def notas_do_aluno(id_aluno):
    """Retorna lista de (disciplina, nota) para um aluno."""
    resultado = []
    for disc in disciplinas:
        nota = notas.get((id_aluno, disc["id"]), None)
        resultado.append({"disciplina": disc["nome"], "nota": nota})
    return resultado


def notas_da_disciplina(id_disc):
    """Retorna lista de (aluno, nota) para uma disciplina."""
    resultado = []
    for aluno in alunos:
        nota = notas.get((aluno["id"], id_disc), None)
        resultado.append({"aluno": aluno["nome"], "nota": nota})
    return resultado


# ---- ESTATÍSTICAS ----

def media_aluno(id_aluno):
    """Calcula a média das notas de um aluno. Retorna float ou None."""
    valores = [v for (a, d), v in notas.items() if a == id_aluno]
    if not valores:
        return None
    return sum(valores) / len(valores)


def media_disciplina(id_disc):
    """Calcula a média das notas de uma disciplina. Retorna float ou None."""
    valores = [v for (a, d), v in notas.items() if d == id_disc]
    if not valores:
        return None
    return sum(valores) / len(valores)


def resumo_geral():
    """
    Retorna um dicionário com estatísticas gerais:
    total de alunos, disciplinas, notas registadas,
    melhor e pior aluno por média.
    """
    total_notas = len(notas)
    medias = []
    for a in alunos:
        m = media_aluno(a["id"])
        if m is not None:
            medias.append({"nome": a["nome"], "media": m})

    medias_ordenadas = sorted(medias, key=lambda x: x["media"], reverse=True)

    return {
        "total_alunos": len(alunos),
        "total_disciplinas": len(disciplinas),
        "total_notas": total_notas,
        "ranking": medias_ordenadas
    }
