from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
soup = BeautifulSoup(response.text, "html.parser")
all_movie_details = soup.select(".article-title-description__text h3.title")
all_movie_details = all_movie_details[::-1]
movie_titles = [title.getText().replace(")", ".").replace("â\x80\x93", "-") for title in all_movie_details]
file = open("movies.txt")
if len(file.readlines()) >= 1:
    file.close()
    file = open("movies.txt", mode="w")
else:
    file.close()
    file = open("movies.txt", mode="a")
for movie in movie_titles:
    file.write(f"{movie}\n")
file.close()
