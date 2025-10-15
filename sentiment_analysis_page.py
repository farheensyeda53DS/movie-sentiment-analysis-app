# sentiment_analysis_page.py
import streamlit as st
import joblib
import matplotlib.pyplot as plt

# Load the trained model and vectorizer
model = joblib.load('sentiment_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

def sentiment_analysis_page():
    st.title("Sentiment Analysis App")
    st.write("This app predicts whether a given review is **positive** or **negative** and shows sentiment percentages.")

    # Text input
    review_text = st.text_area("Enter a review:", "")

    # Submit Button
    if st.button("Submit"):
        if review_text.strip():  # Check if text is not empty
            # Predict sentiment and probabilities
            review_vectorized = vectorizer.transform([review_text])
            probabilities = model.predict_proba(review_vectorized)[0]
            sentiment_percentages = {
                "Positive Sentiment": probabilities[1] * 100,
                "Negative Sentiment": probabilities[0] * 100
            }
            predicted_label = "Positive" if probabilities[1] > probabilities[0] else "Negative"

            # Highlight result
            if predicted_label == "Positive":
                st.success(f"Sentiment: **{predicted_label}**")
            else:
                st.error(f"Sentiment: **{predicted_label}**")

            # Display percentages
            st.write(f"**Positive Sentiment:** {sentiment_percentages['Positive Sentiment']:.2f}%")
            st.write(f"**Negative Sentiment:** {sentiment_percentages['Negative Sentiment']:.2f}%")

            # Pie chart
            labels = ['Positive Sentiment', 'Negative Sentiment']
            sizes = [sentiment_percentages['Positive Sentiment'], sentiment_percentages['Negative Sentiment']]
            colors = ['lightgreen', 'pink']

            fig, ax = plt.subplots()
            ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
            ax.axis('equal')  # Equal aspect ratio ensures the pie is drawn as a circle.
            plt.title("Sentiment Distribution")

            # Display the pie chart
            st.pyplot(fig)
        else:
            st.warning("Please enter some text for analysis!")
