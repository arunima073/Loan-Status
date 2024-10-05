from flask import Flask,request
import pickle
import sklearn

app=Flask(__name__)

@app.route("/")
def hello_word():
  return "<p>hello oooos</p>"

model_pickle=open("./artefacts/classifier.pkl","rb")
clf=pickle.load(model_pickle)

@app.route("/ping",methods=['GET'])
def pinger():
  return {"MESSAGE":"Hi,I am Pinging....!!!!!"}

@app.route("/predict",methods=['POST'])
def predict():
  loan_req=request.get_json()
  print(loan_req)
  if loan_req['Gender']=='Male':
    Gender = 0
  else:
    Gender = 1
  
  if loan_req['Married']=='Yes':
    Married = 1
  else:
    Married = 0
  
  if loan_req['Credit_History']=='Unclear Debts':
    Credit_History =  1
  else:
    Credit_History = 0

  ApplicantIncome = loan_req['ApplicantIncome']
  LoanAmount = loan_req['LoanAmount']
  
  result = clf.predict([[Gender, Married, ApplicantIncome, LoanAmount, Credit_History]])

  if result==1:
    pred='Approved'
  else:
    pred='Rejected'
  
  return {"loan approve status": pred}
