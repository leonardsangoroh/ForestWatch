from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from dateutil.parser import parse

# Create a Flask app instance
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///events.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_type = db.Column(db.String(50), nullable=False)
    value = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.now)
    details = db.Column(db.String(200), nullable=True)

with app.app_context():
    db.create_all()

# Define a route for the home page
@app.route('/')
def home():
    return "Welcome to the Forest Project!"

# Define a route to handle POST requests for logging sensor data
@app.route('/events', methods=['POST'])
def notify():
    data = request.get_json()
    if not data or 'event' not in data:
        return jsonify({"error": "Invalid data"}), 400
    
    event = Event(
        event_type=data['event'],
        value=data['value'],
        timestamp=parse(data['timestamp']),  # Use parse instead of fromisoformat
        details=data.get('details', 'No additional details')
    )
    db.session.add(event)
    db.session.commit()

    return jsonify({"message": f"{event.event_type.capitalize()} event detected and logged"}), 200

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
