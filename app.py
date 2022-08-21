import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle


app = Flask(__name__)
classifier_dt = pickle.load(open('musicdt.pkl','rb'))
classifier_knn = pickle.load(open('musicknn.pkl','rb'))
classifier_svm = pickle.load(open('musicsvm.pkl','rb'))
classifier_rf = pickle.load(open('musicrf.pkl','rb'))
classifier_NB = pickle.load(open('musicnb.pkl','rb'))

@app.route('/predict1')
def home():
  
    return render_template("index.html")
  
@app.route('/predict',methods=['GET'])
def predict():

    danceability = float(request.args.get('danceability'))
    energy = float(request.args.get('energy'))
    mode = int(request.args.get('mode'))
    speechiness = float(request.args.get('speechiness'))
    acostiness = float(request.args.get('acoustiness'))
    liveness = float(request.args.get('liveness'))
    valence = float(request.args.get('valence'))


    

# CreditScore	Geography	Gender	Age	Tenure	Balance	NumOfProducts	HasCrCard	IsActiveMember	EstimatedSalary	
    Model = (request.args.get('Model'))

    if Model=="Random Forest":
      prediction = classifier_dt.predict([[danceability, energy, mode, speechiness, acoustiness, liveness, valence]])

    elif Model=="Decision Tree":
      prediction = classifier_knn.predict([[danceability, energy, mode, speechiness, acoustiness, liveness, valence]])

    elif Model=="KNN":
      prediction = classifier_svm.predict([[danceability, energy, mode, speechiness, acoustiness, liveness, valence]])

    elif Model=="SVM":
      prediction = classifier_rf.predict([[danceability, energy, mode, speechiness, acoustiness, liveness, valence]])

    else:
      prediction = classifier_NB.predict([[danceability, energy, mode, speechiness, acoustiness, liveness, valence]])

    
    if prediction == [0]:
      return render_template('index.html', prediction_text='Mobile belongs to 1 group i.e acoustic/folk', extra_text =" as per Prediction by " + Model)
    
    elif prediction ==[1]:
      return render_template('index.html', prediction_text='Mobile belongs to 2 group i.e Blues', extra_text ="as per Prediction by " + Model)

    elif prediction ==[2]:
      return render_template('index.html', prediction_text='Mobile belongs to 3 group i.e Coumtry', extra_text ="as per Prediction by " + Model)

    elif prediction ==[3]:
      return render_template('index.html', prediction_text='Mobile belongs to 4 group i.e hip hop', extra_text ="as per Prediction by " + Model)

    elif prediction ==[4]:
      return render_template('index.html', prediction_text='Mobile belongs to 5 group i.e Indie_alt', extra_text ="as per Prediction by " + Model)

    elif prediction ==[5]:
      return render_template('index.html', prediction_text='Mobile belongs to 6 group i.e instrumental', extra_text ="as per Prediction by " + Model)

    elif prediction ==[6]:
      return render_template('index.html', prediction_text='Mobile belongs to 7 group i.e metal', extra_text ="as per Prediction by " + Model)

    elif prediction ==[7]:
      return render_template('index.html', prediction_text='Mobile belongs to 8 group i.e jazz', extra_text ="as per Prediction by " + Model)

    elif prediction ==[8]:
      return render_template('index.html', prediction_text='Mobile belongs to 9 group i.e pop', extra_text ="as per Prediction by " + Model)

    else:
      return render_template('index.html', prediction_text='Mobile belongs to 10 group i.e Rock', extra_text ="as per Prediction by " + Model)

#---------------------------------------------------------

@app.route('/aboutusnew')
def aboutusnew():
    return render_template('aboutus.html')

#----------------------------------------------------------

@app.route('/')
def first():
    return render_template('first.html')


if __name__=="__main__":
    app.run(debug=True)

