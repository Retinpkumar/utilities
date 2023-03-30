import requests
import json


def slack_notification(message, channel, username, webhook_url):
    slack_data = {
        "channel": channel, 
        "username": username, 
        "text": message, 
        "icon_emoji": ":ghost:"
        # "icon_url": None
        }
#     slack_data = {
#     'payload': """{
# 					"channel": "#general", 
# 					"username": "webhookbot",
# 					"attachments":[{
# 									"fallback": "Flash Notification Message",

# 									"text": "Main Title of the Message",
# 									"pretext": "Scraping has been completed for LinkedIn data...",

# 									"color": "#36a64f",

# 									"fields": [
# 												{
# 													"title": "LinkedIn data",
# 													"value": "Size: 1 MB, \nRows: 1453, \nColumns: 12, \nLocation: s3://linkedin/linkedin.json",
# 													"short": false
# 												}
# 											]
# 								}]
#                     }"""
# }
    response = requests.post(
        webhook_url, data=json.dumps(slack_data),
        headers={'Content-Type': 'application/json'}
    )
    if response.status_code != 200:
        raise ValueError('Request to slack returned an error...')
    return response.status_code

