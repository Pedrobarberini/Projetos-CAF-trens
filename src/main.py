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

    print("Iniciando pipeline de dados...\n")

    #Carregamento 
    pedidos, produtos, clientes = carregar_dados()
    print("Dados carregados com sucesso!\n")

    #Limpeza 
    pedidos  = limpar_pedidos(pedidos)
    print("Dados de pedidos limpos com sucesso!\n")
    produtos = limpar_produtos(produtos)
    print("Dados de produtos limpos com sucesso!\n")
    clientes = limpar_clientes(clientes)
    print("Dados de clientes limpos com sucesso!\n")

    salvar_csv(pedidos, write_base, "data", "processed", "dados_limpos.csv")
    print("Dados limpos salvos com sucesso!\n")

    #Integração e criação de variáveis 
    df = integrar_dados(pedidos, produtos, clientes)
    print("Dados integrados com sucesso!\n")

    df = criar_variaveis(df)
    print("Variáveis criadas com sucesso!\n")

    salvar_csv(df, write_base, "data", "processed", "dados_processados.csv")
    print("Dados processados salvos com sucesso!\n")

    salvar_csv(df, write_base, "data", "processed", "dados_integrados.csv")
    print("Dados integrados salvos com sucesso!\n")

    kpis = calcular_kpis(df)
    print("KPIs calculados com sucesso!\n")

    plot_kpis(kpis, df)

    print("Pipeline de dados finalizada com sucesso!")


if __name__ == "__main__":
    main()