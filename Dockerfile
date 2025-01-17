# Utiliser une image de base Python officielle légère
FROM python:3.9-slim

# Mettre à jour le système et installer les dépendances système (optionnel, selon vos besoins)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier uniquement les fichiers nécessaires dans le conteneur pour optimiser la construction
COPY requirements.txt .

# Installer les dépendances Python à partir du fichier requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copier les scripts après l'installation des dépendances pour accélérer la construction en cas de modification
COPY scripts/ ./scripts/

# Définir la commande par défaut pour exécuter le script principal
CMD ["python", "scripts/main.py"]
