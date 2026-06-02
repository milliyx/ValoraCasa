import pandas as pd
import os

csv_dir = r"c:\Users\milli\OneDrive\Documentos\GitHub\ValoraCasa\.github\workflows\CSV"
pred_path = os.path.join(csv_dir, "predicciones_valoracasa.csv")
viv_path = os.path.join(csv_dir, "viviendas_limpio_valuacasa.csv")

try:
    df_pred = pd.read_csv(pred_path)
    print("Predicciones columns:", df_pred.columns.tolist())
    print("Predicciones shape:", df_pred.shape)
    print(df_pred.head(3))
    
    # Read a chunk of viviendas to save memory and time
    df_viv_chunk = pd.read_csv(viv_path, nrows=5000)
    print("\nViviendas columns:", df_viv_chunk.columns.tolist())
    print("Viviendas shape (nrows=5000):", df_viv_chunk.shape)
    print(df_viv_chunk.head(3))
    
    # Let's see if the first Hogar_1 matches the first row in viviendas where renta is close to 1500
    print("\nMatching first row of pred with viviendas where renta is around 1500:")
    first_pred_rent = df_pred.iloc[0]['renta_real']
    matches = df_viv_chunk[abs(df_viv_chunk['renta'] - first_pred_rent) < 0.1]
    print(f"Found {len(matches)} matches in first 5000 rows:")
    print(matches.head(3))
    
except Exception as e:
    print("Error:", e)
