import kagglehub
import pandas as pd

path = kagglehub.dataset_download("divyaraj2006/credit-card-spending-in-india")
df = pd.read_csv(f"{path}/Credit Card Spending in India.csv")
# --------------------------------------------------------------