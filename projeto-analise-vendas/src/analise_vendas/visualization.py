import matplotlib.pyplot as plt

meses = {
    1: "Jan", 2: "Fev", 3: "Mar", 4: "Abr",
    5: "Mai", 6: "Jun", 7: "Jul", 8: "Ago",
    9: "Set", 10: "Out", 11: "Nov", 12: "Dez"
    }

def plot_kpis(kpis, df):
    fig = plt.figure(figsize=(10,6))

    receita = float(kpis["receita_total"])
    lucro = float(kpis["lucro_total"])
    ticket = float(kpis["ticket_medio"])
    fig.text(0.1, 0.93, f"Receita: R$ {receita:,.2f}", fontsize=12)
    fig.text(0.1, 0.88, f"Lucro: R$ {lucro:,.2f}", fontsize=12)
    fig.text(0.1, 0.83, f"Ticket Médio: R$ {ticket:,.2f}", fontsize=12)

    ax = fig.add_axes([0.1, 0.1, 0.8, 0.6])

    receita_mes = df.groupby('mes')['valor_total'].sum()
    


    receita_mes = receita_mes.reindex(range(1, 13), fill_value=0)

    receita_mes.index = receita_mes.index.map(meses)
    receita_mes.plot(kind='bar', ax=ax, color='green')

    ax.tick_params(axis='x', rotation=0)
    
    ax.set_title("Receita Mensal")
    ax.set_xlabel("Mês")
    ax.set_ylabel("Receita (R$)")

    for i, v in enumerate(receita_mes):
        ax.text(i, v, f"{v:,.0f}", ha='center', va='bottom')
    
    
    plt.show()

