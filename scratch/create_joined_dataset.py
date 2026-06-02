import pandas as pd
import os

csv_dir = r"c:\Users\milli\OneDrive\Documentos\GitHub\ValoraCasa\.github\workflows\CSV"
pred_path = os.path.join(csv_dir, "predicciones_valoracasa.csv")
viv_path = os.path.join(csv_dir, "viviendas_limpio_valuacasa.csv")

df_pred = pd.read_csv(pred_path)
df_viv = pd.read_csv(viv_path)
df_rented = df_viv[df_viv['tenencia'] == 1].copy()

# Stable matching: assign each prediction a unique row from df_rented with matching rent
assigned_indices = set()
mapping = []

for idx, row in df_pred.iterrows():
    rent = row['renta_real']
    # Find all matching rows in df_rented
    matches = df_rented[abs(df_rented['renta'] - rent) < 1e-3]
    match_idx = None
    for m_idx in matches.index:
        if m_idx not in assigned_indices:
            match_idx = m_idx
            assigned_indices.add(m_idx)
            break
    
    if match_idx is None:
        # If all matches are assigned, just pick the first match (even if duplicate)
        if len(matches) > 0:
            match_idx = matches.index[0]
        else:
            # Fallback to closest rent
            diffs = abs(df_rented['renta'] - rent)
            match_idx = diffs.idxmin()
            
    mapping.append(match_idx)

df_pred['matched_viv_idx'] = mapping

# Join features from df_viv
df_features = df_viv.loc[mapping].reset_index(drop=True)
df_joined = pd.concat([df_pred, df_features], axis=1)

print("Joined shape:", df_joined.shape)
print("Null values in joined:", df_joined.isnull().sum().sum())
print("First 3 rows of joined:")
print(df_joined[['ID', 'renta_real', 'renta', 'tipo_viv', 'num_cuarto', 'pred_xgb_pesos']].head(3))
