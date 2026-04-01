# Complete Setup Guide: Slack Bot with AI API Integration

This guide traces the steps to completely replicate this project from scratch, including the Slack dashboard configurations, the mock AI API server, and the Python bot using Socket Mode.

## Phase 1: Slack API Dashboard Setup

1. **Create the App:**
   - Go to the [Slack API Dashboard](https://api.slack.com/apps) and click **Create New App** > **From scratch**.
   - Name your app and select your workspace.

2. **Enable Socket Mode:**
   - On the left sidebar, click **Socket Mode** and toggle it **On**.
   - This will prompt you to generate an App-Level Token. Name it (e.g., "Socket Token"). 
   - *Save this token!* It starts with `xapp-` and will be your `SLACK_APP_TOKEN`.

3. **Configure OAuth & Permissions (Scopes):**
   - On the left sidebar, go to **OAuth & Permissions**.
   - Scroll down to **Bot Token Scopes** and add:
     - `app_mentions:read` (Allows the bot to know when it's mentioned)
     - `chat:write` (Allows the bot to send messages)
   
4. **Enable Event Subscriptions:**
   - On the left sidebar, go to **Event Subscriptions**.
   - Toggle **Enable Events** to **On**.
   - Scroll down to **Subscribe to bot events**.
   - Click **Add Bot User Event** and select `app_mention`.

5. **Install / Reinstall to Workspace:**
   - Go to **Install App** on the left sidebar and click **Install to Workspace** (or Reinstall).
   - Authorize the app.
   - You will receive a Bot User OAuth Token. *Save this token!* It starts with `xoxb-` and will be your `SLACK_BOT_TOKEN`.

---

## Phase 2: Mock AI API Server (Node.js)

We created a simple local API to simulate an AI receiving a prompt and generating a reply.

1. **Navigate to the server directory:**
   ```bash
   mkdir "Placeholder Server"
   cd "Placeholder Server"
   ```

2. **Initialize and install dependencies:**
   ```bash
   npm init -y
   npm install express body-parser
   ```

3. **Server Code (`server.js`):**
   Creates a server running on `http://localhost:3000` that listens to `POST /api/chat` and returns a mock AI string.

4. **Run the API:**
   ```bash
   node server.js
   ```

---

## Phase 3: The Slack Bot (Python)

We built a Python script using the official `@slack/bolt` framework to listen to Slack via Socket Mode and forward questions to our mock API.

1. **Navigate to the bot directory:**
   ```bash
   mkdir "Bot Python"
   cd "Bot Python"
   ```

2. **Create the `.env` file:**
   Inside `Bot Python/`, create a file named `.env` and add the tokens you got from Phase 1:
   ```env
   SLACK_BOT_TOKEN=xoxb-your-bot-token
   SLACK_APP_TOKEN=xapp-your-app-token
   ```

3. **Install Python dependencies:**
   ```bash
   pip3 install slack_bolt slack_sdk requests python-dotenv "urllib3<2"
   ```
   *(Note: `urllib3<2` is specified to avoid OpenSSL/LibreSSL compatibility warnings on macOS).*

4. **Bot Code (`bot.py`):**
   The script initializes `App(token=...)`, listens via `@app.event("app_mention")`, parses the text, sends a POST request to `http://localhost:3000/api/chat`, and updates the Slack thread with the response.

5. **Run the Bot:**
   ```bash
   python3 bot.py
   ```
   *Expected Output in terminal: `⚡️ Bolt app is running in Socket Mode!`*

---

## Phase 4: Usage

1. Open your Slack workspace.
2. Go to a channel and invite your bot (e.g., `/invite @YourBotName`).
3. Send a message tagging the bot: `@YourBotName give me a summary of the latest project`.
4. The bot will instantly reply with "_Thinking..._", send your prompt to the local API on port `3000`, and replace the "_Thinking..._" message with the API's generated response!
