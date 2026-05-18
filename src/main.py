import os
import sys
import pandas as pd

from analise_vendas.data_loading   import carregar_dados
from analise_vendas.data_cleaning  import limpar_pedidos, limpar_produtos, limpar_clientes
from analise_vendas.data_processing import integrar_dados, criar_variaveis
from analise_vendas.analysis       import calcular_kpis
from analise_vendas.visualization  import plot_kpis


def get_write_path():
    if hasattr(sys, '_MEIPASS'):
        return os.path.dirname(sys.executable)
    return os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def salvar_csv(df, write_base, *subpaths):
    caminho = os.path.join(write_base, *subpaths)
    os.makedirs(os.path.dirname(caminho), exist_ok=True)
    df.to_csv(caminho, index=False)
    return caminho


def main():
    write_base = get_write_path()
    #Carregamento 
    pedidos, produtos, clientes = carregar_dados()
    
    #Limpeza 
    pedidos  = limpar_pedidos(pedidos)
    produtos = limpar_produtos(produtos)
    clientes = limpar_clientes(clientes)
    salvar_csv(pedidos, write_base, "data", "processed", "dados_limpos.csv")


    #Integração e criação de variáveis 
    df = integrar_dados(pedidos, produtos, clientes)
    df = criar_variaveis(df)
    salvar_csv(df, write_base, "data", "processed", "dados_processados.csv")
    salvar_csv(df, write_base, "data", "processed", "dados_integrados.csv")
    kpis = calcular_kpis(df)

    plot_kpis(kpis, df)

    


if __name__ == "__main__":
    main()