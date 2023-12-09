import joblib
from keras.models import load_model
from flask import Flask, jsonify, request, render_template
from os import path
import sys
import pandas as pd

app = Flask(__name__)

# Folder and models
project_folder = r'C:\Users\User\OneDrive - Centennial College\Documents\Centennial\third semester\Neural\Group Pj\Test01'


# Load saved files 
numerical_features = joblib.load(path.join(project_folder, "numerical_features.joblib"))
categorical_features = joblib.load(path.join(project_folder, "categorical_features.joblib"))
preprocessor = joblib.load(path.join(project_folder, "preprocessor.joblib"))
pipeline = joblib.load(path.join(project_folder, "pipeline.joblib"))
model = load_model(path.join(project_folder, 'best_model.h5'))

                              
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the data from the request
        data = request.get_json(force=True)
        print('Received data:', data)
        
        
         # Extract features from the data
        input_data = {
            'First_Term_Gpa': float(data['First_Term_Gpa']),
            'Second_Term_Gpa': float(data['Second_Term_Gpa']),
            'Math_Score': float(data['Math_Score']),
            'First_Language': int(data['First_Language']),
            'Funding': float(data['Funding']),
            'FastTrack': int(data['FastTrack']),
            'Coop': int(data['Coop']),
            'Residency': int(data['Residency']),
            'Gender': float(data['Gender']),
            'Previous_Education': int(data['Previous_Education']),
            'Age_Group': int(data['Age_Group']),
            'English_Grade': int(data['English_Grade']),
        }
          # Create a DataFrame for the input data
        input_df = pd.DataFrame(input_data, index=[0])
        
        # Preprocess the input data
        preprocessed_data = pipeline.transform(input_df).toarray()
      
       # Make predictions on the preprocessed data
        predictions = model.predict(preprocessed_data)

     
        # Print intermediate values for debugging
        print('Preprocessed features:', preprocessed_data)
        print('Predictions:', predictions)

        # Format the prediction       
        predicted_class = "Will Persist" if predictions[0][0] > 0.5 else "Will Not Persist"

         # Return the prediction as JSON
        result = {'prediction': predicted_class}
        print('Result:', result)
        return jsonify(result)

    except Exception as e:
        print('Error:', str(e))
        return jsonify({'error': str(e)})

#port number
if __name__ == '__main__':
    try:
        port = int(sys.argv[1])
    except:
        port = 12411

    app.run(port=port, debug=True)
