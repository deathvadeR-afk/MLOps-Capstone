# Updated Technology Stack Documentation

This document outlines the updated technology stack for the MLOps Capstone project after implementing the modernization changes.

## Core Technology Stack

### Backend (Python/Flask)
- **Framework**: Flask 3.1.0
- **ML Framework**: scikit-learn 1.5.1
- **Data Processing**: pandas 2.2.3, numpy 2.2.1
- **NLP**: NLTK 3.9.1
- **Model Tracking**: MLflow 2.19.0
- **Model Registry**: DagsHub 0.4.2
- **Data Version Control**: DVC 3.53.0
- **Object Storage**: MinIO 7.2.7 (S3-compatible)
- **Monitoring**: Prometheus Client
- **CORS Support**: flask-cors 5.0.0

### Frontend (React)
- **Framework**: React 18.2.0
- **Build Tool**: react-scripts 5.0.1
- **State Management**: Built-in React hooks
- **Styling**: CSS modules and vanilla CSS

### Infrastructure & Deployment
- **Deployment Platform**: Render (free tier)
- **Containerization**: Docker
- **Version Control**: Git
- **CI/CD**: GitHub Actions (planned)

## Key Changes from Original Stack

### 1. Object Storage
**Before**: Amazon S3 with boto3
**After**: MinIO with boto3 (S3-compatible)
- Added explicit MinIO dependency (minio==7.2.7)
- Updated connection modules to support endpoint URLs
- Maintained backward compatibility with AWS S3

### 2. Frontend Framework
**Before**: Server-side rendered Flask templates only
**After**: Modern React frontend with Flask API backend
- Added flask-cors for cross-origin resource sharing
- Created new JSON API endpoints in Flask
- Built complete React application with components

### 3. Deployment Platform
**Before**: Kubernetes (EKS) with AWS services
**After**: Render (free tier) with simplified deployment
- Removed Kubernetes dependencies
- Archived deployment.yaml
- Created Render configuration files

### 4. Updated Dependencies
- Flask: 3.0.3 → 3.1.0
- NLTK: 3.8.1 → 3.9.1
- pandas: 2.2.2 → 2.2.3
- numpy: 1.26.4 → 2.2.1
- MLflow: 2.15.0 → 2.19.0
- DagsHub: 0.3.34 → 0.4.2

## Dependency Management

### Python Dependencies
Managed through `requirements.txt`:
```bash
# Install all dependencies
pip install -r requirements.txt

# For development
pip install -e .
```

### Frontend Dependencies
Managed through `package.json`:
```bash
# Install frontend dependencies
cd frontend
npm install

# Start development server
npm start

# Build for production
npm run build
```

## Environment Variables

### Required Environment Variables
- `CAPSTONE_TEST`: DagsHub authentication token
- `AWS_ACCESS_KEY_ID`: MinIO access key (for DVC)
- `AWS_SECRET_ACCESS_KEY`: MinIO secret key (for DVC)
- `AWS_ENDPOINT_URL`: MinIO endpoint URL (e.g., http://localhost:9000)

### Example Configuration
```bash
export CAPSTONE_TEST="your_dagshub_token"
export AWS_ACCESS_KEY_ID="minioadmin"
export AWS_SECRET_ACCESS_KEY="minioadmin"
export AWS_ENDPOINT_URL="http://localhost:9000"
```

## Development Workflow

### Backend Development
1. Activate virtual environment
2. Install dependencies: `pip install -r requirements.txt`
3. Run Flask app: `python flask_app/app.py`

### Frontend Development
1. Navigate to frontend directory: `cd frontend`
2. Install dependencies: `npm install`
3. Start development server: `npm start`

### Data Pipeline
1. Run DVC pipeline: `dvc repro`
2. Sync with MinIO: `make sync_data_to_minio`

### Deployment
1. Push to GitHub
2. Connect Render to repository
3. Deploy backend as Web Service
4. Deploy frontend as Static Site

## Testing

### Backend Testing
```bash
# Run Flask app tests
python -m pytest tests/test_flask_app.py

# Run model tests
python -m pytest tests/test_model.py
```

### Frontend Testing
```bash
# Run React tests
cd frontend
npm test
```

## Monitoring

### Prometheus Metrics
- Custom metrics available at `/metrics` endpoint
- Request count, latency, and prediction distribution tracking
- Compatible with external Prometheus servers

## Security Considerations

1. Environment variables for sensitive data
2. CORS configuration for frontend-backend communication
3. Secure connection handling for MinIO and DagsHub
4. No hardcoded credentials in source code

## Future Enhancements

1. Add unit tests for React components
2. Implement CI/CD pipeline with GitHub Actions
3. Add authentication and user management
4. Implement logging aggregation
5. Add performance monitoring dashboards