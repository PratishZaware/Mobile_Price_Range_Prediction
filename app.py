import json
import pickle

from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np 
import pandas as pd

app=Flask(__name__)
model=pickle.load(open('logModel.pkl','rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api',methods=['POST'])
def predict_api():
    data=request.json['data']
    print(data)
    print(np.array(list(data.values())))
    new_data= np.array(list(data.values())).reshape(1,-1)
    
    print(type(new_data))
    print(new_data)
    output=model.predict(new_data)
    output1=int(output)
    print(output[0])
    return jsonify(output1)

@app.route('/predict',methods=['POST'])
def predict():
    data=[float(x) for x in request.form.values()]
    new_data= np.array(data).reshape(1,-1)  
    output=model.predict(new_data)  
    return render_template("home.html",prediction_text="The mobile price range is {}".format(output))


if __name__=="__main__":
    app.run(debug=True)    
    