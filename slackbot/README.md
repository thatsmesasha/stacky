# Stacky Slackbot

- [Description](#description)
- [Installation](#installation)
		- [Slack App](#slack-app)
		- [Run app](#run-app)
			- [Locally](#locally)
			- [Docker](#docker)
			- [Create public URL](#create-public-url)
		- [Subscribe to events](#subscribe-to-events)
- [Interact with your bot](#interact-with-your-bot)

## Description
Stacky Slackbot is a slack bot that is used to easily interact with Stacky Answer Engine.

## Installation

#### Slack App
Create a Slack app on https://api.slack.com/apps/

Add a bot user to your app in the tab **Bot Users**
3
Visit your app's **Install App** page and click **Install App to Team**.

Once you've authorized your app, you'll be presented with your app's tokens in the tab **OAuth & Permissions**. Copy **Bot User OAuth Access Token** value, it will be used later in the installation as `SLACK_BOT_TOKEN`.

In the tab **Basic Information**, copy value of **Signing Secret**, it will be also used later as `SLACK_SIGNING_SECRET`.

#### Run app

Clone the repository and navigate to this folder. You can either run app locally or using docker image.

##### Locally

Define env variables needed for running:

```
export SLACK_BOT_TOKEN=<SLACK_BOT_TOKEN>
export SLACK_SIGNING_SECRET=<SLACK_SIGNING_SECRET>
export SLACK_APP_PORT=<SLACK_APP_PORT>
```

Replace `<SLACK_BOT_TOKEN>` and `<SLACK_SIGNING_SECRET>` with values you obtained in the section [Slack App](#slack-app). `<SLACK_APP_PORT>` can be any port (for example 3000) that will be used by Slack API.

Install requirements and run the app:

```
pip install -r requirements.txt
python app.py
```

##### Docker

Build docker image:

```
docker build -t stacky-slackbot --build-arg SLACK_SIGNING_SECRET=<SLACK_SIGNING_SECRET> --build-arg  SLACK_BOT_TOKEN=<SLACK_BOT_TOKEN> .
```

Replace `<SLACK_BOT_TOKEN>` and `<SLACK_SIGNING_SECRET>` with values you obtained in the section [Slack App](#slack-app).

Create docker container:

```
docker create -p <SLACK_APP_PORT>:3000 --name stacky-slackbot -t stacky-slackbot
```

`<SLACK_APP_PORT>` can be any port (for example 3000) that will be used by Slack API.

Start container:

```
docker start stacky-slackbot
```

##### Create public URL

If you are running the app on the server, you can continue to [Subscribe to events](#subscribe-to-events).

If you are running on your computer, you will need a public url to connect to your app. The recommended choice is https://ngrok.com/ . Follow steps to install and run:

```
./ngrok http <SLACK_APP_PORT>
```

Replace `<SLACK_APP_PORT>` for port you used to run the app.

#### Subscribe to events

Go again to your app page at https://api.slack.com/apps/ .

In the tab **Event Subscriptions** add your **Request URL** (your ngrok URL or server ip + `/slack/events`) and in section **Subscribe to Bot Events** subscribe your app to **app_mention**. Save and toggle **Enable Events**.

You're all set!

## Interact with your bot

Start asking questions in the Slack channel just by mentioning your bot, for example:

```
@Stacky how to write README file?
```
