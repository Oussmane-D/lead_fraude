import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocess_data(df):
    # Supprimer les colonnes non nécessaires
    df = df.drop(columns=["Unnamed: 0", "cc_num", "zip", "unix_time"])

    # Normaliser les colonnes numériques
    scaler = StandardScaler()
    numeric_cols = ["amt", "lat", "long", "city_pop", "merch_lat", "merch_long"]
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

    # Séparer les features et la cible
    X = df.drop(columns=["is_fraud"])
    y = df["is_fraud"]

    print("Données prétraitées :")
    print(X.head())
    return X, y

# Exemple d'utilisation
if __name__ == "__main__":
    df = pd.read_csv("transactions.csv")  # Remplacez par le chargement depuis l'API si nécessaire
    X, y = preprocess_data(df)