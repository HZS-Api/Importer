import os
from src.service.get_incidents import get_incidents
from src.service.api import add_incidents


def lambda_handler(event, context):
    api_url = os.environ['API_URL']
    incidents = get_incidents(event["url"])
    add_incidents(api_url, incidents)
