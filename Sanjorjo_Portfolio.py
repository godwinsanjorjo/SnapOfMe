import streamlit as st
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Portfolio", page_icon=":wave:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://lottie.host/a9ba9b53-6042-4506-8f12-fa4a39f1ccce/jil2QlCICJ.json")

st.subheader("Hi, I am Godwin :comet:")
st.title("This is A Snap of Me")
st.write("My name is Godwin Ryan Sanjorjo. I am a resilient 21-year-old from the home of the sweet people, Medellin, Cebu."
         " I am a big dreamer and a huge fan of dreamers. I am enthusiastic in learning new things"
         " to help myself grow and help inspire those whom I share the same pathways with.")

with st.container():
    st.write("---")
    left_column, right_column = st.columns([1.5, 2.5])  
    with left_column:
        st_lottie(lottie_coding, height=500, key="coding")
    with right_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            Let me give you a little snap of me:
            - I am a 4th year BS Information Technology student.
            - I am pursuing my degree at Cebu Institute of Technology - University.
            - I am staying in Tres De Abril, Labangon, Cebu.
            - I play basketball in my free time since it helps me reconnect.
            - I draw when I want to express myself.
            - I enjoy spending time with my family and friends.
            - I am a big fan of triers, believers, and dream chasers.
            """ 
        )


with st.container():
    st.header("If you feel it, you should chase it. Dream Big!")