# Enhancing-Web-Data-with-LSTMFramework-for-User-Centric-Noise-Reduction
This project aims to improve the quality of web-scraped data by using an LSTM-based Machine Learning model to dynamically remove noise such as advertisements, banners, and irrelevant links.
It offers a simple web-based interface (using Streamlit) where users can log in, input a website URL, scrape the content, clean it, and download the enhanced text.

🚀 Features:
🔒 User Login and Sign-Up
🌐 Web scraping of real-time webpage data
🧹 Dynamic Noise Reduction using LSTM model
📄 Downloadable Cleaned Content
📊 Modern UI with easy navigation (Login, Signup, Dashboard)

🛠 Technologies Used:
Python 3.8+,
Streamlit (Frontend and Web App framework),
BeautifulSoup4 (Web Scraping),
NLTK (Text Tokenization),
TensorFlow (LSTM Model),
Scikit-learn (Data preprocessing),
Pickle (Model serialization).

📦 Installation:

1) Clone the repository:
- git clone https://github.com/your-username/your-repository-name.git
- cd your-repository-name

2) Create a virtual environment (recommended):
- python -m venv venv
- source venv/bin/activate   # On Windows: venv\Scripts\activate

3) Install dependencies:
- pip install -r requirements.txt

4) Run the Streamlit app:
- streamlit run app.py
