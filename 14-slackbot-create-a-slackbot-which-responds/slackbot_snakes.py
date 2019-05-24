from slackeventsapi import SlackEventAdapter
from slackclient import SlackClient

# ==================================================================================
# AUTHORIZATION
# ==================================================================================
# demo only. don't do this for your own app.
slack_signing_secret = YOUR_SECRET  # looks like "52b92e96807f34401eab79c3ce4979a5"
slack_events_adapter = SlackEventAdapter(slack_signing_secret, "/slack/events")
slack_bot_token = YOUR_BOT_TOKEN  # looks like "xoxb-464951176914-464219741968-LBmNSGVz7dtFTbvi7jef6X2d"
slack_client = SlackClient(slack_bot_token)


# ==================================================================================
# EVENTS
# ==================================================================================
@slack_events_adapter.on("message")
def handle_message(event_data):
    message = event_data["event"]
    # If the incoming message contains "hi", then respond with a "Hello" message
    if message.get("subtype") is None and "hi" in message.get('text'):
        channel = message["channel"]
        message = "Hello <@%s>! :tada:" % message["user"]
        print(channel)
        slack_client.api_call(
            "chat.postMessage", channel=channel, text=message)


# Example reaction emoji echo
@slack_events_adapter.on("reaction_added")
def reaction_added(event_data):
    event = event_data["event"]
    emoji = event["reaction"]
    channel = event["item"]["channel"]
    text = ":%s:" % emoji
    slack_client.api_call("chat.postMessage", channel=channel, text=text)


# Error events
@slack_events_adapter.on("error")
def error_handler(err):
    print("ERROR: " + str(err))


# Once we have our event listeners configured, we can start the
# Flask server with the default `/events` endpoint on port 3000
slack_events_adapter.start(port=3000)