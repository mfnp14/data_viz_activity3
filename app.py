import streamlit as st
from utils import *
st.set_page_config(layout='wide')

st.title("Atividade 3 - Credit Card Spending in India (Dashboard)")
st.write("Link: https://www.kaggle.com/datasets/divyaraj2006/credit-card-spending-in-india")
st.image("assets/course_banner.png")

st.write(df.head())

#------------------------------------------------------------

st.set_page_config(layout='wide')
st.sidebar.write("Escolha as páginas")
st.sidebar.markdown("## Seleções no Gráfico")

select_event = st.sidebar.multiselect('Selecione datas', options=date_options)
select_city = st.sidebar.selectbox('Selecione a cidade', options=city_options, index=0)

# Filtrando período
if select_event:
    filtered = filtered[filtered['Date'].dt.normalize().isin(select_event)]
# Filtrando Cidades
if select_city != 'Todas':
    filtered = filtered[filtered['City'] == select_city]

st.write(f'Linhas após filtro: {len(filtered)}')
st.dataframe(filtered.head(20))

#------------------------------------------------------------

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
