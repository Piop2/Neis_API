import requests
from bs4 import BeautifulSoup
from Neis_API.service.info import get_school_website_link


class letters_to_parents:
    def __init__(self, school_name: str) -> None:
        self.school_link = get_school_website_link(school_name=school_name)

    def get_letters_title(self) -> list:
        self.letter_titles = []
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
        html = requests.get(f"{self.school_link}", headers=headers)
        soup = BeautifulSoup(html.content, "html.parser").prettify()
        mainpage_result = soup.split('\n')
        return mainpage_result