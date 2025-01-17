from sklearn.preprocessing import StandardScaler

def preprocess_data(df):
    """
    Prétraite les données : nettoyage et normalisation.
    """
    # Supprimer les colonnes inutiles
    df = df.drop(columns=["Unnamed: 0", "cc_num", "zip", "unix_time"], errors="ignore")

    # Normaliser les colonnes numériques
    numeric_cols = ["amt", "lat", "long", "city_pop", "merch_lat", "merch_long"]
    scaler = StandardScaler()
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

    # Séparer les features (X) et la cible (y)
    X = df.drop(columns=["is_fraud"], errors="ignore")
    y = df["is_fraud"] if "is_fraud" in df.columns else None
    return X, y
