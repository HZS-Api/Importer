import service.get_incidents


def lambda_handler(event, context):
    service.get_incidents.get_incidents(event["url"])
