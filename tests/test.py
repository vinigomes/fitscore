import service


def test_pontos_do_segmento_contrustora_e_incorporadora():
    pontos_segmento = service.get_pontos_segmento("Construtora e Incorporadora")
    assert pontos_segmento == 8


def test_pontos_do_segmento_contrustora():
    pontos_segmento = service.get_pontos_segmento("Construtora")
    assert pontos_segmento == 8


def test_pontos_do_segmento_incorporadora():
    pontos_segmento = service.get_pontos_segmento("Incorporadora")
    assert pontos_segmento == 8


def test_pontos_do_segmento_loteadora():
    pontos_segmento = service.get_pontos_segmento("Loteadora")
    assert pontos_segmento == 8


def test_pontos_do_segmento_obras_proprias():
    pontos_segmento = service.get_pontos_segmento("Obras Próprias")
    assert pontos_segmento == 0


def test_pontos_do_segmento_instaladora():
    pontos_segmento = service.get_pontos_segmento("Instaladora")
    assert pontos_segmento == 6


def test_pontos_do_segmento_reformas():
    pontos_segmento = service.get_pontos_segmento("Reformas")
    assert pontos_segmento == 0


def test_pontos_do_segmento_outros():
    pontos_segmento = service.get_pontos_segmento("Outros")
    assert pontos_segmento == 0


def test_pontos_da_area_engenharia():
    pontos_area = service.get_pontos_area("Engenharia")
    assert pontos_area == 10


def test_pontos_da_area_financeito_e_administrativo():
    pontos_area = service.get_pontos_area("Financeiro e Administrativo")
    assert pontos_area == 10


def test_pontos_da_area_suprimentos():
    pontos_area = service.get_pontos_area("Suprimentos")
    assert pontos_area == 0


def test_pontos_da_area_diretoria():
    pontos_area = service.get_pontos_area("Diretoria")
    assert pontos_area == 10


def test_pontos_da_area_orcamento():
    pontos_area = service.get_pontos_area("Orçamento")
    assert pontos_area == 0


def test_pontos_da_area_planejamento():
    pontos_area = service.get_pontos_area("Planejamento")
    assert pontos_area == 0


def test_pontos_da_area_comercial():
    pontos_area = service.get_pontos_area("Comercial")
    assert pontos_area == 0


def test_pontos_da_area_incorporacao():
    pontos_area = service.get_pontos_area("Incorporação")
    assert pontos_area == 0


def test_pontos_da_area_rh():
    pontos_area = service.get_pontos_area("RH")
    assert pontos_area == 0


def test_pontos_da_area_ti():
    pontos_area = service.get_pontos_area("TI")
    assert pontos_area == 0


def test_pontos_da_area_arquitetura():
    pontos_area = service.get_pontos_area("Arquitetura")
    assert pontos_area == 0


def test_pontos_da_area_outros():
    pontos_area = service.get_pontos_area("Outros")
    assert pontos_area == 0


def test_pontos_do_cargo_socio_proprietario():
    pontos_cargo = service.get_pontos_cargo("Sócio/Proprietário")
    assert pontos_cargo == 8


def test_pontos_do_cargo_diretor():
    pontos_cargo = service.get_pontos_cargo("Diretor")
    assert pontos_cargo == 8


def test_pontos_do_cargo_gestor_de_area():
    pontos_cargo = service.get_pontos_cargo("Gestor de Área")
    assert pontos_cargo == 7


def test_pontos_do_cargo_analista():
    pontos_cargo = service.get_pontos_cargo("Analista")
    assert pontos_cargo == 1


def test_pontos_do_cargo_assistente():
    pontos_cargo = service.get_pontos_cargo("Assistente")
    assert pontos_cargo == 0


def test_pontos_do_cargo_estagiario():
    pontos_cargo = service.get_pontos_cargo("Estagiário")
    assert pontos_cargo == 0


def test_pontos_do_cargo_consultor():
    pontos_cargo = service.get_pontos_cargo("Consultor")
    assert pontos_cargo == 0


def test_pontos_do_cargo_autonomo():
    pontos_cargo = service.get_pontos_cargo("Autônomo")
    assert pontos_cargo == 0


def test_pontos_do_cargo_outros():
    pontos_cargo = service.get_pontos_cargo("Outros")
    assert pontos_cargo == 0


def test_pontos_do_cargo_outros():
    pontos_cargo = service.get_pontos_cargo("Outros")
    assert pontos_cargo == 0


def test_valor_fit_score():
    valor_fit_score = service.get_valor_fit_score("Diretor", "Engenharia", "Construtora")
    assert valor_fit_score == 8.22


def test_fit_score_a():
    fit_score = service.get_fit_score("Diretor", "Engenharia", "Construtora")
    assert fit_score == "a"


def test_fit_score_c():
    fit_score = service.get_fit_score("Gestor de Área", "Diretoria", "Instaladora")
    assert fit_score == "b"


def test_fit_score_c():
    fit_score = service.get_fit_score("Analista", "Diretoria", "Instaladora")
    assert fit_score == "c"

