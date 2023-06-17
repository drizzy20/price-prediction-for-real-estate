import util

import os
import traceback
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


@app.route('/')
def index():
    # app_html_file = "app.html"
    # if not os.path.exists(os.path.join(app.template_folder, app_html_file)):
    #     return f"Error: {app_html_file} not found"
    return render_template("app.html")


@app.route('/get_locations', methods=['GET'])
def get_locations():
    responses = jsonify({'locations': util.get_locations()})
    responses.headers.add('access-control-allow-origin', '*')
    return responses


@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    try:
        print("Request data:", request.form)  # Print the request data for debugging

        total_sqft = float(request.form['total_sqft'])
        location = request.form['location']
        bhk = int(request.form['bhk'])
        bath = int(request.form['bath'])

        response = jsonify({
            'estimated_price': util.get_pedicted_prices(location, total_sqft, bhk, bath)
        })
        response.headers.add('Access-Control-Allow-Origin', '*')

        return response
    except Exception as e:
        traceback.print_exc()  # Print the traceback for debugging
        error_message = f"An error occurred: {str(e)}"
        response = jsonify({'error': error_message})
        response.status_code = 500  # Set status code to indicate internal server error
        return response


if __name__ == "__main__":
    print("Starting python server")
    util.load_artifacts()  # Initialize the artifacts
    app.run(debug=True)
