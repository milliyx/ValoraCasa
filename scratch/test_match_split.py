import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import os

csv_dir = r"c:\Users\milli\OneDrive\Documentos\GitHub\ValoraCasa\.github\workflows\CSV"
pred_path = os.path.join(csv_dir, "predicciones_valoracasa.csv")
viv_path = os.path.join(csv_dir, "viviendas_limpio_valuacasa.csv")

df_pred = pd.read_csv(pred_path)
df_viv = pd.read_csv(viv_path)
df_rented = df_viv[df_viv['tenencia'] == 1].copy()

# Let's check train_test_split on df_rented
# We know the y variable was probably renta or log(renta)
# Let's see if we can match the exact list of renta in the test set.
# Let's try different random_states.
target_rents = df_pred['renta_real'].tolist()

print("Target first 10 rents:", target_rents[:10])

for rs in range(100):
    train, test = train_test_split(df_rented, test_size=2291, random_state=rs)
    test_rents = test['renta'].tolist()
    # Let's see if the first few rents match exactly
    match_count = sum(1 for a, b in zip(test_rents[:10], target_rents[:10]) if abs(a - b) < 1e-5)
    if match_count >= 5:
        print(f"Match found at random_state {rs}! First 10 test rents: {test_rents[:10]}")
        break
else:
    print("No simple train_test_split random_state matched directly.")
