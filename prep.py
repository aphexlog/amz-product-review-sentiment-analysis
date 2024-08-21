import pandas as pd
import boto3
from mypy_boto3_s3 import S3Client
from io import StringIO
import sagemaker
# Create a training job
from sagemaker.estimator import Estimator

# S3 client
client: S3Client = boto3.client('s3') # type: ignore

def prep_reviews(file_obj):
    # Load the CSV file from the file object
    df = pd.read_csv(file_obj['Body'])

    # Remove unwanted features
    # df = df.drop(columns=['UserId', 'ProfileName', 'HelpfulnessNumerator', 'HelpfulnessDenominator'])

    # Prepend Summary and Text to the DataFrame
    df = df[['Summary', 'Text', 'Score']]

    # Create a string buffer to hold the CSV content
    output = StringIO()
    df.to_csv(output, index=False)

    # Get the CSV content as a string
    csv_content = output.getvalue()

    # Return the CSV content
    return csv_content

# Example usage
# data = client.get_object(Bucket='elevator-robot-sagemaker', Key='Reviews.csv')
# prep_reviews(data)

bucket = 'elevator-robot-sagemaker'

src_data = client.get_object(Bucket=bucket, Key='Reviews.csv')

data = prep_reviews(src_data)

# Upload the preprocessed data to S3
client.put_object(Body=data, Bucket=bucket, Key='preprocessing/preprocessed_reviews.csv')

sagemaker_session = sagemaker.Session()
role = sagemaker.get_execution_role()

# Define the S3 URI for the input data
input_data = f's3://{bucket}/preprocessing/preprocessed_reviews.csv'


estimator = Estimator(
    image_uri='arn:aws:sagemaker:us-east-1:865070037744:algorithm/np-gpu-308-c7902823d4100b8dbae6765933fa14fc',  # Replace with your training image URI
    role=role,
    instance_count=1,
    instance_type='ml.t3.medium',
    output_path=f's3://{bucket}/output',
    sagemaker_session=sagemaker_session
)

# Set hyperparameters if necessary
estimator.set_hyperparameters(
    # Add your hyperparameters here
)

# Start the training job
estimator.fit({'train': input_data})
