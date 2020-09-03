import urllib.error
import urllib.parse
import urllib.request


def get_html(url: str) -> str:
    response = urllib.request.urlopen(url)
    return response.read()
