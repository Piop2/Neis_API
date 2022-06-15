import json
import requests
import urllib3, ssl
from bs4 import BeautifulSoup

from Neis_API.service.request.errors import *


def get_request(url, service_name, params):
    """get Neis service request and return raw data"""
    res = requests.get(url=url, params=params, verify=False, json=True)
    res.encoding = "UTF-8"

    text = res.text.replace("<br/>", "\n")
    request = _loads_json(json_s=text)
    status_code = _get_status_code(request=request, key=service_name)
    _check_status_code(status_code=status_code)

    return _get_row_data(request=request, service_name=service_name)

def crawl_website(url):
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

def _loads_json(json_s):
    return json.loads(s=json_s, strict=False)


def _get_status_code(request, key):
    try:
        status_code = request[key][0]["head"][1]["RESULT"]["CODE"]
    except KeyError:
        status_code = request["RESULT"]["CODE"]
    return status_code


def _check_status_code(status_code):
    if status_code == "INFO-000":
        return
    elif status_code == "ERROR-300":
        raise Error300()
    elif status_code == "ERROR-290":
        raise Error290()
    elif status_code == "ERROR-333":
        raise Error333()
    elif status_code == "ERROR-336":
        raise Error336()
    elif status_code == "ERROR-337":
        raise Error337()
    elif status_code == "ERROR-500":
        raise Error500()
    elif status_code == "ERROR-600":
        raise Error600()
    elif status_code == "ERROR-601":
        raise Error601()
    elif status_code == "INFO-300":
        raise Info300()
    elif status_code == "INFO-200":
        raise Info200()
    else:
        raise UnknownStatusCodeError(status_code)


def _get_row_data(request, service_name):
    return request[service_name][1]["row"]
