import os
import re
import logging
import requests
from pathlib import Path
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# Turn on debug logging to see if events are actually arriving
logging.basicConfig(level=logging.DEBUG)

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# Initialize your app with your bot token
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))

# The mock AI API URL
API_URL = "http://localhost:3000/api/chat"

@app.event("app_mention")
def handle_app_mentions(body, say, logger):
    """
    Listens for any time the bot is @mentioned in a channel.
    Strips out the @bot mention from the text, sends the query to the API, and replies.
    """
    try:
        # Extract the event data
        event = body.get("event", {})
        user_id = event.get("user")
        text = event.get("text", "")
        
        # Clean the text by removing the bot mention (e.g., "<@U123456> query")
        clean_text = re.sub(r'<@U[A-Z0-9]+>', '', text).strip()
        
        if not clean_text:
            say(f"Hello <@{user_id}>! You mentioned me, but didn't say anything. How can I help?")
            return

        # Send an initial message to show it's thinking (optional, good UX)
        # Using a thread reply is nice to not clutter the main channel when possible
        initial_reply = say(text=f"_Thinking..._", thread_ts=event.get("ts"))
        
        # Send the user's message to your mock AI API
        response = requests.post(API_URL, json={"message": clean_text})
        
        if response.status_code == 200:
            api_data = response.json()
            reply_text = api_data.get("reply", "No reply found from API.")
            
            # Send the final response from the API back to Slack
            app.client.chat_update(
                channel=event.get("channel"),
                ts=initial_reply["ts"],
                text=f"<@{user_id}>, {reply_text}"
            )
        else:
            app.client.chat_update(
                channel=event.get("channel"),
                ts=initial_reply["ts"],
                text=f"Oops <@{user_id}>, the API returned an error: {response.status_code}"
            )
            
    except Exception as e:
        logger.error(f"Error handling mention: {e}")
        say(f"Sorry <@{user_id}>, something went wrong while processing your request.")

if __name__ == "__main__":
    # Start your app with Socket Mode
    # Make sure SLACK_APP_TOKEN is in your .env starting with xapp-
    handler = SocketModeHandler(app, os.environ.get("SLACK_APP_TOKEN"))
    print("⚡️ Bolt app is running in Socket Mode!")
    handler.start()
