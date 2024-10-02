import google.generativeai as genai
from IPython.display import Markdown, clear_output, display
API_KEY = 'AIzaSyAUlD-Dg3Oy4pIW3frhoSRbr-aoXHkTP_Q'
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel(model_name='gemini-1.5-flash')

import streamlit as st
import google.generativeai as genai
from IPython.display import Markdown, clear_output, display

# Initialize Streamlit app
st.title("Personalized Learning Plan Generator")

# Get user inputs
student_name = st.text_input("Enter your name:")
learning_style = st.selectbox("Select your preferred learning style:", ["Visual", "Auditory", "Kinesthetic", "Reading/Writing"])
course_name = st.text_input("Enter the course name:")
course_duration = st.number_input("Enter the desired course duration (in weeks):", min_value=1, max_value=52, value=1)

# Generate personalized learning plan based on user inputs
if st.button("Generate Learning Plan"):
    prompt = f"""
    Create a personalized learning plan for {student_name} learning {course_name} for {course_duration} weeks. 
    The student's preferred learning style is {learning_style}. 
    The plan should include:
    1. Course description.
    2. Related course recommendations divided by difficulty levels (beginner, intermediate, advanced).
    3. A short quiz on the course with a performance analysis at the end.
    """
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel(model_name='gemini-1.5-flash')
    response = model.generate_content(prompt)
    st.write(response.text)
st.header("Ask Your Doubts")
doubt = st.text_area("Enter your doubt:")
if st.button("Get Answer"):
    prompt = f"""
    Answer the following question about {course_name}:
    {doubt} 
    """
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel(model_name='gemini-1.5-flash')
    response = model.generate_content(prompt)
    st.write(response.text)