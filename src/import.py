import src.service.get_incidents


def lambda_handler(event, context):
    src.service.get_incidents.get_incidents(event["url"])
