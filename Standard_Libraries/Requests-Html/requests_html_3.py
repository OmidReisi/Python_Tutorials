from requests_html import HTML, HTMLSession
import csv

session = HTMLSession()

# this is a response same as the response we get from the requests library
r = session.get(r"https://coreyms.com/")

# this is same as the html object that we created before with HTML class
# print(r.html)


articles = r.html.find("article")

with open(r"./cms_scrape.csv", "w", newline="", encoding="utf-8") as csv_file:

    csv_writer = csv.DictWriter(csv_file, fieldnames=["Headline", "Summary", "Link"])
    csv_writer.writeheader()

    for article in articles:

        # always use try/except blocks when scraping websites because some data might be missing
        try:
            headline = article.find(".entry-title", first=True).text
            summary = article.find(".entry-content p", first=True).text

            # attrs returns a dictionary that contains the attributes for the given html element(tag)
            vid_src = article.find("iframe", first=True).attrs.get("src")
            vid_id = vid_src.split("?")[0].split("/")[-1]

            yt_link = rf"https://youtube.com/watch?v={vid_id}"

        except Exception as e:
            yt_link = None

        csv_writer.writerow({"Headline": headline, "Summary": summary, "Link": yt_link})
