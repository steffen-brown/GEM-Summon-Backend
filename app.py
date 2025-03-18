from flask import Flask, request, jsonify
from flask_cors import CORS
from functools import wraps

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Global variables for storing locations and statuses
latest_phone_location = None   # Phone's summon location
latest_car_location = None     # Car's current location
car_status = "IDLE"            # Car status (IDLE, SUMMONING, ARRIVED)

def token_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token or token != 'sfdvghtrgta4y5tes4srt4awesrfg':
            return jsonify({'message': 'Unauthorized or invalid token'}), 401
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if username == "autobots" and password == "ece484":
        # In a real-world scenario, you'd verify credentials and generate a secure token.
        return jsonify({'message': 'Login successful', 'token': 'sfdvghtrgta4y5tes4srt4awesrfg'}), 200
    else:
        return jsonify({'message': 'Incorrect credentials'}), 400

# ---------------------------
# Phone Summon Location Endpoints
# ---------------------------

@app.route('/location', methods=['POST'])
@token_required
def update_phone_location():
    global latest_phone_location
    data = request.get_json()
    location = data.get('location')
    if location:
        latest_phone_location = location
        return jsonify({'message': 'Phone location updated', 'location': location}), 200
    else:
        return jsonify({'message': 'No location provided'}), 400

@app.route('/latest-location', methods=['GET'])
@token_required
def get_phone_location():
    if latest_phone_location:
        return jsonify({'location': latest_phone_location}), 200
    else:
        return jsonify({'message': 'No phone location data available'}), 404

# ---------------------------
# Car Location Endpoints
# ---------------------------

@app.route('/car-location', methods=['POST'])
@token_required
def update_car_location():
    global latest_car_location
    data = request.get_json()
    location = data.get('location')
    if location:
        latest_car_location = location
        return jsonify({'message': 'Car location updated', 'car_location': location}), 200
    else:
        return jsonify({'message': 'No location provided'}), 400

@app.route('/latest-car-location', methods=['GET'])
@token_required
def get_car_location():
    if latest_car_location:
        return jsonify({'car_location': latest_car_location}), 200
    else:
        return jsonify({'message': 'No car location data available'}), 404

# ---------------------------
# Car Status Endpoints
# ---------------------------

@app.route('/car-status', methods=['POST'])
@token_required
def update_car_status():
    global car_status
    data = request.get_json()
    new_status = data.get('status')
    valid_statuses = ["IDLE", "SUMMONING", "ARRIVED"]
    if new_status and new_status in valid_statuses:
        car_status = new_status
        return jsonify({'message': 'Car status updated', 'car_status': car_status}), 200
    else:
        return jsonify({
            'message': 'Invalid or missing status. Valid statuses are: IDLE, SUMMONING, ARRIVED.'
        }), 400

@app.route('/latest-car-status', methods=['GET'])
@token_required
def get_car_status():
    return jsonify({'car_status': car_status}), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
