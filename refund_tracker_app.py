from flask import Flask, render_template_string, request, redirect, url_for
import json, os, uuid

app = Flask(__name__)

DATA_FILE = 'data.json'
STEPS = [
    "Refund Initiated",
    "Processing by Merchant",
    "Bank Contacted",
    "Bank Processed Payment",
    "Amount Credited"
]

# Load/Save Functions
def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

# Templates
INDEX_HTML = """
<!DOCTYPE html>
<html>
<head><title>Refund Tracker</title></head>
<body>
    <h2>Refund Tracking System</h2>
    <form action="/create" method="post">
        <button type="submit">Create Refund Request</button>
    </form>
    <h3>OR</h3>
    <form action="/track" method="post">
        <label>Enter Tracking ID:</label>
        <input type="text" name="tracking_id" required>
        <button type="submit">Check Status</button>
    </form>
</body>
</html>
"""

TRACK_HTML = """
<!DOCTYPE html>
<html>
<head><title>Track Refund</title></head>
<body>
    <h2>Track Refund</h2>
    {% if error %}
        <p style="color:red;">{{ error }}</p>
    {% endif %}
    <form action="/track" method="post">
        <label>Enter Tracking ID:</label>
        <input type="text" name="tracking_id" required>
        <button type="submit">Check Status</button>
    </form>
    <br><a href="/">Back to Home</a>
</body>
</html>
"""

STATUS_HTML = """
<!DOCTYPE html>
<html>
<head><title>Status</title></head>
<body>
    <h2>Tracking ID: {{ tracking_id }}</h2>
    <p>📦 Current Status: <strong>{{ status }}</strong></p>
    {% if status != "Amount Credited" %}
        <a href="/advance/{{ tracking_id }}">Advance Status</a>
    {% endif %}
    <br><br><a href="/">Back to Home</a>
</body>
</html>
"""

# Routes
@app.route('/')
def index():
    return render_template_string(INDEX_HTML)

@app.route('/create', methods=['POST'])
def create():
    data = load_data()
    tracking_id = str(uuid.uuid4())[:8]
    data[tracking_id] = 0
    save_data(data)
    return render_template_string(STATUS_HTML, tracking_id=tracking_id, status=STEPS[0])

@app.route('/track', methods=['GET', 'POST'])
def track():
    if request.method == 'POST':
        tracking_id = request.form['tracking_id'].strip()
        data = load_data()
        if tracking_id in data:
            return render_template_string(STATUS_HTML, tracking_id=tracking_id, status=STEPS[data[tracking_id]])
        else:
            return render_template_string(TRACK_HTML, error="Invalid Tracking ID")
    return render_template_string(TRACK_HTML)

@app.route('/advance/<tracking_id>')
def advance(tracking_id):
    data = load_data()
    if tracking_id in data and data[tracking_id] < len(STEPS) - 1:
        data[tracking_id] += 1
        save_data(data)
    return redirect(url_for('track'))

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
