from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()

# On charge le modèle UNE SEULE FOIS, au démarrage du serveur
model = joblib.load("regression.joblib")

class Maison(BaseModel):
    taille: float
    nb_chambres: int
    jardin: int

@app.post("/predict")
def predict(maison: Maison):
    # On met les valeurs dans un tableau, avec les mêmes noms de colonnes
    # et le même ordre que pendant l'entraînement
    donnees = pd.DataFrame(
        [[maison.taille, maison.nb_chambres, maison.jardin]],
        columns=["size", "nb_rooms", "garden"]
    )

    prediction = model.predict(donnees)

    return {"y_pred": float(prediction[0])}
