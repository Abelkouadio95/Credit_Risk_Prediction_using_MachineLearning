# Application de Prédiction de Risque de Crédit
Ce repo contient plusieurs version mais je vous recommande la version 2
version 1 : dossier stage2 ( django)
version 2 : dossier version 2 ( améliorée) ( fastAPI + Bootstrap)

Cette application web permet d'évaluer l'éligibilité au crédit d'un client en utilisant un modèle de machine learning entraîné avec une régression logistique.

## 🚀 Fonctionnalités

- **Interface utilisateur moderne** avec Bootstrap 5
- **Formulaire interactif** pour saisir les informations du client
- **Prédiction en temps réel** avec niveau de confiance
- **Design responsive** adapté à tous les appareils
  
## Aperçu
<img width="960" height="540" alt="image" src="https://github.com/user-attachments/assets/9b71590e-f6a5-414c-8daf-09d2a76b9b9e" />
<img width="960" height="540" alt="image" src="https://github.com/user-attachments/assets/5c086967-f0b1-4eaf-b807-16e08d0f387c" />
<img width="960" height="540" alt="image" src="https://github.com/user-attachments/assets/3df23a60-2642-47b3-93f8-99e3e762f4bc" />



## Tools & Technologies
Python
Pandas, NumPy (Data preprocessing)
Scikit-learn (Modeling & evaluation)
Matplotlib, Seaborn (Data visualization)
Google collab Notebook
FatsApi + Bootstrap

## 📋 Variables utilisées par le modèle

Le modèle prend en compte les variables suivantes :

1. **Genre** (Gender)
   - Homme (Male)
   - Femme (Female)

2. **Statut marital** (Married)
   - Marié(e) (Yes)
   - Célibataire (No)

3. **Historique de crédit** (Credit_History)
   - Historique positif (Yes)
   - Pas d'historique/Négatif (No)

4. **Zone de propriété** (Property_Area)
   - Urbaine (Urban)
   - Semi-urbaine (Semiurban)
   - Rurale (Rural)

## 🛠️ Installation

### Prérequis

- Python 3.8 ou supérieur
- pip (gestionnaire de paquets Python)

### Étapes d'installation

1. **Cloner ou télécharger le projet**

2. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```

3. **Vérifier que le modèle est présent**
   - Assurez-vous que le fichier `Model.pkl` est dans le répertoire racine

## 🚀 Lancement de l'application

### Méthode 1 : Directement avec Python
```bash
python app.py
```

### Méthode 2 : Avec Uvicorn
```bash
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

### Méthode 3 : Avec Uvicorn (développement)
```bash
uvicorn app:app --reload
```
puis allez a l'addresse http://127.0.0.1:8000/

## 📡 API Endpoints

### Interface Web
- `GET /` - Page d'accueil avec le formulaire
- `POST /predict` - Prédiction via formulaire HTML


## 🐛 Dépannage

### Erreur "Modèle non disponible"
- Vérifiez que le fichier `Model.pkl` est présent dans le répertoire racine


### Erreur de dépendances
- Vérifiez que toutes les dépendances sont installées : `pip install -r requirements.txt`
- Assurez-vous d'utiliser Python 3.8+

## 📊 Performance du modèle

Le modèle de régression logistique utilisé a une précision d'environ **85.4%** sur les données de test.
Avec un dataset qui contient assez de variables ayant une corrélation avec notre variable cible on peut atteindre un meilleur score


## 📞 Support

Pour toute question ou problème, n'hésitez pas à me contacter, addresse disponible sur mon profil. 
