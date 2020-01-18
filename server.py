import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from twilio.rest import Client

app = Flask(__name__)
model = pickle.load(open('muntu.pkl', 'rb'))


@app.route('/')
def home():
    
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    dangerZone=75
    account_sid = 'ACa5b2898f284381b46bc05c14c2c0ff3d'
    auth_token = '59dea85a451127e47bb4fff3259bd510'
    client = Client(account_sid, auth_token)
    sms1 = 'WARNING! FEVER FOR SENIOR CITIZEN #33 HAS ENTERED THE DANGER ZONE!'
    sms2 = 'WARNING! FEVER FOR SENIOR CITIZEN #22 HAS ENTERED THE DANGER ZONE!'

    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    fever_output = 0.1*round(prediction[0], 2)

    # NOTIFICATION CODE
    if fever_output <= dangerZone:
        print("============= GOOD RESULTS ===============")
        print(fever_output)
        print("Fever Test is Outside DangerZone: GOOD")
        print(dangerZone)
        print("==========================================")
    else:
        print("========= DANGEROUS RESULTS ==============")
        print(fever_output)
        print("Fever Test Detected Danger Breatch: BAD")
        print(dangerZone)
        print("======== WARNING SMS REPORT =============") 
        message = client.messages.create( body='| '+ '\n\n'+sms1+'\n\n'+' |'
        ,from_='+1 855 806 1779', to='+420774348004')
        print(message)
        print("===========================================") 
    return render_template('index.html', prediction_level='Fever Lever: {}'.format(fever_output)+"%")

@app.route('/results',methods=['POST'])
def results():

    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])
    fever_output = prediction[0]
    return jsonify(fever_output)

if __name__ == "__main__":
    app.run(debug=True)