import streamlit as st
import pickle
import requests
from bs4 import BeautifulSoup
import re
import nltk
from nltk.tokenize import sent_tokenize

# Download NLTK resources
nltk.download('punkt')

# Load the LSTM model and tokenizer
@st.cache_resource
def load_model_and_tokenizer():
    with open('lstm_model.pkl', 'rb') as f:
        model = pickle.load(f)
    with open('tokenizer.pkl', 'rb') as f:
        tokenizer = pickle.load(f)
    return model, tokenizer

model, tokenizer = load_model_and_tokenizer()

# Dummy cleaning function (you can enhance it using model predictions later)
def clean_text(text):
    cleaned = re.sub(r'\s+', ' ', text)
    sentences = sent_tokenize(cleaned)
    cleaned_text = '\n\n'.join(sentences)
    return cleaned_text

# Scrape website content
def scrape_website(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        for tag in soup(['script', 'style', 'iframe', 'nav', 'footer', 'header', 'aside', 
                         'form', 'noscript', 'table', 'ul', 'ol', 'menu', 'button', 'svg', 
                         'figure', 'input', 'img', 'label', 'span', 'meta', 'link']):
            tag.extract()
        paragraphs = soup.find_all('p')
        extracted_text = '\n\n'.join([para.get_text() for para in paragraphs])
        return extracted_text
    except Exception as e:
        return f"⚠️ Scraping failed: {str(e)}"

# Dummy user database
user_db = {
    "admin": "admin123"
}

# Login Page
def login_page():
    st.title("🔐 Login to Web Content Enhancer")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login_btn = st.button("Login")
    if login_btn:
        if username in user_db and user_db[username] == password:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success("Login Successful!")
        else:
            st.error("Invalid username or password.")

# Sign Up Page
def signup_page():
    st.title("📝 Create New Account")
    new_username = st.text_input("Create Username")
    new_password = st.text_input("Create Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")
    signup_btn = st.button("Sign Up")
    if signup_btn:
        if new_username in user_db:
            st.error("Username already exists!")
        elif new_password != confirm_password:
            st.error("Passwords do not match!")
        else:
            user_db[new_username] = new_password
            st.success("Account created successfully!")

# Dashboard Page
def dashboard_page():
    st.title(f"📋 Dashboard - Welcome {st.session_state.username}")

    url = st.text_input("Enter Website URL")
    if st.button("Scrape & Clean"):
        if url:
            scraped_text = scrape_website(url)
            cleaned_text = clean_text(scraped_text)
            st.success("Extraction & Cleaning Successful!")
            st.subheader("📝 Cleaned Content")
            st.write(cleaned_text)
            st.download_button("Download Cleaned Content", cleaned_text, file_name="cleaned_content.txt")
        else:
            st.error("Please enter a valid URL.")

    if st.button("Logout"):
        st.session_state.logged_in = False

# Navigation Controller
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Login", "Sign Up", "Dashboard"])

    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False

    if page == "Login":
        login_page()
    elif page == "Sign Up":
        signup_page()
    elif page == "Dashboard":
        if st.session_state.logged_in:
            dashboard_page()
        else:
            st.warning("Please login first.")

if __name__ == "__main__":
    main()
