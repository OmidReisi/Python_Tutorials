import requests
from bs4 import BeautifulSoup
import csv


source = requests.get(r"https://coreyms.com/").text


soup = BeautifulSoup(source, "lxml")

# the select method allows us to use css selectors to get our tags (like find_all returns a list)
articles = soup.select("article:not(.post-1655)")
with open(r"./cms_scrape.csv", "w", newline="", encoding="utf-8") as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=["Headline", "Summary", "Link"])
    csv_writer.writeheader()

    # it's better to add your scraping to a try except block so that even if the website is missing data the script keeps going and doesn't terminate on an exception
    for article in articles:
        try:
            headline = article.h2.a.text
        except Exception:
            headline = None
        try:
            summary = article.find("div", class_="entry-content").p.text
        except Exception:
            summary = None
        try:
            vid_code = (
                article.find("iframe", class_="youtube-player")
                .get("src")
                .split("/")[-1]
                .split("?")[0]
            )
            yt_link = f"https://youtube.com/watch?v={vid_code}"
        except Exception:
            yt_link = None

        csv_writer.writerow({"Headline": headline, "Summary": summary, "Link": yt_link})
