import streamlit as st
from utils import *
st.set_page_config(layout='wide')

st.title("Atividade 3 - Credit Card Spending in India (Dashboard)")
st.write("Link: https://www.kaggle.com/datasets/divyaraj2006/credit-card-spending-in-india")
st.image("assets/course_banner.png")
st.image("assets/dataset.cover.jpg") # <<-- não sei porque está dando erro ao subir essa imagem
 
#st.write(df.head())

#------------------------------------------------------------

st.set_page_config(layout='wide')
st.sidebar.write("Escolha as páginas")
st.sidebar.markdown("## Seleções no Gráfico")

select_event = st.sidebar.multiselect('Selecione datas', options=date_options)
select_city = st.sidebar.selectbox('Selecione a cidade', options=city_options, index=0)
select_gender = st.sidebar.selectbox('Selecione a Gênero', options=gender_options, index=0)

# --------------------------------------------------------
# CARDS TOTAIS
# CARD 1
round_amount = [round(a, 1) for a in df['Amount']]
amount = sum(round_amount)
amount_var = df['Amount'].pct_change().iloc[-1] * 100
amount_format = f"${human_format(amount)}"
amount_var_format = f"{amount_var:.2f}%"

#CARD 2
len_payments = len(df['index'])

#CARD 3
avg_amount = sum(df['Amount'])/len(df['Amount'])
avg_amount_format = f"${human_format(avg_amount)}"

col1, col2, col3 = st.columns(3)
col1.metric("Valor Total", amount_format, amount_var_format, border=True)
col2.metric("Total de Pagamentos", len_payments, border=True)
col3.metric("Valor Médio", avg_amount_format, border=True)

#----------------------------------------------------------------

# Filtrando período
if select_event:
    filtered = filtered[filtered['Date'].dt.normalize().isin(select_event)]
# Filtrando Cidades
if select_city != 'Todas':
    filtered = filtered[filtered['City'] == select_city]

st.write(f'Linhas após filtro: {len(filtered)}')
st.dataframe(filtered.head(20))

#------------------------------------------------------------

with st.container():
    st.write("Gráfico Histórico de Gastos")
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
