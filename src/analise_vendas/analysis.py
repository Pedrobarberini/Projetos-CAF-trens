import numpy as np

def calcular_kpis(df):

    receita_total =  np.sum(df['valor_total'])
    lucro_total = np.sum(df['lucro'])
    ticket_medio = np.mean(df['valor_total'])

    return {
        'receita_total': receita_total,
        'lucro_total': lucro_total,
        'ticket_medio': ticket_medio
    }
