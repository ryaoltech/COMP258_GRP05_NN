-- Run the model first 
file name = COMP258-NN-Group05
Because we have to save some files from the model to use in our app.py file 

--To access the app

Go to terminal or anaconda terminal
go to the folder where the application is and type: python app.py

note: install the flask if necessary
pip install flask 

-- App.py modification 
in the Flask app we have to change the path of the files, please add your path wehere all the codes are togheter, where the model is.
See the example below:

app = Flask(__name__)

# Folder and models
project_folder = 'add/your/path' <--- add your path here 

