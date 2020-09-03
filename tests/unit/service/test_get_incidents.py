import pytest
from bs4 import BeautifulSoup
from src.entity.Incident import Incident
from src.service.get_incidents import get_list_of_attributes
from src.service.get_incidents import set_attributes_to_incident


def test_get_list_of_attributes():
    raw_attributes = [
        BeautifulSoup('<p><strong> velikost: </strong>    střední </p>', 'html.parser'),
        BeautifulSoup('sfgasddg: asdfas', 'html.parser'),
        BeautifulSoup('<p></p>', 'html.parser'),
        BeautifulSoup('<p>asdfdsg: asdfsad</p>', 'html.parser'),
        BeautifulSoup('<strong>asdf:</strong> asdfgdsg', 'html.parser'),
        BeautifulSoup('<p><strong> batman: </strong></p>', 'html.parser')
    ]

    expected = {
        'velikost': 'střední',
        'asdf': 'asdfgdsg',
        'batman': ''
    }

    result = get_list_of_attributes(raw_attributes)

    assert result == expected


def test_get_list_of_attributes_with_empty_raw():
    raw_attributes = []
    expected = {}
    result = get_list_of_attributes(raw_attributes)

    assert result == expected


def test_set_attributes_to_incident():
    incident = Incident()
    attributes = {
        'Popis': '',
        'Typ': 'asdf',
        'Podtyp': '',
        'Okres': 'asdf',
        'Obec': 'asdfsd',
        'Jednotky': 'dskdnj',
        'Stav': 'sdfr'
    }
    result_incident: Incident = set_attributes_to_incident(incident, attributes)

    assert result_incident.get_description() == attributes['Popis']
    assert result_incident.get_type() == attributes['Typ']
    assert result_incident.get_subtype() == attributes['Podtyp']
    assert result_incident.get_region() == attributes['Okres']
    assert result_incident.get_city() == attributes['Obec']
    assert result_incident.get_department() == attributes['Jednotky']
    assert result_incident.get_state() == attributes['Stav']
