import kagglehub
import pandas as pd

path = kagglehub.dataset_download("divyaraj2006/credit-card-spending-in-india")
df = pd.read_csv(f"{path}/Credit Card Spending in India.csv")
df = df.dropna(how="all")
# --------------------------------------------------------------

#-- Selecionar o periodo de coleta
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce')

filtered = df.copy()

date_options = sorted(df['Date'].dt.normalize().unique())
city_options = ['Todas'] + sorted(df['City'].dropna().unique().tolist())
gender_options = ['Todos'] + sorted(df['Gender'].dropna().unique().tolist())
card_options = ['Todos'] + sorted(filtered['Card Type'].unique())

# ------------ Função para Formatar valor $ no card inicial
def human_format(num):
    num = float('{:.3g}'.format(num))
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    return '{}{}'.format(
        '{:f}'.format(num).rstrip('0').rstrip('.'),
        ['', 'K', 'M', 'B', 'T'][magnitude]
    )

#------------------------------------------------------------

card_colors = {
    "Gold": "#F4D35E",
    "Platinum": "#4F5057",
    "Signature": "#5886CC",
    "Silver": "#B0B0B0"
}
