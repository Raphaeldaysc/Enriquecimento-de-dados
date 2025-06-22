# 🏦 Análise e Enriquecimento de Dados Bancários com Python

> Projeto de simulação e enriquecimento de base de dados de clientes bancários utilizando **Python**, **Pandas** e **APIs públicas**.

## 📌 Objetivo

Criar uma base de dados realista e tratada de usuários para simular análises de perfis bancários por faixa etária, instituição financeira e salário estimado. O foco está no **tratamento, enriquecimento e preparação dos dados** com qualidade para futuras análises, relatórios e dashboards.

---

## 🧰 Tecnologias Utilizadas

- Python 3.12+
- Pandas
- Requests
- RandomUser API
- BrasilAPI

---

## 🔄 Pipeline de Transformação

1. **Extração de Dados**
   - Usuários gerados pela API [randomuser.me](https://randomuser.me/)
   - Dados retornados: nome, idade, gênero, cidade, estado

2. **Transformações com Pandas**
   - Classificação por faixa etária (`Menor de idade`, `18 a 29 anos`, etc)
   - Enriquecimento com banco aleatório (via BrasilAPI)
   - Simulação de salário por faixa etária
   - Simulação de tempo como cliente do banco

3. **Exportação**
   - Dados salvos como CSV limpo em `data/data_enriched/`
   - Prontos para análises futuras com Power BI, SQL ou dashboards

---

## 📊 Variáveis Criadas

| Coluna              | Descrição                                       |
|---------------------|-------------------------------------------------|
| faixa_etaria        | Classificação por idade                         |
| banco               | Nome de banco aleatório (via BrasilAPI)         |
| salario_simulado    | Faixa salarial gerada com base no perfil        |
| cliente_desde       | Data simulada de início de relacionamento       |
| anos_de_relacionamento | Tempo total como cliente                     |

---

## 💬 Autor
Desenvolvido por Raphael Dias Câmara

