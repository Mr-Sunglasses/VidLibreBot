import requests
from urllib.parse import quote


def short(url: str):
    url = "https://url-shortener-service.p.rapidapi.com/shorten"
    payload_url = url

    payload = f"url={quote(payload_url)}"
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Key": "e02923797dmshddea57448263f98p13ab17jsn9e252949aa6f",
        "X-RapidAPI-Host": "url-shortener-service.p.rapidapi.com"
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    x = dict(response.json())
    return_link = ""
    for i in x.values():
        return_link = i
    return return_link


