# Módulo central que contém as regras de negócio e a gestão do estado da aplicação.

import ficheiros

# ---- ESTADO GLOBAL (listas de dicionários) ----
# Estas estruturas mantêm os dados carregados em memória enquanto o programa corre,
# evitando leituras constantes ao disco e permitindo operações mais rápidas.
alunos = []
disciplinas = []
# O dicionário de notas usa um tuplo como chave (id_aluno, id_disciplina) e a nota numérica como valor.
notas = {}  # chave: (id_aluno, id_disciplina) -> float
# Variáveis de controlo para gerar IDs únicos e incrementais para novos registos.
_proximo_id_aluno = 1
_proximo_id_disciplina = 1


# ---- INICIALIZAÇÃO ----

def iniciar_dados():
    # Carrega dados dos ficheiros CSV ou cria dados iniciais se não existirem.
    # A declaração 'global' permite modificar as variáveis de estado definidas ao nível do módulo.
    global alunos, disciplinas, notas, _proximo_id_aluno, _proximo_id_disciplina

    # Atualiza as listas em memória com os dados lidos dos ficheiros CSV usando slicing [:]
    # O slicing garante que substituímos os elementos da lista sem criar um novo objeto em memória.
    alunos[:] = ficheiros.carregar_alunos()
    disciplinas[:] = ficheiros.carregar_disciplinas()

    # Limpa o dicionário atual e carrega as notas gravadas.
    notas.clear()
    notas.update(ficheiros.carregar_notas())

    # Caso não existam alunos (primeira execução), introduz alguns dados de exemplo.
    if not alunos:
        nomes_iniciais = ["Alexandre",
                          "Vicente"]
        for nome in nomes_iniciais:
            adicionar_aluno(nome)

    # O mesmo raciocínio para as disciplinas, gerando disciplinas base se estiver vazio.
    if not disciplinas:
        discs_iniciais = ["Matemática", "Português",
                          "Programação", "Inglês", "Fcsi",
                          "Programação II", "Ferramentas e Multimédia",
                          "Hardware de Computadores", "Redes",
                          "Eng. Software", "Base de Dados"]
        for nome in discs_iniciais:
            adicionar_disciplina(nome)

    # Recalcula as variáveis de próximo ID com base no ID mais elevado encontrado nos dados carregados.
    # Isto evita conflitos (IDs repetidos) ao adicionar novos elementos após fechar e reabrir a aplicação.
    if alunos:
        _proximo_id_aluno = max(a["id"] for a in alunos) + 1
    if disciplinas:
        _proximo_id_disciplina = max(d["id"] for d in disciplinas) + 1


def reset():
    """Reinicia todos os dados e apaga os ficheiros."""
    global alunos, disciplinas, notas, _proximo_id_aluno, _proximo_id_disciplina
    # Esvazia os dados em memória
    alunos.clear()
    disciplinas.clear()
    notas.clear()
    # Repõe os IDs para 1
    _proximo_id_aluno = 1
    _proximo_id_disciplina = 1
    # Ao guardar coleções vazias nos ficheiros, estamos efetivamente a limpar o seu conteúdo
    ficheiros.guardar_alunos(alunos)
    ficheiros.guardar_disciplinas(disciplinas)
    ficheiros.guardar_notas(notas)


# ---- ALUNOS ----

def adicionar_aluno(nome):
    """Adiciona um aluno. Retorna mensagem de sucesso ou erro."""
    global _proximo_id_aluno
    nome = nome.strip()
    # Validação: impede que seja criado um aluno com um nome vazio
    if not nome:
        return "ERRO: O nome não pode estar vazio."
    # Percorre todos os alunos existentes para garantir que não são inseridos nomes duplicados (case-insensitive)
    for a in alunos:
        if a["nome"].lower() == nome.lower():
            return f"ERRO: Já existe um aluno com o nome '{nome}'."
    # Cria e guarda o dicionário que representa o aluno
    aluno = {"id": _proximo_id_aluno, "nome": nome}
    alunos.append(aluno)
    # Incrementa o contador para que o próximo aluno receba um ID diferente
    _proximo_id_aluno += 1
    # Grava a alteração para persistir no disco
    ficheiros.guardar_alunos(alunos)
    return f"SUCESSO: Aluno '{nome}' adicionado com ID {aluno['id']}."


def remover_aluno(id_aluno):
    """Remove um aluno e todas as suas notas. Retorna mensagem."""
    global alunos, notas
    aluno = obter_aluno_por_id(id_aluno)
    if not aluno:
        return "ERRO: Aluno não encontrado."

    # Reconstrói a lista de alunos, mantendo apenas aqueles cujo ID não corresponde ao ID a remover
    alunos[:] = [a for a in alunos if a["id"] != id_aluno]

    # Filtra o dicionário de notas. A chave é (id_aluno, id_disc), portanto k[0] é o id_aluno.
    # Remove todas as notas pertencentes ao aluno que está a ser apagado.
    notas_novas = {k: v for k, v in notas.items() if k[0] != id_aluno}
    notas.clear()
    notas.update(notas_novas)

    # Persiste as alterações no disco
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
    # Verifica se já existe outro aluno com o mesmo nome pretendido (ignorando o aluno a ser editado)
    for a in alunos:
        if a["nome"].lower() == novo_nome.lower() and a["id"] != id_aluno:
            return f"ERRO: Já existe um aluno com o nome '{novo_nome}'."
    aluno["nome"] = novo_nome
    ficheiros.guardar_alunos(alunos)
    return f"SUCESSO: Nome atualizado para '{novo_nome}'."


def obter_aluno_por_id(id_aluno):
    """Pesquisa sequencial de aluno por ID."""
    # Devolve o dicionário do aluno caso o ID corresponda, ou 'None' caso não exista
    for a in alunos:
        if a["id"] == id_aluno:
            return a
    return None


def pesquisar_alunos_por_nome(termo):
    """Pesquisa sequencial de alunos cujo nome contenha o termo."""
    termo = termo.strip().lower()
    # Utiliza 'list comprehension' para devolver todos os alunos que contenham a substring
    return [a for a in alunos if termo in a["nome"].lower()]


def listar_alunos_ordenados(criterio="nome"):
    """Retorna alunos ordenados por 'nome' ou 'id'."""
    if criterio == "nome":
        # Ordena alfabeticamente usando o lower() para que as maiúsculas não afetem a ordem
        return sorted(alunos, key=lambda a: a["nome"].lower())
    # Se o critério não for "nome", ordena por identificador
    return sorted(alunos, key=lambda a: a["id"])


# ---- DISCIPLINAS ----

def adicionar_disciplina(nome):
    """Adiciona uma disciplina. Retorna mensagem de sucesso ou erro."""
    global _proximo_id_disciplina
    # Lógica idêntica à de adicionar aluno
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

    # Remove a disciplina da lista em memória
    disciplinas[:] = [d for d in disciplinas if d["id"] != id_disc]

    # Filtra as notas. Como a chave é (id_aluno, id_disc), 'k[1]' representa o ID da disciplina.
    # Elimina todas as notas associadas a esta disciplina para que não fiquem referências órfãs.
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
    # Garante que as referências ao aluno e disciplina são válidas antes de registar a nota.
    aluno = obter_aluno_por_id(id_aluno)
    if not aluno:
        return "ERRO: Aluno não encontrado."
    disc = obter_disciplina_por_id(id_disc)
    if not disc:
        return "ERRO: Disciplina não encontrada."
    # Validação do intervalo esperado
    if valor < 0 or valor > 20:
        return "ERRO: Nota inválida. Deve estar entre 0 e 20."

    # Adiciona a nota ou atualiza uma já existente se for novamente atribuída
    notas[(id_aluno, id_disc)] = valor
    ficheiros.guardar_notas(notas)
    return f"SUCESSO: Nota {valor:.1f} registada para '{aluno['nome']}' em '{disc['nome']}'."


def obter_nota(id_aluno, id_disc):
    """Retorna a nota ou None se não existir."""
    # Usa .get() para não disparar KeyError se a chave ainda não existir no dicionário
    return notas.get((id_aluno, id_disc), None)


def notas_do_aluno(id_aluno):
    """Retorna lista de (disciplina, nota) para um aluno."""
    resultado = []
    # Cruzamento de dados: Itera sobre todas as disciplinas, indo buscar a nota respetiva se existir.
    for disc in disciplinas:
        nota = notas.get((id_aluno, disc["id"]), None)
        resultado.append({"disciplina": disc["nome"], "nota": nota})
    return resultado


def notas_da_disciplina(id_disc):
    """Retorna lista de (aluno, nota) para uma disciplina."""
    resultado = []
    # Cruzamento inverso: Para uma disciplina, vai ver a nota de todos os alunos registados.
    for aluno in alunos:
        nota = notas.get((aluno["id"], id_disc), None)
        resultado.append({"aluno": aluno["nome"], "nota": nota})
    return resultado


# ---- ESTATÍSTICAS ----

def media_aluno(id_aluno):
    """Calcula a média das notas de um aluno. Retorna float ou None."""
    # Usa extração na list comprehension desempacotando as chaves num tuplo '(a, d)' e extraindo só os valores 'v'.
    valores = [v for (a, d), v in notas.items() if a == id_aluno]
    if not valores:
        return None
    # Soma os valores todos e divide pela quantidade de notas encontradas (média simples)
    return sum(valores) / len(valores)


def media_disciplina(id_disc):
    """Calcula a média das notas de uma disciplina. Retorna float ou None."""
    # Filtra os valores apenas para as notas associadas ao ID da disciplina (d == id_disc)
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

    # Ordena os alunos usando a média (de forma descendente, com a nota mais alta primeiro)
    medias_ordenadas = sorted(medias, key=lambda x: x["media"], reverse=True)

    return {
        "total_alunos": len(alunos),
        "total_disciplinas": len(disciplinas),
        "total_notas": total_notas,
        "ranking": medias_ordenadas
    }
