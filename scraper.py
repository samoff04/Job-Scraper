import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"

def scrape_jobs():
    try:
        response = requests.get(URL)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    jobs = soup.select(".card-content")

    job_list = []

    for job in jobs:
        title = job.select_one("h2").text.strip()
        company = job.select_one("h3").text.strip()
        location = job.select_one(".location").text.strip()

        job_list.append([title, company, location])

    return job_list