import pandas as pd
import boto3

def save_predictions_to_s3(df, bucket_name, file_name, aws_access_key, aws_secret_key):
    # Enregistrer les résultats localement
    local_file = "predictions.csv"
    df.to_csv(local_file, index=False)
    
    # Téléverser le fichier sur S3
    s3 = boto3.client('s3', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key)
    s3.upload_file(local_file, bucket_name, file_name)
    print(f"Résultats enregistrés dans S3 : {bucket_name}/{file_name}")