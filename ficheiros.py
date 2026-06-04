# Módulo responsável por lidar com a leitura e escrita de dados
# em ficheiros CSV, garantindo a persistência do sistema de forma local.

import csv
import os

# Constantes que definem os nomes dos ficheiros onde os dados serão guardados
FICHEIRO_ALUNOS = "alunos.csv"
FICHEIRO_DISCIPLINAS = "disciplinas.csv"
FICHEIRO_NOTAS = "notas.csv"


def guardar_alunos(alunos):
    # Abre o ficheiro em modo de escrita ("w"). Sobrescreve o ficheiro se já existir.
    with open(FICHEIRO_ALUNOS, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        # Escreve a primeira linha, que atua como cabeçalho das colunas
        writer.writerow(["id", "nome"])
        # Itera sobre a lista de dicionários (alunos) e escreve cada aluno como uma nova linha
        for aluno in alunos:
            writer.writerow([aluno["id"], aluno["nome"]])


def carregar_alunos():
    alunos = []
    # Verifica se o ficheiro existe antes de tentar ler para evitar um FileNotFoundError
    if not os.path.exists(FICHEIRO_ALUNOS):
        return alunos
    # Abre o ficheiro em modo de leitura ("r")
    with open(FICHEIRO_ALUNOS, "r", newline="", encoding="utf-8") as f:
        # DictReader lê a primeira linha como chaves e as restantes como valores de dicionários
        reader = csv.DictReader(f)
        for row in reader:
            # Converte explicitamente o 'id' para número inteiro (int) antes de guardar na lista
            alunos.append({"id": int(row["id"]), "nome": row["nome"]})
    return alunos


def guardar_disciplinas(disciplinas):
    # A lógica é idêntica à de guardar_alunos, mas aplicada à lista de disciplinas
    with open(FICHEIRO_DISCIPLINAS, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "nome"])
        for disc in disciplinas:
            writer.writerow([disc["id"], disc["nome"]])


def carregar_disciplinas():
    disciplinas = []
    # Retorna uma lista vazia caso não haja ficheiro de disciplinas gravado previamente
    if not os.path.exists(FICHEIRO_DISCIPLINAS):
        return disciplinas
    with open(FICHEIRO_DISCIPLINAS, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Extrai os dados do CSV, convertendo o 'id' para inteiro
            disciplinas.append({"id": int(row["id"]), "nome": row["nome"]})
    return disciplinas


def guardar_notas(notas):
    # Grava o dicionário de notas. A chave original em 'notas' é um tuplo (id_aluno, id_disciplina)
    with open(FICHEIRO_NOTAS, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["id_aluno", "id_disciplina", "nota"])
        # .items() devolve a chave e o valor a cada iteração sobre o dicionário
        for chave, valor in notas.items():
            # Desempacota o tuplo da chave nas respetivas variáveis id_aluno e id_disc
            id_aluno, id_disc = chave
            writer.writerow([id_aluno, id_disc, valor])


def carregar_notas():
    notas = {}
    # Retorna um dicionário vazio caso o ficheiro ainda não exista no disco
    if not os.path.exists(FICHEIRO_NOTAS):
        return notas
    with open(FICHEIRO_NOTAS, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Reconstrói a chave como tuplo, convertendo os IDs gravados no CSV de volta para inteiros
            chave = (int(row["id_aluno"]), int(row["id_disciplina"]))
            # Guarda a nota no dicionário final, garantindo que o valor numérico é float (decimal)
            notas[chave] = float(row["nota"])
    return notas
