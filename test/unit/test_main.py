import pytest

from main import somar_dois_numeros, calcular_area_do_circulo, calcular_volume_do_paralelograma


def testar_somar_dois_numeros():
    # - 1ª Etapa: Configura / Prepara
    # Dados / Valores
    # Entrada / Input
    num1 = 4
    num2 = 5
    # Saída / Output
    resultado_esperado = 9

    # - 2ª Etapa: Executa
    resultado_atual = somar_dois_numeros(num1, num2)

    # - 3ª Etapa: Confirma / Check / Valida
    assert resultado_atual == resultado_esperado


# anotação para utilizar como massa de teste
@pytest.mark.parametrize('raio,resultado_esperado',[
                             # valores
                             (1, 3.14),    # teste nº 1
                             (2, 12.56),   # teste nº 2
                             (3, 28.26),   # teste nº 3
                             (4, 50.24),   # teste nº 4
                             ('a', 'Falha no calculo - Raio não é um número'),  # teste nº 5
                             (' ', 'Falha no calculo - Raio não é um número'),  # teste nº 6
                         ])
def testar_calcular_area_do_circulo(raio, resultado_esperado):
    # 1 - Configura / Comentamos para que os parametros sejam lidos
    # raio = 2
    # resultado_esperado = 12.56

    # 2 - Executa
    resultado_atual = calcular_area_do_circulo(raio)

    # 3 - Valida
    assert resultado_atual == resultado_esperado

def testar_calcular_volume_do_paralelograma():
    #1 - Configura
    largura = 5
    comprimento = 10
    altura = 2
    resultado_esperado = 100

    #2 - Executa
    resultado_atual = calcular_volume_do_paralelograma(largura, comprimento, altura)

    # - Valida
    assert resultado_atual == resultado_esperado