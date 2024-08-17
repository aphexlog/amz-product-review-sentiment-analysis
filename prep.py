import pandas as pd
import boto3
from mypy_boto3_s3 import S3Client

# S3 client
client: S3Client = boto3.client('s3') # type: ignore

def prep_reviews(file_obj):
    # Load the CSV file from the file object
    df = pd.read_csv(file_obj['Body'])

    # Remove unwanted features
    df = df.drop(columns=['UserId', 'ProfileName', 'HelpfulnessNumerator', 'HelpfulnessDenominator'])

    # Prepend Summary and Text to the DataFrame
    df = df[['Summary', 'Text'] + [col for col in df.columns if col not in ['Summary', 'Text']]]

    # Write the new CSV content to a new file
    df.to_csv('Filtered_Reviews2.csv', index=False)

# Example usage
# data = client.get_object(Bucket='elevator-robot-sagemaker', Key='Reviews.csv')
# prep_reviews(data)
#
bucket = 'elevator-robot-sagemaker'
src_key = 'Reviews.csv'

data = client.get_object(Bucket=bucket, Key=src_key)
prep_reviews(data)
