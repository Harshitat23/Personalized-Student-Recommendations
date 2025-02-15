# -*- coding: utf-8 -*-
"""Testline.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1k8F9yBMav7Rrgt4vKE6Guvaj5Yz3JN-r
"""

import requests
import warnings
import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Suppress SSL warnings
warnings.filterwarnings("ignore", category=requests.packages.urllib3.exceptions.InsecureRequestWarning)

# API Endpoints
CURRENT_QUIZ_URLS = [
    "https://jsonkeeper.com/b/LLQT",
    "https://api.jsonserve.com/rJvd7g"
]
HISTORICAL_QUIZ_URL = "https://api.jsonserve.com/XgAgFJ"

def fetch_data(url):
    try:
        response = requests.get(url, verify=False)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

current_quiz_data = [fetch_data(url) for url in CURRENT_QUIZ_URLS]

historical_quiz_data = fetch_data(HISTORICAL_QUIZ_URL)

print("Current Quiz Data:", current_quiz_data)
print("Historical Quiz Data:", historical_quiz_data)

historical_df = pd.DataFrame(historical_quiz_data)
print(df.info())

print(historical_df.head())

def extract_quiz_performance(data):
    performance_records = []
    for quiz in data:
        user_id = quiz.get("user_id", "Unknown")
        performance_records.append({
            "user_id": user_id,
            "score": quiz.get("score", 0),
            "accuracy": float(quiz.get("accuracy", "0 %").replace("%", "")) / 100,
            "correct_answers": quiz.get("correct_answers", 0),
            "incorrect_answers": quiz.get("incorrect_answers", 0),
            "negative_score": quiz.get("negative_score", 0),
            "speed": float(quiz.get("speed", 0))
        })
    return pd.DataFrame(performance_records)

historical_df = extract_quiz_performance(historical_quiz_data)

def analyze_performance(df):
    score_trend = df["score"].mean()
    accuracy_trend = df["accuracy"].mean()
    mistakes_trend = df["incorrect_answers"].mean()
    return score_trend, accuracy_trend, mistakes_trend

score_trend, accuracy_trend, mistakes_trend = analyze_performance(historical_df)

def generate_recommendations(score, accuracy, mistakes):
    recommendations = []
    if accuracy < 0.7:
        recommendations.append("Work on accuracy. Consider revising weak areas.")
    if mistakes > 5:
        recommendations.append("Reduce mistakes by reviewing incorrect answers carefully.")
    if score < 50:
        recommendations.append("Improve your overall score by focusing on high-weightage topics.")
    return recommendations

recommendations = generate_recommendations(score_trend, accuracy_trend, mistakes_trend)

user_input = input("Do you want to enter custom performance values? (yes/no): ").strip().lower()
if user_input == "yes":
    score_trend = float(input("Enter your average score: "))
    accuracy_trend = float(input("Enter your accuracy (0-1, e.g., 0.75 for 75%): "))
    mistakes_trend = int(input("Enter your average number of mistakes: "))

recommendations = generate_recommendations(score_trend, accuracy_trend, mistakes_trend)

print("\nPersonalized Recommendations:")
for rec in recommendations:
    print("- " + rec)

unique_students = historical_df["user_id"].nunique()
print(f"Number of unique students: {unique_students}")

plt.figure(figsize=(8, 5))
sns.barplot(x=["Score", "Accuracy", "Mistakes"], y=[score_trend, accuracy_trend, mistakes_trend])
plt.title("Performance Trends")
plt.ylabel("Value")
plt.show()

accuracy_bins = ['Low (<50%)', 'Medium (50-70%)', 'High (>70%)']
accuracy_counts = [
    len(historical_df[historical_df['accuracy'] < 0.5]),
    len(historical_df[(historical_df['accuracy'] >= 0.5) & (historical_df['accuracy'] < 0.7)]),
    len(historical_df[historical_df['accuracy'] >= 0.7])
]
plt.figure(figsize=(7, 7))
plt.pie(accuracy_counts, labels=accuracy_bins, autopct='%1.1f%%', startangle=90)
plt.title("Accuracy Distribution")
plt.axis('equal')
plt.show()

correlation_matrix = historical_df[['score', 'accuracy', 'correct_answers', 'incorrect_answers', 'negative_score', 'speed']].corr()
plt.figure(figsize=(8, 5))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title("Correlation Matrix of Performance Metrics")
plt.show()

plt.figure(figsize=(8, 5))
sns.histplot(historical_df['score'], kde=True, color='purple', bins=20)
plt.title("Score Distribution")
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

features = ['accuracy', 'speed', 'score', 'incorrect_answers']

scaler = StandardScaler()
student_data = historical_df[features]

student_data_scaled = scaler.fit_transform(student_data)

kmeans = KMeans(n_clusters=3, random_state=42)
historical_df['Cluster'] = kmeans.fit_predict(student_data_scaled)

plt.figure(figsize=(8, 5))
sns.scatterplot(x='accuracy', y='score', hue='Cluster', data=historical_df, palette='viridis', s=100, alpha=0.7)
plt.title("Clusters of Students Based on Accuracy and Score")
plt.xlabel("Accuracy")
plt.ylabel("Score")
plt.legend(title="Student Persona")
plt.show()

personas = {
    0: "The Fast Learner - Quick to Answer, but Needs Focus on Accuracy",
    1: "The Careful Thinker - Accuracy is Strong, but Needs to Improve Speed",
    2: "The Balanced Performer - Good Accuracy and Speed, Needs Consistency"
}

historical_df['Persona'] = historical_df['Cluster'].map(personas)

persona_summary = historical_df.groupby('Persona').agg({
    'accuracy': ['mean', 'std'],
    'speed': ['mean', 'std'],
    'score': ['mean', 'std'],
    'incorrect_answers': ['mean', 'std']
}).reset_index()

print(persona_summary)

def generate_creative_labels(persona_summary):
    insights = []
    for idx, row in persona_summary.iterrows():
        persona = row[('Persona', '')]

        accuracy_mean = row[('accuracy', 'mean')]
        speed_mean = row[('speed', 'mean')]
        score_mean = row[('score', 'mean')]
        incorrect_mean = row[('incorrect_answers', 'mean')]
        if persona == "The Fast Learner - Quick to Answer, but Needs Focus on Accuracy":
            if accuracy_mean < 0.6:
                insights.append(f"{persona}: Try focusing more on accuracy. Speed is your strength, but accuracy needs attention!")
            else:
                insights.append(f"{persona}: Excellent at speed! Consider balancing it with targeted practice to maintain accuracy.")

        elif persona == "The Careful Thinker - Accuracy is Strong, but Needs to Improve Speed":
            if speed_mean < 1.0:
                insights.append(f"{persona}: Your accuracy is impressive! Work on increasing your speed to improve efficiency.")
            else:
                insights.append(f"{persona}: Great accuracy! However, focus on improving time management for better speed.")

        elif persona == "The Balanced Performer - Good Accuracy and Speed, Needs Consistency":
            if score_mean > 70:
                insights.append(f"{persona}: Keep up the good work! You’re excelling in both speed and accuracy. Aim for consistent performance.")
            else:
                insights.append(f"{persona}: You have a great balance, but work on reducing mistakes for an overall better score.")

    return insights
creative_labels = generate_creative_labels(persona_summary)

for label in creative_labels:
    print(label)

def predict_neet_rank(user_id):
    user_scores = historical_df[historical_df["user_id"] == user_id]["score"]

    if user_scores.empty:
        return "No data available for this user."

    avg_score = np.mean(user_scores)
    estimated_rank = max(1, int((720 - avg_score) * 5000 / 720))
    return estimated_rank
user_id = "YcDFSO4ZukTJnnFMgRNVwZTE4j42"
print(f"Estimated NEET rank for user {user_id}: {predict_neet_rank(user_id)}")

