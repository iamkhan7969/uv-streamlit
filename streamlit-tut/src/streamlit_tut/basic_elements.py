import streamlit as st

st.title("To Generate a Balloon")
st.header("Header")
st.subheader("Subheader")
st.subheader("This is even a subheader")

s = "src/streamlit_tut/sound.mp3"  # Ensure correct path

def bal():
    st.balloons()

    # JavaScript for auto-playing sound
    audio_html = f"""
    <audio autoplay>
        <source src="{s}" type="audio/mp3">
    </audio>
    """
    st.markdown(audio_html, unsafe_allow_html=True)

st.button(label="Press me", on_click=bal)



# st.title("To Generate a Ballon")
# st.header("Header")
# st.subheader("Suber")
# st.subheader("This is even sub header")
# # st.text("Text")
# # st.markdown("**Markdown**")
# s="src\streamlit_tut\sound.mp3"
# def bal():
#     st.balloons()
#     st.audio(s)

# st.
# st.button(label="press me",on_click=bal)


# # to run uv run streamlit run src\streamlit_tut\basic_elements.py