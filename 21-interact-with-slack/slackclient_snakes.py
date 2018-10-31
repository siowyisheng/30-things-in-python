import os
import time
import random
from slackclient import SlackClient

slack_token = "xoxb-464951176914-464219741968-LBmNSGVz7dtFTbvi7jef6X2d"
sc = SlackClient(slack_token)

while True:
    x = random.randint(1, 100)
    if x <= 20:
        text = "*Bewaresssss!* I am a fearssssome :snake:"
    elif x <= 40:
        text = ":snake: Q: In which river are you sure to find snakes? A: _The Hiss-issippi River!_ :snake:"
    elif x <= 60:
        text = "_Snake? Snake!?_ *Snaaaake!*"
    elif x <= 80:
        text = "I'm so *hungry* I could eat *a whole cow*! http://www.epicadamwildlife.com/2014/09/19/10-most-unbelievable-things-swallowed-by-snakes/"
    else:
        text = """\
*Snake - Poem* by _Langston Hughes_
Back into the grass-
Gives me the courtesy of road
To let me pass,
That I am half ashamed
To seek a stone
To kill him. """
    sc.api_call("chat.postMessage", channel="CDNNYE6QL", text=text)
    channel_info = sc.api_call("channels.info", channel="CDNNYE6QL")
    if channel_info['channel']['latest']['username'] == 'snakes':
        ts = channel_info['channel']['latest']['ts']
        sc.api_call(
            "reactions.add",
            channel="CDNNYE6QL",
            name="thumbsup",
            timestamp=ts)
        sc.api_call(
            "reactions.add",
            channel="CDNNYE6QL",
            name="thumbsdown",
            timestamp=ts)
    time.sleep(8)
