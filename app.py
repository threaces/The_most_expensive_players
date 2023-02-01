import streamlit as st
from data_cleaning import reading_csv_file, clean_df, top10_most_expensive, list_pos, top10_position, list_of_clubs, top10_club, young_players_df, senior_players_df, age_distribution_df, amount_of_players
from visualisation import horizontal_bar_graph, bar_graph, pie_graph

file_path = "players.csv"
df = top10_most_expensive(clean_df(reading_csv_file(file_path)))
df_top_position = clean_df(reading_csv_file(file_path))
df_club = clean_df(reading_csv_file(file_path))

# setting a basic setup f.e. layout etc.

st.set_page_config(
    page_title= "The most expensive players",
    page_icon = '⚽',
    layout = 'wide')

st.title("The most expensive football players in 2021")
st.header("Hello")
st.markdown('''I found a database with information about the most expensive players in 2021. This a hobbyistic project to practice a skills related to Python (including a libraries like pandas, plotly and newly found streamlit). I'm a fan of football, so that why I chose this dataset for training purposes.\n''') 

st.markdown('''I would like present conclusions about information that I found in that database:\n
⚪Top10 the most expensive players\n
⚪Top10 on each position\n
⚪Which country has the biggest amount of the most expensive players\n
⚪Age distribution in that ranking\n
⚪The most expensive senior player (30 years+)\n
⚪The most expensive teenager (U21)\n''')

st.header("Top10 of the players in ranking")
st.plotly_chart(horizontal_bar_graph(df), use_container_width = True, theme='streamlit')

col1, col2 = st.columns(2)

with col1:
    st.header("Top10 of players on each position")
    option = st.selectbox("Select a position", list_pos)
    tab1, tab2 = st.tabs(['Chart', 'Table'])
    with tab1:
        st.plotly_chart(horizontal_bar_graph(top10_position(df_top_position, option)),  use_container_width = True, theme='streamlit')
    with tab2:
        st.dataframe(top10_position(df_top_position, option))

    st.header("The most expensive U21 players")
    st.plotly_chart(horizontal_bar_graph(young_players_df(df_top_position)), use_container_width=True, theme='streamlit')
    with st.expander("Explanation for graph"):
        st.write("""It's a couple of reasons why young players are so expensive when they played less than 100 matches on professional level:\n
        ⚪ Potential buyers see a player for 10+ years on the highest stage\n
    ⚪ Young player has a good resell value after 3-5 years in club\n
    ⚪ Those players 'delivered' a output immiedately\n\n""")
        st.write("""The most expensive player is Erling Haaland. His market value is bigger than Jadon Sancho by 50M. Haaland is a 
        prolific striker with great acceleration, killer instinct, and outstanding physical parameters. All big clubs are 
        looking for that kind of player because it's a huge gap between 30+ years generation (Benzema, Lewandowski, Ronaldo, etc) 
        and the younger generation. Every single prolific striker has a huge market value. """)

    st.header("Age distribution in database")
    st.plotly_chart(bar_graph(age_distribution_df(df_top_position)), use_container_width=True)
    with st.expander("Explanation for age distribution graph"):
        st.write("""The biggest group in the ranking is a group of players 24 - 26 years old. That group contains 187 players. 
        A lot of conditions have an impact on player market value:\n
        ⚪age\n
    ⚪League where the player is playing\n
    ⚪Statistics (goals + assists)\n
    ⚪Contract situation\n
    ⚪Injury history\n
    ⚪Reselling value\n""")

with col2:
    st.header("The most expensive players in club")
    option_club = st.selectbox("Select a club", list_of_clubs)
    tab1, tab2 = st.tabs(['Chart', 'Table'])
    with tab1:
        st.plotly_chart(horizontal_bar_graph(top10_club(df_top_position, option_club)), use_container_width = True)
    with tab2:
        st.dataframe(top10_club(df_club, option_club))

    st.header("The most expensive 30+ players")
    st.plotly_chart(horizontal_bar_graph(senior_players_df(df_top_position)), use_container_width=True, theme='streamlit')
    with st.expander("Explanation for graph"):
        st.write("""It's a couple of reasons why market value of 30+ players is falling rapidly:\n
        ⚪Potential buyers don't see them like long term option\n
    ⚪Very low/0 resell value after 2-3 years in club\n
    ⚪Increased serious injury probability\n\n""")
        st.write("""Market values in this range of age (30 years+) market values are falling quickly f.e. 
        Cristiano Ronaldo market value is just 40M, but his contribution to clubs (Juventus and Manchester United) is huge and 
        his market value was 100M just 2 year ago (2020). The same situation is with Leo Messi or Robert Lewandowski""")

    st.header("Country represented by the biggest amount of players")
    st.plotly_chart(pie_graph(amount_of_players(df_top_position)), use_container_width=True)

    with st.expander("Explanation for pie graph"):
        st.write("""England has the biggest amount of players in the most expensive players ranking. England is represented by 67 players. 
        It is 13,4% of the total amount in that ranking. France and Spain are on the podium in this ranking. Those countries are 
        represented by 58 and 52 players respectively. Portugal, Belgium and Netherland are very interesting cases, because small group of
        people are living in those countries, but they can trained a lot of great players. Those countries have impressive development system
        for kids.""")


