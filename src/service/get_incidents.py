from src.model.get_html import get_html
from src.entity.Incident import Incident
from bs4 import BeautifulSoup
from typing import List, Dict


def get_incidents(url: str) -> None:
    """
    :param url: url of rss feed
    :return: list of incidents with details
    """
    incidents = get_list_of_incidents(url)
    full_incidents = get_detailed_info_of_incident(incidents)
    print(full_incidents)


def get_list_of_incidents(url: str) -> List[Incident]:
    """
    :param url: url of rss feed
    :return List[Incident]: list of incidents with basic info
    """
    rss_content = get_html(url)
    rss_feed = BeautifulSoup(rss_content, 'lxml-xml')

    incidents = []
    for item in rss_feed.findAll('item'):
        incident = Incident()
        incident.set_title(item.title.text)
        incident.set_link(item.link.text)
        incident.set_pub_date(item.pubDate.text)

        incidents.append(incident)

    return incidents


def get_detailed_info_of_incident(incidents: List[Incident]) -> List[Incident]:
    """
    :param incidents: list of incidents with basic info
    :return List[Incident]: list of incidents with full info
    """
    for incident in incidents:
        html_content = get_html(incident.get_link())

        html_parsed = BeautifulSoup(html_content, 'html.parser')
        html_parsed.select('table')[0].extract()

        attributes = get_list_of_attributes(html_parsed.findAll('p'))
        incident = set_attributes_to_incident(incident, attributes)

    return incidents


def set_attributes_to_incident(incident: Incident, attributes: Dict[str, str]) -> Incident:
    """
    TODO: move to transformer
    :param incident: instances of incidents
    :param attributes: dictionary with attributes
    :return Incident: instances of incidents with set attributes
    """
    incident.set_description(attributes['Popis'])
    incident.set_type(attributes['Typ'])
    incident.set_subtype(attributes['Podtyp'])
    incident.set_region(attributes['Okres'])
    incident.set_city(attributes['Obec'])
    incident.set_department(attributes['Jednotky'])
    incident.set_state(attributes['Stav'])

    return incident


def get_list_of_attributes(raw_attributes: List[BeautifulSoup]) -> Dict[str, str]:
    """
    :param raw_attributes: list of raw data
    :return Dict[str, str]: dictionary with keys and values
    """
    attributes = {}
    for raw_attribute in raw_attributes:
        if not hasattr(raw_attribute.strong, 'text'):
            continue

        key = raw_attribute.strong.text.replace(':', '').strip()

        raw_attribute.strong.extract()
        value = raw_attribute.text.strip()

        attributes[key] = value

    return attributes
