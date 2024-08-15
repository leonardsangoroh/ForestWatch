from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from dateutil.parser import parse
from flask_cors import CORS  # Import the CORS module
import statistics

# Create a Flask app instance
app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///events.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_type = db.Column(db.String(50), nullable=False)
    value = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.now)
    details = db.Column(db.String(200), nullable=True)
    lat = db.Column(db.Float, nullable=True)
    lon = db.Column(db.Float, nullable=True)

with app.app_context():
    db.create_all()

@app.route('/') # ✅
def index():
    total_events = Event.query.count()
    latest_event = Event.query.order_by(Event.timestamp.desc()).first()
    return render_template('overview.html', total_events=total_events, latest_event=latest_event)

#dashboardOne route
@app.route('/dashboard') # ✅
def indexDashboard():
    total_events = Event.query.count()
    latest_event = Event.query.order_by(Event.timestamp.desc()).first()
    return render_template('dashboard.html')

# Define a route to handle POST requests for logging sensor data ✅
@app.route('/events', methods=['POST'])
def events():
    data = request.get_json()
    if not data or 'event' not in data:
        return jsonify({"error": "Invalid data"}), 400
    
    event = Event(
        event_type=data['event'],
        value=data['value'],
        timestamp=parse(data['timestamp']),  # Use parse instead of fromisoformat
        details=data.get('details', 'No additional details'),
        lat=data['location']['lat'],
        lon=data['location']['lon']
    )
    db.session.add(event)
    db.session.commit()

    return jsonify({"message": f"{event.event_type.capitalize()} event detected and logged"}), 200

# get all events from events.db for dashboard_outdated.html ✅
@app.route('/allevents', methods=['GET'])
def get_events():
    events = Event.query.order_by(Event.timestamp.desc()).all()
    event_list = [{
        "id": event.id,
        "event_type": event.event_type,
        "value": event.value,
        "timestamp": event.timestamp,
        "details": event.details,
        "lat": event.lat,
        "lon": event.lon
    } for event in events]
    return jsonify(event_list)

# html pages routes

# root route
#@app.route('/dashboard') # ❌
#def dashboard():
#    total_events = Event.query.count()
#    latest_event = Event.query.order_by(Event.timestamp.desc()).first()
#    return render_template('dashboard_outdated.html', total_events=total_events, latest_event=latest_event)

@app.route('/event_log') # ✅
def event_log():
    events = Event.query.all()
    return render_template('event_log.html', events=events)

@app.route('/geospatial') # ✅
def geospatial():
    events = Event.query.all()
    return render_template('geospatial.html', events=events)

@app.route('/time_series') # ❌
def time_series():
    return render_template('time_series.html')

@app.route('/correlation') # ✅
def correlation():
    events = Event.query.all()
    return render_template('correlation.html', events=events)

# routes to provide data for the charts in dashboard.html
@app.route('/api/event_types', methods=['GET']) # ✅
def get_event_types():
    events = db.session.query(Event.event_type, db.func.count(Event.id)).group_by(Event.event_type).all()
    event_data = {event_type: count for event_type, count in events}
    return jsonify(event_data)

@app.route('/api/temperature_over_time', methods=['GET']) # ✅
def get_temperature_over_time():
    # Filter events to get only temperature events
    events = Event.query.filter_by(event_type='temperature').all()
    timestamps = [event.timestamp.strftime('%Y-%m-%d') for event in events]
    values = [event.value for event in events]
    return jsonify({"dates": timestamps, "values": values})

# endpoint to provide correlation data in correlation.html
@app.route('/api/correlation', methods=['GET']) # ✅
def api_correlation():
    # Fetch temperature and acoustic events from the database
    temp_events = Event.query.filter_by(event_type='temperature').all()
    sound_events = Event.query.filter_by(event_type='acoustic').all()

    # Prepare data lists
    timestamps = []
    temperatures = []
    sound_levels = []

    for event in temp_events:
        timestamps.append(event.timestamp.isoformat())
        temperatures.append(event.value)

    for event in sound_events:
        sound_levels.append(event.value)

    # Ensure that both lists have the same length
    min_length = min(len(temperatures), len(sound_levels))
    if min_length > 0:
        timestamps = timestamps[:min_length]
        temperatures = temperatures[:min_length]
        sound_levels = sound_levels[:min_length]

    return jsonify({
        'timestamps': timestamps,
        'temperature': temperatures,
        'sound': sound_levels
    })

# endpoint to provide map data for geospatial.html
@app.route('/api/locations', methods=['GET']) # ✅
def api_locations():
    # Fetch all events with lat and lon
    events = Event.query.filter(Event.lat.isnot(None), Event.lon.isnot(None)).all()

    # Prepare data list
    locations = [{
        'event_type': event.event_type,
        'value': event.value,
        'timestamp': event.timestamp.isoformat(),
        'lat': event.lat,
        'lon': event.lon
    } for event in events]

    return jsonify(locations)

#endpoint to get time-series data for time_series.html
@app.route('/api/time_series') # ✅
def get_time_series_data():
    events = Event.query.order_by(Event.timestamp).all()
    data = []
    
    for event in events:
        data.append({
            'event_type': event.event_type,
            'timestamp': event.timestamp.isoformat(),
            'value': event.value
        })
    
    return jsonify(data)

#statistics
@app.route('/api/statistics', methods=['GET'])
def get_statistics():
    # Fetch temperature and acoustic values from the database
    temperature_events = Event.query.filter_by(event_type='temperature').all()
    acoustic_events = Event.query.filter_by(event_type='acoustic').all()
    
    # Extract values
    temperature_values = [event.value for event in temperature_events]
    acoustic_values = [event.value for event in acoustic_events]
    
    # Calculate statistics
    def calculate_stats(values):
        if not values:
            return {
                'min': None,
                'max': None,
                'average': None,
                'std_dev': None,
                'count': 0
            }
        return {
            'min': min(values),
            'max': max(values),
            'average': sum(values) / len(values),
            'std_dev': statistics.stdev(values) if len(values) > 1 else 0,
            'count': len(values)
        }
    
    temperature_stats = calculate_stats(temperature_values)
    acoustic_stats = calculate_stats(acoustic_values)
    
    # Return statistics as JSON
    return jsonify({
        'temperature': temperature_stats,
        'acoustic': acoustic_stats
    })



# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
