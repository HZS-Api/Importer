from model.get_html import get_html
from value_object.Incident import Incident
from bs4 import BeautifulSoup
from typing import List


def get_incidents(url: str):
    """
    :param url: url of rss feed
    :return: list of incidents with details
    """
    incidents = get_list_of_incidents(url)
    get_detailed_info_of_incident(incidents)


def get_list_of_incidents(url: str) -> List[Incident]:
    """
    :param url: url of rss feed
    :return List[Incident]: list of incidents with basic info
    """
    rss_content = get_html(url)
    rss_feed = BeautifulSoup(rss_content, 'lxml-xml')

    incidents = []
    for item in rss_feed.findAll('item'):
        incidents.append(Incident({
            'title': item.title.text,
            'link': item.link.text,
            'pub_date': item.pubDate.text,
        }))

    return incidents


def get_detailed_info_of_incident(incidents: List[Incident]):
    for incident in incidents:
        html_content = get_html(incident.get_link())
        html_parsed = BeautifulSoup(html_content, 'html.parser')
        print(html_parsed.prettify())
        break
