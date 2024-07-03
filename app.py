import streamlit as slt, pandas as pd, pickle as pk, requests
from streamlit_extras.stylable_container import stylable_container

slt.set_page_config(layout="wide")
slt.title(':violet[Movie Recommendation System]')

listed_movies = pk.load(open('movs.pkl', 'rb'))
movs = pd.DataFrame(listed_movies)

sim_scr = pk.load(open('similarity_scores.pkl', 'rb'))

def mov_poster(movs_id):
    movs_url_path = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movs_id)
    data_movs = requests.get(movs_url_path)
    data_movs = data_movs.json()
    pst_path = data_movs['poster_path']
    f_path = "https://image.tmdb.org/t/p/w500/" + pst_path
    return f_path


def rcm(sel_mov):
    idx = movs[movs['title'] == sel_mov].index[0]
    dist = sorted(list(enumerate(sim_scr[idx])), reverse=True, key=lambda x:x[1])[1:12]

    rcm_movie_names = []
    rcm_movie_posters = []
    for i in dist[1:11]:
        # fetch the movie poster
        movie_id = movs.iloc[i[0]].movie_id
        rcm_movie_posters.append(mov_poster(movie_id))
        rcm_movie_names.append(movs.iloc[i[0]].title)

    return rcm_movie_names,rcm_movie_posters


mov_nm_sel = slt.selectbox('Recommend me a movie!', sorted(movs['title'].values))

with stylable_container(
    "red",
    css_styles="""
    button:hover {
        background-color: #FF0000;
        color: #FFFFFF;
    }"""
):
    # if slt.button('Recommend A Movie'):
    #     recom = rcm(mov_nm_sel)
    #     slt.write('\n')
    #     slt.write('\n')
    #     slt.markdown('''**:red[Here are you top ten recommended movies:]**''')
    #     cnt = 1
    #     for i in recom:
    #         slt.write(f":blue[{cnt}]. **{i}**")
    #         cnt += 1
    if slt.button('Show Recommendation'):
        rcm_movie_names, rcm_movie_posters = rcm(mov_nm_sel)
        slt.write('\n')
        slt.write('\n')
        slt.subheader('''**:red[Here are you top ten recommended movies:]**''')
        slt.write('\n')
        slt.write('\n')
        col1, col2, col3, col4, col5, col6, col7, col8, col9, col10 = slt.columns(10)
        with col1:
            slt.image(rcm_movie_posters[0])
            slt.write(f"**Movie Name: {rcm_movie_names[0]}**")
        with col2:
            slt.image(rcm_movie_posters[1])
            slt.write(f"**Movie Name: {rcm_movie_names[1]}**")
        with col3:
            slt.image(rcm_movie_posters[2])
            slt.write(f"**Movie Name: {rcm_movie_names[2]}**")
        with col4:
            slt.image(rcm_movie_posters[3])
            slt.write(f"**Movie Name: {rcm_movie_names[3]}**")
        with col5:
            slt.image(rcm_movie_posters[4])
            slt.write(f"**Movie Name: {rcm_movie_names[4]}**")
        with col6:
            slt.image(rcm_movie_posters[5])
            slt.write(f"**Movie Name: {rcm_movie_names[5]}**")
        with col7:
            slt.image(rcm_movie_posters[6])
            slt.write(f"**Movie Name: {rcm_movie_names[6]}**")
        with col8:
            slt.image(rcm_movie_posters[7])
            slt.write(f"**Movie Name: {rcm_movie_names[7]}**")
        with col9:
            slt.image(rcm_movie_posters[8])
            slt.write(f"**Movie Name: {rcm_movie_names[8]}**")
        with col10:
            slt.image(rcm_movie_posters[9])
            slt.write(f"**Movie Name: {rcm_movie_names[9]}**")
