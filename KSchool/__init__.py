import urllib3
import KSchool.Neis_API
import KSchool.website_crawl

urllib3.disable_warnings()

Neis_API = KSchool.Neis_API
website_crawl = KSchool.website_crawl

del urllib3, KSchool