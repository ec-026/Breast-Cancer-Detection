import numpy as np
# from xgboost import XGBClassifier
# from sklearn.ensemble import XGBoost as xgb
# from xgboost.sklearn import XGBClassifier
import pickle
# from sklearn.externals import joblib
from sklearn.ensemble import RandomForestClassifier
# import xgboost as xgb
import pandas as pd
from flask import Flask, request, render_template, flash, get_flashed_messages, redirect, url_for
# import joblib
from dataset import data

app = Flask(__name__)
app.secret_key = 'your_secret_key'
model = pickle.load(open('breast_cancer_detector.pickle', 'rb'))
# model = XGBClassifier.Booster({'nthread':4})
# model.load_model('new.pkl')


@app.route('/', methods=['GET', 'POST'])
def home():
    selected_sample_id = None
    selected_sample_data = {}

    # When form is submitted
    if request.method == 'POST':
        selected_sample_id = request.form.get('sample_data')

        # Find the selected sample data
        for sample in data:
            if str(sample['id']) == selected_sample_id:
                selected_sample_data = sample
                break

    # Get flash messages, if any
    prediction_text = get_flashed_messages()

    return render_template('index.html',
                           data=data,
                           selected_sample_id=selected_sample_id,
                           selected_sample_data=selected_sample_data,
                           prediction_text=prediction_text)


@app.route('/predict', methods=['POST'])
def predict():
    # Extract input features from the form.
    input_features = [float(x) for x in request.form.values()]
    features_value = [np.array(input_features)]

    # Define the feature names in the same order as your model expects.
    features_name = ['mean radius', 'mean texture', 'mean perimeter', 'mean area',
                     'mean smoothness', 'mean compactness', 'mean concavity',
                     'mean concave points', 'mean symmetry', 'mean fractal dimension',
                     'radius error', 'texture error', 'perimeter error', 'area error',
                     'smoothness error', 'compactness error', 'concavity error',
                     'concave points error', 'symmetry error', 'fractal dimension error',
                     'worst radius', 'worst texture', 'worst perimeter', 'worst area',
                     'worst smoothness', 'worst compactness', 'worst concavity',
                     'worst concave points', 'worst symmetry', 'worst fractal dimension']

    # Create a DataFrame for the model prediction.
    df = pd.DataFrame(features_value, columns=features_name)

    # Make the prediction using the model.
    output = model.predict(df)

    # Interpret the model output.
    if output == 0:
        res_val = "breast cancer (Malignant)"
    else:
        res_val = "no breast cancer (Benign)"

    # Store the prediction result in a flash message.
    flash(f'Patient has {res_val}')

    # Redirect back to the home route.
    return redirect(url_for('home'))


if __name__ == "__main__":
    #     app.debug = True
    app.run()
