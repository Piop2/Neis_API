import requests
from bs4 import BeautifulSoup
from KSchool.website_crawl.get import get_school_website_link
from KSchool.website_crawl.get import crawl_website


class Letters:
    """
    학교 사이트 크롤링으로 가정통신문이나 공지사항을 받아옵니다.
    메인화면 가정통신문, 공지사항으로 가는 바로가기 버튼이 없을경우 받아오는 것이 원할하지 않을 수 있습니다.
    """
    def __init__(self, school_name: str) -> None:
        self.school_link = get_school_website_link(school_name=school_name)
        self.letter_link = ""
        self.notification_link = ""
        self.exception_pass = False


    def get_letter_link(self, get_letters: bool = True, get_notifications: bool = False) -> str:
        """
        가정통신문/공지사항 사이트의 링크를 받아오는 함수

        :param get_letters: 가정통신문을 받아을지의 여부
        :param get_notifications: 공지사항을 받아을지의 여부
        :return: str
        """
        self.get_letters = get_letters
        self.get_notifications = get_notifications
        self.soup = crawl_website(self.school_link)
        self.links = self.soup.select('a')
        if get_letters:
            for link in self.links:
                if ("가정" and "통신") in link.get_text():
                    self.letter_link = link['href']
                    break
        if get_notifications:
            for link in self.links:
                if ("공지" and "사항") in link.get_text():
                    self.notification_link = link['href']
                    break
        if not self.exception_pass:
            self.link_exceptions()
        if self.get_letters:
            if self.get_notifications:
                return [self.letter_link, self.notification_link]
            else:
                return self.letter_link
        elif self.get_notifications:
            return self.notification_link
        else:
            return ""


    def link_exceptions(self) -> None:
        """
        링크 예외 처리 함수(전국의 모든? 학교들에 맞춰 예외를 처리할 예정)
        get_letter_link 함수에 귀속

        :return:
        """
        if (self.letter_link or self.notification_link).startswith("/" + self.school_link.split("/")[-1]): #충청복도학교통합홈페이지 예외 처리
            self.letter_link = self.letter_link[len(self.school_link.split("/")[-1]):]
        if self.soup.select('a') == []: #아직 문제 많은 예외처리(학교 사이트들 다 왜이래)
            self.school_link += "main.do"
            self.exception_pass = True
            self.get_letter_link(self.get_letters, self.get_notifications)
            self.school_link = self.school_link.replace("main.do", "")
        if "http" in self.letter_link:
            pass
        else:
            self.letter_link = self.school_link[:-1] + self.letter_link
        if "http" in self.notification_link:
            pass
        else:
            self.notification_link = self.school_link[:-1] + self.notification_link


    def get_letter_titles(self) -> list:
        """
        가정통신문이나 공지사항들의 제목들을 받아오는 함수

        :return: list
        """
        if (self.letter_link and self.notification_link) == "":
            self.letter_link = self.get_letter_link()
        self.content = requests.get(self.school_link + "dggb/module/board/selectBoardListAjax.do", headers={"Referer": self.letter_link}, cookies={"WMONID": "5IO1s4GUsr5", "JSESSIONID": "0ajWJnhY0BzFNN8aLEGKvzIUoIaVY4HgTiVI25zJ8g1BGwyA7n8Zvne1ZL2Tq1Lu.hostingwas1_servlet_engine4"})
        self.soup = BeautifulSoup(self.content.content, 'html.parser')
        print(self.soup.prettify())