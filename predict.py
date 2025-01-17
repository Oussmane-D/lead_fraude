import pandas as pd
import mlflow
import mlflow.sklearn
from sklearn.preprocessing import StandardScaler
import boto3

# Configuration de MLflow
MLFLOW_TRACKING_URI = "https://ousmane-d-mlflow-server-demo.hf.space"  # Remplacez par l'URL de votre serveur MLflow
MLFLOW_MODEL_URI = "runs:/3/model"  # Remplacez par l'URI de votre modèle dans MLflow

# Configuration de S3
S3_BUCKET_NAME = "kub-bucket-ouss"  # Remplacez par le nom de votre bucket S3
S3_DATA_FILE = "transaction.csv"  # Remplacez par le nom de votre fichier de données dans S3
S3_PREDICTIONS_FILE = "predictions.csv"  # Nom du fichier de prédictions à enregistrer dans S3

# Charger les données depuis S3 (bucket public)
def load_data_from_s3():
    # URL publique du fichier S3
    s3_url = f"https://kub-bucket-ouss.s3.eu-west-3.amazonaws.com/transactions.csv"
    
    # Charger les données dans un DataFrame pandas
    df = pd.read_csv(s3_url)
    print("Données chargées depuis S3 :")
    print(df.head())
    return df

# Charger le modèle depuis MLflow
def load_model_from_mlflow():
    # Configurer l'URL de MLflow
    mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)
    
    # Charger le modèle
    model = mlflow.sklearn.load_model(MLFLOW_MODEL_URI)
    print("Modèle chargé depuis MLflow.")
    return model

# Faire des prédictions
def predict_fraud(df, model):
    # Prétraiter les données (supposons que vous avez besoin de normaliser les données)
    scaler = StandardScaler()
    X = df.drop("is_fraud", axis=1)  # Supprimez la colonne cible si elle existe
    X_scaled = scaler.fit_transform(X)
    
    # Faire des prédictions
    df["fraud_prediction"] = model.predict(X_scaled)
    print("Prédictions terminées :")
    print(df.head())
    return df

# Enregistrer les résultats dans S3
def save_predictions_to_s3(df):
    # Enregistrer les résultats localement
    local_file = "predictions.csv"
    df.to_csv(local_file, index=False)
    
    # Téléverser le fichier sur S3
    s3 = boto3.client('s3', aws_access_key_id='', aws_secret_access_key='')
    s3.upload_file(local_file, S3_BUCKET_NAME, S3_PREDICTIONS_FILE)
    print(f"Résultats enregistrés dans S3 : {S3_BUCKET_NAME}/{S3_PREDICTIONS_FILE}")

# Fonction principale
def main():
    # Charger les données depuis S3
    df = load_data_from_s3()
    
    # Charger le modèle depuis MLflow
    model = load_model_from_mlflow()
    
    # Faire des prédictions
    df_with_predictions = predict_fraud(df, model)
    
    # Enregistrer les résultats dans S3
    save_predictions_to_s3(df_with_predictions)

# Exécuter le script
if __name__ == "__main__":
    main()