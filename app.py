from flask import Flask, render_template, request

from flask import Flask, render_template, request

app = Flask(__name__,template_folder ="template")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    distance = float(request.form['distance'])
    transport = request.form['transport']
    electricity = float(request.form['electricity'])
    food = request.form['food']

    # Emission factors
    transport_emissions = {
        'car': 0.21,
        'bus': 0.1,
        'bike': 0.0
    }

    food_emissions = {
        'veg': 2.0,
        'nonveg': 5.0
    }

    # Calculation
    total_emission = (
        distance * transport_emissions.get(transport, 0) +
        electricity * 0.5 +
        food_emissions.get(food, 0)
    )

    return render_template('result.html', emission=round(total_emission, 2))

if __name__ == '__main__':
    app.run(debug=True) 