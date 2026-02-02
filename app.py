from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(__name__)

#Load the trained model

model = joblib.load('ames_housing_model.pkl')

@app.route('/')
def home():

    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # 2. Get data from the frontend
        data = request.json
        print("Received Data:", data)



        features = [
            float(data['Overall Qual']),
            float(data['Gr Liv Area']),
            float(data['Total Bsmt SF']),
            float(data['1st Flr SF']),
            float(data['Garage Cars']),
            float(data['Garage Area']),
            int(data['Year Built']),
            int(data['Full Bath']),
            int(data['Year Remod/Add']),
            float(data['Mas Vnr Area']),
            int(data['Fireplaces']),
            float(data['BsmtFin SF 1'])
        ]

        #Make the prediction

        final_features = [np.array(features)]
        prediction = model.predict(final_features)

        return jsonify({'predicted_price': prediction[0]})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == "__main__":
    app.run(debug=True)