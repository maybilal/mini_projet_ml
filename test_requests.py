import requests

reponse = requests.get("http://127.0.0.1:8000/predict")

print("Code de statut :", reponse.status_code)
print("Contenu :", reponse.json())
