from django.shortcuts import render
import joblib
import numpy as np

def home_page(request):
    data = {}
    if request.method == "POST":
        type = int(request.POST.get('type'))
        amount = float(request.POST.get('amount'))
        oldbalanceOrg = float(request.POST.get('oldbalanceOrg'))
        newbalanceOrg = float(request.POST.get('newbalanceOrg'))
        oldbalanceDest = float(request.POST.get('oldbalanceDest'))
        newbalanceDest = float(request.POST.get('newbalanceDest'))
        result = None

        dataset = np.array([type,amount,oldbalanceOrg,newbalanceOrg,oldbalanceDest,newbalanceDest])
        print(dataset)

        my_model = joblib.load('my_model.sav')
        result = my_model.predict([dataset])

        print(result)
        output = 'No Fraud'
        if result[0] == 1:
            output = 'Fraud'
        data = {
            'type' : type,
            'amount' : amount,
            'oldbalanceOrg' : oldbalanceOrg,
            'newbalanceOrg' : newbalanceOrg,
            'oldbalanceDest' : oldbalanceDest,
            'newbalanceDest' : newbalanceDest,
            'result' : output
        }
    return render(request,"index.html",data)