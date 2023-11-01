from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def calculator():
    """render the template"""
    return render_template('calculator.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    """calculate the expression"""
    try:
        expression = request.form['expression']
        result = eval(expression)
        return jsonify({"result": result})
    except:
        return jsonify({"error": "Invalid expression"})

if __name__ == '__main':
    app.run()
