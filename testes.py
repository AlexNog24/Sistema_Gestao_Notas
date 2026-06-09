import os
import pytest
import logica
import ficheiros

# Redirecionar os ficheiros para não corromper os reais
ficheiros.FICHEIRO_ALUNOS = "teste_alunos.csv"
ficheiros.FICHEIRO_DISCIPLINAS = "teste_disciplinas.csv"
ficheiros.FICHEIRO_NOTAS = "teste_notas.csv"


def setup_teste():
    """
    Como não usamos fixtures, esta função tem de ser chamada no início de cada teste.
    Apaga os ficheiros de teste anteriores, limpa a memória e inicializa os dados padrão.
    """
    # Apagar ficheiros temporários para garantir um estado sempre limpo
    for f in [ficheiros.FICHEIRO_ALUNOS, ficheiros.FICHEIRO_DISCIPLINAS, ficheiros.FICHEIRO_NOTAS]:
        if os.path.exists(f):
            os.remove(f)

    # Limpar estado global
    logica.alunos.clear()
    logica.disciplinas.clear()
    logica.notas.clear()

    # Carregar dados padrão (2 alunos predefinidos e 11 disciplinas)
    logica.iniciar_dados()


# ---- TESTES ALUNOS ----

def test_adicionar_aluno():
    setup_teste()
    assert "SUCESSO" in logica.adicionar_aluno("Carlos")
    assert "ERRO" in logica.adicionar_aluno("   ")
    assert "ERRO" in logica.adicionar_aluno(
        "Alexandre")  # Nome já existe (ID 1)


def test_incremento_id_aluno():
    setup_teste()
    # A base de dados inicia com IDs 1 e 2. Vamos remover o ID 1.
    logica.remover_aluno(1)
    # Adicionar um novo aluno; ele deve receber o ID 3 (maior ID existente que é 2, + 1).
    logica.adicionar_aluno("Carlos")
    aluno = logica.obter_aluno_por_id(3)
    assert aluno is not None
    assert aluno["nome"] == "Carlos"
    assert logica.obter_aluno_por_id(1) is None


def test_remover_aluno():
    setup_teste()
    # Remover por ID numérico
    assert "SUCESSO" in logica.remover_aluno(1)
    assert "ERRO" in logica.remover_aluno(999)


def test_editar_aluno():
    setup_teste()
    assert "SUCESSO" in logica.editar_aluno(1, "Alexandre Magno")
    assert "ERRO" in logica.editar_aluno(999, "Maria")
    assert "ERRO" in logica.editar_aluno(
        1, "Vicente")  # Nome já pertence ao ID 2


def test_verificar_existencia_aluno():
    setup_teste()
    assert logica.obter_aluno_por_id(1) is not None
    assert logica.obter_aluno_por_id(999) is None
    assert len(logica.pesquisar_alunos_por_nome("alex")) > 0


# ---- TESTES DISCIPLINAS ----

def test_adicionar_disciplina():
    setup_teste()
    assert "SUCESSO" in logica.adicionar_disciplina("Física Avançada")
    assert "ERRO" in logica.adicionar_disciplina("Matemática")
    assert "ERRO" in logica.adicionar_disciplina("")


def test_incremento_id_disciplina():
    setup_teste()
    # A base de dados inicia com 11 disciplinas (IDs 1 a 11). Vamos remover o ID 1.
    logica.remover_disciplina(1)
    # Ao adicionar uma nova, deve receber o ID 12 (maior ID existente que é 11, + 1).
    logica.adicionar_disciplina("Física Computacional")
    disc = logica.obter_disciplina_por_id(12)
    assert disc is not None
    assert disc["nome"] == "Física Computacional"
    assert logica.obter_disciplina_por_id(1) is None


def test_remover_disciplina():
    setup_teste()
    assert "SUCESSO" in logica.remover_disciplina(1)
    assert "ERRO" in logica.remover_disciplina(999)


def test_verificar_existencia_disciplina():
    setup_teste()
    assert logica.obter_disciplina_por_id(1) is not None
    assert logica.obter_disciplina_por_id(999) is None


# ---- TESTES NOTAS ----

def test_atribuir_nota():
    setup_teste()
    assert "SUCESSO" in logica.atribuir_nota(1, 1, 15)
    assert "ERRO" in logica.atribuir_nota(1, 1, 25)
    assert "ERRO" in logica.atribuir_nota(1, 1, -1)
    assert "ERRO" in logica.atribuir_nota(999, 1, 10)
    assert "ERRO" in logica.atribuir_nota(1, 999, 10)


def test_remover_dados_apaga_notas():
    setup_teste()
    logica.atribuir_nota(1, 1, 15)
    assert logica.obter_nota(1, 1) == 15

    logica.remover_aluno(1)
    assert logica.obter_nota(1, 1) is None
