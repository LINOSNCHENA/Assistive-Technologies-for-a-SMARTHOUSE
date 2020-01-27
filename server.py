import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from twilio.rest import Client
from numpy import array
app = Flask(__name__)
model = pickle.load(open('xmuntu1.pkl', 'rb'))

@app.route('/')
def home():    
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    dangerZone=0.5
    account_sid = 'xxx'
    auth_token  = 'xx'
    client = Client(account_sid, auth_token)
    sms1 = 'WARNING! FEVER FOR SENIOR CITIZEN #33 HAS ENTERED THE DANGER ZONE!'
    recieved_features = [float(x) for x in request.form.values()]
    proccessed_features = [np.array(recieved_features)]
    # list to array of data processed_features
    processed_features = array(proccessed_features)
    processed_features = processed_features.reshape((processed_features.shape[0], 8))
    prediction = model.predict(processed_features)   
    # Extract first element in prediction array
    fever_output = prediction[0]
    print("============= FEVER OUTPUTS _A ==============="+'\n')
    print(fever_output)
    print("============= FEVER OUTPUTS _B_==============="+'\n')
     
    # NOTIFICATION CODE
    if fever_output == dangerZone:
        print("Fever Test is NEGETIVE: RELAXING")
        print("==========================================")
    else:
        print("Fever Test is POSITIVE: ATTENTION")
      #  message = client.messages.create( body='| '+ '\n\n'+sms1+'\n\n'+' |'
       # ,from_='xx806 172789', to='xxx0040')
        #print(message)
        print("===========================================") 
    return render_template('index.html', prediction_level='Fever Lever: {}'.format(fever_output)+"-:PerCent%")

@app.route('/results',methods=['POST'])
def results():
    enterData = request.get_json(force=True)
   # prediction = model.predict([np.array(list(enterData.values()))])
   # prediction = model.predict(enterData.values())
    prediction = model.predict(enterData)
   # fever_output = prediction[0]
    return jsonify(fever_output)

if __name__ == "__main__":
    app.run(debug=True)