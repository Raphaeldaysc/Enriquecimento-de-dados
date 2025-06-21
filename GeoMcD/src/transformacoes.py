"""
Módulo para transformar e enriquecer dados de usuários com faixa etária, banco e simulação de salário.
"""

import random
import pandas as pd
import requests

# === Carregamento de dados ===
try:
    df = pd.read_csv("../data/data_raw/usuarios.csv", encoding="utf-8-sig")
except FileNotFoundError:
    raise FileNotFoundError(
        "Arquivo 'usuarios.csv' não encontrado em ../data/data_raw/")
except Exception as e:
    raise Exception(f"Erro ao carregar CSV: {e}")

# === Funções de enriquecimento ===


def faixa_etaria(idade):
    """
    Retorna a faixa etária com base na idade.

    Args:
        idade (int): Idade da pessoa

    Returns:
        str: Categoria de faixa etária
    """
    if idade < 18:
        return "Menor de idade"
    elif idade < 30:
        return "18 a 29 anos"
    elif idade < 50:
        return "30 a 49 anos"
    else:
        return "50 anos ou mais"


def banco_aleatorio():
    """
    Retorna um nome de banco aleatório da BrasilAPI.

    Returns:
        str: Nome do banco ou 'Banco X' em caso de erro
    """
    try:
        url = "https://brasilapi.com.br/api/banks/v1"
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            bancos = r.json()
            return random.choice(bancos)['name']
    except:
        pass
    return "Banco X"


def simular_salario(faixa):
    """
    Simula salário com base na faixa etária.

    Args:
        faixa (str): Categoria da faixa etária

    Returns:
        int: Valor salarial simulado
    """
    if faixa == "Menor de idade":
        return random.randint(600, 1100)
    elif faixa == "18 a 29 anos":
        return random.randint(1418, 3400)
    else:
        return random.randint(3400, 10000)

# === Aplicação das transformações ===


df["faixa_etaria"] = df["idade"].apply(faixa_etaria)
df["banco"] = df["nome"].apply(lambda _: banco_aleatorio())
df["salario_simulado"] = df["faixa_etaria"].apply(simular_salario)

df.to_csv("../data/data_processed/usuarios_enriquecidos.csv",
          index=False, encoding="utf-8-sig")
