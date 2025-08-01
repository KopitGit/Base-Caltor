from flask import Flask, jsonify, request
from calculator import Calculator
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

calc = Calculator()

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    operation = data.get('operation')
    num1 = data.get('num1')
    num2 = data.get('num2', None)
    
    try:
        result = calc.perform_operation(operation, num1, num2)
        return jsonify({'result': result, 'status': 'success'})
    except Exception as e:
        return jsonify({'error': str(e), 'status': 'error'}), 400

if __name__ == '__main__':
    app.run(debug=True)