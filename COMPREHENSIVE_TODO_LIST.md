# MLOps Capstone Project - Comprehensive To-Do List

This document outlines all the necessary changes and tasks for modernizing the MLOps Capstone project with the agreed-upon architecture:

1. Replace Amazon S3 with MinIO for object storage
2. Create a React frontend that connects to the Flask backend API
3. Deploy the application to Render (free tier)
4. Maintain all existing MLOps tools (MLflow, DagsHub, DVC, Prometheus, Grafana)
5. Remove Kubernetes dependencies

## Task 1: Replace Amazon S3 with MinIO for Object Storage

### Overview
Replace AWS S3 object storage with MinIO, an open-source object storage system that is S3-compatible.

### Implementation Steps

#### Step 1: Update S3 Connection Module
Modify `src/connections/s3_connection.py` to support MinIO endpoints:

1. Add endpoint_url parameter to the constructor
2. Configure boto3 client to work with MinIO
3. Update logging to distinguish between S3 and MinIO

✅ **COMPLETED**

#### Step 2: Update Data Ingestion Script
Update `src/data/data_ingestion.py` to use MinIO:

1. Add commented example of MinIO usage
2. Keep existing data URL as default
3. Document how to switch between S3 and MinIO

✅ **COMPLETED**

#### Step 3: Update Makefile for MinIO Compatibility
Update the Makefile to include MinIO-specific commands:

1. Add MinIO configuration variables
2. Create new targets for MinIO sync operations
3. Document usage of both S3 and MinIO commands

✅ **COMPLETED**

#### Step 4: Update DVC Configuration Documentation
Update project documentation to reflect MinIO usage:

1. Modify projectflow.txt to show MinIO configuration
2. Document MinIO setup process
3. Explain how to configure DVC with MinIO

✅ **COMPLETED**

## Task 2: Create React Frontend for Flask Backend API

### Overview
Create a modern React frontend that connects to the existing Flask backend API, separating the frontend from the backend for a more scalable and maintainable architecture.

### Implementation Steps

#### Step 1: Modify Flask Backend for CORS Support
Update the Flask application to allow cross-origin requests from the React frontend:

1. Add flask-cors dependency to requirements.txt
2. Enable CORS in the Flask app
3. Create a new API endpoint that returns JSON responses

✅ **COMPLETED**

#### Step 2: Create React Application Structure
Create a new directory for the React frontend with the following structure:

```
frontend/
├── public/
│   ├── index.html
│   └── favicon.ico
├── src/
│   ├── components/
│   │   ├── SentimentAnalyzer.js
│   │   └── ResultDisplay.js
│   ├── App.js
│   ├── App.css
│   └── index.js
├── package.json
└── README.md
```

✅ **COMPLETED**

#### Step 3: Implement React Components
Create all necessary React components:

1. Main App component
2. SentimentAnalyzer component for text input
3. ResultDisplay component for showing predictions
4. CSS styling for a modern UI

✅ **COMPLETED**

#### Step 4: Update Project Documentation
Update documentation to reflect the new architecture:

1. Modify PROJECT_EXPLANATION.md to include frontend directory
2. Update README.md with new setup instructions
3. Document the new API endpoints

✅ **COMPLETED**

## Task 3: Deploy Application to Render (Free Tier)

### Overview
Deploy both the Flask backend and React frontend to Render's free tier for public access without AWS costs.

### Implementation Steps

#### Step 1: Prepare Backend for Render Deployment
Create Render configuration files for the Flask backend:

1. Create render.yaml for backend service configuration
2. Ensure all dependencies are properly listed
3. Test the application locally with Render-like environment variables

✅ **COMPLETED**

#### Step 2: Prepare Frontend for Render Deployment
Create Render configuration for the React frontend:

1. Ensure package.json has proper build scripts
2. Test the build process locally
3. Configure API endpoint URLs for Render deployment

✅ **COMPLETED**

#### Step 3: Set Up Render Account and Deploy
Deploy both services to Render:

1. Create a free Render account
2. Connect GitHub repository
3. Deploy backend as Web Service
4. Deploy frontend as Static Site
5. Configure environment variables for DagsHub credentials

🕒 **Pending** - Requires user to create Render account and deploy

#### Step 4: Configure Custom Domains (Optional)
Set up custom domains if desired:

1. Purchase or configure domain names
2. Set up DNS records in Render
3. Configure SSL certificates

🕒 **Pending** - Optional step

## Task 4: Maintain Existing MLOps Tools

### Overview
Keep all existing MLOps tools (MLflow, DagsHub, DVC, Prometheus, Grafana) functioning as they are, since they're compatible with Render deployment.

### Implementation Steps

#### Step 1: Verify MLflow/DagsHub Integration
Ensure MLflow continues to work with Render:

1. Test environment variable configuration in Render
2. Verify model loading from DagsHub
3. Confirm experiment tracking still works

🕒 **Pending** - Will be verified during deployment

#### Step 2: Maintain DVC Workflows
Keep DVC functioning for local development:

1. Document that DVC is only needed locally
2. Ensure DVC pipelines still work for experiment reproduction
3. Confirm model registration process continues to work

🕒 **Pending** - Will be verified during deployment

#### Step 3: Preserve Prometheus Metrics
Keep Prometheus metrics endpoint available:

1. Verify /metrics endpoint works on Render
2. Document how to set up external Prometheus scraping
3. Confirm all custom metrics are still collected

🕒 **Pending** - Will be verified during deployment

#### Step 4: Document Tool Usage
Update documentation to explain tool usage with Render:

1. Explain which tools work locally vs. remotely
2. Document environment variable requirements
3. Provide troubleshooting guidance

🕒 **Pending** - Will be completed after deployment

## Task 5: Remove Kubernetes Dependencies

### Overview
Remove all Kubernetes-specific configurations and dependencies since Render provides its own orchestration.

### Implementation Steps

#### Step 1: Archive Kubernetes Configuration
Handle the existing Kubernetes deployment file:

1. Rename deployment.yaml to deployment.yaml.archive
2. Document why this change was made
3. Keep as reference for potential future Kubernetes deployment

✅ **COMPLETED**

#### Step 2: Update Documentation
Update all documentation to reflect the change:

1. Remove references to kubectl commands
2. Update deployment instructions
3. Explain the new Render-based deployment process

🕒 **Pending** - Need to update documentation

#### Step 3: Clean Up Related Files
Remove or archive Kubernetes-related files:

1. Check for any other Kubernetes configuration files
2. Archive or remove EKS-specific setup instructions
3. Update projectflow.txt to reflect new deployment process

🕒 **Pending** - Need to check for other Kubernetes files

## Chronological Implementation Guide

### Phase 1: Infrastructure Changes (Days 1-3)
1. Implement MinIO integration
2. Test locally with MinIO server
3. Update all related documentation

✅ **COMPLETED**

### Phase 2: Frontend Development (Days 4-7)
1. Add CORS support to Flask backend
2. Create React frontend application
3. Test frontend-backend integration locally
4. Update project documentation

✅ **COMPLETED**

### Phase 3: Deployment Preparation (Days 8-10)
1. Create Render configuration files
2. Test deployment process locally
3. Prepare for production deployment
4. Update deployment documentation

✅ **COMPLETED**

### Phase 4: Production Deployment (Days 11-12)
1. Set up Render account
2. Deploy both services
3. Configure environment variables
4. Test production deployment

🕒 **Pending** - Requires user action

### Phase 5: Cleanup and Documentation (Day 13)
1. Remove Kubernetes dependencies
2. Finalize all documentation
3. Create user guides
4. Perform final testing

🕒 **Pending** - Will be completed after deployment

## Success Criteria

### For MinIO Integration:
- [x] Can switch between S3 and MinIO with configuration changes
- [x] All DVC operations work with MinIO
- [x] Documentation is clear and complete

### For React Frontend:
- [x] Frontend successfully connects to backend API
- [x] User interface is responsive and user-friendly
- [x] All existing functionality is preserved
- [x] Error handling works properly

### For Render Deployment:
- [ ] Backend deploys successfully to Render
- [ ] Frontend deploys successfully to Render
- [ ] Application is accessible via public URLs
- [ ] All MLOps tools continue to function
- [ ] Environment variables are properly configured

### For Documentation:
- [ ] All changes are properly documented
- [ ] Setup instructions are clear and complete
- [ ] Troubleshooting guide is available
- [ ] Architecture diagrams are updated

## Risk Mitigation

### Potential Issues and Solutions:

1. **MinIO Compatibility Issues**
   - Risk: Some S3 operations may not work exactly the same with MinIO
   - Solution: Thorough testing of all data operations

2. **CORS Configuration Problems**
   - Risk: Frontend may not be able to communicate with backend
   - Solution: Proper CORS configuration and error handling

3. **Render Deployment Failures**
   - Risk: Application may not deploy correctly to Render
   - Solution: Local testing with Render-like environment

4. **Performance Issues**
   - Risk: Free tier limitations may affect performance
   - Solution: Optimize application and monitor resource usage

5. **Data Loss During Migration**
   - Risk: Data may be lost during S3 to MinIO migration
   - Solution: Backup all data before migration and verify after

## Tools and Resources Needed

### Software:
- MinIO server (for local testing)
- Node.js and npm (for React development)
- Render account (free tier)
- GitHub account (for deployment)

### Knowledge:
- Basic React development
- Flask API development
- Render deployment process
- MinIO administration
- DVC workflows

### Time Estimate:
- Total: 13 days (part-time development)
- MinIO Integration: 3 days
- React Frontend: 4 days
- Render Deployment: 3 days
- Documentation and Cleanup: 3 days

## Next Steps

1. Create Render account
2. Deploy application to Render
3. Verify all functionality
4. Update remaining documentation
5. Test with production environment