from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if city:
        return jsonify({"city": city, "temperature": "22°C", "condition": "Sunny"})
    else:
        return jsonify({"error": "City not provided"}), 400

if __name__ == '__main__':
    app.run(debug=True)
