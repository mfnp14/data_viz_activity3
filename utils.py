import kagglehub
import pandas as pd

path = kagglehub.dataset_download("divyaraj2006/credit-card-spending-in-india")
df = pd.read_csv(f"{path}/Credit Card Spending in India.csv")
df = df.dropna(how="all")
# --------------------------------------------------------------

#-- Selecionar o periodo de coleta
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce')

date_options = sorted(df['Date'].dt.normalize().unique())
city_options = ['Todas'] + sorted(df['City'].dropna().unique().tolist())
gender_options = ['Todas'] + sorted(df['Gender'].dropna().unique().tolist())

filtered = df.copy()


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