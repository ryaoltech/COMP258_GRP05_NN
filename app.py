#!/usr/bin/env python
# coding: utf-8

# In[2]:


from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Retrieve data from the form
    numerical_features = [
        float(request.form['First_Term_Gpa']),
        float(request.form['Second_Term_Gpa']),
        float(request.form['High_School_Average_Mark']),
        float(request.form['Math_Score'])
    ]
    categorical_features = [request.form[column] for column in app.config['CATEGORICAL_COLUMNS']]

    # Perform prediction using your neural network model (replace this with your actual prediction logic)
    prediction_result = "Prediction Result"

    return render_template('index.html', prediction_result=prediction_result)

if __name__ == '__main__':
    app.config['CATEGORICAL_COLUMNS'] = ['First Language', 'Funding', 'School', 'FastTrack', 'Coop', 'Residensy', 'Gender', 'Previous_Education', 'Age_Group', 'English_Grade', 'First_Year_Persistence']
    app.run(debug=True)


# In[ ]:




