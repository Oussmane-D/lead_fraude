import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import mlflow
import mlflow.sklearn
from scripts.preprocess_data import preprocess_data

def train_model(data_path):
    """
    Charge les données, les prétraite, entraîne un modèle et l'enregistre dans MLflow.
    """
    # Charger les données
    df = pd.read_csv(data_path)

    # Prétraiter les données
    X, y = preprocess_data(df)

    # Diviser les données en ensembles d'entraînement et de test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Entraîner le modèle
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    # Évaluer le modèle
    y_pred = model.predict(X_test)
    print("Rapport de classification :")
    print(classification_report(y_test, y_pred))

    # Enregistrer le modèle dans MLflow
    with mlflow.start_run():
        mlflow.log_params({"model": "RandomForest", "random_state": 42})
        mlflow.sklearn.log_model(model, "fraud_detection_model")
        print("Modèle enregistré avec MLflow.")

if __name__ == "__main__":
    data_path = "data/transactions.csv"  # Chemin relatif vers le fichier
    train_model(data_path)
