import pandas as pd
import os

csv_dir = r"c:\Users\milli\OneDrive\Documentos\GitHub\ValoraCasa\.github\workflows\CSV"
pred_path = os.path.join(csv_dir, "predicciones_valoracasa.csv")
viv_path = os.path.join(csv_dir, "viviendas_limpio_valuacasa.csv")

try:
    df_pred = pd.read_csv(pred_path)
    df_viv = pd.read_csv(viv_path)
    
    # Filter viviendas to only rented ones
    df_rented = df_viv[df_viv['tenencia'] == 1].copy()
    print("Full Rented viviendas shape:", df_rented.shape)
    print("Predicciones shape:", df_pred.shape)
    
    # Let's see if we can match them by renting value or order
    # Let's check the first few rent values in both
    print("\nFirst 10 Rented Viviendas rents:", df_rented['renta'].head(10).tolist())
    print("First 10 Predicciones rents:", df_pred['renta_real'].head(10).tolist())
    
    # Let's attempt to match by aligning them or doing a merge
    # Wait, let's see if there is another way they are matched.
    # Are the lengths close? Yes, df_rented is probably larger (e.g., if there are owned homes with imputation or if the test set is a split).
    # Let's count how many rented homes have renta > 0
    df_rented_nonzero = df_rented[df_rented['renta'] > 0]
    print("\nRented non-zero rents shape:", df_rented_nonzero.shape)
    
except Exception as e:
    print("Error:", e)
