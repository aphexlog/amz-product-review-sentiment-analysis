import pandas as pd

def prep_reviews(file_obj):
    # Load the CSV file from the file object
    df = pd.read_csv(file_obj['Body'])

    # Remove unwanted features
    df = df.drop(columns=['UserId', 'ProfileName', 'HelpfulnessNumerator', 'HelpfulnessDenominator'])

    # Prepend Summary and Text to the DataFrame
    df = df[['Summary', 'Text'] + [col for col in df.columns if col not in ['Summary', 'Text']]]

    # Write the new CSV content to a new file
    df.to_csv('Filtered_Reviews.csv', index=False)

# Example usage
# data = client.get_object(Bucket='elevator-robot-sagemaker', Key='Reviews.csv')
# prep_reviews(data)
