📦 Refund Tracker App

A simple web-based Refund Tracking System built using Flask.
Users can create refund requests and track their status using a unique tracking ID.

🚀 Features
🔹 Generate unique tracking IDs for refunds
🔹 Track refund status in real-time
🔹 Step-by-step progress updates
🔹 Lightweight and easy to deploy
🔹 No database required (uses JSON file storage)
🛠️ Tech Stack
Backend: Flask (Python)
Frontend: HTML (rendered using Flask templates)
Storage: JSON file (data.json)
📂 Project Structure
refund-tracker/
│── refund_tracker_app.py   # Main Flask application
│── data.json               # Stores tracking data (auto-created)
│── README.md               # Project documentation
⚙️ Installation & Setup
1. Clone the Repository
git clone https://github.com/your-username/refund-tracker.git
cd refund-tracker
2. Create Virtual Environment (optional but recommended)
python -m venv venv
source venv/bin/activate     # Linux/Mac
venv\Scripts\activate        # Windows
3. Install Dependencies
pip install flask
4. Run the App
python refund_tracker_app.py
5. Open in Browser
http://127.0.0.1:5000
🔄 How It Works
User creates a refund request → gets a Tracking ID

Status starts at:

Refund Initiated
Progression steps:
Refund Initiated
Processing by Merchant
Bank Contacted
Bank Processed Payment
Amount Credited
Status updates are stored in a JSON file
📸 Routes Overview
Route	Method	Description
/	GET	Home page
/create	POST	Create new refund
/track	GET/POST	Track refund
/advance/<tracking_id>	GET	Move to next step
