"""app.py"""
import ast
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def calculator():
    """app.py"""
    return render_template('calculator.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    """Calculator.py"""
    try:
        expression = request.form['expression']
        # Use a safer expression evaluation method like 'ast.literal_eval'
        result = ast.literal_eval(expression)
        return jsonify({"result": result})
    except (ValueError, SyntaxError):
        return jsonify({"error": "Invalid expression"})

if __name__ == '__main__':
    app.run(debug=True)
