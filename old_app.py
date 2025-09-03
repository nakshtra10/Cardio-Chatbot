import streamlit as st
from ans import querry_answer,feedback_loop
import time
from new_pred import show_pp

st.set_page_config(page_title="Rxghav's HealthCare Chatbot")
st.title("HeartBot v1.0")
st.write('This chatbot is created to answer questions and querries related to heart and the diseases associated with it. We have used pre trained BERT and tuned it to answer the questions correctly and classfiy using SVM Classifier Algorithm')

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

def clear_chat_history():
    st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]
st.button('Clear Chat History', on_click=clear_chat_history)


# Options dropdown for regular chat or providing feedback
option = st.selectbox("Choose an option:", ["Chat Mode","Prediction Mode" ,"Feedback Mode"])

if option == "Chat Mode":
    # React to user input
    if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
        prompt_new = f"User: {prompt}"
        st.chat_message("user").markdown(prompt_new)
    # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

    def response_generator():
        response = f"HeartBot: {querry_answer(prompt)}"
        for word in response.split():
            yield word + " "
            time.sleep(0.05)
    # Display assistant response in chat message container and slowly print using the typewriter effect to mimic real chat
    with st.chat_message("assistant"):
        response = st.write_stream(response_generator())

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

elif option == "Prediction Mode":
    show_pp()

else:
    new_ques = st.text_input("Enter the Corrected Question:")
    new_ans = st.text_input("Enter the Corrected Answer:")
    if st.button("Submit Feedback"):
        feedback_loop(new_ques, new_ans)
        st.success("Thank you for adding on to the dataset.")