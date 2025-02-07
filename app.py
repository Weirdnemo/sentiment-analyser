import streamlit as st
import time
import pandas as pd
import asyncio
from mock_data import MockDataGenerator
from sentiment_analyzer import SentimentAnalyzer
from data_processor import DataProcessor
from visualizer import Visualizer
from discord_bot import create_discord_bot

# Initialize session state
if 'data_processor' not in st.session_state:
    st.session_state.data_processor = DataProcessor()
if 'mock_generator' not in st.session_state:
    st.session_state.mock_generator = MockDataGenerator()
if 'sentiment_analyzer' not in st.session_state:
    st.session_state.sentiment_analyzer = SentimentAnalyzer()
if 'visualizer' not in st.session_state:
    st.session_state.visualizer = Visualizer()
if 'discord_bot' not in st.session_state:
    st.session_state.discord_bot = None

# Page configuration
st.set_page_config(
    page_title="Mood Map",
    page_icon="🎯",
    layout="wide"
)

# Sidebar configuration
# st.sidebar.title("Configuration")

# # Discord configuration
# with st.sidebar.expander("Discord Settings", expanded=True):
#     st.markdown("""
#     ### Setup Instructions
#     1. Create a Discord bot in the [Developer Portal](https://discord.com/developers/applications)
#     2. Enable Message Content Intent in Bot settings
#     3. Invite bot to your server
#     4. Right-click channel & copy Channel ID (Need Developer Mode)
#
#     [View Full Setup Guide](https://github.com/your-repo/README.md)
#     """)
#
#     discord_token = st.text_input("Discord Bot Token", type="password")
#     channel_id = st.text_input("Channel ID")
#
#     if st.button("Connect Discord"):
#         if discord_token:
#             try:
#                 st.session_state.discord_bot = create_discord_bot(discord_token)
#                 st.success("Discord bot configured! Start fetching messages to see the data.")
#             except Exception as e:
#                 st.error(f"Error connecting to Discord: {str(e)}")
#
#     if st.session_state.discord_bot and channel_id:
#         if st.button("Fetch Discord Messages"):
#             try:
#                 with st.spinner('Fetching messages from Discord...'):
#                     messages = asyncio.run(st.session_state.discord_bot.get_recent_messages(channel_id))
#                     if not messages.empty:
#                         analyzed_messages = st.session_state.sentiment_analyzer.analyze_messages(messages)
#                         st.session_state.data_processor.update_data(analyzed_messages)
#                         st.success(f"Fetched {len(messages)} messages from Discord!")
#                     else:
#                         st.info("No messages found in the specified channel. Make sure the bot has access to this channel.")
#             except Exception as e:
#                 st.error(f"Error fetching Discord messages: {str(e)}\nMake sure the Channel ID is correct and the bot has access to the channel.")
#
#     if st.session_state.discord_bot:
#         st.success("✅ Bot is connected")
#         if channel_id:
#             st.info("💬 Channel ID is set")
#

# Title and description
st.title("🎯Mood Map")
st.markdown("""
Monitor the emotional pulse of your hackathon in real-time! This dashboard analyzes
participant messages to track the overall mood and sentiment trends throughout the event.
""")

# Create two columns for the layout
col1, col2 = st.columns([2, 1])

with col1:
    # Message input section
    st.subheader("📝 Message Input")
    message_input = st.text_area("Type a message to analyze:", "")
    if st.button("Send Message"):
        if message_input:
            new_message = pd.DataFrame([{
                'timestamp': pd.Timestamp.now(),
                'user': 'User',
                'message': message_input
            }])
            analyzed_message = st.session_state.sentiment_analyzer.analyze_messages(new_message)
            st.session_state.data_processor.update_data(analyzed_message)
            st.success("Message sent and analyzed!")

    # Generate mock data button
    if st.button("Generate Mock Data"):
        mock_data = st.session_state.mock_generator.generate_batch(5, 10)
        analyzed_data = st.session_state.sentiment_analyzer.analyze_messages(mock_data)
        st.session_state.data_processor.update_data(analyzed_data)
        st.success("Generated and analyzed mock messages!")

with col2:
    # Current mood display
    st.subheader("😊 Current Mood")
    mood, sentiment_value = st.session_state.data_processor.get_current_mood()
    st.markdown(f"### {mood}")

    # Display mood gauge
    st.plotly_chart(
        st.session_state.visualizer.create_mood_gauge(sentiment_value),
        use_container_width=True
    )

# Statistics section
st.subheader("📊 Mood Statistics")
stats = st.session_state.data_processor.get_stats()
col1, col2, col3, col4 = st.columns(4)
col1.metric("Message Count", stats["message_count"])
col2.metric("Average Sentiment", f"{stats['avg_sentiment']:.2f}")
col3.metric("Positive Messages", f"{stats['positive_ratio']:.1f}%")
col4.metric("Negative Messages", f"{stats['negative_ratio']:.1f}%")

# Sentiment timeline
st.subheader("📈 Sentiment Timeline")
if len(st.session_state.data_processor.data) > 0:
    rolling_sentiment = st.session_state.data_processor.get_rolling_sentiment()
    timeline = st.session_state.visualizer.create_sentiment_timeline(
        st.session_state.data_processor.data,
        rolling_sentiment
    )
    st.plotly_chart(timeline, use_container_width=True)
else:
    st.info("No messages to display yet. Add some messages to see the sentiment timeline!")

# Add auto-refresh using modern Streamlit method
if 'auto_refresh' not in st.session_state:
    st.session_state.auto_refresh = True

# # Auto-refresh toggle
# auto_refresh = st.sidebar.checkbox('Enable Auto-refresh', value=st.session_state.auto_refresh)
# st.session_state.auto_refresh = auto_refresh
#
# if st.session_state.auto_refresh:
#     time.sleep(30)
#     st.rerun()