# Copyright 2017 Softplan
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


def get_fit_score(cargo, area, segmento):
    fit_score = None
    valor_fit_score = get_valor_fit_score(cargo, area, segmento)
    if valor_fit_score >= 7.5:
        fit_score = "a"
    elif valor_fit_score >= 5:
        fit_score = "b"
    elif valor_fit_score >= 2.5:
        fit_score = "c"
    elif valor_fit_score >= 0:
        fit_score = "d"
    return fit_score


def get_valor_fit_score(cargo, area, segmento):
    pontos_cargo = get_pontos_cargo(cargo)
    pontos_area = get_pontos_area(area)
    pontos_segmento = get_pontos_segmento(segmento)
    peso_cargo = 0.46
    peso_area = 0.11
    peso_segmento = 0.43
    fit_score_cargo = pontos_cargo * peso_cargo
    fit_score_area = pontos_area * peso_area
    fit_score_segmento = pontos_segmento * peso_segmento
    valor_fit_score = fit_score_cargo + fit_score_area + fit_score_segmento
    return valor_fit_score


def get_pontos_cargo(info_cargo):
    if info_cargo == "Sócio/Proprietário":
        return 8
    elif info_cargo == "Diretor":
        return 8
    elif info_cargo == "Gestor de Área":
        return 7
    elif info_cargo == "Analista":
        return 1
    elif info_cargo == "Assistente":
        return 0
    elif info_cargo == "Estagiário":
        return 0
    elif info_cargo == "Consultor":
        return 0
    elif info_cargo == "Autônomo":
        return 0
    elif info_cargo == "Outros":
        return 0


def get_pontos_area(info_area):
    if info_area == "Engenharia":
        return 10
    elif info_area == "Financeiro e Administrativo":
        return 10
    elif info_area == "Suprimentos":
        return 0
    elif info_area == "Diretoria":
        return 10
    elif info_area == "Orçamento":
        return 0
    elif info_area == "Planejamento":
        return 0
    elif info_area == "Comercial":
        return 0
    elif info_area == "Incorporação":
        return 0
    elif info_area == "RH":
        return 0
    elif info_area == "TI":
        return 0
    elif info_area == "Arquitetura":
        return 0
    elif info_area == "Outros":
        return 0


def get_pontos_segmento(info_segmento):
    if info_segmento == "Construtora e Incorporadora":
        return 8
    elif info_segmento == "Construtora":
        return 8
    elif info_segmento == "Incorporadora":
        return 8
    elif info_segmento == "Loteadora":
        return 8
    elif info_segmento == "Obras Próprias":
        return 0
    elif info_segmento == "Instaladora":
        return 6
    elif info_segmento == "Reformas":
        return 0
    elif info_segmento == "Outros":
        return 0
