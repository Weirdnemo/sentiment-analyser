# Mood Map - Discord Integration Guide (Optional)

## Setting up the Discord Bot

1. **Create a Discord Application and Bot**
   - Go to [Discord Developer Portal](https://discord.com/developers/applications)
   - Click "New Application" and give it a name
   - Go to the "Bot" section and click "Add Bot"
   - Under the bot settings, enable these options:
     - MESSAGE CONTENT INTENT
     - PRESENCE INTENT
     - SERVER MEMBERS INTENT

2. **Get the Bot Token**
   - In the Bot section, click "Reset Token" to get your bot token
   - Save this token securely - you'll need it for the application

3. **Invite the Bot to Your Server**
   - Go to the "OAuth2" section
   - Select "bot" under "SCOPES"
   - Under "Bot Permissions", select:
     - Read Messages/View Channels
     - Read Message History
     - Send Messages
   - Copy the generated URL and open it in your browser
   - Select your server and click "Authorize"

4. **Get the Channel ID**
   - In Discord, enable Developer Mode:
     - Go to User Settings > App Settings > Advanced
     - Turn on Developer Mode
   - Right-click on the channel you want to monitor
   - Click "Copy Channel ID"

## Using the Bot in Hackathon Mood Map

1. **Connect the Bot**
   - Open the sidebar in the application
   - Expand "Discord Settings"
   - Paste your Bot Token in the "Discord Bot Token" field
   - Click "Connect Discord"

2. **Fetch Messages**
   - After connecting, paste your Channel ID in the "Channel ID" field
   - Click "Fetch Discord Messages"
   - The application will retrieve recent messages and analyze their sentiment

3. **Real-time Updates**
   - Once connected, the bot will automatically capture new messages
   - The dashboard will update to show the latest sentiment analysis
   - You can toggle auto-refresh in the sidebar to see updates automatically

## How to Run This

### Prerequisites
Ensure you have Python installed. You also need to install the required dependencies.

### Install Dependencies
Run the following command in your terminal or command prompt:
```sh
pip install -r requirements.txt
```

### Running the Application
Navigate to the directory where `app.py` is located and run:
```sh
streamlit run app.py
```

### Required Libraries
Make sure the following libraries are installed in your `requirements.txt`:
```
discord-py>=2.4.0
nltk>=3.9.1
numpy>=2.2.2
pandas>=2.2.3
plotly>=6.0.0
streamlit>=1.42.0
twilio>=9.4.4
```

### Notes
- Keep your bot token secure and never share it publicly.
- Ensure your bot has the required permissions in the Discord server.
- If you encounter errors, check that all dependencies are installed correctly.

