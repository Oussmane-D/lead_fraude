import mlflow
import mlflow.sklearn

def save_model(model, model_name):
    # Enregistrer le modèle dans MLflow
    with mlflow.start_run():
        mlflow.sklearn.log_model(model, model_name)
        print(f"Modèle {model_name} enregistré avec MLflow.")

# Exemple d'utilisation
if __name__ == "__main__":
    from scripts.train_model import train_model
    from preprocess_data import preprocess_data
    import pandas as pd

    df = pd.read_csv("transactions.csv")  # Remplacez par le chargement depuis l'API si nécessaire
    X, y = preprocess_data(df)
    model = train_model(X, y)
    save_model(model, "fraud_detection_model")