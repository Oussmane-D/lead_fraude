import pandas as pd
from sklearn.preprocessing import StandardScaler
import mlflow
import mlflow.sklearn
from preprocess_data import preprocess_data

# Configuration
MLFLOW_TRACKING_URI = "https://ousmane-d-mlflow-server-demo.hf.space"
MLFLOW_MODEL_URI = "runs:/3/fraud_detection_model"

def predict_fraud(data_path):
    """
    Charge les données, prétraite et effectue des prédictions avec un modèle MLflow.
    """
    # Charger les données
    df = pd.read_csv(data_path)

    # Charger le modèle depuis MLflow
    mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)
    model = mlflow.sklearn.load_model(MLFLOW_MODEL_URI)

    # Prétraiter les données
    X, _ = preprocess_data(df)

    # Effectuer des prédictions
    predictions = model.predict(X)
    df["fraud_prediction"] = predictions

    # Sauvegarder les résultats
    df.to_csv("predictions.csv", index=False)
    print("Prédictions sauvegardées dans 'predictions.csv'.")

if __name__ == "__main__":
    data_path = "data/transactions.csv"  # Chemin relatif vers le fichier
    predict_fraud(data_path)
