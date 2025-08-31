import streamlit as st
import plotly.express as px
from utils import *
st.set_page_config(layout='wide')

st.title("Atividade 3 - Credit Card Spending in India (Dashboard)")
st.write("Link: https://www.kaggle.com/datasets/divyaraj2006/credit-card-spending-in-india")
st.image("assets/course_banner.png")
st.image("assets/dataset-cover.jpg", width=400)

#------------------------------------------------------------

st.set_page_config(layout='wide')
st.sidebar.write("Escolha as páginas")
st.sidebar.markdown("## Seleções no Gráfico")

select_event = st.sidebar.multiselect('Selecione datas', options=date_options)
select_city = st.sidebar.selectbox('Selecione a cidade', options=city_options, index=0)
select_gender = st.sidebar.selectbox('Selecione o gênero', options=gender_options, index=0)
select_card_type = st.sidebar.radio('Selecione um tipo de cartão', card_options)

#------------------------------------------------------------

# Filtrando período
if select_event:
    filtered = filtered[filtered['Date'].dt.normalize().isin(select_event)]
# Filtrando Cidades
if select_city != 'Todas':
    filtered = filtered[filtered['City'] == select_city]
# Filtrando por tipo de cartão
if select_card_type != 'Todos':
    filtered_card = filtered[filtered['Card Type'] == select_card_type]
else:
    filtered_card = filtered

# -----------------------------------------------------------
# CARDS TOTAIS
# CARD 1
rounded_amount = sum([round(a, 1) for a in filtered['Amount']])
amount_format = f"$ {human_format(rounded_amount)}"

#CARD 2
len_payments = len(filtered['index'])

#CARD 3
avg_amount = sum(filtered['Amount'])/len(filtered['Amount'])
avg_amount_format = f"$ {human_format(avg_amount)}"

col1, col2, col3 = st.columns(3)
col1.metric("Valor Total", amount_format, border=True)
col2.metric("Número de Pagamentos", len_payments, border=True)
col3.metric("Valor Médio", avg_amount_format, border=True)

#------------------------------------------------------------

st.write(f'Linhas após filtro: {len(filtered)}')
st.dataframe(filtered.head(20))

#------------------------------------------------------------


tab1, tab2 = st.tabs(["Pie chart", "Box plot"])
with tab1:
    st.subheader("Gráfico dos tipos de cartão (por cidade)")
    card_type_count = filtered["Card Type"].value_counts()
    fig1 = px.pie(card_type_count, values="count", names=card_type_count.index, color=card_type_count.index, color_discrete_map=card_colors)
    st.plotly_chart(fig1, key="pie_chart")

with tab2:
    st.subheader("Box plot de custo de transação (por tipo de cartão)")
    fig2 = px.box(
        filtered_card,
        x="Card Type",
        y="Amount",
        color="Card Type",
        color_discrete_map=card_colors,
        points="all",
        labels={"Amount": "Valor ($)", "Card Type": "Tipo de Cartão"},
    )
    st.plotly_chart(fig2, key="box_plot")

#------------------------------------------------------------

with st.container():
    st.subheader("Gráfico Histórico de Gastos (por data e cidade)")
grouped_data = (
    filtered
    .assign(Date=filtered['Date'].dt.normalize())
    .groupby('Date', as_index=False)['Amount']
    .sum()
    .sort_values('Date')
)

if grouped_data.empty:
    st.info('Não há dados selecionados')
else:
    chart_df = grouped_data.set_index('Date')
    st.bar_chart(data=chart_df, use_container_width=True)
