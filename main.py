import streamlit as st
import re
from google.generativeai import GenerativeModel
import google.generativeai as genai


def make_bold(text):
    """Converts text within double asterisks to bold HTML format."""
    pattern = r"\*\*(.*?)\*\*"
    return re.sub(pattern, r"<b>\1</b>", text)


class GeminiFarmingQA:
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        self.model = GenerativeModel('gemini-pro')

    def get_farming_answer(self, question: str) -> str:
        """Gets farming-related answers using Gemini API."""
        prompt = f"""
        As a farming expert, please provide practical advice for the following question:
        {question}

        Focus on providing:
        - Clear, actionable steps
        - Practical solutions
        - Relevant farming context
        """

        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Sorry, couldn't process your question. Error: {str(e)}"


def main():
    st.title("Rajendra GPT")

    # Sidebar for navigation
    st.sidebar.title("Navigation")
    option = st.sidebar.selectbox("Choose an option", ["Start New Chat", "View Previous Searches"])

    if option == "Start New Chat":
        # Initialize the GeminiFarmingQA object
        gemini_qa = GeminiFarmingQA(api_key="AIzaSyApr1pUs4lfuODKeiiUFJi_gFQns4DdBYg")  # Replace with your actual API key

        # Get user input for the question
        question = st.text_input("Enter your question:")

        if st.button("Send"):
            if question:
                # Get the answer from Gemini API and apply bolding
                answer = gemini_qa.get_farming_answer(question)
                bolded_answer = make_bold(answer)

                # Display the answer in the viewer area
                st.markdown("### Answer:")
                st.markdown(bolded_answer, unsafe_allow_html=True)
            else:
                st.warning("Please enter a question.")

    elif option == "View Previous Searches":
        # Placeholder for previous searches functionality
        st.write("This feature is under development. Please check back later.")


if __name__ == "__main__":
    main()