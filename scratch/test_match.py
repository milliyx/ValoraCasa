import pandas as pd
import os

csv_dir = r"c:\Users\milli\OneDrive\Documentos\GitHub\ValoraCasa\.github\workflows\CSV"
pred_path = os.path.join(csv_dir, "predicciones_valoracasa.csv")
viv_path = os.path.join(csv_dir, "viviendas_limpio_valuacasa.csv")

df_pred = pd.read_csv(pred_path)
df_viv = pd.read_csv(viv_path)

# Let's filter df_viv to tenencia == 1 (rented)
df_rented = df_viv[df_viv['tenencia'] == 1].copy()

print(f"df_pred rows: {len(df_pred)}")
print(f"df_rented rows: {len(df_rented)}")

# Let's see if the test set is a subset of df_rented, and if so, how many have exact matching renta.
# Let's merge on renta_real == renta and see if we can find a unique match for each prediction.
# Note that renta might not be unique, so we can try to find candidate matches.

matched_indices = []
for idx, row in df_pred.iterrows():
    rent = row['renta_real']
    # find matches in df_rented
    matches = df_rented[abs(df_rented['renta'] - rent) < 1e-5]
    if len(matches) == 1:
        matched_indices.append((idx, matches.index[0], 1))
    elif len(matches) > 1:
        matched_indices.append((idx, list(matches.index), len(matches)))
    else:
        matched_indices.append((idx, None, 0))

counts = {0: 0, 1: 0, "many": 0}
for idx, m_idx, count in matched_indices:
    if count == 0:
        counts[0] += 1
    elif count == 1:
        counts[1] += 1
    else:
        counts["many"] += 1

print("Matches counts:", counts)
