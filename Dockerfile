# 1. On part d'une image qui contient déjà Python 3.10
FROM python:3.10-slim

# 2. On se place dans un dossier /app à l'intérieur de la boîte
WORKDIR /app

# 3. On copie la liste des bibliothèques et on les installe
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. On copie tout le reste du projet (code + modèle)
COPY . .

# 5. On indique que le service utilise le port 8000
EXPOSE 8000

# 6. La commande lancée quand le conteneur démarre
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
