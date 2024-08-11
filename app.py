from flask import Flask, request, jsonify

# Create a Flask app instance
app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def home():
    return "Welcome to the Forest Project!"

# Define a route to handle POST requests for logging notifications
@app.route('/notify', methods=['POST'])
def notify():
    # Get data from the POST request
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid data"}), 400
    
    # Example: Access the 'event' field from the JSON data
    event_type = data.get('event')
    if event_type == 'logging':
        # Handle logging event (e.g., send a notification)
        return jsonify({"message": "Logging event detected and notification sent"}), 200
    elif event_type == 'fire':
        # Handle fire event (e.g., send a notification)
        return jsonify({"message": "Fire event detected and notification sent"}), 200
    else:
        return jsonify({"error": "Unknown event type"}), 400

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
