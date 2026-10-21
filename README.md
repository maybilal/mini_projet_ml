# Mini-projet MLOps : API de prédiction du prix des maisons

Service web FastAPI qui expose un modèle de régression linéaire (scikit-learn)
prédisant le prix d'une maison à partir de sa taille, de son nombre de chambres
et de la présence d'un jardin. Le service est conteneurisé avec Docker.

## Fichiers

- `train_model.py` : entraîne le modèle sur `houses.csv` et le sauvegarde dans `regression.joblib`
- `main.py` : API FastAPI, endpoint `POST /predict`
- `requirements.txt` : dépendances Python avec leurs versions
- `Dockerfile` : construction de l'image Docker
- `test_requests.py` : test de l'API avec la bibliothèque requests

## Lancer en local

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

## Lancer avec Docker

```bash
docker build -t mini-projet-ml .
docker run -p 8081:8000 mini-projet-ml
```

## Utiliser l'API

`POST /predict` avec le corps JSON :

```json
{"taille": 100, "nb_chambres": 3, "jardin": 1}
```

Réponse :

```json
{"y_pred": 275617.33}
```

## Déploiement

Le conteneur est déployé sur la VM du cours, sur le port 8077 :
`http://40.66.48.24:8077/predict`
