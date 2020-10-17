from typing import List
from src.entity.Incident import Incident
from src.model.api_request import add_incident

def add_incidents(api_url: str, incidents: List[Incident]) -> None:
    """
    :param api_url: url of API
    :param incidents: List of incidents
    """
    for incident in incidents:
        add_incident(api_url, incident)
