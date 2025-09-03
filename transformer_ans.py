import pandas as pd
from transformers import BertTokenizer, BertModel
from sklearn.svm import SVC
import torch

# Load data
df = pd.read_csv("cardio.csv", encoding='latin-1')

# Load pre-trained BERT tokenizer and model
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
bert_model = BertModel.from_pretrained('bert-base-uncased')

# Encode questions using BERT
encoded_questions = []
for question in df['Question']:
    inputs = tokenizer(question, return_tensors="pt", max_length=512, truncation=True, padding=True)
    with torch.no_grad():
        outputs = bert_model(**inputs)
    encoded_question = torch.mean(outputs.last_hidden_state, dim=1).squeeze().numpy()
    encoded_questions.append(encoded_question)
encoded_questions = torch.tensor(encoded_questions)

# Initialize SVM classifier
svm = SVC(kernel='linear')
svm.fit(encoded_questions, df['Answer'])

def add_new_rows(new_ques_ans, df):
    df = df.append(new_ques_ans, ignore_index=True)
    df.to_csv('cardio.csv', index=False)
    return pd.read_csv('cardio.csv')


feedback_data = []

def transformer_response(input_question):
    inputs = tokenizer(input_question, return_tensors="pt", max_length=512, truncation=True, padding=True)
    with torch.no_grad():
        outputs = bert_model(**inputs)
    encoded_input = torch.mean(outputs.last_hidden_state, dim=1).squeeze().numpy()
    
    #get decision values of the answers
    decision_values = svm.decision_function([encoded_input])[0]

    threshold_values = 0.4
    
    if max(decision_values) >= threshold_values:
        return svm.classes_[decision_values.argmax()]
        #print(f"Chatbot: {predicted_answer}")
    
    else:
        print("Chatbot: Sorry, I am not sure about this. Maybe try again after restarting or help me learn it.")
        
    # Predict answer using SVM classifier
    #predicted_answer = svm.predict([encoded_input])[0]
    
    
    
def feedback_loop(ques, ans):
    # Load existing dataset
    df = pd.read_csv('cardio.csv')
    
    # Create a new row for the corrected question and answer
    new_ques_ans = {"Question": ques, "Answer": ans}
    
    # Append the new question and answer to the dataset
    df = df.append(new_ques_ans, ignore_index=True)
    
    # Save the updated dataset
    df.to_csv('cardio.csv', index=False)
