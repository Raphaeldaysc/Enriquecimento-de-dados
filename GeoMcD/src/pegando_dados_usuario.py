"""
Módulo para gerar dados de usuários aleatórios.

Este script utiliza a API RandomUser para criar um conjunto de dados
com informações de usuários brasileiros.
"""
import pandas as pd
import requests as req


def gerar_usuario(quantidade):
    """
    Gera uma quantidade específica de dados de usuários aleatórios.
    
    Args:
        quantidade (int): Número de usuários a serem gerados.
        
    Returns:
        pandas.DataFrame: DataFrame contendo os dados dos usuários gerados.
        
    Raises:
        Exception: Se a API retornar um código diferente de 200.
    """
    url = f"https://randomuser.me/api/?results={quantidade}&nat=br&inc=name,gender,email,login,dob,cell,location"
    resposta = req.get(url)

    if resposta.status_code != 200:
        raise Exception(f"Erro ao acessar a API: {resposta.status_code}")

    dados = resposta.json()["results"]
    lista_usuarios = []

    for pessoa in dados:
        lista_usuarios.append({
            "nome": f"{pessoa['name']['first']} {pessoa['name']['last']}",
            "genero": pessoa['gender'],
            "email": pessoa['email'],
            "usuario": pessoa['login']['username'],
            "nascimento": pessoa['dob']['date'],
            "idade": pessoa['dob']['age'],
            "telefone": pessoa['cell'],
            "cidade": pessoa['location']['city'],
            "estado": pessoa['location']['state']
        })
    return pd.DataFrame(lista_usuarios)


# Gera 200 usuários e salva em um arquivo CSV
df_usuarios = gerar_usuario(200)
df_usuarios.to_csv("../data/data_raw/usuarios.csv",
                   index=False, encoding="utf-8-sig")
