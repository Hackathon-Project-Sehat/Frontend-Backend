from flask import Flask,jsonify,request
from flask_cors import CORS
import random
import pickle
import pyrebase
from twilio.rest import Client
adhar_Number=214857117822
app=Flask(__name__)
prev=0
CORS(app)
config={
    'apiKey': "AIzaSyDeG_7WW_fq2FtdswAQWEtQRM9CBNXiRgw",
    'authDomain': "sehat-8de79.firebaseapp.com",
    'databaseURL': "https://sehat-8de79-default-rtdb.firebaseio.com",
    'projectId': "sehat-8de79",
    'storageBucket': "sehat-8de79.appspot.com",
    'messagingSenderId': "47743319189",
    'appId': "1:47743319189:web:e701fbee1d15dd2bbdef9c",
}
firebase=pyrebase.initialize_app(config)
db = firebase.database()
storage=firebase.storage()
account_sid = "AC417ef321df1099daa1648a95da3b2a76"
auth_token = "1931e1f8c94996558df56a9c461e6030"
client = Client(account_sid, auth_token)
# Function to get data from the firebase
def getFire():
    try:
        data=db.get()
        if data.val():
            print (data.val())
        else :
            print ("Not available")
    except Exception as e:
        print ("Error",str(e))
#Function to get audio data from vite frontend
@app.route('/api/upload_cataract', methods=['POST'])
def upload_image():
    if 'Files' not in request.files:
        return 'No file part', 400

    files = request.files.getlist('Files')

    # Process or save each file as needed.
    #for file in files:
        # Example: file.save('uploads/' + file.filename)

    return 'Images uploaded successfully'
@app.route("/api/receiveBody/1", methods=['POST'])
def formBody():
    global adhar_Number
    files = request.files['audio']
    try:
        storage.child(str(adhar_Number)).child("Body").child("file1.wav").put(files)
        file_url = storage.child(str(adhar_Number)+"/Body/file1.wav").get_url(None)
        db.child("Patients").child(adhar_Number).child("Checkup").child("General").child("Body Audio").child("file1").child("url").set(file_url)
        return jsonify({'message': 'File uploaded successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# The audio sending functions Body
@app.route("/api/receiveBody/2", methods=['POST'])
def form2Body():
    global adhar_Number
    files = request.files['audio']
    try:
        storage.child(str(adhar_Number)).child("Body").child("file2.wav").put(files)
        file_url = storage.child(str(adhar_Number)+"/Body/file2.wav").get_url(None)
        db.child("Patients").child(adhar_Number).child("Checkup").child("General").child("Body Audio").child("file2").child("url").set(file_url)
        return jsonify({'message': 'File uploaded successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
@app.route("/api/receiveBody/3", methods=['POST'])
def form3Body():
    global adhar_Number
    files = request.files['audio']
    try:
        storage.child(str(adhar_Number)).child("Body").child("file3.wav").put(files)
        file_url = storage.child(str(adhar_Number)+"/Body/file3.wav").get_url(None)
        db.child("Patients").child(adhar_Number).child("Checkup").child("General").child("Body Audio").child("file3").child("url").set(file_url)
        return jsonify({'message': 'File uploaded successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
@app.route("/api/receiveBody/4", methods=['POST'])
def form4Body():
    global adhar_Number
    files = request.files['audio']
    try:
        storage.child(str(adhar_Number)).child("Body").child("file4.wav").put(files)
        file_url = storage.child(str(adhar_Number)+"/Body/file4.wav").get_url(None)
        db.child("Patients").child(adhar_Number).child("Checkup").child("General").child("Body Audio").child("file4").child("url").set(file_url)
        return jsonify({'message': 'File uploaded successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
#Funtions to send Diabetes data
@app.route("/api/receiveDiabetes/1", methods=['POST'])
def formDiabetes():
    global adhar_Number
    files = request.files['audio']
    try:
        storage.child(str(adhar_Number)).child("Diabetes").child("file1.wav").put(files)
        file_url = storage.child(str(adhar_Number)+"/Diabetes/file1.wav").get_url(None)
        db.child("Patients").child(adhar_Number).child("Checkup").child("Diabetes").child("Diabetes Audio").child("file1").child("url").set(file_url)
        return jsonify({'message': 'File uploaded successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
@app.route("/api/receiveDiabetes/2", methods=['POST'])
def formDiabetes2():
    global adhar_Number
    files = request.files['audio']
    try:
        storage.child(str(adhar_Number)).child("Diabetes").child("file2.wav").put(files)
        file_url = storage.child(str(adhar_Number)+"/Diabetes/file2.wav").get_url(None)
        db.child("Patients").child(adhar_Number).child("Checkup").child("Diabetes").child("Diabetes Audio").child("file2").child("url").set(file_url)
        return jsonify({'message': 'File uploaded successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
@app.route("/api/receiveDiabetes/3", methods=['POST'])
def formDiabetes3():
    global adhar_Number
    files = request.files['audio']
    try:
        storage.child(str(adhar_Number)).child("Diabetes").child("file3.wav").put(files)
        file_url = storage.child(str(adhar_Number)+"/Diabetes/file3.wav").get_url(None)
        db.child("Patients").child(adhar_Number).child("Checkup").child("Diabetes").child("Diabetes Audio").child("file3").child("url").set(file_url)
        return jsonify({'message': 'File uploaded successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
@app.route("/api/receiveDiabetes/4", methods=['POST'])
def formDiabetes4():
    global adhar_Number
    files = request.files['audio']
    try:
        storage.child(str(adhar_Number)).child("Diabetes").child("file4.wav").put(files)
        file_url = storage.child(str(adhar_Number)+"/Diabetes/file4.wav").get_url(None)
        db.child("Patients").child(adhar_Number).child("Checkup").child("Diabetes").child("Diabetes Audio").child("file4").child("url").set(file_url)
        return jsonify({'message': 'File uploaded successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
#Functions to send skin audio data :
@app.route("/api/receiveSkin/1", methods=['POST'])
def formSkin():
    global adhar_Number
    files = request.files['audio']
    try:
        storage.child(str(adhar_Number)).child("Skin").child("file1.wav").put(files)
        file_url = storage.child(str(adhar_Number)+"/Skin/file1.wav").get_url(None)
        db.child("Patients").child(adhar_Number).child("Checkup").child("Skin").child("Skin Audio").child("file1").child("url").set(file_url)
        return jsonify({'message': 'File uploaded successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
@app.route("/api/receiveSkin/2", methods=['POST'])
def formSkin2():
    global adhar_Number
    files = request.files['audio']
    try:
        storage.child(str(adhar_Number)).child("Skin").child("file2.wav").put(files)
        file_url = storage.child(str(adhar_Number)+"/Skin/file2.wav").get_url(None)
        db.child("Patients").child(adhar_Number).child("Checkup").child("Skin").child("Skin Audio").child("file2").child("url").set(file_url)
        return jsonify({'message': 'File uploaded successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
@app.route("/api/receiveSkin/3", methods=['POST'])
def formSkin3():
    global adhar_Number
    files = request.files['audio']
    try:
        storage.child(str(adhar_Number)).child("Skin").child("file3.wav").put(files)
        file_url = storage.child(str(adhar_Number)+"/Skin/file3.wav").get_url(None)
        db.child("Patients").child(adhar_Number).child("Checkup").child("Skin").child("Skin Audio").child("file3").child("url").set(file_url)
        return jsonify({'message': 'File uploaded successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
@app.route("/api/receiveSkin/4", methods=['POST'])
def formSkin4():
    global adhar_Number
    files = request.files['audio']
    try:
        storage.child(str(adhar_Number)).child("Skin").child("file4.wav").put(files)
        file_url = storage.child(str(adhar_Number)+"/Skin/file4.wav").get_url(None)
        db.child("Patients").child(adhar_Number).child("Checkup").child("Skin").child("Skin Audio").child("file4").child("url").set(file_url)
        return jsonify({'message': 'File uploaded successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
#Function to send data to the firebase
def sendFire():
    data=999999999999
    db.child("Patients").child(data).child("Name").set("Vanshika Jain")
    print("Data sent")
@app.route('/api/data',methods=['GET'])
def get_data():
    data={
        "message":"Hello this is api end point"
    }
    return jsonify(data)
@app.route('/api/getting',methods=['POST'])
def add_data():
    submit_data=request.get_json()
    print(submit_data)
    return 'Done',201
@app.route('/api/height',methods=['POST'])
def height_data():
    submit_data=request.get_json()
    global adhar_Number
    db.child("Patients").child(adhar_Number).child("Checkup").child("General").child("Height").set(submit_data)
    return 'Done',201
@app.route('/api/preg',methods=['POST'])
def preg_data():
    submit_data=request.get_json()
    global adhar_Number
    db.child("Patients").child(adhar_Number).child("Checkup").child("Diabetes").child("Pregnancies").set(submit_data)
    return 'Done',201
@app.route('/api/bmi',methods=['POST'])
def bmi_data():
    submit_data=request.get_json()
    global adhar_Number
    db.child("Patients").child(adhar_Number).child("Checkup").child("Diabetes").child("Bmi").set(submit_data)
    return 'Done',201
@app.route('/api/insulin',methods=['POST'])
def insulin_data():
    submit_data=request.get_json()
    global adhar_Number
    db.child("Patients").child(adhar_Number).child("Checkup").child("Diabetes").child("Insulin").set(submit_data)
    return 'Done',201
@app.route('/api/pedi',methods=['POST'])
def pedi_data():
    submit_data=request.get_json()
    global adhar_Number
    db.child("Patients").child(adhar_Number).child("Checkup").child("Diabetes").child("Pedigree").set(submit_data)
    return 'Done',201
@app.route('/api/thick',methods=['POST'])
def thickness_data():
    submit_data=request.get_json()
    global adhar_Number
    db.child("Patients").child(adhar_Number).child("Checkup").child("Diabetes").child("Skin Thickness").set(submit_data)
    return 'Done',201
@app.route('/api/bpl',methods=['POST'])
def BPL_data():
    submit_data=request.get_json()
    global adhar_Number
    db.child("Patients").child(adhar_Number).child("Checkup").child("Diabetes").child("Blood Pressure").set(submit_data)
    return 'Done',201
@app.route('/api/gluc',methods=['POST'])
def gluc_data():
    submit_data=request.get_json()
    global adhar_Number
    db.child("Patients").child(adhar_Number).child("Checkup").child("Diabetes").child("Glucose").set(submit_data)
    return 'Done',201
@app.route('/api/selectedButtons',methods=['POST'])
def selectedButtons_data():
    submit_data=request.get_json()
    print(submit_data)
    global adhar_Number
    db.child("Patients").child(adhar_Number).child("Checkup").child("General").child("Body Symptoms").set(submit_data)
    return 'Done' , 201
@app.route('/api/heartConcern',methods=['POST'])
def heartConcern_data():
    submit_data=request.get_json()
    print(submit_data)
    global adhar_Number
    db.child("Patients").child(adhar_Number).child("Checkup").child("Heart").child("Heart Concern").set(submit_data)
    return 'Done' , 201
@app.route('/api/selectedSkin',methods=['POST'])
def selectedSkin_data():
    submit_data=request.get_json()
    print(submit_data)
    global adhar_Number
    db.child("Patients").child(adhar_Number).child("Checkup").child("Skin").child("Skin Symptoms").set(submit_data)
    return 'Done' , 201
@app.route('/api/weight',methods=['POST'])
def weight_data():
    submit_data=request.get_json()
    global adhar_Number
    db.child("Patients").child(adhar_Number).child("Checkup").child("General").child("Weight").set(submit_data)
    return 'Done',201
@app.route('/api/bp',methods=['POST'])
def bp_data():
    submit_data=request.get_json()
    global adhar_Number
    db.child("Patients").child(adhar_Number).child("Checkup").child("General").child("Blood Pressure").set(submit_data)
    return 'Done',201
@app.route('/api/temp',methods=['POST'])
def temp_data():
    submit_data=request.get_json()
    global adhar_Number
    db.child("Patients").child(adhar_Number).child("Checkup").child("General").child("Temp").set(submit_data)
    return 'Done',201
@app.route('/api/beat',methods=['POST'])
def beat_data():
    submit_data=request.get_json()
    global adhar_Number
    db.child("Patients").child(adhar_Number).child("Checkup").child("General").child("Heart Beat").set(submit_data)
    return 'Done',201
@app.route('/api/heartInputData',methods=['POST'])
def heartInput_data():
    global adhar_Number
    submit_data=request.get_json()
    arr=["age","sex","restingbp","serum","agina","maxHR","fastingBS","depression","Electrocardiographic","slope","vColour","thal"]
    for i in arr:
        db.child("Patients").child(adhar_Number).child("Checkup").child("Heart").child(i).set(submit_data[i])
    heart_disease_model = pickle.load(open('Heart_disease_model.sav','rb'))
    heart_diagnosis = ''
    gender=0 if submit_data["sex"]=="female" else 1
    exang=0 if submit_data["agina"]=="no" else 1
    fbs=0 if submit_data["fastingBS"]=="false" else 1
    #here chest pain types is missing value , need to find it and make its frontend too
    heart_prediction = heart_disease_model.predict([[int(submit_data["age"]),gender,3, int(submit_data["restingbp"]),int(submit_data["serum"]),fbs,int(submit_data["Electrocardiographic"]),int(submit_data["maxHR"]),exang,float(submit_data["depression"]),int(submit_data["slope"]),int(submit_data["vColour"]),int(submit_data["thal"])]])                          
        
    if (heart_prediction[0] == 1):
        heart_diagnosis = 'The person is having heart disease'
    else:
        heart_diagnosis = 'The person does not have any heart disease'
    db.child("Patients").child(adhar_Number).child("Checkup").child("Heart").child("Heart Machine Learning Prediction").set(heart_diagnosis)
    return 'Done',201

@app.route('/api/sp',methods=['POST'])
def sp_data():
    submit_data=request.get_json()
    global adhar_Number
    db.child("Patients").child(adhar_Number).child("Checkup").child("General").child("Sp02").set(submit_data)
    return 'Done',201
@app.route('/api/option',methods=['POST'])
def option_data():
    submit_data=request.get_json()
    global adhar_Number
    db.child("Patients").child(adhar_Number).child("Checkup").child("Name").set(submit_data)
    print("Data sent")
    return 'Done',201
@app.route('/api/otp',methods=['POST'])
def otp_data():
    global prev
    submit_data=request.get_json()
    pov=0
    number=0
    while (pov<4):
        number=number*10 + int(submit_data[pov])
        pov=pov+1
    print(number)
    print(prev)
    if (number==prev):
        return 'Done',201
    else :
        return 'False', 500
@app.route('/api/adhar',methods=['POST'])
def adhar_data():
    global prev
    submit_data=request.get_json()
    print(submit_data)
    global adhar_Number
    adhar_Number=submit_data
    random_8_digit_number = random.randint(1000, 9999)
    try:
        data=db.child('Patients').child(submit_data).child('Number').get()
        prev=random_8_digit_number
        if data.val():
            phone_number="+91"+str(data.val())
            message="your OTP is "+str(random_8_digit_number)
            message=client.messages.create(
                to=phone_number,
                from_="+16787103295",
                body=message
            )  
            print("message sent")
    except Exception as e:
        print ("Error",str(e))
    return 'Done',201
if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True)



# Machine learning data inputs sample :
# age = 63
# sex = 1
# cp = 3
# trestbps = 145 
# chol = 233
# fbs = 1
# restecg = 0
# thalach = 150
# exang = 0
# oldpeak = 2.3
# slope = 0
# ca = 0
# thal = 1