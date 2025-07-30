from flask import Flask, render_template, request
import random

app = Flask(__name__, template_folder="template")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    distance = float(request.form['distance'])
    transport = request.form['transport']
    electricity = float(request.form['electricity'])
    food = request.form['food']

    # Transport emission factors (kg CO2 per km)
    transport_emissions = {
        'Car - Petrol': 0.21,
        'Car - Diesel': 0.25,
        'Car - EV': 0.05,
        'Car - Hybrid': 0.13,
        'Bike - Petrol': 0.10,
        'Bike - Electric': 0.03,
        'Bus': 0.08
    }

    # Food emissions (kg CO2 per day)
    food_emissions = {
        'Vegetarian': 1.5,
        'Non-Vegetarian': 2.5
    }

    # Calculate total emission
    total_emission = (
        distance * transport_emissions.get(transport, 0) +
        electricity * 0.92 +
        food_emissions.get(food, 0)
    )

    # Emission range classification
    if total_emission < 2:
        level = "Low"
        color = "green"
    elif total_emission < 5:
        level = "Moderate"
        color = "orange"
    else:
        level = "High"
        color = "red"

    return render_template(
        'result.html',
        emission=round(total_emission, 2),
        level=level,
        color=color
    )

# AI advice generator route
@app.route('/ai-advice')
def ai_advice():
    tips = [
        "🚲 Switch to cycling or walking for short distances.",
        "💡 Use LED bulbs to save electricity.",
        "♻️ Reduce, reuse, and recycle as much as possible.",
        "🥦 Eat more plant-based meals.",
        "🔌 Unplug devices when not in use.",
        "🌳 Plant a tree to offset your emissions.",
        "🚌 Use public transport instead of personal vehicles.",
        "🔋 Switch to renewable energy sources if available."
    ]
    return random.choice(tips)

if __name__ == '__main__':
    app.run(debug=True)
