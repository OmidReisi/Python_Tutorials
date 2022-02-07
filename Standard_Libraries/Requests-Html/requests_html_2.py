from requests_html import HTML

with open(r"./simple.html", "r") as html_file:

    source = html_file.read()
    html = HTML(html=source)

# just like html object you can navigate through your element object
articles = html.find("div.article")
for article in articles:
    headline = article.find("h2", first=True)
    summary = article.find("p", first=True)
    print(headline.text)
    print(summary.text)
    print()
