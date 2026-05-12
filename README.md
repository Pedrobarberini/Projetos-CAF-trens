# 📊 Projeto de Análise de Vendas com Python

## 📌 Sobre o Projeto

Este projeto tem como objetivo realizar uma análise de dados de vendas utilizando Python, com foco em boas práticas de organização de código, manipulação de dados e geração de insights.

A aplicação simula um pipeline de dados completo, desde a leitura de arquivos brutos até a geração de métricas de negócio (KPIs).

---

## 🎯 Objetivos

* Praticar manipulação de dados com **Pandas** e **NumPy**
* Estruturar um projeto de dados de forma profissional
* Criar um pipeline de dados (ETL simplificado)
* Gerar métricas relevantes para tomada de decisão

---

## 🧠 Funcionalidades

✔ Leitura de dados CSV
✔ Limpeza e tratamento de dados
✔ Integração de múltiplas tabelas (merge)
✔ Criação de variáveis de negócio
✔ Cálculo de KPIs
✔ Exportação de dados processados

---

## 🔄 Pipeline de Dados

O fluxo do projeto segue as seguintes etapas:

```
Dados Brutos → Limpeza → Processamento → Análise → Output
```

### Etapas:

1. **Carregamento**

   * Leitura dos arquivos CSV

2. **Limpeza**

   * Remoção de duplicados
   * Tratamento de valores nulos
   * Padronização de dados

3. **Processamento**

   * Merge entre tabelas
   * Criação de colunas:

     * valor_total
     * custo_total
     * lucro

4. **Análise**

   * Cálculo de KPIs

5. **Exportação**

   * Salvamento dos dados tratados

---
### Etapas de alteração de dados:

projeto-analise-vendas\data\raw

-clientes.csv
-pedidos.csv
-produtos.csv

parametro de dados:

cliente : cliente_id,nome,cidade,estado

pedidos : pedido_id,cliente_id,produto_id,data_pedido,quantidade,preco_custo,desconto,frete

produtos : produto_id,nome,categoria,preco_unitario
---

## 📊 KPIs Gerados

O projeto calcula as seguintes métricas:

* 💰 Receita total
* 📈 Lucro total
* 🧾 Ticket médio

Exemplo de saída:

```
{
  "receita_total": 31670.0,
  "lucro_total": 10720.0,
  "ticket_medio": 1583.5
}
```

---

## 🛠️ Tecnologias Utilizadas

* Python 3
* Pandas
* NumPy
* mapplotlib
---

## ▶️ Como Executar o Projeto

### 1. Clonar o repositório

```
git clone https://github.com/Pedrobarberini/Treinamento-Python.git
```

### 2. Acessar a pasta

```
cd Treinamento-Python
```

### 3. Instalar dependências

```
pip install -r requirements.txt
```

### 4. Executar o projeto

```
python main.py
```

---

## 📂 Saídas do Projeto

Após a execução, os arquivos serão gerados em:

```
data/processed/
```

Exemplo:

* dados_limpos.csv
* dados_completos.csv

---

## 📈 Possíveis Melhorias

* Criação de dashboards com gráficos
* Análises por estado e categoria
* Automação do pipeline
* Integração com banco de dados
* Testes automatizados

---

## 💼 Sobre o Projeto

Este projeto foi desenvolvido com foco em aprendizado prático e simulação de um ambiente real de análise de dados, seguindo boas práticas de engenharia de dados e organização de código.

---

## 👨‍💻 Autor

**Pedro Barberini**

* GitHub: https://github.com/Pedrobarberini
* Portfólio: https://pedrobarberini.github.io/Curriculo/

---

## ⭐ Considerações Finais

Este projeto representa a evolução prática no uso de Python para análise de dados, cobrindo desde conceitos básicos até a construção de um pipeline estruturado.

---

[1]: https://docs.github.com/pt/actions/tutorials/build-and-test-code/python?utm_source=chatgpt.com "Criar e testar o Python - Documentos do GitHub"
