# ValoraCasa | Decision Intelligence Hub

Aplicación web estática para presentar el proyecto **ValoraCasa** como un hub ejecutivo de Business Intelligence, storytelling y demo funcional.

## ¿Qué incluye?

- Landing narrativa del problema de negocio.
- Dashboard BI con KPIs y gráficas interactivas.
- Comparación de modelos: Regresión Lineal, Random Forest y XGBoost.
- Simulador referencial de renta sugerida.
- Guion ejecutivo para exposición.

## Importante

El simulador incluido es una **demo referencial** basada en los principales hallazgos del análisis. No ejecuta el modelo XGBoost real en tiempo real. Para producción, se recomienda conectar el modelo entrenado mediante una API o backend.

## Publicar con GitHub Pages

1. Crea un repositorio nuevo en GitHub, por ejemplo: `valoracasa-bi-hub`.
2. Sube estos archivos al repositorio:
   - `index.html`
   - `.nojekyll`
   - `README.md`
3. En GitHub entra a **Settings > Pages**.
4. En **Build and deployment**, elige:
   - Source: `Deploy from a branch`
   - Branch: `main`
   - Folder: `/root`
5. Guarda los cambios.
6. GitHub generará un link parecido a:
   `https://TU-USUARIO.github.io/valoracasa-bi-hub/`

## Sobre Power BI

Sí se puede embeber Power BI, pero hay dos caminos:

1. **Publish to web / iframe público:** fácil, pero el reporte queda público.
2. **Power BI Embedded API:** profesional, pero requiere Azure/Microsoft Entra, tokens y backend. No es ideal para GitHub Pages puro porque GitHub Pages es estático y no debe guardar secretos ni tokens.

Para este proyecto académico, esta versión con Chart.js es suficiente y más fácil de publicar.
