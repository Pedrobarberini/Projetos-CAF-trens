import os
import sys
import pandas as pd


def get_read_path():
    """Retorna o caminho base para LEITURA dos dados (dentro do .exe ou do projeto)."""
    if hasattr(sys, '_MEIPASS'):
        return sys._MEIPASS
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))


def carregar_dados():
    base_path = get_read_path()

    path_pedidos  = os.path.join(base_path, "data", "raw", "pedidos.csv")
    path_produtos = os.path.join(base_path, "data", "raw", "produtos.csv")
    path_clientes = os.path.join(base_path, "data", "raw", "clientes.csv")

    pedidos  = pd.read_csv(path_pedidos)
    produtos = pd.read_csv(path_produtos)
    clientes = pd.read_csv(path_clientes)

    return pedidos, produtos, clientes