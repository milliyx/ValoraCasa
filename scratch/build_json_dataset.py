import pandas as pd
import json
import os

csv_dir = r"c:\Users\milli\OneDrive\Documentos\GitHub\ValoraCasa\.github\workflows\CSV"
pred_path = os.path.join(csv_dir, "predicciones_valoracasa.csv")
viv_path = os.path.join(csv_dir, "viviendas_limpio_valuacasa.csv")

df_pred = pd.read_csv(pred_path)
df_viv = pd.read_csv(viv_path)
df_rented = df_viv[df_viv['tenencia'] == 1].copy()

# Match predicciones to viviendas
assigned_indices = set()
mapping = []

for idx, row in df_pred.iterrows():
    rent = row['renta_real']
    matches = df_rented[abs(df_rented['renta'] - rent) < 1e-3]
    match_idx = None
    for m_idx in matches.index:
        if m_idx not in assigned_indices:
            match_idx = m_idx
            assigned_indices.add(m_idx)
            break
    if match_idx is None:
        if len(matches) > 0:
            match_idx = matches.index[0]
        else:
            match_idx = abs(df_rented['renta'] - rent).idxmin()
    mapping.append(match_idx)

# Extract features
df_features = df_viv.loc[mapping].reset_index(drop=True)

# Construct cases dictionary
casos_dict = {}

for idx, row_pred in df_pred.iterrows():
    row_viv = df_features.iloc[idx]
    
    # Map tipo_viv
    tv = int(row_viv['tipo_viv'])
    if tv == 2:
        tipo_viv = "depto"
    elif tv in [3, 4]:
        tipo_viv = "cuarto"
    else:
        tipo_viv = "casa_sol"
        
    # Map tam_loc
    tl = int(row_viv['tam_loc'])
    if tl == 1:
        loc = "urbana_g"
    elif tl == 2:
        loc = "urbana_m"
    elif tl == 3:
        loc = "urbana_p"
    else:
        loc = "rural"
        
    # Map est_socio
    estrato = int(row_viv['est_socio'])
    
    # Map mat_pisos
    mp = int(row_viv['mat_pisos'])
    if mp == 3:
        piso = "mosaico"
    elif mp == 1:
        piso = "tierra"
    else:
        piso = "cemento"
        
    # Map agua_ent
    ae = int(row_viv['agua_ent'])
    if ae == 1:
        agua = "dentro"
    elif ae == 2:
        agua = "fuera"
    else:
        agua = "no"
        
    # Map checkboxes
    bano = bool(int(row_viv['bano_comp']) >= 1)
    dren = bool(int(row_viv['drenaje']) in [1, 2])
    calentador = bool(int(row_viv['calent_gas']) == 1 or int(row_viv.get('calent_sol', 2)) == 1)
    cisterna = bool(int(row_viv['cisterna']) == 1)
    tinaco = bool(int(row_viv['tinaco_azo']) == 1)
    
    # Save case data
    case_key = row_pred['ID'] # Hogar_1, etc.
    casos_dict[case_key] = {
        "rentaReal": float(row_pred['renta_real']),
        "predXgb": float(row_pred['pred_xgb_pesos']),
        "predRf": float(row_pred['pred_rf_pesos']),
        "inputs": {
            "tipoViv": tipo_viv,
            "loc": loc,
            "estrato": estrato,
            "cuartos": int(row_viv['num_cuarto']),
            "dorm": int(row_viv['cuart_dorm']),
            "focos": int(row_viv['focos']),
            "piso": piso,
            "agua": agua,
            "bano": bano,
            "dren": dren,
            "calentador": calentador,
            "cisterna": cisterna,
            "tinaco": tinaco
        }
    }

# Save cases dictionary to assets
assets_dir = r"c:\Users\milli\OneDrive\Documentos\GitHub\ValoraCasa\assets"
os.makedirs(assets_dir, exist_ok=True)
json_path = os.path.join(assets_dir, "datos_completos_valoracasa.json")

with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(casos_dict, f, ensure_ascii=False, indent=2)

print(f"Successfully wrote {len(casos_dict)} real cases to {json_path}")
print("Sample case:", list(casos_dict.items())[0])
