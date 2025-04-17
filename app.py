import streamlit as st

st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)


st.sidebar.success("Select a demo above")

st.title("# Welcome to My Space")




st.image("lord-hanuman-black-3840x2160-14679.png")

col1 ,  col2 , col3 = st.columns(3)

st.write("I surrender to Hanuman, the messenger of Lord Rama, who is swift as the mind and fast as the wind. He has mastered his senses and is the wisest among the wise. He is the son of the wind god and the chief among the Vanaras (monkey tribe).")
# with col3:
st.write("Rama Singhasan Singh, Maruti Veer Maharaj |SadaShiv, Sankat Mochan, Jai Hanuman Mooradhaar ||")