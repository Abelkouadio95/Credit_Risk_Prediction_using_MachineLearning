from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import pickle
import pandas as pd
import numpy as np
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="Prédiction de Risque de Crédit", version="1.0.0")

# Configuration des templates et fichiers statiques
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Chargement du modèle
import os
model = None
try:
    model_path = 'Model.pkl'
    print(f"Tentative de chargement du modèle depuis: {os.path.abspath(model_path)}")
    print(f"Le fichier existe: {os.path.exists(model_path)}")
    
    if os.path.exists(model_path):
        with open(model_path, 'rb') as file:
            model = pickle.load(file)
        print(f"Modèle chargé avec succès! Type: {type(model)}")
    else:
        print(f"Erreur: Le fichier {model_path} n'existe pas")
        print(f"Fichiers dans le répertoire: {os.listdir('.')}")
except Exception as e:
    print(f"Erreur lors du chargement du modèle: {e}")
    import traceback
    traceback.print_exc()
    model = None

# Modèle Pydantic pour la validation des données
class CreditData(BaseModel):
    gender: str
    married: str
    credit_history: str
    property_area: str

# Dictionnaires de mapping pour les variables catégorielles
gender_mapping = {'Male': 1, 'Female': 0}
married_mapping = {'Yes': 1, 'No': 0}
credit_history_mapping = {'Yes': 1, 'No': 0}
property_area_mapping = {'Urban': 2, 'Semiurban': 1, 'Rural': 0}

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Page d'accueil avec le formulaire de prédiction"""
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict", response_class=HTMLResponse)
async def predict(request: Request, 
                  gender: str = Form(...),
                  married: str = Form(...),
                  credit_history: str = Form(...),
                  property_area: str = Form(...)):
    """Endpoint pour la prédiction via formulaire HTML"""
    
    if model is None:
        return templates.TemplateResponse("index.html", {
            "request": request,
            "error": "Erreur: Modèle non disponible"
        })
    
    try:
        # Préparation des données
        input_data = {
            'Credit_History': credit_history_mapping.get(credit_history, 0),
            'Gender': gender_mapping.get(gender, 0),
            'Married': married_mapping.get(married, 0),
            'Property_Area': property_area_mapping.get(property_area, 0)
        }
        
        # Création du DataFrame
        df = pd.DataFrame([input_data])
        
        # Prédiction
        prediction = model.predict(df)[0]
        probability = model.predict_proba(df)[0]
        
        # Interprétation du résultat
        result = "CRÉDIT ACCORDÉ" if prediction == 1 else "CRÉDIT REFUSÉ"
        confidence = probability[1] if prediction == 1 else probability[0]
        confidence_percent = round(confidence * 100, 2)
        
        return templates.TemplateResponse("index.html", {
            "request": request,
            "result": result,
            "confidence": confidence_percent,
            "input_data": {
                "gender": gender,
                "married": married,
                "credit_history": credit_history,
                "property_area": property_area
            }
        })
        
    except Exception as e:
        return templates.TemplateResponse("index.html", {
            "request": request,
            "error": f"Erreur lors de la prédiction: {str(e)}"
        })


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 