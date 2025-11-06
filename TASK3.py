import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
df=pd.read_csv(r"C:\Users\priya\OneDrive\Desktop\archive (2)\student_feedback.csv")
print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())
df['Average_Score']=df[['Well versed with the subject','Explains concepts in an understandable way','Use of presentations','Degree of difficulty of assignments','Solves doubts willingly','Structuring of the course','Provides support for students going above and beyond','Course recommendation based on relevance']].mean(axis=1)
print(df['Average_Score'].head(5))
def get_sentiment(score):
    if score > 6.0:
        return 'Positive'
    elif score < 4.0:
        return 'Negative'
    else:
        return 'Netural'
df['Sentiment'] = df['Average_Score'].apply(get_sentiment)
df['Sentiment'].value_counts().plot(kind='bar',color=['green','red','yellow'])
plt.title("Sentiment Analysis")
plt.ylabel("No of feedbacks")
plt.show()

