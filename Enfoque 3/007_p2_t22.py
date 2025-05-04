import pandas as pd

caracteristicas = load_iris().feature_names
importancias = modelo_boost.feature_importances_

explicacion = pd.DataFrame({
    "Característica": caracteristicas,
    "Importancia": importancias
}).sort_values(by="Importancia", ascending=False)

print(explicacion)
