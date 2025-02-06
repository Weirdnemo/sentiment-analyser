import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

class Visualizer:
    @staticmethod
    def create_sentiment_timeline(df, rolling_sentiment):
        fig = go.Figure()
        
        # Add scatter plot for individual sentiments
        fig.add_trace(go.Scatter(
            x=df['timestamp'],
            y=df['sentiment'],
            mode='markers',
            name='Messages',
            marker=dict(size=8, color='rgba(255, 75, 75, 0.5)')
        ))
        
        # Add line plot for rolling average
        fig.add_trace(go.Scatter(
            x=df['timestamp'],
            y=rolling_sentiment,
            mode='lines',
            name='Trend',
            line=dict(width=3, color='rgb(255, 75, 75)')
        ))
        
        fig.update_layout(
            title='Sentiment Timeline',
            xaxis_title='Time',
            yaxis_title='Sentiment Score',
            hovermode='x unified',
            template='plotly_white',
            height=400
        )
        
        return fig

    @staticmethod
    def create_mood_gauge(sentiment_value):
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=sentiment_value,
            domain={'x': [0, 1], 'y': [0, 1]},
            gauge={
                'axis': {'range': [-1, 1]},
                'bar': {'color': "rgb(255, 75, 75)"},
                'steps': [
                    {'range': [-1, -0.5], 'color': "rgb(255, 150, 150)"},
                    {'range': [-0.5, 0], 'color': "rgb(255, 200, 200)"},
                    {'range': [0, 0.5], 'color': "rgb(200, 255, 200)"},
                    {'range': [0.5, 1], 'color': "rgb(150, 255, 150)"}
                ]
            }
        ))
        
        fig.update_layout(
            title='Current Mood Meter',
            height=250
        )
        
        return fig
