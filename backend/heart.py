
import pickle


# loading the saved models

heart_disease_model = pickle.load(open('Heart_disease_model.sav','rb'))
    
# Diabetes Prediction Page

# Heart Disease Prediction Page
#The labels : Age , Sex, Chest Pain types, Resting Blood Pressure ,Serum Cholestoral in mg/dl,Fasting Blood Sugar > 120 mg/dl,Resting Electrocardiographic results, Maximum Heart Rate achieved,Exercise Induced Angina,ST depression induced by exercise,Slope of the peak exercise ST segment,Major vessels colored by flourosopy,thal: 0 = normal; 1 = fixed defect; 2 = reversable defect

age = 63
sex = 1
cp = 3
trestbps = 145 
chol = 233
fbs = 1
restecg = 0
thalach = 150
exang = 0
oldpeak = 2.3
slope = 0
ca = 0
thal = 1
        
     
# code for Prediction
heart_diagnosis = ''
heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
if (heart_prediction[0] == 1):
    heart_diagnosis = 'The person is having heart disease'
else:
    heart_diagnosis = 'The person does not have any heart disease'
        
print(heart_diagnosis)


        
