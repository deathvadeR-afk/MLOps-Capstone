# MLOps Capstone Project - Complete Explanation

## Project Overview

The MLOps Capstone Project is an end-to-end machine learning operations pipeline designed for educational purposes, specifically focusing on sentiment analysis of movie reviews. The project follows the *cookiecutter-data-science* template structure and implements a complete MLOps workflow from data ingestion to model deployment and monitoring.

## Project Structure and Organization

The project follows a well-organized directory structure:

```
.
├── flask_app/                 # Flask web application for model deployment
├── frontend/                  # React frontend application
├── notebooks/                 # Jupyter notebooks for experimentation
├── scripts/                   # Utility scripts
├── src/                       # Source code organized by functionality
│   ├── connections/           # Database and cloud connection modules
│   ├── features/              # Feature engineering modules
│   ├── logger/                # Logging configuration
│   └── model/                # Model building, evaluation, and registration
├── tests/                    # Unit tests for the application
├── data/                     # Data storage (raw, interim, processed)
├── models/                   # Trained and serialized models
├── reports/                  # Experiment reports and metrics
└── docs/                     # Documentation
```

## Technology Stack

The project leverages a modern MLOps technology stack:

- **Core Languages**: Python 3.10
- **Data Processing**: pandas, numpy, scikit-learn
- **NLP Libraries**: NLTK for text preprocessing
- **Model Tracking**: MLflow with DagsHub integration
- **Version Control**: DVC (Data Version Control)
- **Cloud Services**: MinIO for object storage
- **Containerization**: Docker
- **CI/CD**: GitHub Actions
- **Monitoring**: Prometheus and Grafana
- **Web Framework**: Flask for deployment
- **Testing**: unittest framework

## Core Functionality

### 1. Data Pipeline

The data pipeline consists of several stages defined in `dvc.yaml`:

- **Data Ingestion** (`data_ingestion.py`): Downloads data from a remote source, preprocesses it, and splits it into train/test sets
- **Data Preprocessing** (`data_preprocessing.py`): Cleans and normalizes text data
- **Feature Engineering** (`feature_engineering.py`): Applies Bag of Words vectorization to convert text to numerical features
- **Model Building** (`model_building.py`): Trains a Logistic Regression model
- **Model Evaluation** (`model_evaluation.py`): Evaluates model performance and logs metrics to MLflow
- **Model Registration** (`register_model.py`): Registers the model in MLflow Model Registry

### 2. Experimentation

The project includes three experimentation notebooks:

1. **Baseline Experiment** (`exp1.ipynb`): Establishes a baseline model using Logistic Regression with Bag of Words
2. **Algorithm Comparison** (`exp2_bow_vs_tfidf.py`): Compares multiple algorithms (Logistic Regression, Naive Bayes, XGBoost, Random Forest, Gradient Boosting) with both Bag of Words and TF-IDF vectorization
3. **Hyperparameter Tuning** (`exp3_lor_bow_hp.py`): Performs hyperparameter tuning for Logistic Regression

### 3. Model Management

The project uses MLflow for comprehensive model management:
- **Tracking**: Logs parameters, metrics, and artifacts for each experiment
- **Registry**: Registers models and manages their lifecycle stages (None, Staging, Production)
- **Versioning**: Maintains different versions of models

### 4. Deployment

The model is deployed through multiple stages:

1. **Flask Application** (`app.py`): A web application that serves predictions through a REST API and includes a simple UI
2. **React Frontend**: A modern user interface that communicates with the Flask backend
3. **Docker Containerization** (`Dockerfile`): Packages the application for consistent deployment
4. **Monitoring**: Integrates Prometheus metrics for application monitoring

### 5. CI/CD Pipeline

The project implements a comprehensive CI/CD pipeline using GitHub Actions that includes:
- Automated testing
- Docker image building
- Deployment to Render (free tier)

## Key Components Analysis

### Data Processing Pipeline

The data processing pipeline follows a clear flow:
1. Raw data is ingested from a remote source or MinIO
2. Text preprocessing normalizes the data (lowercasing, stop word removal, lemmatization, etc.)
3. Feature engineering converts text to numerical features using Bag of Words
4. The processed data is used to train a Logistic Regression model

### Model Training and Evaluation

The model training process includes:
- Hyperparameter tuning using GridSearchCV
- Cross-validation for robust evaluation
- Comprehensive metrics logging (accuracy, precision, recall, F1-score)
- Model artifact logging with MLflow

### Deployment Architecture

The deployment architecture is designed for scalability and reliability:
- Flask application serves predictions through REST API
- React frontend provides a modern user interface
- Docker ensures consistent environments
- Prometheus integration enables monitoring
- Deployed to Render for free hosting

### Monitoring and Observability

The system includes monitoring capabilities:
- Custom Prometheus metrics for request count, latency, and prediction distribution
- Health endpoints for service monitoring
- Structured logging for debugging and audit trails

## Configuration and Parameters

The project uses YAML configuration files for managing parameters:
- `params.yaml`: Defines parameters for data ingestion and feature engineering
- `config.json`: Contains database connection details
- Environment variables for sensitive information (DagsHub tokens)

## Testing Strategy

The project includes unit tests for:
- Model loading and signature verification
- Flask application endpoints
- Performance validation against defined thresholds

## Cloud Infrastructure

The project is designed to work with free-tier services:
- MinIO for object storage (self-hosted or cloud)
- Render for application hosting
- DagsHub for MLflow model tracking

## Project Workflows

The project supports multiple workflows through:
- **Makefile**: Standard data science commands (requirements, data, lint, clean)
- **DVC Pipeline**: Reproducible machine learning workflows
- **GitHub Actions**: Automated CI/CD processes

## Security Considerations

The project implements security best practices:
- Environment variables for sensitive credentials
- Secure connection handling for cloud services
- Proper error handling to prevent information leakage

## Conclusion

This MLOps Capstone Project demonstrates a comprehensive end-to-end machine learning pipeline that covers all aspects of modern ML engineering:
1. Data management with version control
2. Experiment tracking and model management
3. Automated testing and validation
4. Modern frontend-backend architecture
5. Containerized deployment
6. Monitoring and observability
7. CI/CD automation

The project serves as an excellent educational resource for understanding how to build production-ready machine learning systems with proper MLOps practices.