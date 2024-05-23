"""
This module contains the route which implements the web service to compute the standard deviation of the Halstfede Dimensions.
"""
from flask import Flask, jsonify, request, make_response
from service.standard_deviation import compute_standard_deviation
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

app = Flask(__name__)


@app.route('/compute_std_dev', methods=['POST'])
@cross_origin()
def compute_standard_deviation_route():
    """
    Web Service to compute the standard deviation of all of the six Halstfede Dimensions.

    Parameters:
        request: The request must contain a list of JSON objects describing the community of developers.
        The request should have the following shape:
            [
                {"number": 3, "nationality": "Germany"},
                {"number": 4, "nationality": "Spain"}
            ]
        So number is the number of developers of a certain Nationality

    Returns:
        dictx: a dictionary containing the standard deviation of each of the 6 Halstfede Dimensions
    """
    try:
        data = request.get_json()
    except Exception as e:
        return make_response(jsonify({'error': 'Invalid input'}), 400)

    result, country_null_metrics = compute_standard_deviation(data)

    result['null_values'] = country_null_metrics
    
    return jsonify(result), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)