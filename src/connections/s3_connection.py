import boto3
import pandas as pd
import logging
from src.logger import logging
from io import StringIO

# # Configure logging
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

class s3_operations:
    def __init__(self, bucket_name, aws_access_key, aws_secret_key, region_name="us-east-1", endpoint_url=None):
        """
        Initialize the s3_operations class with AWS credentials and S3 bucket details.
        For MinIO, provide the endpoint_url parameter.
        """
        self.bucket_name = bucket_name
        # If endpoint_url is provided, use it for MinIO; otherwise, use default AWS S3
        client_params = {
            'aws_access_key_id': aws_access_key,
            'aws_secret_access_key': aws_secret_key,
            'region_name': region_name
        }
        
        if endpoint_url:
            client_params['endpoint_url'] = endpoint_url
            # For MinIO, path style is often needed
            client_params['config'] = boto3.session.Config(s3={'addressing_style': 'path'})
            
        self.s3_client = boto3.client('s3', **client_params)
        service_name = "MinIO" if endpoint_url else "S3"
        logging.info(f"Data Ingestion from {service_name} bucket initialized")

    def fetch_file_from_s3(self, file_key):
        """
        Fetches a CSV file from the S3 bucket and returns it as a Pandas DataFrame.
        :param file_key: S3 file path (e.g., 'data/data.csv')
        :return: Pandas DataFrame
        """
        try:
            service_name = "MinIO" if hasattr(self.s3_client, 'endpoint_url') else "S3"
            logging.info(f"Fetching file '{file_key}' from {service_name} bucket '{self.bucket_name}'...")
            obj = self.s3_client.get_object(Bucket=self.bucket_name, Key=file_key)
            df = pd.read_csv(StringIO(obj['Body'].read().decode('utf-8')))
            logging.info(f"Successfully fetched and loaded '{file_key}' from {service_name} that has {len(df)} records.")
            return df
        except Exception as e:
            service_name = "MinIO" if hasattr(self.s3_client, 'endpoint_url') else "S3"
            logging.exception(f"❌ Failed to fetch '{file_key}' from {service_name}: {e}")
            return None

# Example usage
# if __name__ == "__main__":
#     # For AWS S3
#     # data_ingestion = s3_operations("bucket-name", "AWS_ACCESS_KEY", "AWS_SECRET_KEY")
#     
#     # For MinIO
#     # data_ingestion = s3_operations("bucket-name", "MINIO_ACCESS_KEY", "MINIO_SECRET_KEY", 
#     #                               endpoint_url="http://localhost:9000")
#     # df = data_ingestion.fetch_file_from_s3("data.csv")

#     if df is not None:
#         print(f"Data fetched with {len(df)} records..")  # Display first few rows of the fetched DataFrame