import mlflow
import mlflow.sklearn
from scripts.load_data import load_data_from_api
from scripts.preprocess_data import preprocess_data

def predict_fraud(api_url, model_uri):
    """
    Charge les données, prétraite et effectue des prédictions avec un modèle MLflow.
    """
    # Charger les données depuis l'API
    df = load_data_from_api(api_url)

    # Charger le modèle depuis MLflow
    model = mlflow.sklearn.load_model(model_uri)

    # Prétraiter les données
    X, _ = preprocess_data(df)

    # Effectuer des prédictions
    predictions = model.predict(X)
    df["fraud_prediction"] = predictions

    # Sauvegarder les résultats localement
    df.to_csv("predictions.csv", index=False)
    print("Prédictions sauvegardées dans 'predictions.csv'.")

if __name__ == "__main__":
    API_URL = "https://real-time-payments-api.herokuapp.com/current-transactions"
    MLFLOW_MODEL_URI = "runs:/3/fraud_detection_model"
    predict_fraud(API_URL, MLFLOW_MODEL_URI)
