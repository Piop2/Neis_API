import requests
from bs4 import BeautifulSoup
from Neis_API.service.info import get_school_website_link
from Neis_API.service.request import crawl_website


class letters_to_parents:
    def __init__(self, school_name: str) -> None:
        self.school_link = get_school_website_link(school_name=school_name)

    def get_letter_link(self) -> str:
        self.letter_link = ""
        self.soup = crawl_website(self.school_link)
        self.links = self.soup.select('a')
        for link in self.links:
            if link.get_text() == "가정통신문":
                self.letter_link = link['href']
                break
        if "http" in self.letter_link:
            pass
        else:
            self.letter_link = self.school_link[:-1] + self.letter_link
        return self.letter_link
