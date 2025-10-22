# YT-Capstone-Project
This is an end to end mlops capstone project for educational purpose.

## Architecture
This project now follows a modern web application architecture with:
- **Frontend**: React application for user interface
- **Backend**: Flask API for serving predictions
- **Model Serving**: MLflow for model management and serving

## Setup and Running

### Backend (Flask API)
1. Navigate to the flask_app directory
2. Install dependencies: `pip install -r requirements.txt`
3. Run the application: `python app.py`

### Frontend (React)
1. Navigate to the frontend directory
2. Install dependencies: `npm install`
3. Run the application: `npm start`

The frontend will be available at http://localhost:3000 and will communicate with the backend API at http://localhost:5000.