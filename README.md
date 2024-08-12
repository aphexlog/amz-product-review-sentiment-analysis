# Project: Sentiment Analysis on Amazon Reviews Using Amazon SageMaker

## Project Description

This project focuses on building a sentiment analysis model to evaluate Amazon product reviews using Amazon SageMaker. We'll leverage a pre-existing dataset and follow a structured approach to data collection, preprocessing, model training, evaluation, and deployment.

## Day 1: Data Collection & Preprocessing

**Task:** Utilize an existing dataset of Amazon product reviews. For this exercise, we will use [this Kaggle dataset](https://www.kaggle.com/datasets/arhamrumi/amazon-product-reviews).

**Steps:**

- Load the dataset into a SageMaker notebook.
- Perform basic data cleaning:
  - Removing null values.
  - Applying basic text preprocessing (e.g., lowercasing, removing punctuation).
- Split the dataset into training and test sets.

## Day 2: Model Training, Evaluation & Deployment

**Task:** Train a simple sentiment analysis model using SageMaker’s built-in algorithms, such as BlazingText or an LSTM model.

**Steps:**

- Train the model on your preprocessed data.
- Evaluate the model’s performance using metrics like accuracy or F1-score.
- Deploy the trained model as an endpoint in SageMaker.
- Create a simple test where you input a new review and get the predicted sentiment.

## Bonus (Optional, if time permits):

**Model Inference & API Integration:**

- Create a small API using Lambda or a Flask app to take new review inputs and return the sentiment prediction.

**Visualization:**

- Use Matplotlib or Seaborn to visualize the distribution of sentiments in your dataset.

## Time Breakdown:

- **Day 1:** 4-6 hours for data collection and preprocessing.
- **Day 2:** 4-6 hours for model training, evaluation, and deployment.
