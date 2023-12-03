from django.shortcuts import render
import pickle
import numpy as np
model=pickle.load(open('model2.pkl', 'rb'))

# Create your views here.
def home(request):
    
    return render(request,"index.html")
def predict(request):
    dis =request.GET['dis']
    hor =request.GET['hor']
    weight =request.GET['weight']
    acce = request.GET['acce']
    input = [dis,hor,weight,acce]
    output = model.predict([input])
    output = np.round(output[0], 2).item()
    output = str(output)+"mpg"
    return render(request,"index.html",{'output':output})
def predict(request):
    dis =request.GET['dis']
    hor =request.GET['hor']
    weight =request.GET['weight']
    acce = request.GET['acce']
    input = [dis,hor,weight,acce]
    output = model.predict([input])
    output = np.round(output[0], 2).item()
    output = str(output)+"mpg"
    return render(request,"result.html",{'output':output,'displacement':dis,'horsepower':hor,'weight':weight,'acceleration':acce})
