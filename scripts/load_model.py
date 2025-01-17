import mlflow
import mlflow.sklearn

def load_model_from_mlflow(tracking_uri, model_uri):
    # Configurer l'URL de MLflow
    mlflow.set_tracking_uri(tracking_uri)
    
    # Charger le modèle
    model = mlflow.sklearn.load_model(model_uri)
    print("Modèle chargé depuis MLflow.")
    return model