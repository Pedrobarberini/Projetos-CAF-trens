import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

COLORS = {
    "accent":  "#00e5ff",
    "purple":  "#7c3aed",
    "amber":   "#f59e0b",
    "green":   "#10b981",
    "rose":    "#f43f5e",
    "indigo":  "#6366f1",
    "bg":      "#111827",
    "grid":    "rgba(255,255,255,0.04)",
    "text":    "#f0f4ff",
    "muted":   "#6b7280",
}

PALETTE = [
    "#00e5ff", "#7c3aed", "#f59e0b", "#10b981",
    "#f43f5e", "#6366f1", "#06b6d4", "#a78bfa",
]

PLOTLY_LAYOUT = dict(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(family="DM Sans, sans-serif", color=COLORS["text"], size=12),
    title_font=dict(family="Syne, sans-serif", size=16, color=COLORS["text"]),
    legend=dict(
        bgcolor="rgba(255,255,255,0.04)",
        bordercolor="rgba(0,229,255,0.15)",
        borderwidth=1,
        font=dict(size=10),
        orientation="h",
        yanchor="bottom",
        y=-0.32,
        xanchor="center",
        x=0.5,
    ),
    xaxis=dict(
        gridcolor=COLORS["grid"],
        zerolinecolor=COLORS["grid"],
        tickangle=0,
        tickfont=dict(size=10),
        tickmode="linear",
        automargin=True,
    ),
    yaxis=dict(
        gridcolor=COLORS["grid"],
        zerolinecolor=COLORS["grid"],
        tickfont=dict(size=11),
    ),
    bargap=0.25,
    margin=dict(l=16, r=16, t=48, b=90),
    hoverlabel=dict(
        bgcolor=COLORS["bg"],
        bordercolor=COLORS["accent"],
        font_size=12,
        font_family="DM Sans, sans-serif",
    ),
)


def _apply_layout(fig, extra: dict = None):
    layout = PLOTLY_LAYOUT.copy()
    if extra:
        layout.update(extra)
    fig.update_layout(**layout)
    return fig


def _bar_style(fig):
    fig.update_traces(
        marker=dict(line=dict(width=0), opacity=0.9),
        selector=dict(type="bar"),
    )
    return fig


CSS = """
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:wght@300;400;500&display=swap');

:root {
  --bg-main:     #0a0e1a;
  --bg-card:     #111827;
  --accent:      #00e5ff;
  --accent2:     #7c3aed;
  --accent3:     #f59e0b;
  --text:        #f0f4ff;
  --muted:       #6b7280;
  --border:      rgba(0,229,255,0.12);
  --glow:        0 0 30px rgba(0,229,255,0.15);
  --glow-strong: 0 0 60px rgba(0,229,255,0.28);
  --radius:      16px;
}

html, body, [class*="css"] {
  font-family: 'DM Sans', sans-serif !important;
  background-color: var(--bg-main) !important;
  color: var(--text) !important;
}

#MainMenu, footer, header { visibility: hidden; }
.stDeployButton { display: none; }

.stApp {
  background: var(--bg-main) !important;
  background-image:
    radial-gradient(ellipse 80% 50% at 20% -10%, rgba(0,229,255,0.07) 0%, transparent 60%),
    radial-gradient(ellipse 60% 40% at 80% 110%, rgba(124,58,237,0.07) 0%, transparent 60%),
    repeating-linear-gradient(0deg, transparent, transparent 39px, rgba(255,255,255,0.013) 39px, rgba(255,255,255,0.013) 40px),
    repeating-linear-gradient(90deg, transparent, transparent 39px, rgba(255,255,255,0.013) 39px, rgba(255,255,255,0.013) 40px) !important;
}

.block-container {
  padding: 2rem 3rem !important;
  max-width: 1400px !important;
}

h1 {
  font-family: 'Syne', sans-serif !important;
  font-weight: 800 !important;
  font-size: 2rem !important;
  letter-spacing: 0.12em !important;
  text-transform: uppercase !important;
  background: linear-gradient(135deg, #00e5ff 0%, #a78bfa 50%, #f59e0b 100%) !important;
  -webkit-background-clip: text !important;
  -webkit-text-fill-color: transparent !important;
  background-clip: text !important;
  animation: titleFade 2.0s ease forwards;
}

@keyframes titleFade {
  from { opacity: 0; transform: translateY(-10px); }
  to   { opacity: 1; transform: translateY(0); }
}

[data-testid="metric-container"] {
  background: var(--bg-card) !important;
  border: 1px solid var(--border) !important;
  border-radius: var(--radius) !important;
  padding: 1.2rem 1.5rem !important;
  box-shadow: var(--glow), inset 0 1px 0 rgba(255,255,255,0.04) !important;
  position: relative;
  overflow: hidden;
  animation: cardIn 1.5s ease forwards;
  transition: transform 0.25s ease, box-shadow 0.25s ease !important;
}

[data-testid="metric-container"]::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 2px;
  background: linear-gradient(90deg, var(--accent), var(--accent2));
}

[data-testid="metric-container"]:hover {
  transform: translateY(-3px) !important;
  box-shadow: var(--glow-strong), inset 0 1px 0 rgba(255,255,255,0.08) !important;
}

[data-testid="metric-container"] label {
  font-size: 0.72rem !important;
  font-weight: 500 !important;
  letter-spacing: 0.1em !important;
  text-transform: uppercase !important;
  color: var(--muted) !important;
}

[data-testid="metric-container"] [data-testid="stMetricValue"] {
  font-family: 'Syne', sans-serif !important;
  font-size: 1.5rem !important;
  font-weight: 700 !important;
  color: var(--text) !important;
}

@keyframes cardIn {
  from { opacity: 0; transform: translateY(14px); }
  to   { opacity: 1; transform: translateY(0); }
}

[data-testid="stPlotlyChart"] {
  background: var(--bg-card) !important;
  border: 1px solid var(--border) !important;
  border-radius: var(--radius) !important;
  padding: 0.5rem !important;
  box-shadow: var(--glow) !important;
  animation: chartIn 0.8s ease forwards;
  transition: box-shadow 0.3s ease, transform 0.3s ease !important;
}

[data-testid="stPlotlyChart"]:hover {
  box-shadow: var(--glow-strong) !important;
  transform: translateY(-2px) !important;
}

@keyframes chartIn {
  from { opacity: 0; transform: scale(0.97); }
  to   { opacity: 1; transform: scale(1); }
}

.stButton > button {
  background: rgba(0,229,255,0.08) !important;
  border: 1px solid rgba(0,229,255,0.3) !important;
  border-radius: 8px !important;
  color: var(--accent) !important;
  font-family: 'DM Sans', sans-serif !important;
  font-size: 0.8rem !important;
  padding: 0.3rem 1rem !important;
  transition: background 0.2s ease, box-shadow 0.2s ease !important;
}

.stButton > button:hover {
  background: rgba(0,229,255,0.18) !important;
  box-shadow: 0 0 12px rgba(0,229,255,0.2) !important;
}

::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: var(--bg-main); }
::-webkit-scrollbar-thumb { background: var(--accent2); border-radius: 99px; }

[data-testid="column"] { padding: 0 0.5rem !important; }
"""


def inject_css():
    st.markdown(f"<style>{CSS}</style>", unsafe_allow_html=True)


def plot_kpis(kpis, df):
    inject_css()

    receita = float(kpis["receita_total"])
    lucro   = float(kpis["lucro_total"])
    ticket  = float(kpis["ticket_medio"])

    st.markdown(
        "<h1 style='text-align:center'>Dashboard de Vendas</h1>",
        unsafe_allow_html=True,
    )

    # KPIs linha 1
    col1, col2, col3 = st.columns(3)
    col1.metric("Receita Total", f"R$ {receita:,.2f}")
    col2.metric("Lucro Total",   f"R$ {lucro:,.2f}")
    col3.metric("Ticket Médio",  f"R$ {ticket:,.2f}")

    st.markdown("<br>", unsafe_allow_html=True)

    # KPIs linha 2
    col4, col5, col6, col7 = st.columns(4)
    col4.metric("Pedidos",    df["pedido_id"].nunique())
    col5.metric("Clientes",   df["cliente_id"].nunique())
    col6.metric("Produtos",   df["produto_id"].nunique())
    col7.metric("Categorias", df["categoria"].nunique())

    st.markdown("<br>", unsafe_allow_html=True)

    # Meses
    meses = {
        1:"Jan", 2:"Fev", 3:"Mar", 4:"Abr",
        5:"Mai", 6:"Jun", 7:"Jul", 8:"Ago",
        9:"Set", 10:"Out", 11:"Nov", 12:"Dez",
    }
    meses_inv = {v: k for k, v in meses.items()} 

    # Gráfico: Receita por Mês 
    receita_mes = (
        df.groupby("mes")["valor_total"]
        .sum()
        .reset_index()
    )
    receita_mes["mes"] = receita_mes["mes"].astype(int).map(meses)

    fig_mes = px.bar(
        receita_mes,
        x="mes",
        y="valor_total",
        title="Receita por Mês",
        color="mes",
        color_discrete_sequence=PALETTE,
        category_orders={"mes": list(meses.values())},
        labels={"mes": "", "valor_total": "Valor Total"},
    )
    _bar_style(fig_mes)
    _apply_layout(fig_mes, extra={"showlegend": False})

    # Gráfico: Receita por Estado 
    receita_estado = (
        df.groupby("estado")["valor_total"]
        .sum()
        .reset_index()
    )

    fig_estado = px.bar(
        receita_estado,
        x="estado",
        y="valor_total",
        title="Receita por Estado",
        color="estado",
        color_discrete_sequence=PALETTE,
        labels={"estado": "", "valor_total": "Valor Total"},
    )
    _bar_style(fig_estado)
    _apply_layout(fig_estado, extra={"showlegend": False})

    # Linha 1: Receita por Mês + Receita por Estado
    cols_top = st.columns(2)
    cols_top[0].plotly_chart(fig_mes,    use_container_width=True, key="grafico_mes")
    cols_top[1].plotly_chart(fig_estado, use_container_width=True, key="grafico_estado")

    st.markdown("<br>", unsafe_allow_html=True)

    # Filtro por mês via selectbox
    estados_disponiveis = ["Todos"] + sorted(df["estado"].unique().tolist())

    col_mes, col_estado = st.columns(2)

    meses_disponiveis = ["Todos"] + [
        meses[m] for m in sorted(df["mes"].astype(int).unique())
    ]

    mes_sel = col_mes.selectbox(
        "Filtrar por mês:",
        options=meses_disponiveis,
        index=0,
        key="filtro_mes_select",
    )
    estado_sel = col_estado.selectbox(
        "Filtrar por estado:",
        options=estados_disponiveis,
        index=0,
        key="filtro_estado_select",
    )    

    # Aplica filtro 
    df_filtrado = df.copy()

    if mes_sel != "Todos":
        mes_num     = meses_inv[mes_sel]
        df_filtrado = df[df["mes"].astype(int) == mes_num]
    else:
        df_filtrado = df

    if estado_sel != "Todos":
        df_filtrado = df_filtrado[df_filtrado["estado"] == estado_sel]

    # Título dinâmico para o gráfico de categorias
    partes = []
    if mes_sel != "Todos": partes.append(mes_sel)
    if estado_sel != "Todos": partes.append(estado_sel)
    titulo_cat = "Receita por Categoria - " + ", ".join(partes) if partes else "Receita por Categoria - Todos os meses e estados"

    # Gráfico: Donut filtrado
    receita_categoria = (
        df_filtrado.groupby("categoria")["valor_total"]
        .sum()
        .reset_index()
    )

    fig_categoria = px.pie(
        receita_categoria,
        names="categoria",
        values="valor_total",
        title=titulo_cat,
        color_discrete_sequence=PALETTE,
        hole=0.55,
    )
    fig_categoria.update_traces(
        textfont=dict(family="DM Sans, sans-serif", size=12),
        marker=dict(line=dict(color=COLORS["bg"], width=2)),
    )
    _apply_layout(fig_categoria)
    st.plotly_chart(fig_categoria, use_container_width=True, key="chart_categoria")