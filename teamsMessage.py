# source: https://stackoverflow.com/questions/59371631/send-automated-messages-to-microsoft-teams-using-python/59371723#59371723?newreg=a827387a77ef446ca6f6f4b4b5c5d1d7
# 1. Create a webhook in MS Teams

## Add an incoming webhook to a Teams channel:

## Navigate to the channel where you want to add the webhook and select (•••) Connectors from the top navigation bar.
## Search for Incoming Webhook, and add it.
## Click Configure and provide a name for your webhook.
## Copy the URL which appears and click "OK".
# 2. Install pymsteams

pip install pymsteams
import pymsteams
myTeamsMessage = pymsteams.connectorcard("<Microsoft Webhook URL>")
myTeamsMessage.text("this is my text")
myTeamsMessage.send()
