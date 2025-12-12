import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/news")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

articles = soup.find_all(name="span", class_="titleline")
article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.find("a").getText()
    article_texts.append(text)
    link = article_tag.find("a").get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

max_score_index = article_upvotes.index(max(article_upvotes))
print(article_texts[max_score_index])
print(article_links[max_score_index])