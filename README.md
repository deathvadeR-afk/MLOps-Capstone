# MLOps Capstone Project

This is a modern end-to-end MLOps capstone project for educational purposes, featuring sentiment analysis of movie reviews with a complete ML pipeline and web interface.

## Architecture Overview

This project follows a modern web application architecture with:

- **Frontend**: React application for user interface
- **Backend**: Flask API for serving predictions
- **Model Serving**: MLflow with DagsHub for model management and serving
- **Data Management**: DVC for data version control
- **Object Storage**: MinIO (S3-compatible) for data storage
- **Monitoring**: Prometheus for metrics collection
- **Deployment**: Render (free tier) for hosting

## Technology Stack

### Backend (Python/Flask)
- Flask 3.1.0 - Web framework
- MLflow 2.19.0 - Model tracking and registry
- DagsHub 0.4.2 - MLflow tracking server
- NLTK 3.9.1 - Natural language processing
- scikit-learn 1.5.1 - Machine learning
- pandas 2.2.3 / numpy 2.2.1 - Data processing
- Prometheus Client - Metrics collection
- flask-cors 5.0.0 - Cross-origin resource sharing
- boto3 1.34.131 - AWS SDK (for MinIO compatibility)
- minio 7.2.7 - MinIO client

### Frontend (React)
- React 18.2.0 - JavaScript library for UI
- react-scripts 5.0.1 - Build toolchain

### Infrastructure
- DVC 3.53.0 - Data version control
- Docker - Containerization
- Render - Deployment platform (free tier)
- MinIO - Object storage (S3-compatible)

## Project Structure

```
.
├── flask_app/                 # Flask web application
│   ├── app.py                 # Main Flask application
│   ├── requirements.txt       # Flask dependencies
│   └── templates/             # HTML templates
├── frontend/                  # React frontend application
│   ├── src/                   # React source code
│   ├── public/                # Static assets
│   ├── package.json           # Frontend dependencies
│   └── render.yaml           # Frontend Render config
├── src/                       # Data science modules
│   ├── data/                 # Data processing scripts
│   ├── features/             # Feature engineering
│   ├── model/                # Model training/evaluation
│   ├── connections/          # Database connections
│   └── logger/               # Logging configuration
├── notebooks/                # Jupyter notebooks
├── data/                     # Data storage
├── models/                   # Trained models
├── tests/                    # Unit tests
├── requirements.txt          # Python dependencies
├── requirements-dev.txt      # Development dependencies
├── Makefile                 # Build automation
├── setup.py                 # Package setup
└── render.yaml              # Backend Render config
```

## Setup and Running

### Prerequisites
- Python 3.8+
- Node.js 14+
- npm 6+
- Git

### Environment Variables
Create a `.env` file with the following variables:
```bash
CAPSTONE_TEST=your_dagshub_token
AWS_ACCESS_KEY_ID=minio_access_key
AWS_SECRET_ACCESS_KEY=minio_secret_key
AWS_ENDPOINT_URL=http://localhost:9000  # For local MinIO
```

### Backend (Flask API)
1. Create virtual environment: `python -m venv venv`
2. Activate virtual environment: `source venv/bin/activate` (Linux/Mac) or `venv\Scripts\activate` (Windows)
3. Install dependencies: `pip install -r requirements.txt`
4. Run the application: `python flask_app/app.py`

### Frontend (React)
1. Navigate to the frontend directory: `cd frontend`
2. Install dependencies: `npm install`
3. Run the application: `npm start`

The frontend will be available at http://localhost:3000 and will communicate with the backend API at http://localhost:5000.

### Using Makefile Commands
```bash
# Install Python dependencies
make requirements

# Install development dependencies
make dev-requirements

# Install frontend dependencies
make frontend-install

# Start frontend development server
make frontend-start

# Build frontend for production
make frontend-build

# Sync data to MinIO
make sync_data_to_minio

# Sync data from MinIO
make sync_data_from_minio
```

## Data Pipeline
1. Run DVC pipeline: `dvc repro`
2. Commit changes: `dvc commit`
3. Push to remote: `dvc push`

## Deployment
This project is configured for deployment on Render:

1. Push code to GitHub
2. Connect Render to your repository
3. Deploy backend as Web Service using `render.yaml`
4. Deploy frontend as Static Site using `frontend/render.yaml`

## Monitoring
Prometheus metrics are available at `http://localhost:5000/metrics`

## Testing
```bash
# Backend tests
python -m pytest tests/

# Frontend tests
cd frontend && npm test
```

## License
This project is licensed under the MIT License.