import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def horizontal_bar_graph(df):
    
    fig = px.bar(df, x='Market Value In Millions(£)', y='Name', orientation='h', height = 600, text = 'Market Value In Millions(£)')
    fig.update_traces(textfont_size = 16, marker_color = 'rgb(22, 177, 243)')

    return fig

def bar_graph(df):

    fig = px.bar(df, x=df.index, y='Amount of players', height = 600, text = 'Amount of players')
    fig.update_traces(textfont_size = 16, marker_color = 'rgb(22, 177, 243)')

    return fig

def pie_graph(df):
    fig = px.pie(df, values="% of players in ranking", names=df.index, height=556)
    #fig.update_traces(textfont_size = 16, marker_color = 'rgb(22, 177, 243)')

    return fig