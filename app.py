from flask import Flask, render_template, request,url_for,abort
from flask_cors import cross_origin
import pickle
import numpy as np
import sklearn
import pandas as pd

model=pickle.load(open('models/model.pkl','rb'))

app = Flask(__name__)

@app.route('/',methods=['GET'])
@cross_origin()
def Home():
    return render_template('inde.html')



@app.route("/predict", methods=['GET','POST'])
@cross_origin()
def predict():
    
    if request.method == 'POST':
        
        Designation = float(request.form['Designation']) 
        
        MentalFatigueScore=float(request.form['Mental Fatigue Score'])
        
        Gender=request.form['Gender']
        if(Gender=='Female'):
                Female=1
                Male=0
        else:
            Female=0
            Male=1
    
        WFHSetupAvailable=request.form['WFH Setup Available']
        if(WFHSetupAvailable=='Yes'):
                Yes=1
                No=0
        else:
            Yes=0
            No=1
        
         
        
        day = int(request.form['Day'])
        
        year = int(request.form['Year'])
        
        prediction=model.predict(np.array([[Designation,MentalFatigueScore,Female,Male,No,Yes,day,year]]))
        
        output=round(prediction[0],2)
        if output:
            return render_template('output.html',prediction_text=output)
    else:
        return render_template('inde.html')

if __name__=="__main__":
    
    app.run(
    debug=True, passthrough_errors=True,
    use_debugger=False, use_reloader=False)
    