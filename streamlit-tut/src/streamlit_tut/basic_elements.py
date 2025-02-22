import streamlit as st



def bal():
    st.balloons()
    
st.chat_message(name="human")

a=st.chat_input(placeholder="Enter Your Name",on_submit=bal)
st.title(f"Happy Birthday {a}")
st.markdown("**------------------------------------------------------------------------------------------**")
st.subheader("I \"Hamdan Durrani\" will wish you the best Birthday ever.")
st.subheader("Just enter your name below")



# to run uv run streamlit run src\streamlit_tut\basic_elements.py