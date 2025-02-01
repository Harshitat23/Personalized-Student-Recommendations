# Personalized-Student-Recommendations
A Python-based analysis tool that evaluates quiz performance from NEET Testline app, predicting valuable insights, personalized recommendations, and rank prediction of students.


# PROJECT OVERVIEW

This project analyzes quiz performance data from the NEET Testline app to provide personalized student recommendations. By evaluating quiz responses, historical performance trends, and topic-wise accuracy, it generates insights to help students improve their preparation. Additionally, a probabilistic model predicts a student's estimated NEET rank based on past quiz performance and previous years' NEET results.

# FEATURES

1) Data Analysis: Extracts patterns in student performance, including weak areas, strengths, and improvement trends.

2) Personalized Recommendations: Suggests specific topics, question types, and difficulty levels for improvement.

3) Student Persona Analysis: Identifies learning styles, key strengths, and potential problem areas.

4) Rank Prediction Model: Uses historical performance and statistical modeling to estimate a student’s potential NEET rank.

# Approach

1. Data Analysis
Extract quiz responses, topic distributions, and difficulty levels.

2. Recommendations
Recommend according to the performance, suggestions are being povided.

4. Student Persona Profiling
Classify students into personas based on accuracy and consistency.
Example personas: "The Fast Learner" ,"The Careful Thinker"," "The Balanced Performer".

5. NEET Rank Prediction
A probabilistic model using quiz scores.
Predict estimated ranks based on quiz performance trends.

# Visualisations - 

![image](https://github.com/user-attachments/assets/1d3600de-7bf7-4594-a3f6-86baf2a6fb72)

Here, it can be seen that comparison of three performance metrics: Score, Accuracy, and Mistakes.
-> Score has the highest value, Accuracy is represented with a lower value, indicating a moderate level of correctness, Mistakes have a small but visible value, suggesting some errors were made.
-> The graph highlights the dominance of the score metric.

![image](https://github.com/user-attachments/assets/186c364a-b6cd-4858-b4a9-983ac191854b)

The pie chart shows "Accuracy Distribution", proportion of different accuracy levels among historical data
-> High (>70%): Representing the majority at 57.1%, indicating most instances achieved high accuracy.
-> Low (<50%): Comprising 28.6%, showing a considerable number of instances with low accuracy.
-> Medium (50-70%): The smallest segment at 14.3%, reflecting fewer instances with medium accuracy.
The chart visually emphasizes that over half of the cases had high accuracy, while medium accuracy is the least frequent.

![image](https://github.com/user-attachments/assets/821683f7-b419-4fb5-a14d-80544337b6c7)

The histogram titled "Score Distribution" shows the frequency of scores.
-> Scores around 40 have the highest frequency.
-> A smaller peak is visible near 120, suggesting some high-scoring instances.
-> The distribution is somewhat spread out, with scores ranging from below 20 to above 100.

![image](https://github.com/user-attachments/assets/76c39bfa-8520-4e35-b4b6-5ed6ff2f9d84)

This heatmap indicates that the key areas for improvement of student performance are such as reducing incorrect answers to boost accuracy and overall score.

# Student Persona
![image](https://github.com/user-attachments/assets/70d4dad0-fa2c-498e-8f6d-1f9d79cb52bc)

Here, clustering of students is done into three distinct personas based on accuracy, speed, and score:

The Fast Learner (Cluster 0)
Quick response time but lower accuracy.
Strength: Speed and agility in answering.
Weakness: Needs to improve precision to boost overall performance.

The Careful Thinker (Cluster 1)
High accuracy but slower response times.
Strength: Strong understanding and careful decision-making.
Weakness: Needs to increase speed to optimize performance.

The Balanced Performer (Cluster 2)
Well-rounded with good accuracy and speed.
Strength: Consistency across metrics.
Weakness: Needs slight improvements in stability to maximize results.

This segmentation helps tailor strategies like, accuracy drills for fast learners, speed training for careful thinkers, and consistency-building exercises for balanced performers.
