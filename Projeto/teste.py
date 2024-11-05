import streamlit as st

st.write(st.session_state)
nome = st.text_input("Digite seu nome", key="usuário")
st.write(st.session_state)
if st.button("Entrar no sistema"):
    st.write(st.session_state)


