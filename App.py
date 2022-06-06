from flask import Flask, request, render_template

import pickle

file1= open('Body Fat Estimator.pkl','rb')
M1= pickle.load(file1)
file1.close()

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])## Web Architect 

# POST, GET, PUT, PATCH, and DELETE

def pred():
    if request.method == 'POST':
        my_dist = request.form
        
        density = float(my_dist['density'])
        abdoman = float(my_dist['abdoman'])
        chest = float(my_dist['chest'])
        weight = float(my_dist['weight'])
        hip = float(my_dist['hip'])
        thigh = float(my_dist['thigh'])
        
        input_feature = [[density,abdoman,chest,weight,hip,thigh]]
        prediction = M1.predict(input_feature)[0].round(2)
        
        string= 'Body fat estimated is' + str(prediction)+'%'
        
        return render_template('show.html',string=string)
    
    return render_template('home.html')
                
    