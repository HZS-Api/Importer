import urllib.error
import urllib.parse
import urllib.request


def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()
