# 💼 Job Scraper Streamlit App

## 🚀 Overview
This is a simple **Streamlit web application** that scrapes job listings from a demo website and displays them in an interactive dashboard. The project demonstrates web scraping, data extraction, and UI development using Python.

## ✨ Features
- Scrapes job title, company, and location
- Displays results in an interactive table
- One-click scraping using Streamlit button
- Download scraped data as CSV
- Clean and beginner-friendly UI

## 🛠️ Tech Stack
- Python
- Streamlit
- BeautifulSoup4
- Requests
- Pandas

## 📁 Project Structure
job-scraper-streamlit/
├── app.py              
├── scraper.py          
├── requirements.txt    
├── README.md           
└── .gitignore          

## 🌐 Data Source
https://realpython.github.io/fake-jobs/

## ⚙️ Installation & Setup

### 1. Clone the repository
git clone https://github.com/your-username/job-scraper-streamlit.git
cd job-scraper-streamlit

### 2. Create virtual environment (optional but recommended)
python -m venv venv

Activate it:

Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

### 3. Install dependencies
pip install -r requirements.txt

### 4. Run the Streamlit app
streamlit run app.py

### 5. Open in browser
After running, open:
http://localhost:8501

## 🎯 How to Use
1. Click "Scrape Jobs" button
2. Wait for data to load
3. View results in table format
4. Download CSV file

## 📊 Output
- Job Title
- Company Name
- Location
- Downloadable CSV file

## ⚠️ Requirements
- Python 3.7+
- Internet connection required
- Streamlit installed via requirements.txt
- Proper `.gitignore` to avoid unnecessary files

## 🚀 Future Improvements
- Add search and filters (job title, company, location)
- Add charts and analytics dashboard
- Deploy on Streamlit Cloud (live project link)
- Extend scraper to multiple websites
