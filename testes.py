"""
testes.py
Testes básicos às funções da lógica usando assert.
Execute diretamente: python testes.py
"""

import logica


def setup():
    """Reinicia o estado antes de cada conjunto de testes."""
    logica.alunos.clear()
    logica.disciplinas.clear()
    logica.notas.clear()
    logica._proximo_id_aluno = 1
    logica._proximo_id_disciplina = 1


# ---- TESTES DE ALUNOS ----

def teste_adicionar_aluno():
    setup()
    msg = logica.adicionar_aluno("Ana")
    assert "SUCESSO" in msg, f"Esperava SUCESSO, obteve: {msg}"
    assert len(logica.alunos) == 1
    assert logica.alunos[0]["nome"] == "Ana"
    print("  [OK] teste_adicionar_aluno")


def teste_adicionar_aluno_duplicado():
    setup()
    logica.adicionar_aluno("Ana")
    msg = logica.adicionar_aluno("Ana")
    assert "ERRO" in msg, f"Esperava ERRO para nome duplicado, obteve: {msg}"
    assert len(logica.alunos) == 1
    print("  [OK] teste_adicionar_aluno_duplicado")


def teste_adicionar_aluno_nome_vazio():
    setup()
    msg = logica.adicionar_aluno("   ")
    assert "ERRO" in msg
    assert len(logica.alunos) == 0
    print("  [OK] teste_adicionar_aluno_nome_vazio")


def teste_remover_aluno():
    setup()
    logica.adicionar_aluno("Rui")
    id_rui = logica.alunos[0]["id"]
    msg = logica.remover_aluno(id_rui)
    assert "SUCESSO" in msg
    assert len(logica.alunos) == 0
    print("  [OK] teste_remover_aluno")


def teste_remover_aluno_inexistente():
    setup()
    msg = logica.remover_aluno(999)
    assert "ERRO" in msg
    print("  [OK] teste_remover_aluno_inexistente")


def teste_editar_aluno():
    setup()
    logica.adicionar_aluno("Carlos")
    id_c = logica.alunos[0]["id"]
    msg = logica.editar_aluno(id_c, "Carlos Silva")
    assert "SUCESSO" in msg
    assert logica.alunos[0]["nome"] == "Carlos Silva"
    print("  [OK] teste_editar_aluno")


def teste_pesquisar_alunos():
    setup()
    logica.adicionar_aluno("Maria")
    logica.adicionar_aluno("Mariana")
    logica.adicionar_aluno("João")
    resultado = logica.pesquisar_alunos_por_nome("mari")
    assert len(
        resultado) == 2, f"Esperava 2 resultados, obteve {len(resultado)}"
    print("  [OK] teste_pesquisar_alunos")


def teste_listar_alunos_ordenados():
    setup()
    logica.adicionar_aluno("Zé")
    logica.adicionar_aluno("Ana")
    logica.adicionar_aluno("Manel")
    ordenados = logica.listar_alunos_ordenados("nome")
    nomes = [a["nome"] for a in ordenados]
    assert nomes == sorted(
        nomes, key=str.lower), f"Lista não está ordenada: {nomes}"
    print("  [OK] teste_listar_alunos_ordenados")


# ---- TESTES DE DISCIPLINAS ----

def teste_adicionar_disciplina():
    setup()
    msg = logica.adicionar_disciplina("Matemática")
    assert "SUCESSO" in msg
    assert len(logica.disciplinas) == 1
    print("  [OK] teste_adicionar_disciplina")


def teste_adicionar_disciplina_duplicada():
    setup()
    logica.adicionar_disciplina("Matemática")
    msg = logica.adicionar_disciplina("Matemática")
    assert "ERRO" in msg
    print("  [OK] teste_adicionar_disciplina_duplicada")


def teste_remover_disciplina():
    setup()
    logica.adicionar_disciplina("Física")
    id_f = logica.disciplinas[0]["id"]
    msg = logica.remover_disciplina(id_f)
    assert "SUCESSO" in msg
    assert len(logica.disciplinas) == 0
    print("  [OK] teste_remover_disciplina")


# ---- TESTES DE NOTAS ----

def teste_atribuir_nota_valida():
    setup()
    logica.adicionar_aluno("Beatriz")
    logica.adicionar_disciplina("Inglês")
    id_a = logica.alunos[0]["id"]
    id_d = logica.disciplinas[0]["id"]
    msg = logica.atribuir_nota(id_a, id_d, 15.0)
    assert "SUCESSO" in msg
    assert logica.obter_nota(id_a, id_d) == 15.0
    print("  [OK] teste_atribuir_nota_valida")


def teste_atribuir_nota_invalida():
    setup()
    logica.adicionar_aluno("Beatriz")
    logica.adicionar_disciplina("Inglês")
    id_a = logica.alunos[0]["id"]
    id_d = logica.disciplinas[0]["id"]
    msg = logica.atribuir_nota(id_a, id_d, 25.0)
    assert "ERRO" in msg
    msg2 = logica.atribuir_nota(id_a, id_d, -1.0)
    assert "ERRO" in msg2
    print("  [OK] teste_atribuir_nota_invalida")


def teste_remover_aluno_apaga_notas():
    setup()
    logica.adicionar_aluno("Tiago")
    logica.adicionar_disciplina("Prog")
    id_a = logica.alunos[0]["id"]
    id_d = logica.disciplinas[0]["id"]
    logica.atribuir_nota(id_a, id_d, 18.0)
    assert len(logica.notas) == 1
    logica.remover_aluno(id_a)
    assert len(logica.notas) == 0
    print("  [OK] teste_remover_aluno_apaga_notas")


# ---- TESTES DE ESTATÍSTICAS ----

def teste_media_aluno():
    setup()
    logica.adicionar_aluno("Inês")
    logica.adicionar_disciplina("Mat")
    logica.adicionar_disciplina("Pt")
    id_a = logica.alunos[0]["id"]
    id_d1 = logica.disciplinas[0]["id"]
    id_d2 = logica.disciplinas[1]["id"]
    logica.atribuir_nota(id_a, id_d1, 10.0)
    logica.atribuir_nota(id_a, id_d2, 20.0)
    m = logica.media_aluno(id_a)
    assert m == 15.0, f"Esperava 15.0, obteve {m}"
    print("  [OK] teste_media_aluno")


def teste_media_aluno_sem_notas():
    setup()
    logica.adicionar_aluno("Pedro")
    id_a = logica.alunos[0]["id"]
    m = logica.media_aluno(id_a)
    assert m is None
    print("  [OK] teste_media_aluno_sem_notas")


def teste_media_disciplina():
    setup()
    logica.adicionar_aluno("A1")
    logica.adicionar_aluno("A2")
    logica.adicionar_disciplina("Fcsi")
    id_a1 = logica.alunos[0]["id"]
    id_a2 = logica.alunos[1]["id"]
    id_d = logica.disciplinas[0]["id"]
    logica.atribuir_nota(id_a1, id_d, 8.0)
    logica.atribuir_nota(id_a2, id_d, 12.0)
    m = logica.media_disciplina(id_d)
    assert m == 10.0, f"Esperava 10.0, obteve {m}"
    print("  [OK] teste_media_disciplina")


def teste_resumo_geral():
    setup()
    logica.adicionar_aluno("X")
    logica.adicionar_disciplina("Y")
    id_a = logica.alunos[0]["id"]
    id_d = logica.disciplinas[0]["id"]
    logica.atribuir_nota(id_a, id_d, 14.0)
    r = logica.resumo_geral()
    assert r["total_alunos"] == 1
    assert r["total_disciplinas"] == 1
    assert r["total_notas"] == 1
    assert len(r["ranking"]) == 1
    assert r["ranking"][0]["media"] == 14.0
    print("  [OK] teste_resumo_geral")


# ---- EXECUÇÃO DOS TESTES ----

def correr_testes():
    print("=" * 40)
    print("A executar testes...")
    print("=" * 40)

    print("\n[Alunos]")
    teste_adicionar_aluno()
    teste_adicionar_aluno_duplicado()
    teste_adicionar_aluno_nome_vazio()
    teste_remover_aluno()
    teste_remover_aluno_inexistente()
    teste_editar_aluno()
    teste_pesquisar_alunos()
    teste_listar_alunos_ordenados()

    print("\n[Disciplinas]")
    teste_adicionar_disciplina()
    teste_adicionar_disciplina_duplicada()
    teste_remover_disciplina()

    print("\n[Notas]")
    teste_atribuir_nota_valida()
    teste_atribuir_nota_invalida()
    teste_remover_aluno_apaga_notas()

    print("\n[Estatísticas]")
    teste_media_aluno()
    teste_media_aluno_sem_notas()
    teste_media_disciplina()
    teste_resumo_geral()

    print("\n" + "=" * 40)
    print("Todos os testes passaram com sucesso!")
    print("=" * 40)


if __name__ == "__main__":
    correr_testes()
