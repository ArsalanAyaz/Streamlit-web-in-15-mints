import streamlit as st

# Create a homepage
st.title("Welcome to My Website")
st.header("About Me")
st.write("""
    Hello! I am a Python developer, and this is a simple website built using Streamlit. 
    You can customize this with more information about yourself.
""")

# Contact section
st.header("Contact")
st.write("""
    You can reach me at:
    - Email: example@example.com
    - Phone: 123-456-7890
""")

# Form for user input
st.header("Leave a Message")
name = st.text_input("Enter your name:")
message = st.text_area("Enter your message:")

if st.button("Submit"):
    st.write(f"Thank you for your message, {name}!")