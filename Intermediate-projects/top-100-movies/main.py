import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

data = requests.get(URL).text

soup = BeautifulSoup(data, "html.parser")

raw_movies_titles = soup.find_all(name="h3", class_="title")
movies_titles = [i.getText() for i in raw_movies_titles][::-1]

with open("movies.txt", "w") as file:
    for movie in movies_titles:
        file.write(f"\n{movie}")
