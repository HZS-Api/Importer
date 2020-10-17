import requests
import json
from src.entity.Incident import Incident

def add_incident(api_url: str, incident: Incident) -> None:
    add_incident_url = api_url + "/incident"
    payload = json.dumps(incident.get_data())
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", add_incident_url, headers=headers, data = payload)

    print(response.text.encode('utf8'))
