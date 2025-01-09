import streamlit as st

home_page = st.Page(
    page="views/home.py",
    title='Home',
    icon=":material/home:"
)

obsity_page = st.Page(
    page="views/obesity.py",
    title="obesity",
    icon=":material/boy:"
)

calories_page = st.Page(
    page="views/calories.py",
    title="calories",
    icon=":material/local_fire_department:"
)

skin_page = st.Page(
    page="views/skin.py",
    title="skin",
    icon=":material/dermatology:"
)

about_page = st.Page(
    page="views/about.py",
    title="about",
    icon=":material/info:"
)

pg = st.navigation(pages=[home_page,obsity_page,calories_page,skin_page,about_page])

pg.run()
