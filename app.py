import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(layout="wide")

df = pd.read_csv("Dataset.csv",index_col=[0],lineterminator='\n')

name_list = df["Name"].tolist()
poster_list = df["Img_Link"].tolist()
links_list = df['Link'].tolist()
dev_list = df['Developer'].tolist()
from Game import get_rec

def recommend(name):
    recommended_games = pd.DataFrame()
    recommended_games['Name'] = get_rec(name)
    games = []
    imgs = []
    links = []
    devs = []
    games.append(recommended_games['Name'].tolist())
    for i in recommended_games.index:
        imgs.append(poster_list[i])
        links.append(links_list[i])
        devs.append(dev_list[i])
    return games,imgs,links

st.title("GameRS - Game Recommender System")
st.text("A video-game recommendation engine for PC games")

selected_game_name = option = st.selectbox("Type or use the drop-down menu to select a game.", options=(name_list))
button = st.button("Recommend")

if button:
    st.subheader("Recommendations for %s:" % selected_game_name)
    #First row of games
    with st.container():
        names, posters, links= recommend(selected_game_name)
        game1, game2, game3, game4, game5 = st.columns(5)

        with game1:
            url = links[0]
            st.image(posters[0])
            st.write(names[0][0])
            st.caption("For more details - [Click here](%s)" % url)

        with game2:
            url = links[1]
            st.image(posters[1])
            st.write(names[0][1])
            st.caption("For more details - [Click here](%s)" % url)

        with game3:
            url = links[2]
            st.image(posters[2])
            st.write(names[0][2])
            st.caption("For more details - [Click here](%s)" % url)
        
        with game4:
            url = links[3]
            st.image(posters[3])
            st.write(names[0][3])
            st.caption("For more details - [Click here](%s)" % url)

        with game5:
            url = links[4]
            st.image(posters[4])
            st.write(names[0][4])
            st.caption("For more details - [Click here](%s)" % url)

    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")

    #Second Row of games
    with st.container():
        names, posters, links = recommend(selected_game_name)
        game6, game7, game8, game9, game10 = st.columns(5)

        with game6:
            url = links[5]
            st.image(posters[5])
            st.write(names[0][5])
            st.caption("For more details - [Click here](%s)" % url)

        with game7:
            url = links[6]
            st.image(posters[6])
            st.write(names[0][6])
            st.caption("For more details - [Click here](%s)" % url)

        with game8:
            url = links[7]
            st.image(posters[7])
            st.write(names[0][7])
            st.caption("For more details - [Click here](%s)" % url)
        
        with game9:
            url = links[8]
            st.image(posters[8])
            st.write(names[0][8])
            st.caption("For more details - [Click here](%s)" % url)

        with game10:
            url = links[9]
            st.image(posters[9])
            st.write(names[0][9])
            st.caption("For more details - [Click here](%s)" % url)

    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")

    #Third Row of games
    with st.container():
        names, posters, links = recommend(selected_game_name)
        game11, game12, game13, game14, game15 = st.columns(5)

        with game11:
            url = links[10]
            st.image(posters[10])
            st.write(names[0][10])
            st.caption("For more details - [Click here](%s)" % url)

        with game12:
            url = links[11]
            st.image(posters[11])
            st.write(names[0][11])
            st.caption("For more details - [Click here](%s)" % url)

        with game13:
            url = links[12]
            st.image(posters[12])
            st.write(names[0][12])
            st.caption("For more details - [Click here](%s)" % url)
        
        with game14:
            url = links[13]
            st.image(posters[13])
            st.write(names[0][13])
            st.caption("For more details - [Click here](%s)" % url)

        with game15:
            url = links[14]
            st.image(posters[14])
            st.write(names[0][14])
            st.caption("For more details - [Click here](%s)" % url)
    
        st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")

    #Fourth Row of games
    with st.container():
        names, posters, links = recommend(selected_game_name)
        game16, game17, game18, game19, game20 = st.columns(5)

        with game16:
            url = links[15]
            st.image(posters[15])
            st.write(names[0][15])
            st.caption("For more details - [Click here](%s)" % url)

        with game17:
            url = links[16]
            st.image(posters[16])
            st.write(names[0][16])
            st.caption("For more details - [Click here](%s)" % url)

        with game18:
            url = links[17]
            st.image(posters[17])
            st.write(names[0][17])
            st.caption("For more details - [Click here](%s)" % url)
        
        with game19:
            url = links[18]
            st.image(posters[18])
            st.write(names[0][18])
            st.caption("For more details - [Click here](%s)" % url)

        with game20:
            url = links[19]
            st.image(posters[19])
            st.write(names[0][19])
            st.caption("For more details - [Click here](%s)" % url)