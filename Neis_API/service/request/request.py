import json
import requests

import errors


def get_request(url, service_name, params):
    """get Neis service request and return raw data"""
    res = requests.get(url=url, params=params, verify=False, json=True)
    res.encoding = "UTF-8"
    json_s = res.text.replace("<br/>", "\n")

    request = _loads_json(json_s=json_s)

    status_code = _get_status_code(request=request, key=service_name)

    _check_status_code(status_code=status_code)

    return _get_raw_data(request=request, service_name=service_name)


def _loads_json(json_s):
    return json.loads(s=json_s, strict=False)


def _get_status_code(request, key):
    try:
        status_code = request[key][0]["head"][1]["RESULT"]["CODE"]
    except KeyError:
        status_code = request["RESULT"]["CODE"]
    return status_code


class UnknownStatusCodeError(Exception):
    def __init__(self, status_code):
        super().__init__("Unknown service error: %s" % status_code)
        return


def _check_status_code(status_code):
    if status_code == "ERROR-300":
        raise errors.Error300()
    elif status_code == "ERROR-290":
        raise errors.Error290()
    elif status_code == "ERROR-333":
        raise errors.Error333()
    elif status_code == "ERROR-336":
        raise errors.Error336()
    elif status_code == "ERROR-337":
        raise errors.Error337()
    elif status_code == "ERROR-500":
        raise errors.Error500()
    elif status_code == "ERROR-600":
        raise errors.Error600()
    elif status_code == "ERROR-601":
        raise errors.Error601()
    elif status_code == "INFO-300":
        raise errors.Info300()
    elif status_code == "INFO-200":
        raise errors.Info200()
    else:
        raise UnknownStatusCodeError(status_code)


def _get_raw_data(request, service_name):
    return request[service_name][1]["row"]
