import os

for root, dirs, files in os.walk(r"c:\Users\milli\OneDrive\Documentos\GitHub\ValoraCasa"):
    for file in files:
        if file.endswith(".ipynb") or file.endswith(".py"):
            print(os.path.join(root, file))
