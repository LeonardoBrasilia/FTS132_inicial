import pytest
import requests

base_url = 'https://petstore.swagger.io/v2/pet'
headers = {'Content-Type': 'application/json'}

def testar_incluir_pet():
    # Configura
    # Dados de entrada vem do pet1.json
    status_code_esperado = 200
    nome_pet_esperado = 'Snoopy'
    tag_esperada = 'vacinado'

    # Executa
    resposta = requests.post(
        url=base_url,
        data=open('C:/Users/corre/PycharmProjects/fts132_inicial/test/db/pet1.json', 'rb'),
        headers=headers
    )

    # Formata
    print(resposta)
    print(resposta.status_code)
    corpo_da_resposta = resposta.json()
    print(corpo_da_resposta)

    # Valida
    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['name'] == nome_pet_esperado
    # assert corpo_da_resposta['tags.name'] == tag_esperada