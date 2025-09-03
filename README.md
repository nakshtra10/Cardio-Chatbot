# Cardiovascular Chatbot with Heart Disease Prediction

Welcome to the GitHub repository for our Cardiovascular Chatbot! This project integrates a chatbot that answers basic queries related to heart health and includes a prediction model to assess your risk of heart disease. Here's an overview of the project and how to run it.

### Features

- **Chatbot Functionality**: Answers basic queries related to cardiovascular health using TF-IDF and cosine similarity for relevance.
- **Heart Disease Prediction**: Uses a random forest classifier to predict the risk of heart disease based on user input data.
- **User-Friendly UI**: Implemented with Streamlit for easy interaction and visualization.
- **Feedback Loop**: Enhances data over time with user feedback to improve response accuracy.
- **Data Handling**: Utilizes numpy and pandas for efficient CSV data access and manipulation.

### Technologies and Algorithms Used

- **Programming Languages**: Python
- **Machine Learning**: Random Forest Classifier
- **Natural Language Processing**: TF-IDF (Term Frequency-Inverse Document Frequency), Cosine Similarity
- **Web Framework**: Streamlit
- **Data Handling**: numpy, pandas

### How to Run

To run the Cardiovascular Chatbot and Prediction Model locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/cardiovascular-chatbot.git
   cd cardiovascular-chatbot
   ```

2. **Install Dependencies**:
   Ensure you have Python 3.x installed. Install required libraries using pip:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**:
   Start the Streamlit application:
   ```bash
   streamlit run app.py
   ```

4. **Interact with the Chatbot**:
   - Open your web browser and navigate to `http://localhost:8501`.
   - You'll see the user-friendly UI where you can interact with the chatbot.
   - Enter queries related to heart health and receive answers based on TF-IDF and cosine similarity.
   - Provide feedback to improve the chatbot's responses over time.

### Contributing

We welcome contributions to improve the chatbot's functionality, expand the prediction model, or enhance the user interface. Please fork the repository, make your changes, and submit a pull request. Let's work together to make cardiovascular health information more accessible and accurate!

### License

This project is licensed under the MIT License - see the `LICENSE` file for details.

### Contact

For any questions or feedback, please contact us at raghavendra.bhargava2004@gmail.com.

Enjoy using the Cardiovascular Chatbot and stay heart-healthy! 🫀
