import discord
from discord.ext import commands
import asyncio
from datetime import datetime, timedelta
import pandas as pd

class DiscordBot:
    def __init__(self, token):
        self.token = token
        self.bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
        self.messages_queue = asyncio.Queue()
        
        @self.bot.event
        async def on_ready():
            print(f'{self.bot.user} has connected to Discord!')
            
        @self.bot.event
        async def on_message(message):
            # Ignore messages from the bot itself
            if message.author == self.bot.user:
                return
                
            # Convert message to our standard format
            message_data = {
                'timestamp': pd.Timestamp(message.created_at),
                'user': str(message.author),
                'message': message.content
            }
            
            # Add to queue
            await self.messages_queue.put(message_data)
            await self.bot.process_commands(message)
    
    async def start(self):
        """Start the Discord bot"""
        await self.bot.start(self.token)
    
    async def get_recent_messages(self, channel_id, limit=100):
        """Fetch recent messages from a specific channel"""
        messages = []
        channel = self.bot.get_channel(int(channel_id))
        
        if channel:
            async for message in channel.history(limit=limit):
                if message.author != self.bot.user:
                    messages.append({
                        'timestamp': pd.Timestamp(message.created_at),
                        'user': str(message.author),
                        'message': message.content
                    })
        
        return pd.DataFrame(messages)
    
    async def get_new_messages(self):
        """Get new messages from the queue"""
        messages = []
        
        # Get all available messages from the queue
        while not self.messages_queue.empty():
            try:
                message = self.messages_queue.get_nowait()
                messages.append(message)
            except asyncio.QueueEmpty:
                break
                
        return pd.DataFrame(messages) if messages else None

def create_discord_bot(token):
    """Create and return a Discord bot instance"""
    return DiscordBot(token)
