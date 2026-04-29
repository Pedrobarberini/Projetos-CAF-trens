import pandas as pd


def integrar_dados(pedidos, produtos, clientes):
    """Faz o merge entre pedidos, produtos e clientes."""
    pedidos_produtos  = pedidos.merge(produtos, on='produto_id', how='left')
    dados_integrados  = pedidos_produtos.merge(clientes, on='cliente_id', how='left')
    return dados_integrados


def criar_variaveis(dados):
    """Cria colunas derivadas de data e valores financeiros."""
    dados = dados.copy()
    dados['data_pedido'] = pd.to_datetime(dados['data_pedido'])

    dados['ano']  = dados['data_pedido'].dt.year
    dados['mes']  = dados['data_pedido'].dt.month
    dados['dia']  = dados['data_pedido'].dt.day

    dados['valor_total'] = dados['quantidade'] * dados['preco_unitario']
    dados['custo_total'] = dados['quantidade'] * dados['preco_custo']
    dados['lucro']       = dados['valor_total'] - dados['custo_total']

    return dados