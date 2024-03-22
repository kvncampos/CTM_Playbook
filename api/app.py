from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# Load data from ctm_data.json file
with open('docs/ctm_data.json', 'r') as file:
    ctm_data = json.load(file)
    
    
# Route for /keys/all
@app.route('/', methods=['GET'])
def home():
    return jsonify({"hello": "world"})

# Route for /keys/all
@app.route('/api/keys/all', methods=['GET', 'POST'])
def get_keys_data():
    if request.method == 'POST':
        # Handle the POST request
        data = request.json  # Assuming JSON data is sent in the request
        # Process the data as needed
        # Return a JSON response with status code 200 to indicate success
        return jsonify({"message": "Success"}), 200
    
    return jsonify(ctm_data)

if __name__ == '__main__':
    app.run(debug=True, port=5002)
