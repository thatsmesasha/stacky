from slackeventsapi import SlackEventAdapter
from slackclient import SlackClient
import os
import re

port = os.environ['SLACK_APP_PORT']

slack_signing_secret = os.environ['SLACK_SIGNING_SECRET']
slack_events_adapter = SlackEventAdapter(slack_signing_secret, '/slack/events')

slack_bot_token = os.environ['SLACK_BOT_TOKEN']
slack_client = SlackClient(slack_bot_token)

@slack_events_adapter.on('app_mention')
def handle_message(event_data):
    print(event_data)
    message_reveived = event_data['event']

    # parse only user messages
    if 'subtype' not in message_reveived:
        message_reveived_clean = re.sub(r'<@[0-9A-Z].*?>', '', message_reveived['text'], flags=re.MULTILINE).strip()
        message_to_send = "Hello <@{}>! :tada: I repeat: {}".format(message_reveived['user'], message_reveived_clean)

        print('Sending message to user <@{}> in channel <@{}>: {}'.format(message_reveived['user'], message_reveived['channel'], message_to_send))
        slack_client.api_call('chat.postMessage', channel=message_reveived['channel'], text=message_to_send)


@slack_events_adapter.on('error')
def error_handler(err):
    print('ERROR: {}'.format(str(err)))

slack_events_adapter.start(port=port, host='0.0.0.0')
