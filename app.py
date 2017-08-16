from flask import Flask, abort, request
import service


app = Flask(__name__)


@app.route('/')
def index():
    return "Intellead Fitscore"


@app.route('/fitscore', methods=['POST'])
def get_fitscore():
    data = request.get_json()
    if data is None:
        abort(400)
    cargo = data['cargo']
    area = data['area']
    segmento = data['segmento']
    if (cargo is None) | (cargo == '') | (area is None) | (area == '') | (segmento is None) | (segmento == ''):
        abort(400)

    peso_cargo = 0.46
    peso_area = 0.11
    peso_segmento = 0.43

    fitscore_a = 7.5
    fitscore_b = 5
    fitscore_c = 2.5
    fitscore_d = 0

    #Area
    area_engenharia = 10
    area_financeiro_e_administrativo = 10
    area_suprimentos = 0
    area_diretoria = 10
    area_orcamento = 0
    area_planejamento = 0
    area_comercial = 0
    area_incorporacao = 0
    area_rh = 0
    area_ti = 0
    area_arquitetura = 0
    area_outros = 0

    #Segmentos
    segmento_construtora_e_incorporadora = 8
    segmento_construtora = 8
    segmento_incorporadora = 8
    segmento_loteadora = 8
    segmento_obras_proprias = 0
    segmento_instaladora = 6
    segmento_reformas = 0
    segmento_outros = 0

    #Infos
    info_cargo = cargo
    info_area = area
    info_segmento = segmento

    pontos_cargo = service.get_pontos_cargo(info_cargo)

    if(info_area == "Engenharia"):
        pontos_area = area_engenharia
    elif (info_area == "Financeiro e Administrativo"):
        pontos_area = area_financeiro_e_administrativo
    elif (info_area == "Suprimentos"):
        pontos_area = area_suprimentos
    elif (info_area == "Diretoria"):
        pontos_area = area_diretoria
    elif (info_area == "Orçamento"):
        pontos_area = area_orcamento
    elif (info_area == "Planejamento"):
        pontos_area = area_planejamento
    elif (info_area == "Comercial"):
        pontos_area = area_comercial
    elif (info_area == "Incorporação"):
        pontos_area = area_incorporacao
    elif (info_area == "RH"):
        pontos_area = area_rh
    elif (info_area == "TI"):
        pontos_area = area_ti
    elif (info_area == "Arquitetura"):
        pontos_area = area_arquitetura
    elif (info_area == "Outros"):
        pontos_area = area_outros

    if(info_segmento == "Construtora e Incorporadora"):
        pontos_segmento = segmento_construtora_e_incorporadora
    elif(info_segmento == "Construtora"):
        pontos_segmento = segmento_construtora
    elif(info_segmento == "Incorporadora"):
        pontos_segmento = segmento_incorporadora
    elif(info_segmento == "Loteadora"):
        pontos_segmento = segmento_loteadora
    elif(info_segmento == "Obras Próprias"):
        pontos_segmento = segmento_obras_proprias
    elif(info_segmento == "Instaladora"):
        pontos_segmento = segmento_instaladora
    elif(info_segmento == "Reformas"):
        pontos_segmento = segmento_reformas
    elif(info_segmento == "Outros"):
        pontos_segmento = segmento_outros

    fitscore_cargo = pontos_cargo * peso_cargo
    fitscore_area = pontos_area * peso_area
    fitscore_segmento = pontos_segmento * peso_segmento
    valor_fitscore = fitscore_cargo + fitscore_area + fitscore_segmento

    fitscore = None
    if(valor_fitscore >= fitscore_a):
        fitscore = "a"
    elif(valor_fitscore >= fitscore_b):
        fitscore = "b"
    elif(valor_fitscore >= fitscore_c):
        fitscore = "c"
    elif(valor_fitscore >= fitscore_d):
        fitscore = "d"
    return fitscore


if __name__ == '__main__':
    app.run(debug=True)
