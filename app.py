import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle


app = Flask(__name__)
classifier_dt = pickle.load(open('mobiledt.pkl','rb'))
classifier_knn = pickle.load(open('mobileknn.pkl','rb'))
classifier_svm = pickle.load(open('mobilesvm.pkl','rb'))
classifier_rf = pickle.load(open('mobilerf.pkl','rb'))
classifier_NB = pickle.load(open('mobilenb.pkl','rb'))

@app.route('/predict1')
def home():
  
    return render_template("index.html")
  
@app.route('/predict',methods=['GET'])
def predict():

    battery_power = int(request.args.get('battery_power'))
    clock_speed = float(request.args.get('clock_speed'))
    fc = int(request.args.get('fc'))
    int_memory = int(request.args.get('int_memory'))
    m_dep = float(request.args.get('m_dep'))
    mobile_wt = float(request.args.get('mobile_wt'))
    n_cores = int(request.args.get('n_cores'))
    pc = int(request.args.get('pc'))
    px_height = float(request.args.get('px_height'))
    px_width = float(request.args.get('px_width'))
    ram = int(request.args.get('ram'))
    sc_h = float(request.args.get('sc_h'))
    sc_w = float(request.args.get('sc_w'))
    talk_time = int(request.args.get('talk_time'))


    blue = (request.args.get('blue'))

    if blue=="Yes":
      blue = 1
    else:
      blue = 0

    dual_sim = (request.args.get('dual_sim'))

    if dual_sim=="Yes":
      dual_sim = 1
    else:
      dual_sim = 0

    four_g = (request.args.get('four_g'))

    if four_g=="Yes":
      four_g = 1
    else:
      four_g = 0

    three_g = (request.args.get('three_g'))

    if three_g=="Yes":
      three_g = 1
    else:
      three_g = 0

    touch_screen = (request.args.get('touch_screen'))

    if touch_screen=="Yes":
      touch_screen = 1
    else:
      touch_screen = 0

    wifi = (request.args.get('wifi'))

    if wifi=="Yes":
      wifi = 1
    else:
      wifi = 0


    

# CreditScore	Geography	Gender	Age	Tenure	Balance	NumOfProducts	HasCrCard	IsActiveMember	EstimatedSalary	
    Model = (request.args.get('Model'))

    if Model=="Random Forest":
      prediction = classifier_dt.predict([[battery_power, clock_speed, fc, int_memory, m_dep, mobile_wt, n_cores, pc, px_height, px_width, ram, sc_h, sc_w, talk_time, blue, dual_sim, four_g, three_g, touch_screen, wifi]])

    elif Model=="Decision Tree":
      prediction = classifier_knn.predict([[battery_power, clock_speed, fc, int_memory, m_dep, mobile_wt, n_cores, pc, px_height, px_width, ram, sc_h, sc_w, talk_time, blue, dual_sim, four_g, three_g, touch_screen, wifi]])

    elif Model=="KNN":
      prediction = classifier_svm.predict([[battery_power, clock_speed, fc, int_memory, m_dep, mobile_wt, n_cores, pc, px_height, px_width, ram, sc_h, sc_w, talk_time, blue, dual_sim, four_g, three_g, touch_screen, wifi]])

    elif Model=="SVM":
      prediction = classifier_rf.predict([[battery_power, clock_speed, fc, int_memory, m_dep, mobile_wt, n_cores, pc, px_height, px_width, ram, sc_h, sc_w, talk_time, blue, dual_sim, four_g, three_g, touch_screen, wifi]])

    else:
      prediction = classifier_NB.predict([[battery_power, clock_speed, fc, int_memory, m_dep, mobile_wt, n_cores, pc, px_height, px_width, ram, sc_h, sc_w, talk_time, blue, dual_sim, four_g, three_g, touch_screen, wifi]])

    
    if prediction == [0]:
      return render_template('index.html', prediction_text='Mobile belongs to 1st group', extra_text =" as per Prediction by " + Model)
    
    elif prediction ==[1]:
      return render_template('index.html', prediction_text='Mobile belongs to 2nd group', extra_text ="as per Prediction by " + Model)

    elif prediction ==[2]:
      return render_template('index.html', prediction_text='Mobile belongs to 3rd group', extra_text ="as per Prediction by " + Model)

    else:
      return render_template('index.html', prediction_text='Mobile belongs to 4th group', extra_text ="as per Prediction by " + Model)

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

