import csv
import os

FICHEIRO_ALUNOS = "alunos.csv"
FICHEIRO_DISCIPLINAS = "disciplinas.csv"
FICHEIRO_NOTAS = "notas.csv"


def guardar_alunos(alunos):
    with open(FICHEIRO_ALUNOS, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "nome"])
        for aluno in alunos:
            writer.writerow([aluno["id"], aluno["nome"]])


def carregar_alunos():
    alunos = []
    if not os.path.exists(FICHEIRO_ALUNOS):
        return alunos
    with open(FICHEIRO_ALUNOS, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            alunos.append({"id": int(row["id"]), "nome": row["nome"]})
    return alunos


def guardar_disciplinas(disciplinas):
    with open(FICHEIRO_DISCIPLINAS, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "nome"])
        for disc in disciplinas:
            writer.writerow([disc["id"], disc["nome"]])


def carregar_disciplinas():
    disciplinas = []
    if not os.path.exists(FICHEIRO_DISCIPLINAS):
        return disciplinas
    with open(FICHEIRO_DISCIPLINAS, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            disciplinas.append({"id": int(row["id"]), "nome": row["nome"]})
    return disciplinas


def guardar_notas(notas):
    with open(FICHEIRO_NOTAS, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["id_aluno", "id_disciplina", "nota"])
        for chave, valor in notas.items():
            id_aluno, id_disc = chave
            writer.writerow([id_aluno, id_disc, valor])


def carregar_notas():
    notas = {}
    if not os.path.exists(FICHEIRO_NOTAS):
        return notas
    with open(FICHEIRO_NOTAS, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            chave = (int(row["id_aluno"]), int(row["id_disciplina"]))
            notas[chave] = float(row["nota"])
    return notas
