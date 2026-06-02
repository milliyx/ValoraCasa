import pandas as pd
import numpy as np
import os

csv_dir = r"c:\Users\milli\OneDrive\Documentos\GitHub\ValoraCasa\.github\workflows\CSV"
pred_path = os.path.join(csv_dir, "predicciones_valoracasa.csv")
viv_path = os.path.join(csv_dir, "viviendas_limpio_valuacasa.csv")

df_pred = pd.read_csv(pred_path)
df_viv = pd.read_csv(viv_path)
df_rented = df_viv[df_viv['tenencia'] == 1].copy()

print(df_pred.head(5))
