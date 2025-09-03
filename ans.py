import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

df = pd.read_csv("cardio.csv",encoding='latin-1')
#initializing tfidf vectorizer
vec = TfidfVectorizer()
vec.fit(np.concatenate((df['Question'],df['Answer'])))

#number of token/keywords generated from the dataset
feature_col = vec.get_feature_names()
#len(feature_col)
#973 keywords are generated from this 

df_vec = vec.transform(df['Question'])

def querry_answer(input_question):    
    input_question_vec = vec.transform([input_question])
    similarity = cosine_similarity(input_question_vec,df_vec)
    closest_ans = np.argmax(similarity,axis=1)
    return df['Answer'].iloc[closest_ans].values[0]
    #print(f"Response from chatbot is: {df['Answer'].iloc[closest_ans].values[0]}")

# Function to update the dataset based on user feedback
def feedback_loop(new_question, new_answer):
    new_df = pd.read_csv("cardio.csv",encoding='latin-1')
    new_df = new_df.append({'Question': new_question, 'Answer': new_answer}, ignore_index=True)
    new_df.to_csv('cardio.csv', index=False)


