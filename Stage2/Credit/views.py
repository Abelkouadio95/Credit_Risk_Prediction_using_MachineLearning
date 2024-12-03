from django.shortcuts import render
import numpy as np
import pickle
import pathlib
import os

import sklearn
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


parent = pathlib.Path(__file__).parent.resolve()
model = pickle.load(open(os.path.join(parent, 'model.pkl'), 'rb'))


# Create your views here.


def index(request):

    prediction_text = None

    if request.method == 'POST':
        int_features = [int(request.POST['ch']), int(request.POST['m']), int(request.POST['ci'])]
        final_features = [np.array(int_features)]
        pd = model.predict(final_features)

        output = round(pd[0], 2)
        if output == 1:
            prediction_text = {'message':"Client solvable, peux benéficier du credit !"}
        else:
            prediction_text = {'message':" Désolé, le credit ne pourra pas etre accordé !"}

    return render(request,'index.html',prediction_text)
