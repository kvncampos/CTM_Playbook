from flask import Flask, jsonify
import json

app = Flask(__name__)

# Load data from ctm_data.json file
with open('docs/ctm_data.json', 'r') as file:
    ctm_data = json.load(file)

# Route for /keys/all
@app.route('/api/keys/all', methods=['GET'])
def get_keys_data():
    return jsonify(ctm_data)

if __name__ == '__main__':
    app.run(debug=True, port=5002)
