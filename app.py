import streamlit as st
import pandas as pd
from scraper import scrape_jobs

st.set_page_config(page_title="Job Scraper App", layout="wide")

st.title("💼 Job Scraper Dashboard")
st.write("Scrape job listings from a demo website and view them instantly.")

if st.button("🔍 Scrape Jobs"):
    with st.spinner("Scraping jobs... please wait"):
        data = scrape_jobs()

    if data:
        df = pd.DataFrame(data, columns=["Title", "Company", "Location"])

        st.success(f"Total Jobs Found: {len(df)}")

        st.dataframe(df)

        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Download CSV",
            data=csv,
            file_name="jobs.csv",
            mime="text/csv"
        )
    else:
        st.error("Failed to fetch jobs.")