import pandas as pd

# CSV file kholo (latin-1 isliye, kyunki file mein special characters hain)
df = pd.read_csv("data/DataCoSupplyChainDataset.csv", encoding="latin-1")

# Kitni rows aur columns hain
print(df.shape)

# Pehli 5 rows dekho
print(df.head())

# Columns ke naam aur data type dekho
print(df.info())