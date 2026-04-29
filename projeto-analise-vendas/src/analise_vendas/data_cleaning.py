import pandas as pd


def limpar_pedidos(df):
    df = df.drop_duplicates()
    df["data_pedido"] = pd.to_datetime(df["data_pedido"], errors='coerce')
    df = df.dropna()
    return df


def limpar_produtos(df):
    df = df.drop_duplicates()
    df["preco_unitario"] = pd.to_numeric(df["preco_unitario"], errors='coerce')
    df = df.dropna()
    return df


def limpar_clientes(df):
    df = df.drop_duplicates()
    df["cliente_id"] = pd.to_numeric(df["cliente_id"], errors='coerce')
    df = df.dropna()
    return df