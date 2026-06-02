import pandas as pd
import os

csv_dir = r"c:\Users\milli\OneDrive\Documentos\GitHub\ValoraCasa\.github\workflows\CSV"
viv_path = os.path.join(csv_dir, "viviendas_limpio_valuacasa.csv")

df_viv = pd.read_csv(viv_path, nrows=10000)

cols_to_check = [
    'tipo_viv', 'tam_loc', 'est_socio', 'mat_pisos', 'agua_ent',
    'bano_comp', 'drenaje', 'calent_gas', 'cisterna', 'tinaco_azo',
    'num_cuarto', 'cuart_dorm', 'focos', 'excusado'
]

for col in cols_to_check:
    if col in df_viv.columns:
        print(f"Column: {col}")
        print("  Unique values (first few):", df_viv[col].unique()[:10])
        print("  Value counts:")
        print(df_viv[col].value_counts().head(5))
        print("-" * 30)
