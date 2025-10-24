from setuptools import find_packages, setup

setup(
    name='mlops-capstone',
    packages=find_packages(),
    version='1.0.0',
    description='Modern MLOps Capstone Project with React Frontend and MinIO Integration',
    author='Sagar',
    license='MIT',
    install_requires=[
        'Flask>=3.1.0',
        'flask-cors>=5.0.0',
        'mlflow>=2.19.0',
        'dagshub>=0.4.2',
        'nltk>=3.9.1',
        'numpy>=2.2.1',
        'pandas>=2.2.3',
        'scikit-learn>=1.5.1',
        'prometheus_client>=0.20.0',
        'boto3>=1.34.0',
        'minio>=7.2.7',
        'dvc>=3.53.0',
        'dvc-s3>=3.2.0'
    ],
    python_requires='>=3.8',
)