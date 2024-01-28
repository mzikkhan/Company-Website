import streamlit as st
from send_email import send_email
import pandas as pd

st.header("Contact Me")

df = pd.read_csv('topics.csv')

with st.form(key="email_form"):
    user_email = st.text_input("Your Email Address: ")
    topic = st.selectbox('What topic do you want to discuss?',
                         df['topic'])
    raw_message = st.text_area("Text: ")
    message = f"""
Subject: New email from {user_email}
From: {user_email}
Topic: {topic}
{raw_message}"""
    button = st.form_submit_button()
    if button:
        send_email(message)
        st.info("Your email was sent successfully!")
        