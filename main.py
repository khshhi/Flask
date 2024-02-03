import pickle
import pandas as pd
import numpy as np
from flask import Flask, render_template, request

#OOPs concept will be appled

app=Flask(__name__)
model=pickle.load(open('model.pkl','rb'))


#route give the endpoint
#It can be assumed as"URL/"" 
@app.route('/')
#return if the above is true
def index():
    return render_template("index.html")

@app.route('/predict',methods=['GET','POST'])
def predict():
    age = request.form.get('Age') # Convert to float
    gender = request.form.get('Gender')
    education_level = request.form.get('Education Level')
    years_of_experience = request.form.get('Years of Experience')  # Convert to float

    # Create a DataFrame
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction=model.predict(final_features)
    output=round(prediction[0],2)
    print(output)
    return render_template('index.html', prediction_text="Employee Salary should be ${}".format(output))

if __name__=='__main__':
    app.run(debug=True)