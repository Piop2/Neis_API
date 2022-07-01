import requests
import urllib3, ssl
from bs4 import BeautifulSoup


def crawl_website(url: str) -> BeautifulSoup:
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
        html = requests.get(str(url), headers=headers, allow_redirects=True)
        content = BeautifulSoup(html.content, "html.parser")
    except:
        ctx = ssl.create_default_context()
        ctx.set_ciphers('DEFAULT@SECLEVEL=1')
        http = urllib3.PoolManager(ssl_version=ssl.PROTOCOL_TLS, ssl_context=ctx)
        html = http.request("GET", url, preload_content=False).read()
        content = BeautifulSoup(html, "html.parser")
    return content

def get_school_website_link(school_name: str) -> str:
    school_link = ""
    limit = 10
    while limit >= 0:
        soup = crawl_website(f"https://www.google.com/search?q={school_name}")
        first_result = soup.select_one(".yuRUbf")
        first_results = str(first_result).split('href="')
        school_link = first_results[1].split('"')[0]
        if "wiki" in school_link:
            limit -= 1
            school_link = ""
        else:
            break
    return school_link